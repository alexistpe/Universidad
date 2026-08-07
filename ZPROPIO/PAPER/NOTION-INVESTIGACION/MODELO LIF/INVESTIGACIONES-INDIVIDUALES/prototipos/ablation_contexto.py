"""Ablacion del contexto temporal/estacional en el Modelo C.

Variantes probadas sobre los mismos datos y protocolo que
prototipo_eddf_real.py (ajuste 2020-2024-06, calibracion 2024-07-2025-06,
validacion anio 6 = 2025-07-2026-07):

  C_ref      : Modelo C actual. Los spikes de 6 sensores + PRECIP graduada +
               las 4 features de contexto (sin/cos doy, sin/cos hora) entran
               DIRECTAS al readout de la alerta.
  C_sinctx   : Modelo C SIN las 4 features de contexto (se eliminan).
  C_neuronas : Modelo C donde las 4 features de contexto se tratan como
               NEURONAS LIF particulares: membrana EMA propia, umbral de
               disparo theta_i (percentil 90), spikes integrados por la
               alerta con tau_A (igual que los sensores fisicos).

En todos: pesos por regresion logistica, theta_A calibrado en calibracion
maximizando CSI, evaluacion en validacion con CSI/POD/FAR/bias.
"""

import numpy as np

from prototipo_lif import entrenar_logistico, puntuar, metricas
from prototipo_lif_spikes import capa_sensores_spikes, features_alerta
from prototipo_eddf_real import (
    cargar_datos,
    normalizar_estacional,
    capa_ema,
    calibrar_umbral_fino,
    TAUS_VEC,
)


def construir_c(df, X, ctx, fit_mask, calib_mask, val_mask, y_fit, y_cal):
    """Devuelve (features_variante, nombre) usando la misma logica del Modelo C."""
    n = len(df)
    # sensores fisicos spike (igual que B y C)
    A = capa_ema(X, TAUS_VEC)
    theta_i = np.percentile(A[fit_mask], 90, axis=0)
    _, S = capa_sensores_spikes(X, TAUS_VEC, theta_i)
    # PRECIP graduada (canal analogico)
    nivel_precip = X[:, 5]
    return A, S, nivel_precip


def evaluar(F, fit_mask, calib_mask, val_mask, y_fit, y_cal, y_val, nom):
    w, mu, sd = entrenar_logistico(F[fit_mask], y_fit)
    p_cal = puntuar(F[calib_mask], w, mu, sd)
    theta = calibrar_umbral_fino(y_cal, p_cal)
    p_val = puntuar(F[val_mask], w, mu, sd)
    csi, pod, far, tp, fp, fn = metricas(y_val, p_val, theta)
    bias = (tp + fp) / (tp + fn) if (tp + fn) else 0.0
    w_obs = w[: F.shape[1]]
    print("  %-11s CSI=%.3f POD=%.3f FAR=%.3f bias=%.2f (TP=%d FP=%d FN=%d) theta=%.2f"
          % (nom, csi, pod, far, bias, tp, fp, fn, theta))
    return csi, pod, far, w_obs


def main():
    df = cargar_datos()
    idx = df.index
    fit_mask = idx < "2024-07-01"
    calib_mask = (idx >= "2024-07-01") & (idx < "2025-07-01")
    val_mask = idx >= "2025-07-01"
    y = df["y_next"].to_numpy()
    y_fit, y_cal, y_val = y[fit_mask], y[calib_mask], y[val_mask]

    X, ctx = normalizar_estacional(df, fit_mask)
    n = len(df)

    # base comun: sensores spike + PRECIP graduada
    A = capa_ema(X, TAUS_VEC)
    theta_i = np.percentile(A[fit_mask], 90, axis=0)
    _, S = capa_sensores_spikes(X, TAUS_VEC, theta_i)
    nivel_precip = X[:, 5]
    EB = features_alerta(S, 1.0)  # tau_A = 1 h (el elegido para C)

    print("== ABLACION DEL CONTEXTO EN EL MODELO C ==")
    print("tasa lluvia val: %.3f%%\n" % (100 * y_val.mean()))

    # C_ref: [EB, nivel_precip, ctx]
    FC_ref = np.column_stack([EB, nivel_precip, ctx])
    csi_ref, pod_ref, far_ref, w_ref = evaluar(
        FC_ref, fit_mask, calib_mask, val_mask, y_fit, y_cal, y_val, "C_ref")
    print("    pesos (ctx sin/cos doy, sin/cos hora):",
          np.round(w_ref[7:11], 3))

    # C_sinctx: [EB, nivel_precip]
    FC_sin = np.column_stack([EB, nivel_precip])
    csi_sin, pod_sin, far_sin, _ = evaluar(
        FC_sin, fit_mask, calib_mask, val_mask, y_fit, y_cal, y_val, "C_sinctx")

    # C_neuronas: [EB, nivel_precip, E_ctx] con ctx como neuronas LIF con spike
    taus_ctx = [24.0, 24.0, 1.0, 1.0]  # doy lento (estacion), hora rapida
    A_ctx = capa_ema(ctx, taus_ctx)
    theta_ctx = np.percentile(A_ctx[fit_mask], 90, axis=0)
    _, S_ctx = capa_sensores_spikes(ctx, taus_ctx, theta_ctx)
    E_ctx = features_alerta(S_ctx, 1.0)
    tasa_ctx = S_ctx[fit_mask].mean(axis=0)
    print("    neuronas de contexto: theta_ctx =", np.round(theta_ctx, 3))
    print("    tasa de disparo de las neuronas de contexto (fit):",
          np.round(tasa_ctx, 3))
    FC_neu = np.column_stack([EB, nivel_precip, E_ctx])
    csi_neu, pod_neu, far_neu, w_neu = evaluar(
        FC_neu, fit_mask, calib_mask, val_mask, y_fit, y_cal, y_val, "C_neuronas")
    print("    pesos de los spikes de contexto:", np.round(w_neu[7:11], 3))

    print("\n== RESUMEN ==")
    print("  C_ref      (ctx directas): CSI=%.3f POD=%.3f FAR=%.3f"
          % (csi_ref, pod_ref, far_ref))
    print("  C_sinctx   (sin ctx)     : CSI=%.3f POD=%.3f FAR=%.3f"
          % (csi_sin, pod_sin, far_sin))
    print("  C_neuronas (ctx como LIF): CSI=%.3f POD=%.3f FAR=%.3f"
          % (csi_neu, pod_neu, far_neu))
    print("  Delta vs C_ref: sin-contexto %+.3f | neuronas %+.3f"
          % (csi_sin - csi_ref, csi_neu - csi_ref))


if __name__ == "__main__":
    main()
