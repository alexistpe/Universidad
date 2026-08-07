# Definicion formal de lluvia, modelos y resultados con datos reales EDDF

**Proposito:** formalizar QUE se predice (la definicion de "lluvia"), COMO se predice (4 modelos, sus parametros y umbrales ideales), con QUE datos (5 anos de entrenamiento + el ano 6 de validacion en Frankfurt), y CUAL es el mejor metodo y como se mejoro dentro de las bases LIF.

**Estado:** resultados obtenidos y verificables con `prototipos/prototipo_eddf_real.py` (datos en `prototipos/datos/`).

---

## 1. Definicion formal del evento "lluvia"

**Evento:** lluvia = precipitacion horaria **>= 0.25 mm/h**.

Se predice con una hora de antelacion: `y[t+1] = 1` si `prcp[t+1] >= 0.25 mm/h`. Todas las features usan datos hasta `t` (sin fuga de informacion futura).

**Justificacion del valor 0.25 mm/h:**
1. **Resolucion de pluviometro de bajo costo:** las estaciones economicas usan pluviometros de cubeta basculante con resolucion de ~0.2 mm por cubetada. 0.25 mm/h es la lluvia minima que una estacion de bajo costo puede medir de forma fiable; por debajo de ese valor el sensor no distingue lluvia de ruido/mojadura.
2. **DWD (glosario oficial de intensidad de precipitacion):** la DWD clasifica:
   - `Spruehregen` (llovizna): >= 0.1 mm/h en 60 min (moderada 0.1-0.5 mm/h).
   - `Regen` (lluvia): >= 2.5 mm/h en 60 min.
   0.25 mm/h queda por encima de la llovizna medida y por debajo de la lluvia: representa "lluvia medible real" (no simple rocio/llovizna).
3. **Evento raro:** con este umbral, en EDDF llueve el **5.41%** de las horas (2020-2026). Es un evento raro, lo que justifica usar CSI/POD/FAR y no accuracy.

---

## 2. Datos y protocolo (entrenar 5 anos, validar el ano 6)

**Estacion:** 10637 = EDDF, Frankfurt Flughafen (50.05 N, 8.6 E, 111 m), Alemania.
**Fuente:** DWD horaria (via meteostat), variables: temp, rhum, pres, wdir, wspd, prcp.
**Periodo completo:** 2020-01-01 → 2026-07-11 (57193 horas, sin faltantes en las variables usadas).

**Splits:**
| Conjunto | Periodo | n | Tasa de lluvia |
| --- | --- | --- | --- |
| Ajuste (entrena pesos) | 2020-01-01 → 2024-06-30 | 39432 | 5.645% |
| Calibracion (umbrales e hiperparametros) | 2024-07-01 → 2025-06-30 | 8760 | 4.897% |
| **Validacion (anio 6)** | **2025-07-01 → 2026-07-10** | 9001 | 4.877% |

La division es temporal (no se baraja) para respetar la prediccion pasado→futuro. Los hiperparametros y umbrales se eligen SOLO en calibracion; el ano 6 de validacion no se usa para calibrar nada.

**Normalizacion de features:** anomalia estacional z-score respecto de la climatologia diaria (ventana 31 dias) calculada SOLO en el conjunto de ajuste, clip a [-3,3] y mapeo a [0,1]. La precipitacion se normaliza como `min(prcp/1 mm/h, 1)` (intensidad relativa). Contexto temporal: sin/cos(doy) y sin/cos(hora).

**Variables (6 sensores):** T (temp), HR (humedad), P (presion), u y v (viento en componentes), PRECIP (precipitacion actual).

---

## 3. Modelos, estructura y parametros

### 3.1. Baseline: modelo de umbral fijo (persistencia)

**Regla:** lluvia la proxima hora si `prcp[t] >= 0.25 mm/h`.

- **Que se definio como "umbral fijo":** 0.25 mm/h sobre la precipitacion actual. Es la propia definicion formal del evento aplicada a la hora actual.
- **Por que ese valor (justificacion DWD/estacion):**
  - La persistencia ("si llueve ahora, seguira lloviendo") es la **referencia estandar de nowcasting** usada por los servicios meteorologicos (DWD incluye observaciones de precipitacion como predictor primario a cortisimo plazo; WMO la usa como baseline de verificacion de nowcasting).
  - El umbral 0.25 coincide con la resolucion minima del pluviometro de bajo costo (cubeta de ~0.2 mm) y con la frontera llovizna/lluvia del glosario DWD.
- **Componentes:** ninguno. Sin memoria, sin combinacion de variables. Un solo umbral fijo sobre una variable.

### 3.2. Modelo A: unica neurona de alerta con pesos ponderados

**Estructura:** 6 sensores LIF en modo subumbral (actividad continua = filtro EMA fijo) + 4 features de contexto + 1 neurona de alerta = regresion logistica.

```
V_i[t] = α_i·V_i[t-1] + (1−α_i)·x̂_i[t]    6 sensores fijos (EMA), τ_m por variable
a_i[t] = V_i[t]                             actividad continua (membrana)
I_A[t] = Σ w_i·a_i[t] + Σ v_j·ctx_j[t]      alerta: evidencia combinada
P = σ(I_A[t] − θ_A)                         decision probabilistica
```

| Parametro | Valor | Tipo |
| --- | --- | --- |
| τ_m por sensor [h] | T=3, HR=3, P=2, u=1, v=1, PRECIP=1 | **Fijo** (fisica: lentas T/HR, rapidas P/viento/lluvia) |
| V_rest / V_reset | 0 / 0 (modo subumbral) | Fijo |
| Pesos w_i (6) + v_j (4) + bias | aprendidos | **Aprendido** |
| θ_A (umbral de la alerta) | **0.12** (max CSI en calibracion) | **Aprendido** |

Pesos aprendidos: `w = [0.13, 0.342, −0.459, 0.012, −0.211, 0.805]` → PRECIP domina (0.805), HR positiva (0.342), P negativa (−0.459: presion alta → menos lluvia), contexto v = [−0.054, 0.178, −0.05, −0.021].

**Interpretacion de la acumulacion de potencia:** `I_A` es la evidencia instantanea (suma ponderada de las actividades integradas y el contexto). `θ_A` = cuanta evidencia combinada se necesita para declarar lluvia. Como las actividades ya son filtros con memoria, la "potencia" es la persistencia ponderada de las anomalias.

### 3.3. Modelo B: 7 neuronas LIF (6 sensor + 1 alerta)

**Estructura:** cada sensor es una neurona LIF completa que DISPARA spikes con su umbral propio θ_i; la alerta (7ma neurona LIF) integra los spikes con su memoria τ_A y decide con θ_A.

```
V_i[t] = α_i·V_i[t-1] + (1−α_i)·x̂_i[t]    6 neuronas sensor
spike_i[t] = 1 si V_i[t] ≥ θ_i ; V_i <- 0    (disparo + reset)
E_i[t] = EMA(spike_i, τ_A)                    alerta integra spikes (memoria)
I_A[t] = Σ w_i·E_i[t] + Σ v_j·ctx_j[t]
P = σ(I_A[t] − θ_A)
```

| Parametro | Valor | Tipo |
| --- | --- | --- |
| τ_m por sensor [h] | igual que A | Fijo |
| V_rest / V_reset | 0 / 0 (reset total al disparar) | Fijo |
| θ_i por sensor (umbral propio) | percentil 90 de la actividad en ajuste → [0.717, 0.695, 0.734, 0.70, 0.723, 0.089] | **Aprendido** (busqueda en calibracion) |
| Tasa de disparo por sensor | [0.017, 0.016, 0.019, 0.035, 0.039, 0.069] | medicion |
| τ_A (memoria de la alerta) | **1 h** (max CSI en calibracion) | **Aprendido** |
| Pesos w_i (6) | [−0.014, 0.015, −0.241, −0.03, −0.1, 0.987] | Aprendido |
| θ_A | **0.21** (max CSI en calibracion) | **Aprendido** |

**Interpretacion de la acumulacion de potencia:** cada spike es "la variable entro en su rango de alarma". La alerta integra con τ_A = 1 h cuantos spikes (alarmas por variable) llegaron recientemente; `θ_A` = cuantas alarmas ponderadas acumuladas se necesitan para declarar lluvia. Nota: el sensor de PRECIP tiene θ_i muy bajo (0.089) y tasa de disparo alta (6.9%): es el disparador principal.

### 3.4. Modelo C: mejora sobre bases LIF (codificacion graduada de la precipitacion)

**Modificacion de un componente fundamental:** el LIF tiene dos modos de salida — la actividad subumbral (graduada, continua) y el spike (binario). A y B usan UNO de ellos; **C usa ambos para la variable dominante**. El sensor de precipitacion aporta, ademas de su spike, el NIVEL de su membrana (intensidad graduada 0..1). Los demas sensores siguen en modo spike.

```
spike_i[t] como en B (6 canales)
+ nivel_precip[t] = x̂_prcp[t] (intensidad graduada, canal extra)
I_A[t] = Σ w_i·E_i[t] + w_precip·nivel_precip[t] + Σ v_j·ctx_j[t]
```

| Parametro | Valor | Tipo |
| --- | --- | --- |
| τ_m, V_rest, V_reset, θ_i | igual que B (percentil 90) | Fijo / aprendido como B |
| τ_A (memoria de la alerta) | **1 h** (max CSI en calibracion) | **Aprendido** |
| Pesos spikes (6) | [−0.021, 0.021, −0.239, −0.043, −0.091, 0.608] | Aprendido |
| Peso canal graduado PRECIP | **0.424** | Aprendido |
| θ_A | **0.10** (max CSI en calibracion) | **Aprendido** |

**Justificacion meteorologica:** la intensidad actual de la lluvia es el mejor predictor de continuacion (los eventos intensos duran mas; el diagnostico lo confirma: los aciertos tienen PRECIP media 0.705 vs 0.519 en las falsas alarmas). Codificarla de forma graduada en vez de binaria le da a la alerta informacion de "cuanto esta lloviendo", no solo "esta lloviendo o no".

**Interpretacion de la acumulacion de potencia:** la alerta acumula con memoria τ_A la suma ponderada de los spikes de precursores MAS la intensidad graduada de la precipitacion; `θ_A` = potencia acumulada minima para alarmar.

---

## 4. Umbral ideal de cada modelo

| Modelo | θ_A ideal (calibracion) | θ_i / τ_A | Interpretacion del umbral |
| --- | --- | --- | --- |
| A | 0.12 | — | evidencia combinada instantanea minima |
| B | 0.21 | θ_i=percentil 90; τ_A=1 h | alarmas ponderadas acumuladas minimas |
| C | 0.10 | θ_i=percentil 90; τ_A=1 h | potencia acumulada (spikes + intensidad) minima |

**Estabilidad del umbral ideal:** probando que umbral daria el mejor CSI directamente en el ano 6 (sin calibrar), se obtiene ~0.15 para A y B frente a 0.12/0.21 calibrado en el ano 5. La deriva es ~0.05-0.06 y el CSI resultante cambia poco (0.31-0.34), lo que indica que los modelos son **robustos al punto de operacion**, no sobreajustados a un umbral.

---

## 5. Resultados en validacion (anio 6: 2025-2026)

Tasa de lluvia en validacion: 4.88%. Metrics: **CSI** (calidad global, mayor = mejor), **POD** (que fraccion de lluvias detecto), **FAR** (que fraccion de alertas fueron falsas, menor = mejor).

| Modelo | CSI | POD | FAR | Bias | Delta CSI vs baseline |
| --- | --- | --- | --- | --- | --- |
| Baseline (umbral fijo 0.25, persistencia) | 0.336 | 0.503 | **0.497** | 1.00 | — |
| A (alerta unica con pesos) | 0.314 | 0.542 | 0.573 | 1.27 | −0.023 |
| B (7 neuronas LIF) | 0.342 | 0.565 | 0.536 | 1.22 | +0.005 |
| **C (LIF con PRECIP graduada)** | **0.344** | **0.569** | 0.535 | 1.23 | **+0.008** |

**Lectura:**
1. **La persistencia es un baseline muy fuerte** (CSI 0.336): para predecir la lluvia de la proxima hora, "si llueve ahora, seguira" ya es dificil de superar.
2. **Modelo A (continuo + pesos) NO supera al baseline** en estos datos reales (−0.023). Los pesos aprenden meteorologia correcta (PRECIP domina, HR positiva, P negativa), pero el modo continuo diluye el disparo de persistencia.
3. **Modelo B (spikes) supera al baseline** (+0.005 CSI, POD 0.565 vs 0.503): la cuantizacion a spikes actua como filtro de ruido y el umbral propio del sensor de PRECIP crea un disparador de persistencia mas limpio.
4. **Modelo C es el mejor** (+0.008 CSI sobre baseline, POD 0.569): sumar la intensidad graduada de la precipitacion al spike mejora la deteccion sin aumentar el FAR respecto de B.

**Diferencia con los datos sinteticos (prototipos previos):** en los datos sinteticos el Modelo A superaba al baseline, porque la etiqueta sintetica premiaba la persistencia de anomalias. Con datos reales, la persistencia de la precipitacion misma es el predictor dominante, y los spikes (B/C) rinden mejor que la actividad continua (A). Es un cambio de ranking real que muestra por que la validacion con datos reales es imprescindible.

---

## 6. La mejora pedida (aumentar CSI / minimizar FAR manteniendo POD)

**Lo que se probo (y se descarto) para reducir FAR:**
- Confirmacion temporal (exigir K horas seguidas de evidencia): REDUCE el CSI (filtra tambien eventos reales cortos).
- Canales de tendencia (EMA de la derivada de cada variable): no aportan ganancia (los precursores de tendencia no discriminan entre aciertos y falsas alarmas).
- Umbrales de histéresis / compuertas por humedad o presion: colapsan el POD.

**El limite que explica el techo:** en el modelo C, de las 288 falsas alarmas, **218 (76%) ocurren cuando ya esta lloviendo** — es decir, la lluvia se corto antes de la hora siguiente. Son eventos de corta duracion (la lluvia en Frankfurt es intermitente) que **ningun precursor de superficie puede anticipar** con 1 h de antelacion; solo 70 (24%) son alarmas prematuras evitables.

**La mejora disenada que SI funciono (Modelo C):** codificacion graduada de la precipitacion (spike binario + nivel de membrana). Sobre las bases LIF (misma ecuacion, misma arquitectura sensor→alerta), se modifico el componente de salida del sensor dominante para darle a la alerta la intensidad, no solo el evento. Resultado: **CSI 0.344 (el maximo), POD 0.569 (el maximo), y el FAR mas bajo de los modelos LIF (0.535)**.

**Recomendacion de uso:** si la prioridad es deteccion (no perderse lluvias), **Modelo C** con θ_A=0.10. Si la prioridad es minimizar falsas alarmas, usar **Modelo B** con un θ_A mas alto (p. ej. 0.30) para operar en el punto de menor FAR; el trade-off POD/FAR se elige con el umbral, que es el unico parametro a ajustar en el despliegue.

---

## 7. Como reproducirlo

```bash
cd prototipos
python3 prototipo_eddf_real.py
```

Requiere: `numpy`, `pandas` y los datos `datos/eddf_10637_horario_2020_2026.csv` (ya incluidos). El codigo usa solo numpy para las neuronas LIF (sin sklearn ni librerias SNN).
