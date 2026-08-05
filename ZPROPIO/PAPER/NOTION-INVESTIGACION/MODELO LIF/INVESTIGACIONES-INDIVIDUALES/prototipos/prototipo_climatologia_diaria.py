"""Prototipo de climatologia diaria suavizada (granularidad A).

Implementa y valida la climatologia por day-of-year con ventana centrada
circular (+-15 dias) descrita en Codificacion_Estacionalidad_Viento.md, B.6.5.
Usa datos sinteticos horarios con ciclo estacional + diurno + ruido, de modo
que se puede ejecutar sin esperar los datos reales de EDDF.

Salidas de control:
  1) Rango y suavidad de mu(d) / sd(d) (sin saltos en fronteras de mes).
  2) Media anual de la anomalia ~ 0 y desvio ~ 1.
  3) Las 4 features de contexto temporal sin/cos(doy) + sin/cos(hora).
"""

import numpy as np
import pandas as pd


def sintetizar_horario(anios=5, seed=42):
    rng = np.random.default_rng(seed)
    n = anios * 8760
    idx = pd.date_range("2020-01-01", periods=n, freq="h")
    doy = idx.dayofyear.to_numpy()
    hora = idx.hour.to_numpy()

    ciclo_anual = 10.0 + 8.0 * np.cos(2 * np.pi * (doy - 197) / 365.25)
    ciclo_diurno = 4.0 * np.cos(2 * np.pi * (hora - 14) / 24)
    ruido = rng.normal(0, 1.5, n)

    df = pd.DataFrame(
        {
            "T": ciclo_anual + ciclo_diurno + ruido,
            "P": 1013.0 - 6.0 * np.sin(2 * np.pi * doy / 365.25) + rng.normal(0, 2.0, n),
            "doy": doy,
            "hour": hora,
        },
        index=idx,
    )
    return df


def climatologia_diaria(train_df, var, win=15, min_n=50):
    doy = train_df["doy"].to_numpy().astype(int)
    x = train_df[var].to_numpy()
    mu, sd = np.full(367, np.nan), np.full(367, np.nan)
    for d in range(1, 367):
        delta = np.abs(((doy - d + 183) % 365) - 183)
        mask = delta <= win
        if mask.sum() >= min_n:
            mu[d] = np.mean(x[mask])
            sd[d] = np.std(x[mask]) + 1e-12
    dias = np.arange(1, 367)
    ok = ~np.isnan(mu[dias])
    mu_lin = np.interp(dias, dias[ok], mu[dias][ok])
    sd_lin = np.interp(dias, dias[ok], sd[dias][ok])
    mu_out = np.empty(367)
    sd_out = np.empty(367)
    mu_out[1:] = mu_lin
    sd_out[1:] = sd_lin
    mu_out[0] = mu_lin[0]
    sd_out[0] = sd_lin[0]
    return mu_out, sd_out


def main():
    df = sintetizar_horario()

    df_train = df.iloc[: int(len(df) * 0.7)]
    df_test = df.iloc[int(len(df) * 0.7):]

    mu_T, sd_T = climatologia_diaria(df_train, "T")
    mu_P, sd_P = climatologia_diaria(df_train, "P")

    anom_train = (df_train["T"].to_numpy() - mu_T[df_train["doy"].to_numpy().astype(int)]) / sd_T[
        df_train["doy"].to_numpy().astype(int)
    ]
    anom_test = (df_test["T"].to_numpy() - mu_T[df_test["doy"].to_numpy().astype(int)]) / sd_T[
        df_test["doy"].to_numpy().astype(int)
    ]

    saltos = np.max(np.abs(np.diff(mu_T)))
    print("== Control 1: suavidad de la climatologia ==")
    print(f"max salto entre dias consecutivos de mu_T: {saltos:.4f} °C/dia")
    print(f"mu_T(1 ene) = {mu_T[1]:.2f} °C | mu_T(15 jul) = {mu_T[196]:.2f} °C")
    print(f"mu_P(1 ene) = {mu_P[1]:.2f} hPa | mu_P(15 jul) = {mu_P[196]:.2f} hPa")

    print("\n== Control 2: anomalias sobre train y test ==")
    print(f"train: media = {anom_train.mean():.3f}  sd = {anom_train.std():.3f}")
    print(f"test : media = {anom_test.mean():.3f}  sd = {anom_test.std():.3f}")

    print("\n== Control 3: features de contexto temporal ==")
    df["doy_sin"] = np.sin(2 * np.pi * df.index.dayofyear / 365.25)
    df["doy_cos"] = np.cos(2 * np.pi * df.index.dayofyear / 365.25)
    df["hod_sin"] = np.sin(2 * np.pi * df.index.hour / 24)
    df["hod_cos"] = np.cos(2 * np.pi * df.index.hour / 24)
    print(df[["doy_sin", "doy_cos", "hod_sin", "hod_cos"]].describe().loc[["min", "max", "mean"]])

    print("\n== Control 4: correlacion anomalia -> lluvia sintetica ==")
    df["T_anom"] = (df["T"].to_numpy() - mu_T[df["doy"].to_numpy().astype(int)]) / sd_T[
        df["doy"].to_numpy().astype(int)
    ]
    df["lluvia"] = (df["T_anom"] > 0.5).astype(int) | (df["hod_sin"] > 0.7).astype(int)
    print(f"tasa de lluvia sintetica: {df['lluvia'].mean():.3f}")
    print(f"P(lluvia | anomalia>0.5): {df.loc[df['T_anom'] > 0.5, 'lluvia'].mean():.3f}")


if __name__ == "__main__":
    main()
