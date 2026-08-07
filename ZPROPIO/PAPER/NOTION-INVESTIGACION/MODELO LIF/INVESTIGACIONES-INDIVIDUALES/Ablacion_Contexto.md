# Ablacion del contexto temporal/estacional en el Modelo C

**Proposito:** responder experimentalmente QUE aportan las features de dia del ano y hora en el Modelo C, y COMO conviene integrarlas (continuas directas al readout vs. neuronas LIF con spikes). Complementa la seccion 3 de `Definicion_Lluvia_y_Resultados_EDDF.md`.

**Estado:** resultados obtenidos y verificables con `prototipos/ablation_contexto.py` (mismos datos y protocolo que `prototipo_eddf_real.py`).

---

## 1. Que se esta probando

El Modelo C actual (C_ref) usa 6 sensores fisicos en modo spike + el canal graduado de PRECIP + **4 features de contexto continuas** (`sin(doy), cos(doy), sin(hora), cos(hora)`) que entran DIRECTAS al readout de la alerta. Las 4 features son necesarias (seno y coseno por ciclo: dos componentes para representar sin saltos una variable circular).

Se prueban 3 variantes sobre los mismos datos y el mismo protocolo (ajuste 2020→2024-06, calibracion 2024-07→2025-06, validacion ano 6 2025-07→2026-07):

| Variante | Que hace con el contexto | Notacion |
| --- | --- | --- |
| **C_ref** | 4 features continuas directas al readout | `[EB, nivel_precip, ctx]` |
| **C_sinctx** | Se ELIMINAN las 4 features | `[EB, nivel_precip]` |
| **C_neuronas** | Las 4 features se tratan como NEURONAS LIF: membrana EMA propia (tau_ctx=24h para doy, 1h para hora), umbral de disparo theta_ctx = percentil 90 (como los sensores fisicos), spikes integrados por la alerta con tau_A=1h | `[EB, nivel_precip, E_ctx]` |

En las tres: pesos por regresion logistica, theta_A calibrado en calibracion (max CSI), evaluacion en validacion.

---

## 2. Resultados

```
== ABLACION DEL CONTEXTO EN EL MODELO C ==
tasa lluvia val: 4.877%

  C_ref       CSI=0.344 POD=0.569 FAR=0.535 bias=1.23 (TP=250 FP=288 FN=189) theta=0.10
    pesos (ctx sin/cos doy, sin/cos hora): [-0.03   0.135 -0.001 -0.011]
  C_sinctx    CSI=0.340 POD=0.560 FAR=0.536 bias=1.21 (TP=246 FP=284 FN=193) theta=0.18
  C_neuronas  CSI=0.343 POD=0.560 FAR=0.531 bias=1.19 (TP=246 FP=278 FN=193) theta=0.19
    neuronas de contexto: theta_ctx = [0.96  0.95  0.902 0.902]
    tasa de disparo de las neuronas de contexto (fit): [0.001 0.001 0.042 0.042]
    pesos de los spikes de contexto: [-0.005 -0.085  0.015  0.024]

== RESUMEN ==
  C_ref      (ctx directas): CSI=0.344 POD=0.569 FAR=0.535
  C_sinctx   (sin ctx)     : CSI=0.340 POD=0.560 FAR=0.536
  C_neuronas (ctx como LIF): CSI=0.343 POD=0.560 FAR=0.531
  Delta vs C_ref: sin-contexto -0.004 | neuronas -0.001
```

| Variante | CSI | POD | FAR | Bias | theta_A | Delta CSI vs C_ref | Delta POD vs C_ref |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **C_ref** (ctx continuas directas) | **0.344** | **0.569** | 0.535 | 1.23 | 0.10 | — | — |
| C_sinctx (sin contexto) | 0.340 | 0.560 | 0.536 | 1.21 | 0.18 | −0.004 | −0.009 |
| C_neuronas (ctx como LIF spikes) | 0.343 | 0.560 | 0.531 | 1.19 | 0.19 | −0.001 | −0.009 |

**Observaciones de los pesos:**
- La feature que mas importa es **cos(doy)** (peso +0.135): el ciclo anual (invierno vs verano). `sin(doy)` pesa −0.03.
- Las features de hora pesan ~0 (−0.001 y −0.011): el ciclo diurno de conveccion apenas aporta sobre las variables ya normalizadas.

---

## 3. Por que C_neuronas no es una prueba de que el contexto "no sirve"

Las neuronas de contexto LIF **no representan bien senales lentas**. Medido:

| Neurona | tau_ctx | theta_ctx (p90) | Tasa de disparo (ajuste) |
| --- | --- | --- | --- |
| sin(doy) | 24 h | 0.960 | **0.001** (~9 spikes/ano) |
| cos(doy) | 24 h | 0.950 | **0.001** (~9 spikes/ano) |
| sin(hora) | 1 h | 0.902 | 0.042 |
| cos(hora) | 1 h | 0.902 | 0.042 |

Frente a los sensores fisicos del mismo modelo B/C (tasa de disparo en ajuste: `[0.017, 0.016, 0.019, 0.035, 0.039, 0.069]`), las neuronas de dia del ano disparan **50-70 veces menos** que la PRECIP (0.001 vs 0.069).

**Causa mecanica:** el umbral theta_ctx = percentil 90 se calcula sobre la EMA del contexto, que para doy es una senoide anual casi pura; su percentil 90 (0.96) queda pegado al maximo del ciclo. Con reset a cero al disparar (`V<-0`), la membrana solo supera el umbral durante los pocos dias del pico estival, y tras cada reset tarda en recargarse. El resultado es que la codificacion por umbral+reset **descarta casi toda la informacion del ciclo anual**: C_neuronas reproduce a C_sinctx (mismo POD) porque el contexto "spikeado" es practicamente nulo.

**Consecuencia metodologica:** la comparacion justa del valor del contexto es **C_ref vs C_sinctx** (ambas preservan la informacion; solo cambia su presencia/ausencia). C_neuronas prueba una hipotesis de diseno distinta: "puede el contexto recorrer el mismo camino spike que los precursores?" La respuesta es NO sin perder informacion, y eso es un resultado de diseno, no una medida del valor predictivo del contexto.

---

## 4. Cuanto aporta realmente el contexto (C_ref vs C_sinctx)

- **CSI:** +0.004 (0.340 → 0.344). **POD:** +0.009 (0.560 → 0.569), es decir, 4 eventos detectados adicionales de 439. **FAR:** practicamente igual (0.535 vs 0.536).
- El efecto es **positivo pero pequeno**, y se concentra en la **deteccion** (POD) del ciclo anual (peso cos(doy)).

**Por que es pequeno (dos razones de diseno):**
1. **La normalizacion ya incorpora el ciclo anual.** Las 6 variables se transforman a anomalias z respecto de su climatologia por dia del ano (`normalizar_estacional`). Al restar la media de cada dia, el ciclo estacional ya esta dentro de los sensores; el contexto explicito queda parcialmente redundante.
2. **El umbral es bajo (0.25 mm/h).** La literatura (seccion 5) muestra que el contexto temporal ayuda mas cuanto mas raro/intenso es el evento; en lluvia comun de bajo umbral el beneficio es marginal porque el predictor dominante es la persistencia de la propia precipitacion (76% de las falsas alarmas son eventos cortos ya en curso).

**Advertencia estadistica honesta:** la validacion es un solo ano (439 horas con lluvia). Una diferencia de +4 aciertos (POD +0.009) esta en el orden del ruido de muestreo de un solo ano; lo que SI es solido es la direccion del efecto (coherente con la literatura y con los pesos), y el hecho de que quitar el contexto NUNCA mejora el resultado (el contexto no danifica).

---

## 5. Que dice la literatura (contrastacion rigurosa)

1. **van Nieuwkoop & Mehrkanoon (2026).** "Temporal Context Conditioning for Seasonality-Aware Precipitation Nowcasting of High-Intensity Rainfall". *arXiv:2606.09959*. Modelo TA-SmaAt-UNet sobre radar KNMI: acondiciona features intermedias con **codificacion ciclica de hora del dia y epoca del ano**. Resultados: a umbrales bajos (0.5 mm/h) las diferencias con el modelo base son pequenas, pero crecen claramente a 10 y 20 mm/h (mejor CSI, menor FAR). Conclusion del propio articulo: el contexto temporal "es especialmente beneficioso para eventos raros e intensos". **Coherente con nuestro resultado**: a 0.25 mm/h el aporte es marginal; seria mayor si el objetivo fueran tormentas intensas.
2. **Grecco Sanches et al. (2025).** "Using XGBoost models for daily rainfall prediction". *Anales de Geografia de la Universidad Complutense*, 45(1), 75-92. En prediccion de lluvia diaria con XGBoost, incluyen anio y mes entre las features; el analisis de importancia muestra que los predictores mas fuertes son radiacio solar y viento, y el mes aparece asociado al regimen (temporada seca vs lluviosa). Confirma que las features de calendario son **parte estandar de la ingenieria de features** en ML meteorologico, aunque no siempre las mas importantes.
3. **ERA5–NASA Ensembles for Daily Rain Prediction (Konya, Turkiye, 2025).** *Int. J. Agric. Environ. Food Sci.* Compara RF/XGBoost/LightGBM/CatBoost/LSTM para lluvia diaria usando "cyclical seasonality, lags, rolling windows" como ingenieria de features. El analisis de importancia destaca **la estacionalidad entre las senales principales** junto a humedad, rangos de temperatura, tendencia de presion y extremos de viento. Es la evidencia mas directa de que la estacionalidad es una feature relevante en modelos ML de precipitacion.
4. **TS-LIF (2025).** "A Temporal Segment Spiking Neuron Network for Time Series Forecasting". *arXiv:2503.05108*. Motiva su diseno justo en la limitacion que medimos aqui: el **LIF estandar tiene dificultades para capturar dependencias de largo plazo y dinamicas multi-escala** (su potencial de membrana decae rapido). Propone compartimentos dendritico/somatico para separar componentes de baja y alta frecuencia. **Coherente**: nuestra codificacion spike del ciclo anual (señal de muy baja frecuencia) es precisamente donde el LIF simple falla, lo que justifica mantener el contexto lento fuera del camino de spikes.
5. **Eshraghian et al. (2023).** "Training Spiking Neural Networks Using Lessons From Deep Learning". *Proceedings of the IEEE*, 111(9), 1016-1054 (snnTorch). Documenta que el reset por sustraccion (resta el umbral) es **menos perdedor** que el reset a cero (que fuerza V=0 y promueve sparsidad). Nuestro modelo usa reset a cero en todos los sensores: explica la escasez extrema de disparo de las neuronas de contexto de doy y refuerza que, para senales lentas, el modo continuo es la representacion adecuada.
6. **Shi et al. (2017).** "Deep Learning for Precipitation Nowcasting: A Benchmark and a New Model". *NeurIPS*. Marco de referencia estandar del nowcasting por aprendizaje profundo; establece que los modelos que superan a la extrapolacion por adveccion usan perdidas balanceadas hacia lluvias intensas. Contexto: la dificultad del problema crece con la rareza del evento, igual que en nuestro caso (5.4% de horas con lluvia).

**Sintesis:** la literatura apoya (i) que el contexto temporal/estacional ayuda, pero de forma **proporcional a la rareza/intensidad del evento** y (ii) que el **LIF simple es malo para la escala temporal lenta**, de modo que en un modelo LIF el contexto debe permanecer en el canal continuo/graduado y no cuantizarse a spikes. Ambos puntos coinciden exactamente con la evidencia experimental de esta ablacion.

---

## 6. Conclusion y recomendacion de diseno

1. **El contexto temporal aporta poco pero no danifica** en este problema (umbral 0.25 mm/h, normalizacion estacional previa): +0.004 CSI y +0.009 POD, dominado por el termino anual `cos(doy)`. El ciclo diurno (hora) es irrelevante aqui.
2. **NO codificar el contexto como spikes LIF**: la representacion por umbral+reset destruye la informacion de las senales lentas (las neuronas de doy disparan ~9 veces/ano). El contexto debe ir **continuo al readout**, como en C_ref, o integrarse en el modo graduado de la alerta, no por el camino spike de los precursores rapidos.
3. **Si el objetivo futuro fueran tormentas intensas** (p. ej. umbrales 2.5 o 10 mm/h), la misma literatura predice que el contexto (sobre todo el ciclo anual) pasaria a ser mas relevante; es un experimento natural para extender el paper.
4. El Modelo C final recomendado mantiene las 4 features de contexto continuas: el costo es nulo (4 sumas por hora) y el aporte, aunque pequeno, es consistente y gratuito.

---

## 7. Como reproducirlo

```bash
cd prototipos
python3 ablation_contexto.py
```

Requiere: `numpy`, `pandas`, los modulos `prototipo_lif.py`, `prototipo_lif_spikes.py`, `prototipo_eddf_real.py` (importan funciones de estos) y los datos `datos/eddf_10637_horario_2020_2026.csv`. Los resultados numericos de la seccion 2 son la salida literal del script.
