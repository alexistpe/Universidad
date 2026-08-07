# Decision de diseno: neuronas sensor fijas vs entrenables

**Proposito:** Determinar si las 6 neuronas sensor del modelo LIF deben ser filtros fijos (diseno actual) o neuronas con parametros aprendidos por variable (propuesta), y cuantificar que cambia en arquitectura, entrenamiento, complejidad y resultados esperados.

**Estado:** Analisis de decision. Complementa `Diseno_Modelo_LIF.md` y `Codificacion_Estacionalidad_Viento.md` (Pregunta D).

---

## 1. Resumen ejecutivo

- El diseno actual usa 6 neuronas sensor como **filtros temporales fijos** (IIR/EMA) y entrena SOLO la neurona de alerta (regresion logistica, 11 pesos libres). Es una arquitectura de **reservorio computacional**, legitimada por la literatura (Jaeger 2001; Lukosevicius & Jaeger 2009).
- La propuesta (que cada neurona sensor aprenda sus propios rangos/patrones y emita spikes hacia la alerta) es valida y esta respaldada por la literatura de **umbrales aprendibles por neurona** (LTMD, NeurIPS 2022) y **tiempo de membrana aprendible** (PLIF, Fang et al. 2021). La intuicion de que "mas parametros por neurona puede mejorar precision" tiene apoyo empirico.
- Sin embargo, "entrenar cada neurona individualmente" en modo supervisado **no existe como tal**: la etiqueta de lluvia es UNA por hora, no hay etiqueta por neurona. Las neuronas intermedias se entrenan **conjuntamente** con gradiente sustituto (Neftci et al. 2019), o sus parametros se fijan/seleccionan por busqueda en validacion.
- La union de variables en la alerta es **inherente e inevitable**: en cualquier arquitectura, la alerta recibe UNA senal escalar (la suma ponderada de las contribuciones de las variables). La diferencia entre disenos es *que se combina* (actividad continua vs spikes) y *donde se aprende* (solo alerta vs tambien sensores).
- **Recomendacion:** camino intermedio. Mantener 1 neurona LIF por variable (filosofia LIF intacta), pero hacer **aprendibles los umbrales de disparo θ_i** (rango por variable) manteniendo τ_m fijo con analisis de sensibilidad. Esto da "cada neurona aprende su rango" con solo +6 parametros, baja complejidad e interpretabilidad maxima. Evaluar con ablation CSI contra el diseno actual sobre los mismos datos.

---

## 2. Pregunta de diseno

¿Deben las neuronas sensor ser fijas (solo la alerta aprende) o cada variable debe tener una neurona LIF que aprenda sus propios rangos y patrones y alimente con spikes a la alerta?

La hipotesis a evaluar es: *"si cada variable pasa por una neurona que aprendio su propio rango y patron, la alerta recibe informacion mas util (una decision por variable) en vez de un valor continuo interpretado por la alerta, lo que aumenta la precision."*

---

## 3. Modelo actual (como funciona la union de variables)

### 3.1. Arquitectura

```
Capa 1 (fija): 6 neuronas sensor
   V_i[t] = α_i·V_i[t-1] + (1-α_i)·x̂_i[t]      (filtro IIR / EMA)
   τ_m,i fijado por fisica (2-4 h), θ_i = percentil 90-95 del train
   Salida: actividad continua a_i[t] = V_i[t]

Contexto: sin/cos(doy), sin/cos(hora)            (4 features, no son LIF)

Capa 2 (entrenable): neurona de alerta = regresion logistica
   I_A[t] = Σ_i w_i·a_i[t] + Σ_j v_j·ctx_j[t]    (UNA senal escalar)
   P(lluvia) = σ(I_A − θ_A)
```

### 3.2. La union de variables (respuesta directa)

**Si, la alerta recibe una unica senal de "carga": la suma ponderada de todas las variables.** Concretamente:

- Cada sensor manda su actividad `a_i[t]` (que tan anomala/persistente esta su variable).
- La alerta las multiplica por pesos `w_i` y las SUMA con el contexto: `I_A[t]`.
- `I_A[t]` es un escalar por paso temporal: la "corriente" que carga la membrana de la alerta `V_A[t] = α_A·V_A[t-1] + (1−α_A)·I_A[t]`.
- La alerta dispara cuando `V_A ≥ θ_A`.

Con spikes seria identico pero con `a_i[t] ∈ {0,1}`: `I_A[t] = Σ_i w_i·spike_i[t]`. Sigue siendo un escalar ponderado; la diferencia es que la alerta integra *eventos* con su propia memoria `τ_A` (el timing importa: "recibir suficientes spikes").

**Punto clave:** la combinacion no es un defecto del diseno actual — es la definicion de una alerta. Un clasificador binario, por construccion, converge toda la informacion a una sola decision. La pregunta real no es "combinar o no" sino "que se combina y donde se aprende".

### 3.3. Parametros del diseno actual

| Parametro | Valor | Aprendido |
| --- | --- | --- |
| τ_m,i (6 sensores) | fijo por fisica (2-4 h) | No |
| θ_i (6 sensores) | percentil 90-95 del train | No |
| w_i (6) + v_j (4) | — | **Si (regresion logistica)** |
| bias b (≡ −θ_A) | — | **Si**, luego θ_A se recalibra en validacion |
| τ_A (alerta) | 1.5 h | No |

Aprendibles: **11**. Fijos: ~13. Total del modelo: ~24.

### 3.4. Como se entrena

1. `capa_features` genera la matriz `A` de actividades (paso determinista, sin aprendizaje).
2. Regresion logistica (BCE) sobre `[A | contexto]` → aprende `w`, `b` (train).
3. Barrido de umbral θ_A en validacion maximizando CSI.
4. CSI/POD/FAR en test.

**El prototipo validado** (`prototipos/prototipo_lif.py`) con este diseno: pesos `[+0.63, +0.59, ~0, ~0]` (identifica las variables informativas), LIF `CSI=0.163` vs baseline `CSI=0.123`.

---

## 4. La propuesta: neuronas sensor con parametros aprendidos

La idea de fondo: *"cada variable tiene su neurona LIF individual que aprende sus propios rangos y patrones, dispara spikes cuando se acerca un evento de lluvia, y esos spikes alimentan a la alerta."*

Se puede implementar con 3 niveles de cambio crecientes:

### Variante V1: Umbrales θ_i aprendibles (RECOMENDADA)

Cada neurona sensor aprende **su propio umbral de disparo θ_i** (su "rango de alarma"). τ_m queda fijo con analisis de sensibilidad. Salida: spikes `s_i[t] = 1[V_i[t] ≥ θ_i]`.

- Como se entrena: (a) busqueda en validacion (simple, sin gradiente), o (b) gradiente sustituto sobre θ_i (LTMD). La alerta sigue siendo regresion logistica sobre `[spikes | contexto]` (o sobre actividad + spikes).
- Parametros aprendidos: 11 + 6 = **17**. Complejidad de entrenamiento: baja.
- Interpretabilidad: **maxima** — "el sensor de humedad dispara SOLO cuando la humedad esta en el rango peligroso aprendido".
- Soporte en literatura: **LTMD (NeurIPS 2022)**: umbrales aprendibles mejoran precision y velocidad de convergencia; PLIF (Fang et al. 2021): heterogeneidad de parametros por neurona es biologicamente plausible y mejora expresividad.

### Variante V2: τ_m aprendibles (tiempos de memoria)

Ademas de θ_i, cada neurona aprende **su constante de tiempo τ_m** (que patron temporal detecta: rapido vs lento).

- Parametros aprendidos: 11 + 6 + 6 = **23**. Complejidad: media (requiere gradiente sustituto estable).
- Soporte: PLIF, ASN (Yin et al. 2020).
- Riesgo: el τ_m ya se puede barrer por sensibilidad barata; entrenarlo agrega poco si la sensibilidad muestra que el CSI no cambia mucho con τ_m.

### Variante V3: Entrenamiento end-to-end completo

Se entrena todo (sensores + alerta) con gradiente sustituto y BPTT (snnTorch/Norse/SpikingJelly). Es la "Opción B" del doc.

- Parametros: ~23 + posibles pesos de entrada. Complejidad: **alta** (no-diferenciabilidad del spike, BPTT, estabilizacion del umbral).
- Soporte: Neftci et al. (2019) gradiente sustituto; TrSG (Kook et al., WACV 2026) muestra que entrenar umbrales con SG es **inestable** sin tecnicas especificas.
- Contradice el objetivo "no super complejo".

---

## 5. Lo que dice la literatura (evidencia)

### 5.1. A favor del diseno actual (filtros fijos + readout entrenado)

- **Reservoir computing** (Jaeger 2001; Maass 2002; Lukosevicius & Jaeger 2009): un sistema dinamico fijo que expande la historia de la entrada + un readout lineal entrenado es un paradigma establecido y exitoso para series temporales. La separacion "expansor fijo / readout entrenado" es un principio teorico, no una limitacion.
- **Schiller & Steil (2005)**: en RNN entrenadas con gradiente, los cambios dominantes ocurren en los pesos de salida — el readout hace la mayor parte del aprendizaje.
- Interpretacion para el LIF: la neurona sensor con τ_m fijo YA es una feature temporal rica (EMA de toda la historia). El peso `w_i` ya aprende cuanto importa esa variable. El diseno actual no es "debil"; es la practica estandar de RC.

### 5.2. A favor de la propuesta (parametros aprendibles por neurona)

- **LTMD (NeurIPS 2022)**: umbrales de disparo aprendibles por neurona mejoran la precision y la velocidad de convergencia en clasificacion; la heterogeneidad de umbrales por neurona captura distinta sensibilidad.
- **PLIF (Fang et al. 2021)**: τ aprendible es biologicamente plausible (neuronas heterogeneas) y aumenta expresividad.
- **MTS con SNN** (Fang, Shrestha & Qiu 2020): para series multivariables, lo comun es **una poblacion de neuronas por canal** con distintos τ y ganancia — la representacion por neurona por variable es la practica establecida, y el entrenamiento se hace end-to-end con gradiente sustituto.
- **Cautela** (Frontiers Neurosci 2025): un codificador LIF con UN solo tipo de evento por sensor rindio PEOR que codificaciones mas ricas (level-crossing, send-on-delta) — el spike binario por variable pierde informacion si no se compensa (con poblaciones, con actividad continua, o con la integracion τ_A de la alerta).

### 5.3. Lo que NO se puede hacer

- **Entrenar cada neurona "individualmente" con supervisado no existe**: no hay etiqueta por variable. La etiqueta es una por hora. Todo aprendizaje supervisado de neuronas intermedias es **conjunto** (credit assignment global via BPTT o busqueda).
- Si se quiere aprendizaje verdaderamente independiente por neurona, es **no supervisado (STDP)** — y entonces la neurona aprende los patrones *frecuentes* de su variable, sin saber si son precursores de lluvia. La alerta igual debe aprender que sensores sirven.

---

## 6. Cuanto cambia cada variante

| Aspecto | Actual | V1 (θ aprendibles) | V2 (θ+τ) | V3 (end-to-end) |
| --- | --- | --- | --- | --- |
| Parametros aprendidos | 11 | 17 | 23 | 23+ |
| Cada sensor dispara spike propio | No | Si | Si | Si |
| Sensor aprende su rango (θ_i) | No | **Si** | Si | Si |
| Sensor aprende su escala temporal (τ_m) | No | No | Si | Si |
| Alerta integra spikes con τ_A | Opcional | Si | Si | Si |
| Metodo de entrenamiento | reg. logistica | busqueda o SG | SG | SG + BPTT |
| Complejidad | Baja | Baja | Media | Alta |
| Interpretabilidad por variable | Media | **Alta** | Alta | Baja |
| Requiere libreria SNN | No | No (o snnTorch) | snnTorch | snnTorch/Norse |

---

## 7. Resultados experimentales (ablation sobre datos sinteticos)

Ejecutado con `prototipos/prototipo_lif_spikes.py` sobre los mismos datos sinteticos que el prototipo continuo (AR(1) estacionario, 4 variables, 2 informativas + 2 falsas, etiqueta = persistencia 6 h + 5% de ruido, 3 anos). Los hiperparametros del modelo B (percentil θ_i y τ_A) se eligieron en validacion; test no se toco. El barrido de τ_A mostro un maximo de CSI en validacion en τ_A = 12 h (CSI-val 0.103 @ 0.5 h → 0.224 @ 12 h → 0.189 @ 24 h): el τ_A = 1.5-2 h heuristico del diseno era demasiado corto y penalizaba la version con spikes.

| Modelo | CSI | POD | FAR | θ_A | Delta CSI vs baseline |
| --- | --- | --- | --- | --- | --- |
| A: actividad continua + readout ponderado (diseno actual) | **0.163** | 0.255 | **0.688** | 0.20 | +0.040 |
| B: sensores LIF con spikes, θ_i aprendidos, alerta integra con τ_A = 12 h | 0.166 | **0.332** | 0.752 | 0.15 | +0.043 |
| B2: spikes instantaneos (sin integracion τ_A) | 0.069 | 0.123 | 0.862 | 0.10 | −0.053 |
| Baseline: umbral fijo sobre X0 | 0.123 | 0.313 | 0.832 | (umbral X0=0.70) | — |

Tasa de lluvia en test: 7.9%. Detalles del modelo B: percentil θ_i = 70 (validacion), θ_i ≈ [0.568, 0.574, 0.588, 0.593], tasa de disparo por sensor (train) ≈ [0.030, 0.030, 0.056, 0.136].

### Lectura de los resultados

1. **V1 (spikes integrados) NO es peor que el diseno actual en CSI (0.166 vs 0.163, empate dentro del ruido), pero cambia el punto de operacion:** detecta MAS eventos (POD 0.332 vs 0.255) a costa de mas falsas alarmas (FAR 0.752 vs 0.688). La hipotesis "el spike por variable da informacion mas util" no produce una ganancia de CSI atribuible en estos datos.
2. **La integracion τ_A es lo que hace viable a los spikes, no los spikes en si.** Sin ella (B2) el CSI colapsa a 0.069 (por debajo del baseline): el spike binario por variable pierde la magnitud y la alerta no puede acumular evidencia. Esto confirma experimentalmente la cautela de Frontiers Neurosci 2025 (§5.2): el spike unico por sensor necesita la memoria de la alerta para no perder informacion.
3. **Los spikes de los sensores informativos son raros (~3% de las horas)**: con θ_i en el percentil 70 sobre la membrana libre, los sensores informativos (τ_m = 6 h) disparan pocas veces porque el reset los mantiene bajos mucho tiempo; los no informativos (τ = 1-3 h) disparan mas (5.6-13.6%). El readout aprende a compensarlo con pesos, pero la tasa de disparo por sensor deja de ser un indicador fiable de importancia (los pesos siguen siendo los que deciden).
4. **Interpretabilidad:** B mantiene la lectura "cada sensor dispara solo cuando su variable esta en su rango de alarma", lo cual es valioso para el paper aunque no se traduzca en mayor CSI.
5. **Conclusion de diseno:** el diseno actual (actividad continua + readout) es **suficiente**; la variante V1 es un **alternativo equivalente** con mejor POD e interpretabilidad por variable, no una mejora. Si el paper quiere el claim "SNN con spikes por variable", V1 es defendible; si quiere el mejor CSI con la minima complejidad, A gana (menos parametros, sin τ_A que calibrar).

---

## 8. Recomendacion y roadmap

**Recomendacion: Variante V1** — 1 neurona LIF por variable (filosofia LIF intacta), umbrales de disparo θ_i aprendidos por variable, τ_m fijo con sensibilidad, alerta que integra spikes con τ_A y pesos aprendidos. La ablation (§7) la confirma como alternativa equivalente al diseno actual, con mejor POD e interpretabilidad, a cambio de calibrar τ_A.

Pasos propuestos:

1. ~~Ablation controlada sobre los datos sinteticos del prototipo~~ **HECHA** (§7): actual (A) vs V1 con spikes y θ_i por busqueda en validacion (B) vs spikes sin integracion (B2). Resultado: CSI A=0.163, B=0.166, B2=0.069, baseline=0.123. V1 es equivalente en CSI con mejor POD y peor FAR; la integracion τ_A es imprescindible.
2. **Pendiente:** confirmar que los θ_i aprendidos por variable son interpretables en datos reales (perfil de disparo del sensor antes de lluvia) — en sinteticos la tasa de disparo por sensor no distingue informativas de falsas (§7, punto 3).
3. **Veredicto del paso 1:** no hay ganancia robusta de V1 sobre A; se reporta la ablation como evidencia de que el diseno actual es suficiente, y V1 como variante spike equivalente e interpretable si el paper quiere spikes por variable.
4. Extender la ablation a los datos EDDF reales cuando esten disponibles.

---

## 9. Referencias clave

1. **Jaeger, H. (2001)**. *The "echo state" approach to analysing and training recurrent neural networks*. GMD Report 148.
2. **Maass, W.; Natschläger, T.; Markram, H. (2002)**. *Real-time computing without stable states: A new framework for neural computation based on perturbations*. Neural Computation.
3. **Lukosevicius, M.; Jaeger, H. (2009)**. *Reservoir computing approaches to recurrent neural network training*. Computer Science Review 3(3), 127-149.
4. **Neftci, E. O.; Mostafa, H.; Zenke, F. (2019)**. *Surrogate gradient learning in spiking neural networks*. IEEE Signal Processing Magazine 36(6), 51-63.
5. **Fang, W.; et al. (2021)**. *Incorporating learnable membrane time constant to enhance learning of spiking neural networks* (PLIF). ICCV.
6. **Kook, H.; Yu, B.; Oh, J.; Park, E. (2026)**. *Stabilizing direct training of spiking neural networks: membrane potential initialization and threshold-robust surrogate gradient* (TrSG). WACV.
7. **Fang, H.; Shrestha, A.; Qiu, Q. (2020)**. *Multivariate time series classification using spiking neural networks*. arXiv:2007.03547.
8. **Schiller, U. D.; Steil, J. J. (2005)**. *Analyzing the weight dynamics of recurrent learning algorithms*. Neurocomputing.
9. **Frontiers in Neuroscience (2025)**. *Signal-to-event encoding parameter selection for multiple event classification with SNNs*.
