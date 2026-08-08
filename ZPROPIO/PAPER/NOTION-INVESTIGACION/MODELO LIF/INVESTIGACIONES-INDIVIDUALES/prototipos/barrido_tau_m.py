"""Sensibilidad del Modelo B a la memoria de los sensores tau_m (datos reales EDDF).

Barre un multiplicador aplicado a los tau_m de la linea base
(tau = {temp:3, rhum:3, pres:2, u:1, v:1, prcp:1} h) y mide CSI/POD/FAR
del Modelo B en validacion, con la misma metodologia de prototipo_eddf_real.py
(theta_i por percentil y tau_A elegidos por validacion en cada punto).

Sirve para la leccion pendiente: es tau_m un hiperparametro sensible?

Ejecutar: python3 barrido_tau_m.py
"""
import numpy as np
import pandas as pd

from prototipo_eddf_real import cargar_datos, normalizar_estacional, capa_ema, VARIABLES, TAUS, TAUS_VEC
from prototipo_lif_spikes import capa_sensores_spikes, features_alerta, csi_validacion
from prototipo_lif import metricas, entrenar_logistico, puntuar


def main():
    df = cargar_datos()
    idx = df.index
    fit_mask = idx < "2024-07-01"
    calib_mask = (idx >= "2024-07-01") & (idx < "2025-07-01")
    val_mask = idx >= "2025-07-01"
    y = df["y_next"].to_numpy()
    y_fit, y_cal, y_val = y[fit_mask], y[calib_mask], y[val_mask]
    X, ctx = normalizar_estacional(df, fit_mask)

    print("== SENSIBILIDAD A tau_m (Modelo B, validacion EDDF 2025-2026) ==")
    print("tau_m base: %s h" % TAUS)
    print("para cada multiplicador se re-eligen theta_i (percentil) y tau_A en calibracion")
    print()
    print("mult | tau_m resultante (h) [T HR P u v PRCP] | CSI   POD   FAR | theta_i p | tau_A")
    print("-" * 100)

    for mult in [0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 4.0]:
        taus = TAUS_VEC * mult
        A = capa_ema(X, taus)
        mejor = (0.0, 90.0, 1.0)
        for p in range(60, 96, 5):
            theta_i = np.percentile(A[fit_mask], p, axis=0)
            _, S = capa_sensores_spikes(X, taus, theta_i)
            for ta in [1.0, 2.0, 3.0, 6.0, 12.0, 24.0]:
                FB = np.column_stack([features_alerta(S, ta), ctx])
                c = csi_validacion(FB[fit_mask], y_fit, FB[calib_mask], y_cal)
                if c > mejor[0]:
                    mejor = (c, p, ta)
        _, p_sel, tau_A = mejor
        theta_i = np.percentile(A[fit_mask], p_sel, axis=0)
        _, S = capa_sensores_spikes(X, taus, theta_i)
        FB = np.column_stack([features_alerta(S, tau_A), ctx])
        w, mu, sd = entrenar_logistico(FB[fit_mask], y_fit)
        p_cal = puntuar(FB[calib_mask], w, mu, sd)
        theta_A = max((metricas(y_cal, p_cal, u)[0], u) for u in np.arange(0.01, 0.99, 0.01))[1]
        p_val = puntuar(FB[val_mask], w, mu, sd)
        csi, pod, far, *_ = metricas(y_val, p_val, theta_A)
        print("%-4.2f | %s | %.3f %.3f %.3f | %d | %.0f h"
              % (mult, np.round(taus, 2), csi, pod, far, p_sel, tau_A))


if __name__ == "__main__":
    main()
