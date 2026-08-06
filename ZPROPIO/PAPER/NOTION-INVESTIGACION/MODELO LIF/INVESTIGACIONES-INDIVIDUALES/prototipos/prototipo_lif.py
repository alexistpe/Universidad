"""Prototipo del modelo LIF simplificado (guia de codificacion).

Implementa la cadena completa de Diseno_Modelo_LIF.md:
  1) datos sinteticos horarios con autocorrelacion + etiqueta de lluvia
  2) capa de features: EMA/LIF por variable (filtro IIR fijo)  -> actividades
  3) features de contexto temporal sin/cos(doy) + sin/cos(hora)
  4) entrenamiento del readout: regresion logistica (BCE) sobre las features
  5) calibracion del umbral de la alerta en validacion (maximizar CSI)
  6) evaluacion en test: CSI / POD / FAR vs baseline de umbrales fijos

Solo usa numpy. Ejecutar: python3 prototipo_lif.py
"""

import numpy as np


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


def ar1(n, phi, sigma, rng, low=0.05, high=0.95):
    """AR(1) estacionario con desviacion estandar ~sigma alrededor de la media."""
    mid = 0.5 * (low + high)
    s = np.empty(n)
    s[0] = rng.normal(0.0, sigma)
    var = sigma * sigma * (1 - phi * phi)
    for t in range(1, n):
        s[t] = phi * s[t - 1] + np.sqrt(var) * rng.normal()
    return np.clip(mid + s, low, high)


def sintetizar(anios=3, m=4, seed=1):
    rng = np.random.default_rng(seed)
    n = anios * 8760
    doy = (np.arange(n) % 366) + 1
    hora = np.arange(n) % 24

    X = np.column_stack([ar1(n, 0.9, 0.2, rng) for _ in range(m)])

    y = ((np.convolve(X[:, 0], np.ones(6) / 6, "same") > 0.65)
         & (np.convolve(X[:, 1], np.ones(6) / 6, "same") > 0.65)).astype(int)
    flip = rng.random(n) < 0.05
    y[flip] = 1 - y[flip]

    ctx = np.column_stack([
        np.sin(2 * np.pi * doy / 365.25),
        np.cos(2 * np.pi * doy / 365.25),
        np.sin(2 * np.pi * hora / 24),
        np.cos(2 * np.pi * hora / 24),
    ])
    return X, y, ctx


def capa_features(X, taus):
    alphas = np.exp(-1.0 / np.asarray(taus, float))
    A = np.empty_like(X)
    V = np.zeros(X.shape[1])
    for t in range(X.shape[0]):
        V = alphas * V + (1 - alphas) * X[t]
        A[t] = V
    return A


def entrenar_logistico(X, y, lr=0.5, epochs=300):
    """Regresion logistica sobre features estandarizadas (mu/sd de train)."""
    mu = X.mean(axis=0)
    sd = X.std(axis=0) + 1e-9
    Z = (X - mu) / sd
    Z1 = np.column_stack([Z, np.ones(len(Z))])
    w = np.zeros(Z1.shape[1])
    for _ in range(epochs):
        w -= lr * (Z1.T @ (sigmoid(Z1 @ w) - y)) / len(y)
    return w, mu, sd


def puntuar(X, w, mu, sd):
    Z = np.column_stack([(X - mu) / sd, np.ones(len(X))])
    return sigmoid(Z @ w)


def metricas(y, p, umbral):
    pred = p >= umbral
    tp = int(np.sum((pred == 1) & (y == 1)))
    fp = int(np.sum((pred == 1) & (y == 0)))
    fn = int(np.sum((pred == 0) & (y == 1)))
    csi = tp / (tp + fp + fn) if (tp + fp + fn) else 0.0
    pod = tp / (tp + fn) if (tp + fn) else 0.0
    far = fp / (tp + fp) if (tp + fp) else 0.0
    return csi, pod, far, tp, fp, fn


def calibrar_umbral(y_val, p_val, paso=0.05, minimo=0.10, maximo=0.95):
    mejor = (0.0, minimo)
    for u in np.arange(minimo, maximo, paso):
        csi = metricas(y_val, p_val, u)[0]
        if csi > mejor[0]:
            mejor = (csi, u)
    return mejor[1]


def calibrar_umbral_x(y_val, x_val, variable=0):
    mejor = (0.0, 0.5)
    for u in np.arange(0.25, 0.95, 0.05):
        csi = metricas(y_val, (x_val[:, variable] > u).astype(int), 0.5)[0]
        if csi > mejor[0]:
            mejor = (csi, u)
    return mejor[1]


def main():
    rng = np.random.default_rng(7)
    X, y, ctx = sintetizar()
    n = len(y)
    idx_train = slice(0, int(0.7 * n))
    idx_val = slice(int(0.7 * n), int(0.85 * n))
    idx_test = slice(int(0.85 * n), n)

    taus = [6.0, 6.0, 3.0, 1.0]
    A = capa_features(X, taus)

    def build(idx):
        return np.column_stack([A[idx], ctx[idx]])

    Xtr, ytr = build(idx_train), y[idx_train]
    Xval, yval = build(idx_val), y[idx_val]
    Xte, yte = build(idx_test), y[idx_test]

    w, mu, sd = entrenar_logistico(Xtr, ytr)
    w_obs = w[: X.shape[1]]
    w_ctx = w[X.shape[1]: -1]

    p_val = puntuar(Xval, w, mu, sd)
    umbral = calibrar_umbral(yval, p_val)

    p_te = puntuar(Xte, w, mu, sd)
    csi, pod, far, tp, fp, fn = metricas(yte, p_te, umbral)

    ux = calibrar_umbral_x(yval, X[idx_val], variable=0)
    base = (X[idx_test][:, 0] > ux).astype(int)
    csi_b, pod_b, far_b, *_ = metricas(yte, base, 0.5)

    act_tr = A[idx_train]
    umbrales_sensor = np.percentile(act_tr, 95, axis=0)
    tasa_spikes = [np.mean(act_tr[:, i] >= umbrales_sensor[i]) for i in range(A.shape[1])]

    print("== Capa de features (LIF/EMA) ==")
    print("tau_m por variable [h]:", taus)
    print("alphas:", np.round(np.exp(-1.0 / np.asarray(taus)), 2))
    print("actividad final (media por variable):", np.round(A.mean(axis=0), 3))

    print("\n== Umbrales de disparo de sensores (percentil 95, train) ==")
    print("theta_i:", np.round(umbrales_sensor, 3))
    print("tasa de disparo por sensor:", np.round(tasa_spikes, 3))

    print("\n== Readout aprendido (regresion logistica, features estandarizadas) ==")
    print("pesos w (por variable):", np.round(w_obs, 3))
    print("pesos v (contexto):", np.round(w_ctx, 3))
    print("bias b:", np.round(w[-1], 3))

    print("\n== Calibracion y test ==")
    print("umbral calibrado en validacion (theta_A):", round(umbral, 3))
    print("LIF:   CSI=%.3f  POD=%.3f  FAR=%.3f  (TP=%d FP=%d FN=%d)" % (csi, pod, far, tp, fp, fn))
    print("Base:  CSI=%.3f  POD=%.3f  FAR=%.3f  (umbral X0=%.2f)" % (csi_b, pod_b, far_b, ux))
    print("tasa lluvia en test:", round(yte.mean(), 3))


if __name__ == "__main__":
    main()
