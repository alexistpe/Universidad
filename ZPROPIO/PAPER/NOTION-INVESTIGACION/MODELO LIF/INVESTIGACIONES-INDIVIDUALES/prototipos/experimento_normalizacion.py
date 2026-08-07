"""Experimento: robustez del Modelo B a la normalizacion de la entrada.

Compara 3 esquemas de preprocesado de X sobre el MISMO modelo y protocolo:
  a) estacional-z (actual): anomalia estacional clip [-3,3] -> [0,1]
  b) min-max global por variable (sin estacionalidad) -> [0,1]
  c) crudo: sin ninguna normalizacion (unidades fisicas)

Fija theta_i = percentil 90 y tau_A = 1 h (valores calibrados del modelo real)
para aislar el efecto de la normalizacion. Entrena readout logistico estandarizado
y calibra theta_A en validacion. Evalua en el ano 6 (2025-2026).

Resultado: CSI practicamente identico en los 3 -> la arquitectura LIF + readout
logistico es invariante a la escala de entrada. La normalizacion estacional se
mantiene por interpretabilidad y significado de "anomalia-precursor", no por
precision. Ejecutar: python3 experimento_normalizacion.py
"""
import numpy as np

from prototipo_eddf_real import (
    cargar_datos,
    normalizar_estacional,
    capa_ema,
    TAUS_VEC,
    VARIABLES,
)
from prototipo_lif import entrenar_logistico, puntuar, metricas
from prototipo_lif_spikes import capa_sensores_spikes, features_alerta


def calibrar_umbral_fino(y, p):
    mejor = (0.0, 0.10)
    for u in np.arange(0.01, 0.99, 0.01):
        c = metricas(y, p, u)[0]
        if c > mejor[0]:
            mejor = (c, u)
    return mejor[1]


def main():
    df = cargar_datos()
    idx = df.index
    fit_mask = idx < "2024-07-01"
    calib_mask = (idx >= "2024-07-01") & (idx < "2025-07-01")
    val_mask = idx >= "2025-07-01"
    y = df["y_next"].to_numpy()
    y_fit, y_cal, y_val = y[fit_mask], y[calib_mask], y[val_mask]

    Xest, ctx = normalizar_estacional(df, fit_mask)

    Xmm = np.empty_like(Xest)
    for j, v in enumerate(VARIABLES):
        s = df[v].to_numpy().astype(float)
        lo, hi = s[fit_mask].min(), s[fit_mask].max()
        Xmm[:, j] = (s - lo) / (hi - lo) if hi > lo else 0.0

    Xraw = df[VARIABLES].to_numpy().astype(float)

    print("== Modelo B con theta_i=percentil90, tau_A=1h, readout estandarizado ==")
    print("(unica diferencia: como se preprocesa la entrada X)\n")
    for nombre, X in [("estacional-z", Xest), ("min-max global", Xmm), ("crudo", Xraw)]:
        A = capa_ema(X, TAUS_VEC)
        theta_i = np.percentile(A[fit_mask], 90, axis=0)
        _, S = capa_sensores_spikes(X, TAUS_VEC, theta_i)
        E = features_alerta(S, 1.0)
        F = np.column_stack([E, ctx])
        w, mu, sd = entrenar_logistico(F[fit_mask], y_fit)
        theta_A = calibrar_umbral_fino(y_cal, puntuar(F[calib_mask], w, mu, sd))
        p_val = puntuar(F[val_mask], w, mu, sd)
        csi, pod, far, tp, fp, fn = metricas(y_val, p_val, theta_A)
        print("%-15s CSI=%.3f POD=%.3f FAR=%.3f theta_A=%.2f (TP=%d FP=%d FN=%d)"
              % (nombre, csi, pod, far, theta_A, tp, fp, fn))
        print("    theta_i:", np.round(theta_i, 2))


if __name__ == "__main__":
    main()
