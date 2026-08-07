"""Prototipo final con datos reales EDDF (estacion 10637, Frankfurt Flughafen).

DEFINICION FORMAL DE LLUVIA
    Evento: precipitacion horaria >= 0.25 mm/h.
    Justificacion del valor:
      (a) resolucion minima de un pluviometro de bajo costo de cubeta
          basculante ~0.2 mm/cubetada -> 0.25 mm/h es la lluvia minima
          medible de forma fiable en una estacion de bajo costo;
      (b) el glosario de intensidad de la DWD clasifica >=0.1 mm/h como
          "Spruehregen" (llovizna) medida; 0.25 mm/h queda por encima de la
          llovizna y por debajo de "Regen" (>= 2.5 mm/h en 60 min), es decir,
          "lluvia medible real".

PREDICCION
    y[t+1] = 1 si llovio la hora siguiente (prcp[t+1] >= 0.25). Las features
    usan SOLO datos hasta t (sin fuga de informacion futura).

SPLIT (entrenar 5 anos, validar el ano 6)
    Ajuste:        2020-01-01 .. 2024-06-30   (parte del periodo 2020-2025)
    Calibracion:   2024-07-01 .. 2025-06-30   (hiperparametros y umbrales)
    Validacion:    2025-07-01 .. 2026-07-10   (anio 6, periodo 2025-2026)

MODELOS (que senal manda cada sensor y donde se aprende)
    Baseline : umbral fijo (persistencia). Lluvia la proxima hora si
               prcp[t] >= 0.25 mm/h. El umbral es la propia definicion del
               evento; la persistencia es la referencia estandar de nowcasting
               (DWD/WMO).
    A        : unica neurona de alerta con pesos ponderados. 6 sensores LIF
               fijos en modo subumbral (EMA, actividad continua) + 4 contexto
               + readout logistico. Aprende w y theta_A.
    B        : 7 neuronas LIF (6 sensor + 1 alerta). Cada sensor dispara un
               spike cuando su membrana supera su umbral propio theta_i
               (percentil aprendido en calibracion); la alerta integra los
               spikes ponderados con su memoria tau_A y decide con theta_A.
               Aprende theta_i, tau_A, w, theta_A.
    C        : mejora sobre B sobre bases LIF. Anade el modo GRADUADO del LIF:
               la variable dominante (precipitacion) aporta su nivel de
               membrana (intensidad analogica) ademas del spike; la alerta
               combina spikes binarios de precursores + intensidad graduada
               con tau_A. Modifica un componente fundamental (la codificacion
               de la salida del sensor: binaria vs graduada).

METRICAS: CSI/POD/FAR (+bias) en validacion. Hiperparametros en calibracion.
"""
import numpy as np
import pandas as pd

from prototipo_lif import entrenar_logistico, puntuar, metricas
from prototipo_lif_spikes import capa_sensores_spikes, features_alerta, csi_validacion

RUTA_DATOS = "datos/eddf_10637_horario_2020_2026.csv"
VARIABLES = ["temp", "rhum", "pres", "u", "v", "prcp"]
NOMBRES = ["T", "HR", "P", "u", "v", "PRECIP"]
TAUS = {"temp": 3.0, "rhum": 3.0, "pres": 2.0, "u": 1.0, "v": 1.0, "prcp": 1.0}
TAUS_VEC = np.array([TAUS[v] for v in VARIABLES])
UMBRAL_LLUVIA = 0.25  # mm/h, definicion formal


def cargar_datos():
    df = pd.read_csv(RUTA_DATOS, index_col=0, parse_dates=True).sort_index()
    df["prcp"] = df["prcp"].astype(float)
    rad = np.radians(df["wdir"].astype(float))
    df["u"] = df["wspd"].astype(float) * np.sin(rad)
    df["v"] = df["wspd"].astype(float) * np.cos(rad)
    df["y"] = (df["prcp"] >= UMBRAL_LLUVIA).astype(int)
    df["y_next"] = df["y"].shift(-1).fillna(0).astype(int)
    return df.dropna(subset=["y_next"])


def normalizar_estacional(df, fit_mask):
    """Anomalia estacional z por dia del ano (climatologia solo de train) -> [0,1]."""
    idx = df.index
    doy = idx.dayofyear
    n = len(df)
    X = np.empty((n, len(VARIABLES)))
    fit = df[fit_mask]
    for j, v in enumerate(VARIABLES):
        if v == "prcp":
            X[:, j] = np.clip(df["prcp"].to_numpy() / 1.0, 0.0, 1.0)
            continue
        s = fit[v].to_numpy()
        sdoy = fit.index.dayofyear.to_numpy()
        med = pd.Series(s, index=sdoy).groupby(level=0).mean().reindex(range(1, 367))
        std = pd.Series(s, index=sdoy).groupby(level=0).std().reindex(range(1, 367))
        med = med.rolling(31, center=True, min_periods=1).mean()
        std = std.rolling(31, center=True, min_periods=1).mean()
        std = std.fillna(std.median()).clip(lower=1e-6)
        med = med.fillna(med.median())
        z = (df[v].to_numpy() - med[doy].to_numpy()) / std[doy].to_numpy()
        X[:, j] = 0.5 + np.clip(z, -3.0, 3.0) / 6.0
    ctx = np.column_stack([
        np.sin(2 * np.pi * doy / 365.25),
        np.cos(2 * np.pi * doy / 365.25),
        np.sin(2 * np.pi * idx.hour / 24),
        np.cos(2 * np.pi * idx.hour / 24),
    ])
    return X, ctx


def capa_ema(X, taus):
    alphas = np.exp(-1.0 / np.asarray(taus, float))
    A = np.empty_like(X)
    V = np.zeros(X.shape[1])
    for t in range(X.shape[0]):
        V = alphas * V + (1.0 - alphas) * X[t]
        A[t] = V
    return A


def calibrar_umbral_fino(y, p):
    mejor = (0.0, 0.10)
    for u in np.arange(0.01, 0.99, 0.01):
        c = metricas(y, p, u)[0]
        if c > mejor[0]:
            mejor = (c, u)
    return mejor[1]


def main():
    df = cargar_datos()
    n = len(df)
    idx = df.index
    fit_mask = idx < "2024-07-01"
    calib_mask = (idx >= "2024-07-01") & (idx < "2025-07-01")
    val_mask = idx >= "2025-07-01"
    y = df["y_next"].to_numpy()
    y_fit, y_cal, y_val = y[fit_mask], y[calib_mask], y[val_mask]
    X, ctx = normalizar_estacional(df, fit_mask)
    prcp = df["prcp"].to_numpy()
    llueve_ahora = prcp >= UMBRAL_LLUVIA

    print("== DATOS REALES EDDF (10637 Frankfurt Flughafen) ==")
    print("periodo:", idx.min(), "->", idx.max(), "| n =", n)
    print("tasa lluvia (prcp>=%.2f mm/h) total: %.3f%%" % (UMBRAL_LLUVIA, 100 * y.mean()))
    print("splits: ajuste=%d (%.3f%% lluvia) | calib=%d (%.3f%%) | val=%d (%.3f%%)"
          % (len(y_fit), 100 * y_fit.mean(), len(y_cal), 100 * y_cal.mean(),
             len(y_val), 100 * y_val.mean()))

    # ============ BASELINE (umbral fijo, persistencia) ============
    print("\n== BASELINE: umbral fijo (persistencia) ==")
    print("  regla: lluvia la proxima hora si prcp[t] >= %.2f mm/h" % UMBRAL_LLUVIA)
    print("  por que 0.25: es la definicion formal del evento; coincide con la")
    print("  resolucion de un pluviometro de bajo costo (~0.2 mm/cubetada) y la")
    print("  DWD mide llovizna desde 0.1 mm/h (glosario de intensidad). La")
    print("  persistencia es la referencia estandar de nowcasting (DWD/WMO).")
    for nom, m in [("calib", calib_mask), ("val", val_mask)]:
        pred = llueve_ahora[m].astype(int)
        csi, pod, far, tp, fp, fn = metricas(y[m], pred, 0.5)
        bias = (tp + fp) / (tp + fn) if (tp + fn) else 0.0
        print("  %s: CSI=%.3f POD=%.3f FAR=%.3f bias=%.2f (TP=%d FP=%d FN=%d)"
              % (nom, csi, pod, far, bias, tp, fp, fn))

    # ============ MODELO A: unica neurona de alerta con pesos ============
    print("\n== MODELO A: unica neurona de alerta con pesos ponderados ==")
    print("  [sensores fijos en modo subumbral + readout ponderado]")
    A = capa_ema(X, TAUS_VEC)
    FA = np.column_stack([A, ctx])
    w, mu, sd = entrenar_logistico(FA[fit_mask], y_fit)
    p_cal = puntuar(FA[calib_mask], w, mu, sd)
    theta_A = calibrar_umbral_fino(y_cal, p_cal)
    p_val = puntuar(FA[val_mask], w, mu, sd)
    csiA, podA, farA, tpA, fpA, fnA = metricas(y_val, p_val, theta_A)
    biasA = (tpA + fpA) / (tpA + fnA) if (tpA + fnA) else 0.0
    print("  parametros FIJOS: tau_m=%s h | V_rest=0 | V_reset=0 (modo subumbral)" % TAUS)
    print("  parametros APRENDIDOS: pesos w=%s" % np.round(w[:6], 3))
    print("    pesos contexto v=%s | bias b=%.3f" % (np.round(w[6:-1], 3), w[-1]))
    print("  umbral IDEAL de la alerta: theta_A=%.2f (max CSI en calibracion)" % theta_A)
    print("  val: CSI=%.3f POD=%.3f FAR=%.3f bias=%.2f (TP=%d FP=%d FN=%d)"
          % (csiA, podA, farA, biasA, tpA, fpA, fnA))
    print("  acumulacion de potencia: I_A = sum(w_i*a_i + v_j*ctx_j) es la")
    print("    evidencia instantanea; theta_A = cuanta evidencia combinada se")
    print("    necesita para declarar lluvia.")

    # ============ MODELO B: 7 neuronas LIF (6 sensor + 1 alerta) ============
    print("\n== MODELO B: 7 neuronas LIF (6 sensor + 1 alerta) ==")
    print("  [sensores disparan spikes con umbral propio; la alerta integra]")
    mejor = (0.0, 90.0, 1.0)
    for p in range(60, 96, 5):
        theta_i = np.percentile(A[fit_mask], p, axis=0)
        _, S = capa_sensores_spikes(X, TAUS_VEC, theta_i)
        for ta in [1.0, 2.0, 3.0, 6.0, 12.0, 24.0]:
            FB = np.column_stack([features_alerta(S, ta), ctx])
            c = csi_validacion(FB[fit_mask], y_fit, FB[calib_mask], y_cal)
            if c > mejor[0]:
                mejor = (c, p, ta)
    _, p_sel, tau_A_B = mejor
    theta_i = np.percentile(A[fit_mask], p_sel, axis=0)
    _, S = capa_sensores_spikes(X, TAUS_VEC, theta_i)
    EB = features_alerta(S, tau_A_B)
    FB = np.column_stack([EB, ctx])
    wB, muB, sdB = entrenar_logistico(FB[fit_mask], y_fit)
    theta_AB = calibrar_umbral_fino(y_cal, puntuar(FB[calib_mask], wB, muB, sdB))
    p_valB = puntuar(FB[val_mask], wB, muB, sdB)
    csiB, podB, farB, tpB, fpB, fnB = metricas(y_val, p_valB, theta_AB)
    biasB = (tpB + fpB) / (tpB + fnB) if (tpB + fnB) else 0.0
    print("  parametros FIJOS: tau_m=%s | V_rest=0 | V_reset=0 (reset total al disparar)" % TAUS)
    print("  parametros APRENDIDOS: theta_i (percentil %d en calibracion)" % p_sel)
    print("    theta_i por sensor:", np.round(theta_i, 3))
    print("    tasa de disparo por sensor (ajuste):", np.round(S[fit_mask].mean(axis=0), 3))
    print("    tau_A (memoria de la alerta, integra spikes) = %.0f h" % tau_A_B)
    print("    pesos sobre spikes integrados:", np.round(wB[:6], 3))
    print("  umbral IDEAL de la alerta: theta_A=%.2f (max CSI en calibracion)" % theta_AB)
    print("  val: CSI=%.3f POD=%.3f FAR=%.3f bias=%.2f (TP=%d FP=%d FN=%d)"
          % (csiB, podB, farB, biasB, tpB, fpB, fnB))
    print("  acumulacion de potencia: la alerta integra cuantos spikes (alarmas")
    print("    por variable) llegan en las ultimas tau_A horas; theta_A = cuantas")
    print("    alarmas ponderadas acumuladas se necesitan.")

    # ============ MODELO C: B + modo graduado de la precipitacion ============
    print("\n== MODELO C: LIF con codificacion graduada de la precipitacion ==")
    print("  [modifica la salida del sensor dominante: spike binario + nivel]")
    # canal graduado: nivel de membrana de la precipitacion (intensidad 0..1)
    nivel_precip = X[:, 5]
    mejorC = (0.0, 1.0)
    for ta in [1.0, 2.0, 3.0, 6.0]:
        EBC = features_alerta(S, ta)
        FC = np.column_stack([EBC, nivel_precip, ctx])
        c = csi_validacion(FC[fit_mask], y_fit, FC[calib_mask], y_cal)
        if c > mejorC[0]:
            mejorC = (c, ta)
    tau_A_C = mejorC[1]
    EBC = features_alerta(S, tau_A_C)
    FC = np.column_stack([EBC, nivel_precip, ctx])
    wC, muC, sdC = entrenar_logistico(FC[fit_mask], y_fit)
    theta_AC = calibrar_umbral_fino(y_cal, puntuar(FC[calib_mask], wC, muC, sdC))
    p_valC = puntuar(FC[val_mask], wC, muC, sdC)
    csiC, podC, farC, tpC, fpC, fnC = metricas(y_val, p_valC, theta_AC)
    biasC = (tpC + fpC) / (tpC + fnC) if (tpC + fnC) else 0.0
    print("  parametros FIJOS: igual que B (tau_m, V_rest, V_reset, theta_i)")
    print("  modificacion: el sensor de precipitacion aporta su nivel de membrana")
    print("    (intensidad graduada 0..1) ademas del spike; los demas sensores")
    print("    siguen en modo binario.")
    print("  tau_A (memoria de la alerta) = %.0f h | theta_i = percentil %d" % (tau_A_C, p_sel))
    print("  pesos (spikes de precursores):", np.round(wC[:6], 3))
    print("  peso del canal graduado de precipitacion:", round(wC[6], 3))
    print("  umbral IDEAL de la alerta: theta_A=%.2f (max CSI en calibracion)" % theta_AC)
    print("  val: CSI=%.3f POD=%.3f FAR=%.3f bias=%.2f (TP=%d FP=%d FN=%d)"
          % (csiC, podC, farC, biasC, tpC, fpC, fnC))
    print("  acumulacion de potencia: la alerta acumula con memoria tau_A la suma")
    print("    ponderada de spikes de precursores + la intensidad graduada de la")
    print("    precipitacion; theta_A = potencia acumulada minima para alarmar.")

    # ============ DIAGNOSTICO DEL LIMITE ============
    print("\n== DIAGNOSTICO DEL LIMITE (por que el FAR no baja mas) ==")
    predC = p_valC >= theta_AC
    fpC_mask = predC & (y_val == 0)
    n_fp = int(fpC_mask.sum())
    fp_lloviendo = int((fpC_mask & llueve_ahora[val_mask]).sum())
    print("  de las %d falsas alarmas del modelo C, %d (%.0f%%) ocurren cuando"
          % (n_fp, fp_lloviendo, 100.0 * fp_lloviendo / max(n_fp, 1)))
    print("  YA esta lloviendo (la lluvia se corto antes de la proxima hora):")
    print("  son eventos de corta duracion, no evitables con precursores.")
    print("  solo %d (%.0f%%) son alarmas prematuras (sin lluvia actual)."
          % (n_fp - fp_lloviendo, 100.0 * (n_fp - fp_lloviendo) / max(n_fp, 1)))

    # ============ RESUMEN ============
    print("\n== RESUMEN EN VALIDACION (anio 6: 2025-2026) ==")
    print("tasa de lluvia en validacion: %.3f%%" % (100 * y_val.mean()))
    csi_b, pod_b, far_b, *_ = metricas(y_val, llueve_ahora[val_mask].astype(int), 0.5)
    print("  Baseline: CSI=%.3f POD=%.3f FAR=%.3f" % (csi_b, pod_b, far_b))
    print("  A       : CSI=%.3f POD=%.3f FAR=%.3f" % (csiA, podA, farA))
    print("  B       : CSI=%.3f POD=%.3f FAR=%.3f" % (csiB, podB, farB))
    print("  C       : CSI=%.3f POD=%.3f FAR=%.3f" % (csiC, podC, farC))
    print("Delta CSI vs baseline: A %+.3f | B %+.3f | C %+.3f"
          % (csiA - csi_b, csiB - csi_b, csiC - csi_b))


if __name__ == "__main__":
    main()
