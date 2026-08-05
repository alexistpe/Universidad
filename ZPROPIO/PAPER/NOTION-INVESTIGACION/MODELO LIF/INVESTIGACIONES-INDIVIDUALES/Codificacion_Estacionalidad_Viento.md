# Investigacion: Codificacion neuronal, estacionalidad y viento

**Proposito:** Resolver 3 preguntas metodologicas abiertas del modelo LIF y definir el metodo de entrenamiento. Expande los conceptos de `Normalizacion.md` hacia tres temas concretos: (A) la descomposicion u/v del viento, (B) entrenar por temporada vs. todo el ano, y (C) la codificacion por tasa (rate coding) frente a otras formas de codificacion en SNN. La ultima seccion (D) detalla el metodo de entrenamiento propuesto y que conviene en un modelo de este tipo.

**Alcance:** Este documento NO modifica el documento principal ni la investigacion en Notion. Es material de apoyo para justificar decisiones ya tomadas o por tomar.

---

## Indice

1. Pregunta A: ¿Por que descomponer el viento en componentes u/v?
2. Pregunta B: ¿Entrenar por temporada o con todo el ano?
3. Pregunta C: ¿Que es rate coding y que otras formas de codificacion existen?
4. Pregunta D: Metodo de entrenamiento propuesto y recomendaciones practicas
5. Resumen de decisiones
6. Referencias

---

## Pregunta A: ¿Por que descomponer el viento en componentes u/v?

### A.1. La direccion del viento es un dato circular, no lineal

La direccion del viento es una variable **circular** (definida en el intervalo [0°, 360°)), y como tal **no puede tratarse con estadistica lineal ordinaria** (Fisher, 1993 — *Statistical Analysis of Circular Data*, Cambridge University Press). La razon es estructural:

- 0° y 360° representan **el mismo** rumbo (Norte). Una codificacion lineal los coloca en extremos opuestos del rango.
- Dos vientos de **359°** y **1°** estan fisicamente a **2°** de distancia, pero una metrica euclidiana (y cualquier normalizacion lineal) los considera a **358°** de distancia. La distancia es, por tanto, incorrecta y discontinua en la frontera.

**Ejemplo numerico del problema** (Shu et al., 2025 — WaveHiTS):

> "a prediction of 359° when the true direction is 1° would be penalized as a 358° error, even though the actual error is only 2°."

Este ejemplo esta documentado de forma explicita en la literatura de nowcasting de direccion de viento y es la motivacion central de los metodos que descomponen la direccion en componentes cartesianas.

### A.2. Consecuencias concretas para el modelo LIF

Si la direccion entrara como un solo numero (grados) al pipeline de normalizacion + rate coding:

1. **Z-score sobre grados no tiene sentido**: la media de 359° y 1° por aritmetica lineal es 180° (Sur), cuando la direccion circular media correcta es 0° (Norte). Todo el estadistico (μ, σ) queda contaminado en la frontera.
2. **Min-max discontinuo**: valores alrededor de 0°/360° se proyectan a extremos opuestos de [0,1], creando saltos artificiales en la tasa de disparo de la neurona aunque el viento no haya cambiado de direccion.
3. **Rate coding inestable**: con λ = x̂ · f_max, la tasa de disparo daria saltos bruscos al cruzar la frontera, introduciendo ruido espurio en la neurona de alerta.
4. **La direccion es multi-valuada**: dado un conjunto de variables atmosfericas, la direccion del viento no tiene una solucion unica (es una funcion **multi-valuada** y periodica). Bishop (2006, *Pattern Recognition and Machine Learning*, Springer) documenta que una red que minimiza error cuadratico promedia soluciones invalidas: el promedio de dos direcciones validas no es necesariamente una direccion valida. En el ambito de viento satelital, esto se observo con MLPs convencionales que **fallan** al estimar direccion (Bishop & Nabney, trabajo de scatterometer, Aston University).

### A.3. La descomposicion u/v resuelve el problema

La solucion estandar y documentada es expresar el vector de viento en coordenadas cartesianas:

```
u = WS · sin(dir)     # componente zonal (Este-Oeste)
v = WS · cos(dir)     # componente meridional (Norte-Sur)
```

Esta transformacion:

1. **Elimina la discontinuidad circular**: u y v son variables continuas, lineales y sin frontera artificial. Se convierten en tareas de regresion estandar (Shu et al., 2025).
2. **Conserva toda la informacion del vector**: la magnitud se recupera con WS = √(u² + v²) y la direccion con dir = atan2(u, v). Es una transformacion biyectiva: no se pierde informacion.
3. **Permite z-score independiente por componente** (como ya se decidio en `Normalizacion.md`) y, por tanto, rate coding consistente con las demas variables.
4. **Las componentes u/v son casi-gaussianas** para las direcciones predominantes de una region, lo que hace valido el supuesto del z-score.

### A.4. Evidencia empirica

| Estudio | Hallazgo |
| --- | --- |
| **Shu et al. (2025)**, WaveHiTS, arXiv:2504.06532 | Descomponer en u/v redujo el RMSE de prediccion de direccion ~20-25% (N-HiTS 24.6°→19.8°; RMSE ~19.2-19.4° vs 56-64° de los modelos recurrentes). Ablacion confirma que la descomposicion contribuye por si sola. |
| **Bastos, Cyrino Oliveira & Milidiu (2020)**, ComPonentNet, *Electric Power Systems Research* 190:106922 | Procesar las componentes u y v en ramas separadas de una red convolucional mejora el pronostico de viento frente a procesarlas juntas o usar solo la velocidad. |
| **Alves et al.** (revision sistematica ML viento) | Solo 4.3% de los estudios manejan la direccion; la practica recomendada es descomponer el viento en sus vectores base (u, v). |
| **Serpa-Usta et al. (2025)**, *Atmosphere* 16(11):1292 | Uso de u/v (seno/coseno) para normalizar direccion de viento en variables meteorologicas (ya citado en el doc principal). |
| **Fisher (1993)** | Los metodos lineales no se aplican a datos circulares (fundamento teorico). |

### A.5. Implicacion para la arquitectura del LIF

La variable "viento (velocidad|direccion)" deja de ser **una** entrada y pasa a ser **dos** neuronas de entrada: una para u y una para v, cada una con su propio z-score y su propia tasa de disparo. El vector completo (velocidad Y direccion) queda representado por la pareja (u, v).

> **Consecuencia numerica:** si el modelo contaba "6 neuronas" (5 sensores + alerta), con la descomposicion u/v el viento aporta 2 neuronas, quedando: T, P, HR, u, v, PRECIP (6 sensores) + alerta. Revisar la cuenta de neuronas en la metodologia final del paper.

---

## Pregunta B: ¿Entrenar por temporada o con todo el año?

### B.1. Dos decisiones distintas que conviene separar

Hay dos preguntas que a menudo se mezclan y que conviene separar:

1. **Normalizacion**: ¿con que estadisticos (μ, σ) se estandariza cada variable? → Ya decidido en el doc principal (seccion 6.2): **por estacion**, usando anomalias estacionales. Respaldado por Furtado et al. (2026, arXiv:2508.07062): la señal predictiva de presion/temperatura es la **desviacion** respecto a la climatologia del mes, no el valor absoluto.
2. **Entrenamiento**: ¿se ajusta **un** modelo sobre los 12 meses, o **4 modelos** (uno por estacion)?

La pregunta pendiente es la numero 2.

### B.2. Que dice la literatura de nowcasting

**Evidencia principal: TA-SmaAt-UNet** (van Nieuwkoop & Mehrkanoon, 2026, arXiv:2606.09959):

> "TA-SmaAt-UNet improves upon the core SmaAt-UNet in every season, indicating that the benefit of temporal context is not restricted to a single part of the year. The improvement is particularly relevant in summer, which is also the most difficult season in terms of CSI. This is consistent with previous nowcasting evidence that models often struggle more with convective summer precipitation than with more persistent winter rainfall."

Hallazgos clave del estudio:
- El patron de la literatura no es **entrenar modelos separados por estacion**, sino **entrenar un unico modelo** y darle **contexto estacional** (codificacion ciclica del momento del ano: sin/cos del dia del año y de la hora).
- El contexto estacional es **mas beneficioso cuanto mas raro e intenso es el evento** (mejoras mayores en umbrales de 10 y 20 mm/h que en 0.5 mm/h). Es decir, la estacionalidad importa especialmente para los eventos que mas importan en un sistema de alerta.
- El verano es la estacion mas dificil (conveccion), y el contexto estacional es justamente donde mas ayuda.

**Implicacion directa:** la estrategia respaldada es **un solo modelo + informacion estacional como entrada o como normalizacion**, NO fragmentar el entrenamiento en modelos por estacion.

### B.3. Argumentos practicos para entrenar con el ano completo

| Criterio | Entrenar 1 modelo anual | Entrenar 4 modelos estacionales |
| --- | --- | --- |
| **Volumen de datos** | EDDF 2020-2024: ~43,800 h → ~43,800 muestras | ~10,950 h/estacion → 4x menos datos por modelo |
| **Eventos de lluvia** | Todos los regmenes (convectivo de verano, estratiforme de invierno) | Cada modelo ve solo su regimen; los eventos raros se fragmentan |
| **Robustez** | Umbrales y pesos estimados con mas evidencia | Mas varianza, mayor riesgo de overfitting |
| **Despliegue bajo costo** | 1 modelo, 1 umbral, 1 τ_m desplegable | 4 configuraciones + logica de seleccion de estacion |
| **Transferencia de patrones** | Los precursores comunes (caida de presion, alza de humedad) se aprenden una vez | Cada modelo los reaprende por separado |

Para un LIF simplificado de pocas neuronas y pocos parametros, el dato adicional del ano completo es directamente aprovechable: **mas datos = umbrales y pesos mas estables**.

### B.4. Como evaluar la estacionalidad correctamente (sin sesgar)

La literatura de evaluacion de nowcasting da 3 reglas claras:

1. **El test set debe cubrir al menos un ciclo estacional completo.** En series temporales con estacionalidad, el periodo de prueba debe abarcar el ciclo completo para poder evaluar la captura de la estacionalidad (practica estandar en division temporal; los papers de nowcasting dividen por **años completos consecutivos**, p.ej. entrenar 2008-2020, validar 2006 o 2020, testear 2021).
2. **Reportar metricas por estacion.** Los papers de nowcasting reportan CSI/POD/FAR desglosados por estacion para exponer (no esconder) la dificultad del verano convectivo.
3. **Cuidado con test sets sesgados.** Un año de prueba con eventos extremos concentrados en pocos meses infla o desinfla las metricas. El estudio del DGMR (AMS, AIES 2023) lo maneja explicitamente separando "Test—Heavy" (meses con eventos intensos) de "Test—Light" para no atribuir a la maquina lo que es sesgo del periodo de prueba.

### B.5. Conclusion B

**Recomendacion: entrenar UN solo modelo con todo el año**, con:
- Normalizacion estacional (μ, σ por estacion) — ya decidida.
- Test set de al menos un año completo y reporte de metricas **por estacion** (CSI, POD, FAR, MCC).
- **Opcional (fortalece el paper):** *ablation* comparando el modelo anual vs. 4 modelos estacionales, para demostrar empiricamente la eleccion.

No es contradictorio con la normalizacion estacional: la normalizacion quita el ciclo climatologico para que el modelo de año completo vea **anomalias homogeneas** (la senal real de lluvia), mientras que entrenar por estacion fragmenta datos sin necesidad.

### B.6. Efectividad, coordinacion, complejidad y precision de las variables de tiempo (day-of-year / hour-of-day)

**Aclaracion previa:** en este modelo las variables de tiempo **no son neuronas LIF adicionales**. Son **features de contexto temporal** que entran directamente en el readout (la combinacion lineal). Al estar acotadas en [-1, 1] y ser continuas, **no necesitan rate coding ni integrador**: se agregan como columnas extra a `V_alerta = Σ_i w_i·actividad_i + Σ_j v_j·tiempo_j`.

#### B.6.1. ¿Es realmente efectiva esta metodologia? (evidencia documentada)

| Fuente | Experimento | Resultado documentado |
| --- | --- | --- |
| **TimeSter** — Zeng et al. (2024), arXiv:2412.01557 | Anadir features de tiempo (hora, dia de semana, mes, estacion) a un backbone **lineal** | MSE promedio **-23%** en Electricity y Traffic. Un proyector lineal con features de tiempo supera al mismo proyector sin ellas. |
| **Bansal et al. (2025)**, arXiv:2503.15456 | Codificacion sinusoidal vs. encodings temporales tradicionales (energia) | RMSE **-12.6%** (0.5497 → 0.4802), R² +7.8%, coste de entrenamiento solo **+7.2%** |
| **Khazem & Kanso (2025)**, IEEE CAI | Ablation: modelo completo vs. indices de tiempo crudos (energia) | RMSE 0.095 vs 0.117 (dia 1) ≈ **-19%**. La correlacion del "dia del ano" paso de **-0.23 (crudo) a +0.83 (cos)** |
| **TA-SmaAt-UNet** — van Nieuwkoop & Mehrkanoon (2026), arXiv:2606.09959 | Condicionamiento temporal sin/cos(doy) + hora en nowcasting de radar | Mejora **todas las estaciones**. CSI: 0.5 mm/h 0.594→0.597 (+0.5%); **10 mm/h 0.059→0.103 (+75% rel.)**; **20 mm/h 0.039→0.066 (+69% rel.)** |
| **Ciclo diurno de lluvia** — Gentile et al. (2025), GRL | La conveccion continental de verano tiene un pico diurno marcado (tarde/noche local) | La hora del dia es informacion real para lluvia convectiva: no es uniforme a lo largo del dia |

Matices honestos (para citar en el paper):
- Sin/cos funciona bien con modelos **lineales** (nuestro caso) pero es suboptima con arboles de decision, que parten por una feature a la vez (documentacion de scikit-learn y NVIDIA).
- Para un modelo puramente lineal, la primera armonica de sin/cos puede ser insuficiente para picos diurnos agudos: si la ganancia en validacion es pequena, probar **armonicos superiores** (periodos 365/2, 365/4 y 24/2) o splines periodicos.
- El test set debe cubrir el ciclo completo (seccion B.4) para no atribuir a las features lo que es sesgo del periodo de prueba.

#### B.6.2. ¿Como coordina el modelo todas las variables y como se entrena para interpretarlas?

La coordinacion no se programa a mano ("si es verano entonces..."). Emerge de los pesos aprendidos en el readout:

1. La capa de features (fijada) convierte cada variable en una **actividad de anomalia** `a_i` (cuanto de anomala y persistente esta la variable para la epoca).
2. El readout suma `s(t) = Σ_i w_i·a_i(t) + Σ_j v_j·tiempo_j(t)`, y la probabilidad de lluvia es `P(lluvia) = σ(s(t) − θ_A)`.
3. Las features `tiempo_j` (sin/cos de day-of-year y hora) tienen pesos `v_j` aprendidos.

**El mecanismo clave:** las features de tiempo mueven el **umbral efectivo de decision** segun la epoca:

```
umbral_efectivo(t) = θ_A − Σ_j v_j·tiempo_j(t)
```

- Si el modelo aprende `v_doy_sin > 0`, en verano (sin positivo) el umbral baja: la alerta dispara con anomalias **mas debiles**. Es fisicamente razonable: en verano, pequenos aumentos de humedad + caida de presion preceden conveccion; en invierno la lluvia frontal exige anomalias mas fuertes y persistentes.
- Un peso en `hora_sin` hace al modelo mas sensible a media tarde, cuando la conveccion de verano es mas probable.

**Como se entrena:** el modelo no "interpreta" las variables por diseno; aprende la asociacion estadistica supervisada. Con la etiqueta "¿llovio la proxima hora?" (y=1/0) se minimiza la BCE sobre `σ(s(t) − θ_A)`. El optimizador (regresion logistica en un paso, o busqueda sobre `w` y `v`) ajusta los pesos para separar horas con lluvia de horas sin lluvia. Si la combinacion "humedad alta + caida de presion + fase de verano" predice mejor que sin la fase, el peso `v_doy_sin` sube solo.

**Por que esto reemplaza a los 4 modelos por estacion:** las features de tiempo logran una regla de decision variable con la estacion con **4 parametros** en lugar de 4 modelos completos. Y como la normalizacion (A) ya quito la climatologia, las features de tiempo aportan solo el cambio de *relacion* anomalia→lluvia, no el ciclo en si.

#### B.6.3. ¿Que tan complejo es implementar las variables de tiempo?

| Aspecto | Complejidad |
| --- | --- |
| Neuronas LIF extra | Ninguna: no se agregan neuronas sensor ni integradores |
| Rate coding | No aplica: las features ya estan acotadas en [-1,1] y continuas |
| Parametros nuevos | 4 pesos `v` (doy_sin, doy_cos, hora_sin, hora_cos) en el readout |
| Cambio de codigo | 4 lineas (generar las columnas) + 4 columnas en la matriz del readout |
| Coste computacional | Documentado: +7.2% tiempo de entrenamiento (Bansal et al., 2025). En nuestro caso despreciable (regresion logistica o busqueda). |
| Impacto en lo ya decidido | No cambia τ_m, ni f_max, ni la capa de features, ni la normalizacion estacional |

```python
# Generar las 4 features de contexto temporal (basta con el indice temporal)
df['doy_sin'] = np.sin(2*np.pi*df.index.dayofyear/365.25)
df['doy_cos'] = np.cos(2*np.pi*df.index.dayofyear/365.25)
df['hod_sin'] = np.sin(2*np.pi*df.index.hour/24)
df['hod_cos'] = np.cos(2*np.pi*df.index.hour/24)
# → entran como columnas extra en la matriz X del readout (pesos v aprendidos)
```

#### B.6.4. ¿Cuanta precision real obtiene el modelo? (documentado y honesto)

Las cifras documentadas provienen de otros modelos y dominios; **no son transferibles tal cual** a un LIF de 6-10 neuronas con datos horarios de superficie. Lo que SI se puede afirmar con evidencia:

1. **En modelos lineales**, las features de tiempo producen mejoras de error del orden de **12-23% (MSE/RMSE)** en series con ciclo fuerte (energia, trafico) (TimeSter; Bansal et al.).
2. **En nowcasting**, el contexto temporal/estacional es de **bajo beneficio para lluvia comun** (>0.5 mm/h, CSI +0.5%) y de **alto beneficio para eventos intensos** (CSI +69-75% relativo a 10-20 mm/h) (TA-SmaAt-UNet).
3. **La lluvia convectiva de verano** — la mas dificil de predecir y la mas peligrosa — es justo donde la hora y la estacion aportan mas (TA-SmaAt-UNet; ciclo diurno, Gentile et al., 2025).

**Expectativa razonable para nuestro modelo:** mejora modesta en el CSI global, mayor en verano/eventos convectivos, y posiblemente despreciable en invierno estratiforme. Por eso la decision correcta es convertirlo en una **ablation obligatoria** del paper: modelo con vs. sin features de tiempo, reportado por estacion y por umbral de intensidad. Si la ganancia en validacion es pequena, subir las armonicas o usar splines periodicos antes de descartarlas.

#### B.6.5. Implementacion de la climatologia diaria suavizada (granularidad de la normalizacion A)

**Decision tomada:** la normalizacion estacional usara la **climatologia diaria suavizada** (ventana centrada ±15 dias), no por mes ni por estacion. Reglas:

1. Se calcula **SOLO sobre el conjunto de entrenamiento** (anti-leakage).
2. Para cada dia del ano `d` (1..366), se estiman `μ(d)` y `σ(d)` con todos los registros de entrenamiento cuyo day-of-year cae en `[d−15, d+15]`, usando **distancia circular** (31 dic y 1 ene son vecinos).
3. Con datos horarios de ~3.5 años de entrenamiento, cada ventana tiene ≈ 31 dias × 24 h × 3.5 años ≈ **2.600 muestras**, suficiente para estimar μ y σ estables.
4. Los dias sin datos suficientes se rellenan por interpolacion lineal.

```python
import numpy as np

def climatologia_diaria(train_df, var, win=15, min_n=50):
    """Climatologia suavizada por day-of-year (ventana centrada ±win dias, circular).
    Calculada solo con datos de entrenamiento. Devuelve arrays mu/sd indexados 1..366."""
    doy = train_df['doy'].values.astype(int)
    x   = train_df[var].values
    mu, sd = np.full(367, np.nan), np.full(367, np.nan)
    for d in range(1, 367):
        delta = np.abs(((doy - d + 183) % 365) - 183)   # distancia circular en el ano
        mask = delta <= win
        if mask.sum() >= min_n:
            mu[d] = np.mean(x[mask])
            sd[d] = np.std(x[mask]) + 1e-12
    dias = np.arange(1, 367)
    ok = ~np.isnan(mu[dias])
    return np.interp(dias, dias[ok], mu[dias][ok]), \
           np.interp(dias, dias[ok], sd[dias][ok])

# Aplicacion (una vez por variable con ciclo estacional)
mu_T, sd_T = climatologia_diaria(df_train, 'T')
df['T_anom'] = (df['T'].values - mu_T[df['doy'].values.astype(int)]) \
              / sd_T[df['doy'].values.astype(int)]
```

Notas de implementacion:
- **Año bisiesto:** el dia 366 (31 dic en bisiesto) se mapea cerca del dia 1 del ciclo de 365; la distancia circular con `% 365` lo maneja solo.
- **Donde entra en el pipeline:** la salida `T_anom` alimenta la capa de features (integrador LIF) y luego el rate coding, tal como describe `Normalizacion.md`. La climatologia reemplaza al z-score por estacion: `z = (x − μ(d)) / σ(d)`.
- **Extension diurna (opcional):** la misma funcion se reutiliza sobre la hora (ventana ±2 h) para quitar tambien el ciclo dia/noche de T y HR, o como climatologia 2D (doy × hora). A validar en la ablation.
- **Coste computacional:** 366 iteraciones con mascaras booleanas sobre ~40.000 muestras ≈ fracciones de segundo en numpy. No es un cuello de botella.

---

## Pregunta C: ¿Que es rate coding y que otras formas de codificacion existen?

### C.1. Definicion

En un SNN, la informacion externa (los valores normalizados de las variables) debe convertirse en **trenes de spikes**. A esa conversion se la llama **codificacion neuronal**. La encuesta de referencia la resume asi:

> "Rate codes embed the information in the instantaneous or averaged rate of spike generation... signal amplitudes are directly mapped to spike frequencies." (Neural Processing Letters, 2021)

La clasificacion central divide la codificacion en **rate coding** (codificacion por tasa) y **temporal coding** (codificacion temporal), dependiendo de si la informacion vive en el *numero* de spikes o en el *momento exacto* en que ocurren (Neural Processing Letters, 2021).

### C.2. Taxonomia de formas de codificacion

#### 1. Rate coding (codificacion por tasa) — Adrian & Zotterman (1926)

- **Como funciona:** el valor de la variable se mapea a la **frecuencia de disparo**. Con codificacion de Poisson: `λ = x̂ · f_max`, donde `λ` es la tasa (spikes/segundo), `x̂` el valor normalizado y `f_max` la tasa maxima.
- **Formula del codificador del modelo:** `f = ((x_norm - min)/(max - min)) · f_max` (doc principal, seccion 7.3), con `f_max = 200` spikes/s.
- **Ventajas:** simple de implementar, robusto al ruido (promedia informacion sobre muchos spikes; spikes individuales perdidos o desplazados no cambian la tasa), equivalente a la activacion de una neurona artificial ordinaria, entrenable con los metodos estandar (BPTT / gradiente sustituto).
- **Desventajas:** requiere ventanas largas para estimar la tasa con precision (lento), baja densidad de informacion, mayor numero de spikes y mayor consumo energetico.

#### 2. Temporal coding (codificacion temporal)

La informacion vive en el **momento exacto** de los spikes. Subcategorias:

| Tecnica | Que codifica | Referencia clave |
| --- | --- | --- |
| **TTFS / latency** | El tiempo hasta el primer spike (Δt ∝ 1/amplitud; mayor amplitud → spike mas temprano). Un spike por ventana. | Gollisch & Meister (2008), *Science* 319 |
| **Rank-order (ROC)** | El **orden** de los primeros spikes de una poblacion de neuronas, no los tiempos exactos. | Thorpe & Gautrais (1998) |
| **ISI** | Los intervalos entre spikes consecutivos (mayor capacidad de datos; 2+ spikes/ventana). | Pyramidal cells (biologia) |
| **Phase** | La fase de los spikes respecto a una oscilacion interna de fondo. | Hipocampo, sistema olfativo (O'Keefe & Recce, 1993) |
| **Burst** | Racha de spikes (bursts); alta confiabilidad y eficiencia energetica. | Talamo, corteza auditiva |
| **Temporal contrast** | La **derivada** de la senal (sensores event-driven tipo DVS). | Event-based vision |

#### 3. Otras categorias

- **Population coding (codificacion por poblacion):** el valor se representa con la actividad **colectiva** de un grupo de neuronas (p.ej. campos receptivos gaussianos que mapean el valor continuo a retardos de disparo). La encuesta la define como una **dimension adicional** (cuantas neuronas participan), no como una tercera categoria excluyente: puede haber poblacion tanto en rate como en temporal.
- **Direct coding (codificacion directa):** el valor normalizado se inyecta **directamente como corriente** `I = w·x` sin convertir a spikes. Kim et al. (2022, ICASSP) lo estudian como alternativa eficiente. Es el "Camino B" de `Normalizacion.md`.
- **Multiplexacion:** combina dos esquemas (p.ej. TTFS-phase, ISI-phase) para aumentar capacidad.

### C.3. Comparativa cuantitativa de los esquemas (evidencia)

Guo et al. (2021, *Frontiers in Neuroscience* 15:638474) compararon rate, TTFS, phase y burst en MNIST/Fashion-MNIST con SNN entrenado con STDP, evaluando exactitud, latencia, operaciones sinapticas (SOPs), robustez y tolerancia a fallos:

| Esquema | Exactitud | Latencia de inferencia | SOPs | Robustez |
| --- | --- | --- | --- | --- |
| **TTFS** | Mejor | 4x / 7.5x menor que rate (entrenamiento/inferencia) | 3.5x / 6.5x menos que rate | Sensible a jitter temporal |
| **Rate** | Menor | Lenta (larga latencia para converger) | Alta | Mas robusto y simple |
| **Phase** | Intermedia | Rapida | Muy alta | La mas resiliente al ruido de entrada |
| **Burst** | Buena | Rapida | Alta | Mejor compression y tolerancia a fallos |

La encuesta de Springer (2021) agrega una advertencia clave para la decision de arquitectura:

> "Rate-based schemes... convince through their robustness against fluctuations and noise as well as their simplicity... Temporal encoding schemes on the other hand rely on the precise timing of every single spike and can thus achieve higher information densities and efficiencies. However they involve more complex architectures and lacking training methods."

### C.4. Por que rate coding para ESTE modelo (justificacion)

| Criterio del proyecto | Como lo satisface rate coding |
| --- | --- |
| **Filosofia bajo costo / hardware simple** | El codificador por tasa es el circuito mas simple (un integrador con capacitor); TTFS/ISI requieren circuitos mas complejos (Liu et al., *Neural Encoding Strategies for Neuromorphic Computing*). |
| **Sensores de bajo costo = ruidosos** | Rate coding es el esquema **mas robusto al ruido** (promedia informacion sobre muchos spikes). Es exactamente la tolerancia que necesitan datos de BME280/DHT22/pluviometro de cangilon. |
| **Entrenamiento maduro** | Rate coding se entrena con BPTT/gradiente sustituto; las tecnicas temporales "lacking training methods" (Springer 2021). |
| **Escala temporal horaria** | La desventaja de rate coding (lentitud) es irrelevante: el modelo decide en escala de horas (τ_m 2-4 h, lookback 6-12 h), no de milisegundos. |
| **Consistencia entre variables** | Todas las variables usan la misma f_max=200 y el mismo mapeo λ = x̂·f_max, garantizando tasas comparables (doc principal, seccion 7.2). |
| **Simplicidad de interpretacion** | La tasa de disparo de una neurona sensor equivale a "cuanto de anomala esta esa variable", que es exactamente el rol de detector de anomalias del modelo. |

**Limitacion a reconocer en el paper:** rate coding tiene menor densidad de informacion y mayor gasto energetico por spike que TTFS. Para un LIF de 6 neuronas esto es aceptable, pero se puede mencionar **TTFS como ablation** (comparar exactitud CSI/POD/FAR) si se quiere demostrar la robustez de la eleccion o explorar eficiencia energetica. La comparativa de Guo et al. (2021) da los numeros de referencia para esa discusion.

### C.5. Conclusion C

Rate coding con Poisson y f_max = 200 es la eleccion correcta para los objetivos (bajo costo, sensores ruidosos, escala horaria, entrenamiento simple). Se documenta con: Adrian & Zotterman (1926), Gollisch & Meister (2008), Neural Processing Letters (2021), Guo et al. (2021), Liu et al. y Kim et al. (2022). TTFS queda como alternativa de referencia para una eventual ablation de eficiencia.

---

## Pregunta D: Metodo de entrenamiento propuesto y recomendaciones practicas

### D.1. Idea central: dos etapas (features fijas + readout aprendido)

El LIF simplificado tiene una propiedad que conviene explotar: **la integracion de la membrana es lineal en las entradas**. Con la ecuacion del LIF discretizado (Gerstner et al., 2014 — *Neuronal Dynamics*, Cambridge Univ. Press):

```
V[t] = α·V[t-1] + (1-α)·I[t]        con  α = e^(-Δt/τ_m)
dispara si V ≥ θ ; luego V ← V_reset
```

- La variable **I[t]** (corriente de entrada) es, en rate coding, proporcional al valor normalizado de la variable (I ≈ λ ≈ x̂·f_max).
- Integrar esa corriente con fuga **equivale a un promedio movil exponencial (EMA)** de la variable normalizada: V[t] es esencialmente el z-score **suavizado en el tiempo** con la constante τ_m.
- Por tanto, cada neurona sensor **no necesita aprenderse**: su τ_m y su umbral θ se fijan con criterio fisico/estadistico, y el disparo de la neurona sensor se convierte en un **indicador de "esta variable esta anormalmente alta/persistente"**.

Sobre esas activaciones integradas, la **neurona de alerta** acumula una combinacion lineal:

```
V_alerta[t] = Σ_i w_i · (actividad de la neurona i)        y dispara si V_alerta ≥ θ_A
```

Como la combinacion es lineal, **V_alerta es una regresion logistica sobre las features integradas**. Eso significa que el entrenamiento del modelo se reduce a:

1. **Fijar (no aprender):** τ_m por variable, umbrales de disparo de las neuronas sensor θ_i, f_max, V_reset.
2. **Aprender (parametros libres):** los pesos w_i de las neuronas sensor → neurona de alerta, y el umbral de decision θ_A.

Esta separacion es la clave del metodo: es un modelo **simple, entrenable con pocos parametros y desplegable en hardware de gama baja**, y su decision final es interpretable (cada peso dice cuanta influencia tiene cada variable).

### D.2. Pipeline de entrenamiento paso a paso

#### Etapa 0 — Datos y QC
- Datos horarios EDDF 2020-2024 (NOAA ISD-Lite / Meteostat), 5 variables: T, P, HR, viento, precipitacion.
- QC institucional + verificacion de outliers por variable (ya cubierto en el doc principal).
- **Opcional (recomendado):** simular sensores de bajo costo (BME280, DHT22, pluviometro) con el modelo de 4 componentes de `SIMULACION_SENSORES_BAJO_COSTO.md`, para evaluar la degradacion real.

#### Etapa 1 — Transformaciones por variable (de `Normalizacion.md`)
| Variable | Transformacion | Resultado |
| --- | --- | --- |
| Temperatura | z-score estacional (anomalia) | μ=0, σ=1 |
| Humedad | z-score estacional (anomalia) | μ=0, σ=1 |
| Presion | ΔP/Δt (tendencia 3h) o anomalia, luego z-score | μ=0, σ=1 |
| Viento | descomponer en u, v → z-score por componente | 2 columnas |
| Precipitacion | binaria 0/1 (umbral 0.2 mm) o log(1+x) | compacta |

Los μ y σ se calculan **solo sobre el conjunto de entrenamiento** (nunca mezclar train/test — evita data leakage; Furtado et al., 2026).

#### Etapa 2 — Codificacion a spikes (rate coding)
- Para cada paso de tiempo y cada variable: generar tren de spikes de Poisson con `f = x̂ · f_max`, `f_max = 200` (doc principal, seccion 7).
- Misma f_max para todas las variables → tasas comparables.

#### Etapa 3 — Capa de features (integrador con fuga, FIJADO)
- Cada neurona sensor integra su corriente con `τ_m` propio. Valores sugeridos desde la literatura de precursores (ya investigada): **τ_m en rango 2-4 h** (α ≈ 0.7 a paso horario), coherente con la ventana optima de 6-12 h.
- Criterio de fijado sugerido: la presion (señal rapida, ΔP/Δt) puede integrar con τ_m menor; la humedad (señal lenta) con τ_m mayor. Hacer analisis de sensibilidad.
- Umbral de disparo θ_i de cada neurona sensor: fijado estadisticamente, p.ej. disparar cuando la actividad integrada supera un cierto percentil (ej. z-score > 1.5-2). Alternativa: dejarlo como parametro libre.

#### Etapa 4 — Readout (APRENDIDO)
- Parametros libres: `w = [w_1 ... w_m]` (pesos de las m neuronas sensor → alerta) y `θ_A` (umbral de la alerta).
- Perdida: **binary cross-entropy (BCE)** sobre la etiqueta "llovio en la hora siguiente" (y=1 si la precipitacion de la proxima hora supera el umbral, p.ej. 0.2 mm).
- Metricas de evaluacion: **CSI, POD, FAR, MCC** (no accuracy — la lluvia es rara y accuracy se satura prediciendo "no llueve").

#### Etapa 5 — Optimizacion de los parametros libres

**Opcion A — Busqueda sobre el espacio pequeno (RECOMENDADA para bajo costo):**
- El vector a optimizar es pequeno: m pesos + θ_A (tipicamente 7-11 numeros con 6-10 sensores y 1 umbral).
- Usar **grid search / random search / busqueda bayesiana** (scipy.optimize o Optuna) sobre el conjunto de **validacion**, maximizando CSI (o MCC).
- Con ~200-500 evaluaciones sobre la validacion se obtiene una configuracion estable en minutos en una PC. No requiere GPU ni librerias de SNN.
- **Equivalencia exacta:** puesto que V_alerta es lineal en las features integradas, este readout es matematicamente **una regresion logistica sobre las features integradas**. Se puede entrenar directamente con un solver logistico (sklearn, solo 1 paso) y usar su score como **baseline riguroso** del readout aprendido.

**Opcion B — Gradiente sustituto (ESTANDAR en literatura SNN):**
- Entrenar el SNN completo end-to-end con gradiente sustituto (snnTorch, Norse, SpikingJelly). Util si el paper quiere claim "SNN entrenado end-to-end".
- Mas costoso y requiere libreria; los pesos y umbrales se actualizan con BPTT sobre la perdida BCE.
- Se recomienda como **baseline riguroso** o segunda linea, no como metodo principal del paper de bajo costo.

**Recomendacion:** Opcion A como metodo principal (coherente con "operaciones basicas que producen computo eficiente en hardware de gama baja" del abstract), con la regresion logistica sobre features integradas como pre-baseline y, si hay recursos, gradiente sustituto como comparativa.

#### Etapa 6 — Validacion y prueba
- **Division temporal estricta** 70/15/15, en orden cronologico, sin shuffle (evita data leakage).
- **Test set = al menos un ano completo** (idealmente el ultimo ano disponible) para cubrir el ciclo estacional.
- **Warm-up:** descartar los primeros pasos de cada secuencia para que la membrana se estabilice (practica SNN; Diehl & Cook, 2015).
- **Reporte por estacion:** CSI/POD/FAR desglosados por estacion (Pregunta B).
- **Comparacion con baseline:** modelo de umbrales fijos tipo Zambretti (tendencia de presion 3h + direccion + mes) como control (doc principal, seccion sobre baseline).

### D.3. Ejemplo numerico del paso de entrenamiento

Con datos ficticios para ilustrar (paso horario, f_max=200, α=0.7):

1. A las 14:00 h: x̂_presion = -1.8 (presion en fuerte caida), x̂_humedad = +2.3 (muy humedo).
2. Rate coding: λ_presion = |−1.8|·200 ≈ 360 → se genera un tren Poisson de ~360 spikes/s; λ_humedad ≈ 460 spikes/s.
3. La neurona de presion integra: V_presion[14] = 0.7·V_presion[13] + 0.3·(360/f_max) ≈ acumula. Si V ≥ θ_presion (fijado en, p.ej., z=1.5), **dispara** → aporta su peso a la alerta.
4. La alerta: V_alerta = w_presion·(disparo o actividad integrada) + w_humedad·(...) + ... Si V_alerta ≥ θ_A → **prediccion de lluvia para la hora 15**.
5. Entrenamiento (Opcion A): se prueban combinaciones de (w, θ_A) sobre la validacion; se elige la que maximiza CSI. La etiqueta real ("¿llovio a las 15:00?") es la supervisora de la BCE.

### D.4. Que conviene en un modelo de este tipo (recomendaciones practicas)

1. **Pocos parametros libres.** Un LIF de 6-10 neuronas no necesita redes grandes; mantener el readout lineal evita overfitting y permite busqueda exhaustiva. Menos parametros = entrenamiento mas barato y mas interpretable.
2. **No entrenar la capa sensor con backprop innecesariamente.** Fijar τ_m y θ_i con fisica (precursores) + estadistica (percentiles), y aprender solo la combinacion final. Si se quiere entrenar end-to-end, hacerlo como comparativa, no como metodo principal.
3. **Desbalance de clases.** La lluvia horaria es rara (tipicamente 5-15% de las horas). Usar metricas de confusion balanceadas (CSI, POD, FAR, MCC); calibrar θ_A en validacion; si se entrena por gradiente, usar BCE ponderada o focal (Ko et al., 2022, muestran mejoras de CSI con estrategias anti-desbalance).
4. **Estricta separacion temporal.** Nunca barajar; normalizar con estadisticos solo de train; test de un ciclo estacional completo.
5. **τ_m fundamentado, no ad hoc.** Derivar de la escala temporal de los precursores documentados (2-4 h) y reportar analisis de sensibilidad de CSI vs. τ_m.
6. **Baseline de umbrales fijos como control.** El paper se compara contra Zambretti: mantener ese control siempre.
7. **Reproducibilidad.** Seeds fijas, script/cuaderno versionado, repo publico (como pide la metodologia del doc principal).
8. **Coherencia de la arquitectura.** Revisar el conteo de neuronas al pasar viento a u/v (2 neuronas) y documentar la eleccion de f_max y de pasos de simulacion suficientes para estimar tasas (f_max × duracion de ventana).

### D.5. Resumen del metodo en un esquema

```
DATOS EDDF 2020-2024 (horario)
   │ 0. QC + (opcional) simulacion de sensores de bajo costo
   ▼
TRANSFORMACIONES (por variable)
   T: z-score estacional │ P: ΔP/Δt → z-score │ HR: z-score estacional
   Viento: u = WS·sin(dir), v = WS·cos(dir) → z-score │ PRECIP: binaria o log(1+x)
   ▼
RATE CODING (Poisson, f_max=200, mismo mapeo en todas las variables)
   ▼
CAPA DE FEATURES (fijada): integrador LIF con τ_m (2-4 h) por variable
   → disparo sensor = "variable anomala y persistente"
   ▼
READOUT (aprendido): V_alerta = Σ w_i·actividad_i ; dispara si V_alerta ≥ θ_A
   perdida: BCE (lluvia en la proxima hora) · metricas: CSI, POD, FAR, MCC
   optimizacion: Opcion A (busqueda bayesiana/random de w y θ_A) ← recomendada
               Opcion B (gradiente sustituto end-to-end) ← baseline riguroso
   ▼
VALIDACION: split temporal 70/15/15 · test ≥ 1 ano · reporte por estacion
   comparacion vs. baseline de umbrales fijos (Zambretti)
```

---

## Resumen de decisiones

| Pregunta | Decision | Fuentes |
| --- | --- | --- |
| **Viento** | Descomponer en u = WS·sin(dir), v = WS·cos(dir); z-score por componente; 2 neuronas de entrada. No usar grados ni una sola neurona de direccion. | Fisher (1993); Bishop (2006); Shu et al. (2025); Bastos et al. (2020); Serpa-Usta et al. (2025) |
| **Estacionalidad** | Normalizar con climatologia diaria suavizada (±15 dias, solo train), entrenar UN modelo con todo el ano, test ≥ 1 ciclo estacional, reportar metricas por estacion. Ablation anual-vs-estacional opcional. | van Nieuwkoop & Mehrkanoon (2026); Furtado et al. (2026); AMS/AIES (2023) |
| **Contexto temporal (B)** | Anadir 4 features de contexto al readout: sin/cos(day-of-year) y sin/cos(hora). Bajo coste (+4 pesos), ablation obligatoria por estacion y umbral. | Zeng et al. (2024); Bansal et al. (2025); Khazem & Kanso (2025); Gentile et al. (2025) |
| **Codificacion** | Rate coding Poisson, f_max=200, misma escala en todas las variables. TTFS como ablation opcional de eficiencia. | Neural Processing Letters (2021); Guo et al. (2021); Adrian & Zotterman (1926); Kim et al. (2022) |
| **Entrenamiento** | Dos etapas: capa de features fija (τ_m, θ_i por criterio fisico/estadistico) + readout lineal aprendido (w, θ_A) con BCE y busqueda de hiperparametros sobre validacion. Gradiente sustituto como baseline riguroso. | Gerstner et al. (2014); Diehl & Cook (2015); Ko et al. (2022) |

---

## Referencias

### Viento (u/v)
1. **Fisher, N. I. (1993)**. *Statistical Analysis of Circular Data*. Cambridge University Press.
2. **Bishop, C. M. (2006)**. *Pattern Recognition and Machine Learning*. Springer. — periodicidad y funciones multi-valuadas.
3. **Bishop, C. M.; Nabney, I. T.**. Trabajo sobre estimacion de direccion de viento por scatterometer (Aston University): MLP convencional falla en variable periodica y multi-valuada; se modela la densidad condicional con MDN y nucleos circulares.
4. **Shu, H.; Song, W.; Wang, Y.; Zhang, J.; Tian, W.; Li, C. (2025)**. *WaveHiTS: Wavelet-Enhanced Hierarchical Time Series Modeling for Wind Direction Nowcasting in Eastern Inner Mongolia*. arXiv:2504.06532.
5. **Bastos, B. Q.; Cyrino Oliveira, F. L.; Milidiu, R. L. (2020)**. *ComPonentNet: Processing U- and V-components for spatio-temporal wind speed forecasting*. Electric Power Systems Research, 190, 106922. DOI: 10.1016/j.epsr.2020.106922.
6. **Serpa-Usta, D.; et al. (2025)**. *Atmosphere*, 16(11), 1292. DOI: 10.3390/atmos16111292.

### Estacionalidad
7. **van Nieuwkoop, G.; Mehrkanoon, S. (2026)**. *Temporal Context Conditioning for Seasonality-Aware Precipitation Nowcasting of High-Intensity Rainfall*. arXiv:2606.09959.
8. **Furtado, Molina et al. (2026)**. *Setting the Standard: Recommended Practices for Data Preprocessing in Data-Driven Climate Prediction*. arXiv:2508.07062.
9. **AMS AIES (2023)**. Estudio del DGMR: division por anos consecutivos y manejo del sesgo de periodos de prueba ("Test Heavy/Light").
10. **Ko, J.; Lee, K.; Hwang, H.; Oh, S.-G.; Son, S.-W.; Shin, K. (2022)**. *Effective Training Strategies for Deep-learning-based Precipitation Nowcasting and Estimation*. Computers & Geosciences, 165, 105072. arXiv:2202.10555.
11. **Zeng, C.; Tian, Y.; Zheng, G.; Gao, Y. (2024)**. *How Much Can Time-related Features Enhance Time Series Forecasting?* arXiv:2412.01557.
12. **Bansal, A.; K. Balaji; Lalani, Z. (2025)**. *Temporal Encoding Strategies for Energy Time Series Prediction*. arXiv:2503.15456.
13. **Khazem, S.; Kanso, H. (2025)**. *Cyclical Temporal Encoding and Hybrid Deep Ensembles for Multistep Energy Forecasting*. IEEE CAI (2026). DOI: 10.1109/cai68641.2026.11536464.
14. **Gentile, E. S.; Hunt, K. M. R.; Tomassini, L.; Harvey, B.; Martinez-Alvarado, O. (2025)**. *Global Diurnal Precipitation Cycle in the AI Model GraphCast and a 5-km Unified Model*. Geophysical Research Letters. DOI: 10.1029/2025gl120961.

### Codificacion
15. **Anon. (2021)**. *A Survey of Encoding Techniques for Signal Processing in Spiking Neural Networks*. Neural Processing Letters, 53, 4693-4710. DOI: 10.1007/s11063-021-10562-2.
16. **Guo, W.; Fouda, M. E.; Eltawil, A. M.; Salama, K. N. (2021)**. *Neural Coding in Spiking Neural Networks: A Comparative Study for Robust Neuromorphic Systems*. Frontiers in Neuroscience, 15, 638474. DOI: 10.3389/fnins.2021.638474.
17. **Adrian, E. D.; Zotterman, Y. (1926)**. *The impulses produced by sensory nerve endings*. J. Physiol., 61, 151-171.
18. **Gollisch, T.; Meister, M. (2008)**. *Rapid neural coding in the retina with relative spike latencies*. Science, 319, 1108-1111.
19. **Thorpe, S.; Gautrais, J. (1998)**. *Rank Order Coding*. In: Computational Neuroscience.
20. **Kim, Y.; Park, H.; Moitra, A.; et al. (2022)**. *Rate coding or direct coding: which one is better for accurate, robust, and energy-efficient spiking neural networks?* ICASSP 2022.
21. **Liu, M.; Zheng, H.; Yi, Y. C.**. *Neural Encoding Strategies for Neuromorphic Computing*. (Workshop de VTech.)

### Entrenamiento
22. **Gerstner, W.; Kistler, W. M.; Naud, R.; Paninski, L. (2014)**. *Neuronal Dynamics: From Single Neurons to Networks and Models of Cognition*. Cambridge University Press.
23. **Diehl, P. U.; Cook, M. (2015)**. *Unsupervised learning of digit recognition using spike-timing-dependent plasticity*. Frontiers in Computational Neuroscience, 9, 99.

Los PDFs de acceso abierto (4, 6, 7, 10, 11, 12) estan guardados en `BibliografiaExtraCodificacion/`.
