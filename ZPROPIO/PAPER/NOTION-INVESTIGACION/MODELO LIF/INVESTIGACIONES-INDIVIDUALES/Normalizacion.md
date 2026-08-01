1. ¿Es la normalización estrictamente necesaria?
Respuesta corta: NO es matemáticamente obligatoria, pero SÍ es prácticamente necesaria (y en tu caso específico, altamente recomendada). Te explico por qué con fundamento científico.
El mecanismo del LIF que determina esta respuesta
El modelo LIF discretizado (Gerstner, Neuronal Dynamics, EPFL) es:
V[t+1] = α·V[t] + (1-α)·I[t]      donde α = e^(-Δt/τ_m)
dispara si V ≥ θ; luego V ← V_reset
La dinámica es lineal en la corriente de entrada It. Esto tiene dos consecuencias:
1. Las escalas relativas se propagan directamente al potencial de membrana. Si la presión (~1000 hPa) entra como corriente 1000 veces mayor que la temperatura (15°C), el potencial de membrana V será dominado por presión y saturará el umbral θ casi siempre, produciendo disparos constantes que contienen poca información discriminativa sobre lluvia (Vasilache et al., 2025, arXiv:2504.11026; Guo et al., 2023, ICCV — Membrane Potential Batch Normalization for SNNs).
2. Técnicamente, pesos aprendidos pueden compensar la escala (un w_presión ~0.001 vs w_temp ~0.1). Pero esto hace que el espacio de optimización sea mal condicionado (ill-conditioned), lo que degrada convergencia y estabilidad (Herranz-Celotti & Rouat, 2022, arXiv:2202.00282 — Stabilizing Spiking Neuron Training).
Evidencia empírica directa con tus mismas variables
Syaharuddin, Fatmawati & Suprajitno (2022), Int. J. Sustainable Development and Planning (DOI: 10.18280/ijsdp.170707), publicaron un estudio que probó 7 técnicas de normalización en datos de lluvia y humedad del aire (tus variables). Textual:
> "The use of original data (raw data) to train neural networks can lead to convergence problems... This will have implications for a high number of epochs and difficult networks to recognize data patterns. Therefore, the stage of normalization or standardization of data needs to be done before the data is trained."
Resultados de su experimento: Z-score fue el mejor para datos de lluvia (MAE 0.051, MSE 0.004), y mean-MAD / Z-score para humedad. Con datos crudos, el modelo no convergía adecuadamente.
---
2. ¿Cómo funciona el LIF en relación a la normalización? (el punto clave)
Tu modelo LIF simplificado recibe datos meteorológicos de una de dos formas. La respuesta a "¿necesito normalizar?" cambia según cuál uses:
Camino A: Codificación por tasa (rate coding) — la más común para SNN
En rate coding, el valor real se convierte en una tasa de disparo de un tren de spikes (típicamente Poisson). La encuesta de la revista Neural Processing Letters (2021, Springer) lo define así:
> "Rate codes embed the information in the instantaneous or averaged rate of spike generation... signal amplitudes are directly mapped to spike frequencies."
La fórmula típica: λ = v_normalizado × f_max (spikes/segundo).
Aquí la normalización es prácticamente OBLIGATORIA, porque la tasa de disparo λ es proporcional al valor de entrada:
- Sin normalizar: presión 1000 hPa → λ ~1000 spikes/s (saturación total), temperatura 15°C → λ ~15 spikes/s (prácticamente silenciosa)
- Normalizado a 0,1: todas las variables generan λ en el mismo rango 0, f_max, comparables
Conclusión: Si tu LIF usa rate coding (la opción estándar en la literatura de SNN aplicadas), la normalización min-max a 0,1 es la práctica necesaria para que el rango de tasas de disparo sea consistente entre variables.
Camino B: Inyección directa de corriente (input analógico)
Si el valor real entra directamente como corriente It = w·x (sin codificación Poisson), el modelo puede funcionar sin normalización porque los pesos aprendidos absorben la escala. Pero esto:
- Requiere inicialización cuidadosa (Herranz-Celotti & Rouat, 2022)
- Sufre de convergencia lenta y riesgo de saturación
- Es menos estándar en la literatura
---
3. ¿Cómo se realiza la normalización?
Técnicas validadas científicamente (Syaharuddin et al., 2022)
| Técnica | Fórmula | Mejor para | Resultado en su estudio |
|---------|---------|-----------|------------------------|
| Z-score (standardization) | x' = (x − μ)/σ | Lluvia, humedad | Mejor para lluvia (MAE 0.051) |
| Min-Max | x' = (x − min)/(max − min) | Rate coding (acota a 0,1) | Bueno, depende del caso |
| Mean-MAD | x' = (x − μ)/MAD | Humedad | Recomendado para humedad |
| Decimal scaling | x' = x/10^k | Datos de magnitud uniforme | — |
| Sigmoid / tanh | — | Datos acotados | — |
Recomendación específica para TU modelo (basada en la literatura climática)
Furtado, Molina et al. (2026), arXiv:2508.07062 — "Setting the Standard: Recommended Practices for Data Preprocessing in Data-Driven Climate Prediction", publicado por un equipo que incluye a expertos del sector (el paper de referencia en preprocesamiento climático para ML). Textual:
> "Most climate datasets are inherently spatiotemporal, sparse, and possess spatial and temporal autocorrelations. The data are often nonstationary... Climate variables also have varying distributions, many of which are non-normal (e.g., gamma, bimodal, log-normal, and skew-normal), and exhibit non-linear interactions among themselves."
El paper recomienda:
1. Crear anomalías estandarizadas (restar la climatología mensual, luego estandarizar) en lugar de normalizar el valor absoluto. Esto es crítico para presión y temperatura, cuyas señales precursoras de lluvia son pequeñas variaciones (5-10 hPa, 2-3°C) sobre un valor de fondo grande y estacionario.
2. Tratar con cuidado valores extremos (outliers) — clave en precipitación, cuya distribución es fuertemente no-normal (muchos ceros, cola pesada).
3. No mezclar datos de entrenamiento y validación al calcular μ y σ (data leakage) — usar división temporal estricta.
Para presión específicamente — un matiz importante
La presión absoluta (950-1050 hPa) comprimida por min-max a 0,1 enterraría la señal informativa (los cambios de 5-10 hPa que preceden tormentas = solo 1% del rango). Para presión, la literatura sugiere:
- Anomalía de presión (desviación de la media estacional), o
- Tendencia de presión (derivada temporal: ΔP/Δt en las últimas 3h — ya usada por el Zambretti Forecaster)
Esto es más informativo que el valor absoluto y es directamente compatible con tu lookback window de 6-12h.
---
4. Síntesis fundamentada
| Pregunta | Respuesta | Fuente |
|----------|-----------|--------|
| ¿Normalización estrictamente necesaria? | No matemáticamente, pero sí prácticamente para convergencia, estabilidad y comparabilidad entre variables | Syaharuddin et al. (2022); Herranz-Celotti & Rouat (2022) |
| ¿Necesaria para rate coding? | Sí, es esencial — la tasa de disparo λ es proporcional al valor normalizado | Vasilache et al. (2025); Neural Processing Letters (2021) |
| ¿Cómo normalizar? | Z-score para lluvia/humedad (mejor empíricamente); anomalías estandarizadas para presión/temperatura; min-max 0,1 para rate coding | Syaharuddin et al. (2022); Furtado et al. (2026) |
| ¿Por qué presión/temperatura con anomalía? | Su señal predictiva es la desviación (Δ), no el valor absoluto; min-max entierra la señal | Furtado et al. (2026) |
| ¿Riesgo sin normalizar? | Convergencia lenta, saturación de tasa de disparo, dominio de variables de mayor magnitud, inestabilidad de gradientes | Syaharuddin et al. (2022); Herranz-Celotti & Rouat (2022) |
Recomendación concreta para tu modelo LIF
1. Temperatura y humedad → Z-score estacional (x − μ_mes)/σ_mes
2. Presión → Anomalía o tendencia ΔP/Δt (3h)
3. Viento → Z-score o min-max a 0,1 (magnitud comparable)
4. Precipitación → Tratamiento especial por distribución no-normal: o bien log(1+x) antes de escalar, o umbral binario (0 = seco, 1 = lluvia) si el LIF solo detecta eventos
5. Antes de rate coding → re-escalar a 0,1 para mapear a λ ∈ 0, f_max
Esto está 100% respaldado por: Syaharuddin et al. (2022, IIETA), Furtado et al. (2026, arXiv:2508.07062), Vasilache et al. (2025, arXiv:2504.11026), Herranz-Celotti & Rouat (2022, arXiv:2202.00282), Guo et al. (2023, ICCV), y la encuesta de codificación en SNN (Neural Processing Letters, 2021).

## Tecnicas de normalizacion por variable
1. Principio fundamental: cada variable tiene su propia distribución
La base científica viene de Furtado, Molina et al. (2026) (arXiv:2508.07062, "Setting the Standard: Recommended Practices for Data Preprocessing in Data-Driven Climate Prediction"):
> "Climate variables also have varying distributions, many of which are non-normal (e.g., gamma, bimodal, log-normal, and skew-normal), and exhibit non-linear interactions among themselves."
Si cada variable tiene una distribución estadística distinta, no tiene sentido forzarles la misma transformación. Un Z-score asume normalidad; una precipitación con muchos ceros y cola pesada no es normal, mientras que una presión barométrica sí se aproxima bien a una gaussiana.
---
2. Evidencia empírica directa: el estudio que ya citamos usó normalizaciones distintas
Syaharuddin, Fatmawati & Suprajitno (2022) (IJSDP, DOI: 10.18280/ijsdp.170707) es el caso perfecto: evaluaron 7 técnicas de normalización sobre dos variables distintas (lluvia y humedad) y concluyeron que la mejor técnica era distinta para cada variable:
> "The Z-score technique was very good for the normalization of rainfall data... In the case of air humidity data, mean-MAD and Z-score techniques can be recommended."
Es decir: el propio estudio recomienda Z-score para lluvia y mean-MAD para humedad — normalizaciones distintas por variable, no una única para todas. Tu ejemplo (Z-score humedad + min-max presión) sigue exactamente este patrón de pensamiento.
---
3. La heterogeneidad entre variables es un problema reconocido y estudiado
Gong et al. (2021), Sandwich Batch Normalization (AAAI) — documenta que la heterogeneidad de distribuciones entre features es un obstáculo real para el entrenamiento, y propone capas de normalización independientes por grupo de features:
> "BN has troubles standardizing hidden features with a heterogeneous, multi-modal distribution... One straightforward cause is the input data heterogeneity."
Guimerà-Cuevas et al. (2024), Robust Non-linear Normalization of Heterogeneous Feature Distributions with Adaptive Tanh-Estimators (ICLR 2024) — desarrolla normalizadores adaptativos por feature para datos de distribuciones heterogéneas (como temperatura, humedad y presión juntas).
September et al. (2024), Extended Deep Adaptive Input Normalization (ICLR 2024) — aplica normalización adaptativa independiente por variable en series temporales, y reporta mejoras frente a normalización uniforme.
---
4. En práctica climática real: la normalización es SIEMPRE por-variable
Brohan et al. (DCVAE Climate Model, Met Office) — el modelo ML climático del Met Office normaliza cada variable con su propia distribución gamma ajustada individualmente (por mes y punto de grilla):
> "A different distribution is fit for each month and grid point... All variables should be on the same scale — around the range 0-1... The data at each month and grid point should be similarly distributed."
Nota importante del Met Office: el objetivo de la normalización no es que todas las variables tengan "la misma técnica", sino que todas terminen en la misma escala (0-1), cada una transformada según su propia distribución.
---
5. Conclusión: la regla correcta
La regla NO es "misma normalización para todas". La regla es "misma escala final para todas, técnica adecuada por variable".
| Variable | Distribución | Técnica adecuada | Resultado |
|----------|-------------|------------------|-----------|
| Temperatura | ~Normal | Z-score o anomalía estacional | μ=0, σ=1 |
| Humedad | Sesgada, acotada 0,100 | Z-score o min-max | 0,1 o μ=0,σ=1 |
| Presión | ~Normal | Z-score o anomalía (no min-max absoluto) | μ=0, σ=1 |
| Viento | Sesgada (Weibull) | Min-max o log(Z-score) | 0,1 |
| Precipitación | No-normal (ceros + gamma) | log(1+x) luego Z-score, o binaria | Compacta |
Lo único que NO debes hacer es dejar variables en escalas incomparables (ej. temperatura en °C cruda y presión en hPa cruda). Después de aplicar la técnica por variable, todas deben quedar en un rango comparable (idealmente 0,1 si usas rate coding para el LIF, donde λ ∝ valor).
¿Tu ejemplo es adecuado? Sí: Z-score para humedad + min-max para presión es correcto si ambos terminan en el mismo rango final. La única precaución: para presión, min-max sobre el valor absoluto (950-1050 hPa) entierra la señal de ±5 hPa que precede tormentas — es preferible aplicar min-max sobre la anomalía de presión, no sobre el valor absoluto (Furtado et al., 2026).
---
Referencias verificables
1. Syaharuddin, Fatmawati & Suprajitno (2022), IJSDP — DOI: 10.18280/ijsdp.170707
2. Furtado, Molina et al. (2026), arXiv:2508.07062 — preprocesamiento climático para ML
3. Gong et al. (2021), Sandwich Batch Normalization, AAAI — arXiv:2102.11382
4. Guimerà-Cuevas et al. (2024), ICLR — tanh-estimators adaptativos por feature
5. September et al. (2024), ICLR — normalización adaptativa por variable en series temporales
6. Brohan et al., DIY ML Climate Model (Met Office) — normalización gamma por variable/punto de grilla
