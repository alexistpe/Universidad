"""Traza real del Modelo B alrededor de un evento de lluvia en validacion.

Muestra, hora a hora, el recorrido completo de la senal para un TP real:
x̂_i (anomalia normalizada) -> V_i (membrana del sensor) -> S_i (spike)
-> E_i (memoria por canal de la alerta) -> I_A (potencial) -> P (probabilidad).

Replica el Modelo B de prototipo_eddf_real.py (theta_i = percentil 90 del
ajuste, tau_A=1 h, pesos del readout logistico). I_A y P se reportan en el
espacio CRUDO de las features: w_raw = w_std/sd y b_raw ajustado, para que
I_A = w_raw·E + v_raw·ctx + b_raw sea EXACTAMENTE el logit de P.

Ejecutar: python3 traza_evento_real.py
"""
import numpy as np
import pandas as pd

from prototipo_eddf_real import (
    cargar_datos,
    normalizar_estacional,
    capa_ema,
    VARIABLES,
    TAUS_VEC,
    UMBRAL_LLUVIA,
)
from prototipo_lif_spikes import capa_sensores_spikes, features_alerta
from prototipo_lif import entrenar_logistico, puntuar

TAU_A = 1.0
VENTANA_HORAS = 9


def a_raw(w, mu, sd):
    """Pesos estandarizados (w_std) -> pesos crudos (logit = w_raw·X + b_raw)."""
    wf = w[:-1] / sd
    b_raw = w[-1] - np.sum(w[:-1] * mu / sd)
    return wf, b_raw


def main():
    df = cargar_datos()
    idx = df.index
    horas = np.array([str(h)[:16] for h in idx])
    fit_mask = idx < "2024-07-01"
    val_mask = idx >= "2025-07-01"
    y = df["y_next"].to_numpy()
    prcp = df["prcp"].to_numpy()
    X, ctx = normalizar_estacional(df, fit_mask)

    A = capa_ema(X, TAUS_VEC)
    theta_i = np.percentile(A[fit_mask], 90, axis=0)
    _, S = capa_sensores_spikes(X, TAUS_VEC, theta_i)
    E = features_alerta(S, TAU_A)
    FB = np.column_stack([E, ctx])
    w_std, mu, sd = entrenar_logistico(FB[fit_mask], y[fit_mask])
    p = puntuar(FB, w_std, mu, sd)
    w_raw, b_raw = a_raw(w_std, mu, sd)
    w_sens = w_raw[:6]
    v_ctx = w_raw[6:10]

    val_idx = np.where(val_mask)[0]
    candidatos = [t for t in val_idx if y[t] == 1 and p[t] >= 0.21]
    t = max(candidatos, key=lambda s: p[s]) if candidatos else val_idx[0]

    a0 = max(t - VENTANA_HORAS, 0)
    a1 = min(t + 4, len(y))

    print("== TRAZA REAL DEL MODELO B (TP en validacion) ==")
    print("evento: lluvia prevista la hora %s (y_next=1, P=%.2f >= theta_A=0.21)"
          % (horas[t], p[t]))
    print("theta_i (percentil 90 del ajuste) = %s" % np.round(theta_i, 3))
    print("tau_A (memoria de la alerta) = %.0f h" % TAU_A)
    print("pesos crudos w(sensores) = %s" % np.round(w_sens, 3))
    print("pesos crudos v(contexto) = %s | b_raw = %.3f" % (np.round(v_ctx, 3), b_raw))

    print("\nfila:  hora | prcp |  x̂ (6 sens) | V (6 sens) | spikes | E (6 sens) | I_A |  P  | y_next")
    print("-" * 160)
    for tt in range(a0, a1):
        sp = S[tt].astype(int)
        pot = w_sens @ E[tt] + v_ctx @ ctx[tt] + b_raw
        prob = 1.0 / (1.0 + np.exp(-pot))
        print("%s | %4.1f | %s | %s | %s | %s | %+.2f | %.2f | %d"
              % (horas[tt], prcp[tt],
                 np.round(X[tt], 2), np.round(A[tt], 2),
                 "".join(map(str, sp)), np.round(E[tt], 2),
                 pot, prob, y[tt]))

    print("\nnota: I_A = w_raw·E + v_raw·ctx + b_raw es el logit EXACTO de P")
    print("  (w_raw = w_std/sd: pesos convertidos al espacio crudo de las")
    print("  features). La decision es lluvia la PROXIMA hora si P >= 0.21.")


if __name__ == "__main__":
    main()
