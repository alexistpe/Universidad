"""Prototipo de la variante V1: sensores LIF con umbrales aprendidos + spikes.

Compara dos disenos sobre los MISMOS datos sinteticos de prototipo_lif.py:

  Modelo A (diseno actual): neuronas sensor como filtros fijos (EMA continua),
    readout de regresion logistica sobre la actividad. Solo la alerta aprende.

  Modelo B (propuesta V1): cada sensor es una neurona LIF que dispara spikes
    cuando su variable supera su umbral aprendido theta_i (percentil por
    variable, elegido en validacion). La alerta integra los spikes ponderados
    con su memoria tau_A (leaky-integrated spike train) y decide con theta_A.

Se reporta CSI/POD/FAR en test para ambos + baseline de umbral fijo.
Ejecutar: python3 prototipo_lif_spikes.py
"""

import numpy as np

from prototipo_lif import (
    sintetizar,
    capa_features,
    entrenar_logistico,
    puntuar,
    metricas,
    calibrar_umbral,
    calibrar_umbral_x,
)


def capa_sensores_spikes(X, taus, thetas):
    """Sensores LIF: membrana EMA + spike si V >= theta_i + reset a 0.

    Devuelve (A, S): A = membrana (con resets), S = indicadores de spike 0/1.
    """
    alphas = np.exp(-1.0 / np.asarray(taus, float))
    T, m = X.shape
    V = np.zeros(m)
    A = np.empty_like(X)
    S = np.zeros_like(X)
    for t in range(T):
        V = alphas * V + (1.0 - alphas) * X[t]
        A[t] = V
        spike = V >= thetas
        S[t] = spike.astype(float)
        V[spike] = 0.0
    return A, S


def features_alerta(S, tau_A):
    """Integra los spikes con la memoria de la alerta: EMA con tau_A.

    Equivalente a la dinamica de la neurona de alerta con pesos=1: la suma
    ponderada y la integracion conmutan (ambas lineales), asi que el readout
    logistico sobre E reproduce V_A = sum_i w_i * E_i con theta_A calibrado.
    """
    alpha = np.exp(-1.0 / tau_A)
    T, m = S.shape
    E = np.empty_like(S)
    V = np.zeros(m)
    for t in range(T):
        V = alpha * V + (1.0 - alpha) * S[t]
        E[t] = V
    return E


def evaluar_modelo(Ftr, ytr, Fval, yval, Fte, yte):
    """Entrena readout logistico estandarizado, calibra theta_A en val, evalua test."""
    w, mu, sd = entrenar_logistico(Ftr, ytr)
    p_val = puntuar(Fval, w, mu, sd)
    umbral = calibrar_umbral(yval, p_val)
    p_te = puntuar(Fte, w, mu, sd)
    return metricas(yte, p_te, umbral), umbral


def csi_validacion(Ftr, ytr, Fval, yval):
    """CSI en validacion (para seleccionar hiperparametros sin tocar test)."""
    w, mu, sd = entrenar_logistico(Ftr, ytr)
    p_val = puntuar(Fval, w, mu, sd)
    umbral = calibrar_umbral(yval, p_val)
    return metricas(yval, p_val, umbral)[0]


def main():
    X, y, ctx = sintetizar()
    n = len(y)
    idx_train = slice(0, int(0.7 * n))
    idx_val = slice(int(0.7 * n), int(0.85 * n))
    idx_test = slice(int(0.85 * n), n)
    ytr, yval, yte = y[idx_train], y[idx_val], y[idx_test]

    taus = [6.0, 6.0, 3.0, 1.0]
    tau_A = 2.0

    print("== Modelo A: actividad continua + readout ponderado (diseno actual) ==")
    A = capa_features(X, taus)
    FA = np.column_stack([A, ctx])
    (csi_A, pod_A, far_A, tp_A, fp_A, fn_A), umb_A = evaluar_modelo(
        FA[idx_train], ytr, FA[idx_val], yval, FA[idx_test], yte)

    print("== Modelo B: sensores LIF con spikes + umbrales theta_i aprendidos ==")
    print("  (theta_i por percentil y tau_A elegidos en validacion)")
    Atr_libre = capa_features(X[idx_train], taus)
    mejor = (0.0, 90.0, tau_A)
    for p in range(70, 100, 5):
        theta_i = np.percentile(Atr_libre, p, axis=0)
        _, S = capa_sensores_spikes(X, taus, theta_i)
        for ta in [2.0, 3.0, 6.0, 12.0, 24.0]:
            FB = np.column_stack([features_alerta(S, ta), ctx])
            csi_p = csi_validacion(FB[idx_train], ytr, FB[idx_val], yval)
            if csi_p > mejor[0]:
                mejor = (csi_p, p, ta)
    csi_val_B, p_sel, tau_A = mejor
    tau_A = float(tau_A)

    theta_i = np.percentile(Atr_libre, p_sel, axis=0)
    _, S = capa_sensores_spikes(X, taus, theta_i)
    EB = features_alerta(S, tau_A)
    FB = np.column_stack([EB, ctx])
    (csi_B, pod_B, far_B, tp_B, fp_B, fn_B), umb_B = evaluar_modelo(
        FB[idx_train], ytr, FB[idx_val], yval, FB[idx_test], yte)

    print("== Modelo B2: spikes instantaneos (sin integracion de la alerta) ==")
    FB2 = np.column_stack([S, ctx])
    (csi_B2, pod_B2, far_B2, tp_B2, fp_B2, fn_B2), umb_B2 = evaluar_modelo(
        FB2[idx_train], ytr, FB2[idx_val], yval, FB2[idx_test], yte)

    print("== Baseline: umbral fijo sobre X0 calibrado en validacion ==")
    ux = calibrar_umbral_x(yval, X[idx_val])
    base = (X[idx_test][:, 0] > ux).astype(int)
    csi_b, pod_b, far_b, *_ = metricas(yte, base, 0.5)

    print("\nDetalles del modelo B:")
    print("  percentil theta_i elegido en validacion:", p_sel)
    print("  theta_i por sensor:", np.round(theta_i, 3))
    tasa = S[idx_train].mean(axis=0)
    print("  tasa de disparo por sensor (train):", np.round(tasa, 3))
    print("  tau_A (memoria de la alerta) [h]:", round(tau_A, 1))
    print("  CSI en validacion (modelo B):", round(csi_val_B, 3))

    print("\n== Resultados en test ==")
    print("  tasa de lluvia en test:", round(yte.mean(), 3))
    print("  A   (continuo + pesos):  CSI=%.3f  POD=%.3f  FAR=%.3f  theta_A=%.2f"
          % (csi_A, pod_A, far_A, umb_A))
    print("  B   (spikes integrados): CSI=%.3f  POD=%.3f  FAR=%.3f  theta_A=%.2f"
          % (csi_B, pod_B, far_B, umb_B))
    print("  B2  (spikes instantaneos): CSI=%.3f  POD=%.3f  FAR=%.3f  theta_A=%.2f"
          % (csi_B2, pod_B2, far_B2, umb_B2))
    print("  Base (umbral fijo X0):   CSI=%.3f  POD=%.3f  FAR=%.3f  (umbral=%.2f)"
          % (csi_b, pod_b, far_b, ux))

    print("\nDelta CSI vs baseline:")
    print("  A:   %+.3f" % (csi_A - csi_b))
    print("  B:   %+.3f" % (csi_B - csi_b))
    print("  B2:  %+.3f" % (csi_B2 - csi_b))


if __name__ == "__main__":
    main()
