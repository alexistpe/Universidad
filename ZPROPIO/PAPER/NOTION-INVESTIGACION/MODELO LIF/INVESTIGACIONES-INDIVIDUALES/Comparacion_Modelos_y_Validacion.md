# Comparacion de modelos y validacion del procedimiento

**Proposito:** documento unico y autocontenido que (1) ubica donde esta cada pieza del trabajo, (2) explica como se diseno y cual es la estructura de cada modelo comparado, (3) indica cual es mejor o peor para el objetivo, y (4) evalua si el procedimiento es valido, que se deberia modificar o si no lo es.

**Objetivo del proyecto (recordatorio):** predecir un evento de lluvia ANTES de que suceda (prevision a corto plazo, lead = 1 hora) con un modelo LIF simplificado desplegable en estaciones de bajo costo.

---

## 1. Indice

1. Donde esta cada cosa
2. Objetivo y que significa "predecir antes de que suceda"
3. Los 4 modelos comparados: estructura y diseno de cada uno
4. Resultados: tabla comparativa (mejor / peor)
5. Cual es mejor para el objetivo
6. Validacion del procedimiento (es valido o no)
7. Que modificar (recomendaciones concretas)
8. Veredicto final

---

## 2. Donde esta cada cosa

| Pieza | Archivo | Que contiene |
| --- | --- | --- |
| Diseno completo del LIF | `Diseno_Modelo_LIF.md` | Ecuaciones, arquitectura sensores→alerta, entrenamiento, validacion del prototipo continuo (§9) y ablation spike vs continuo (§9.1) |
| Decision de arquitectura (neuronas fijas vs entrenables) | `Decision_Arquitectura_Neuronas_Sensor.md` | Variantes V1/V2/V3 y los **resultados experimentales** de la ablation (§7) |
| Prototipo continuo (Modelo A) | `prototipos/prototipo_lif.py` | Codigo ejecutable: `python3 prototipo_lif.py` |
| Prototipo spike (Modelos B y B2) | `prototipos/prototipo_lif_spikes.py` | Codigo ejecutable: `python3 prototipo_lif_spikes.py` |
| Preprocesamiento y normalizacion | `Normalizacion.md`, `Codificacion_Estacionalidad_Viento.md`, `SIMULACION_SENSORES_BAJO_COSTO.md` | Investigaciones previas de apoyo |

Todos los archivos estan en:
```
INVESTIGACIONES-INDIVIDUALES/   (raiz del proyecto)
```

---

## 3. Objetivo y que significa "predecir antes de que suceda"

La prediccion es: **"con los datos de la hora actual (y la historia reciente), ¿llovera en la proxima hora?"**

- Entrada: series horarias de 4 variables sinteticas (humedad, presion, temperatura, otra) normalizadas a [0,1].
- Etiqueta `y[t]` = 1 si en la hora siguiente hay lluvia. En los datos sinteticos, la lluvia se genera como "persistencia de 6 horas de valores altos de las variables 0 y 1" + 5% de ruido.
- La estructura temporal es clave para "antes de que suceda": se usa la historia reciente (memoria exponencial `τ_m`) para detectar los precursores (anomalias persistentes) que anuncian la lluvia de la hora siguiente. La prediccion siempre usa datos hasta `t` y predice `t+1`. **No hay fugas de informacion futura.**

---

## 4. Los 4 modelos comparados: estructura y diseno de cada uno

Todos se probaron sobre los MISMOS datos sinteticos (3 anos, 26280 horas, 70% train / 15% validacion / 15% test, en orden temporal). La unica diferencia entre ellos es que SENAL envia cada sensor a la alerta y CUANTO aprende cada parte.

### 4.1. Modelo A — diseno actual: actividad continua + readout ponderado

**Filosofia:** cada sensor es un filtro (suaviza el ruido) y la alerta (regresion logistica) es la unica que aprende. Es la arquitectura estandar de "reservorio computacional".

```
Capa fija:  V_i[t] = α_i·V_i[t-1] + (1−α_i)·x̂_i[t]       4 sensores LIF, τ_m=[6,6,3,1] h
            Salida: actividad continua a_i[t] = V_i[t]     (cuanto lleva integrada cada variable)

Contexto:   sin/cos(doy), sin/cos(hora)                   4 features de estacionalidad

Capa que aprende:  I_A[t] = Σ w_i·a_i[t] + Σ v_j·ctx_j[t]  regresion logistica (11 pesos)
            P(lluvia) = σ(I_A[t] − θ_A),  θ_A=0.20 calibrado en validacion
```

- **Parametros libres:** 11 (los pesos). `τ_m` y contexto son fijos.
- **Lo que aprende:** cuanto pesa cada variable y el contexto. Con los datos sinteticos aprendio `w = [+0.63, +0.59, ~0, ~0]` → identifico correctamente las 2 variables informativas y anulo las 2 falsas.

### 4.2. Modelo B — variante spike V1: sensores con umbral propio + spikes integrados

**Filosofia (la propuesta que tu querias evaluar):** cada sensor tiene SU umbral de alarma `θ_i` aprendido, dispara spikes cuando su variable entra en rango peligroso, y la alerta integra esos spikes con su propia memoria `τ_A`.

```
Capa aprendida por busqueda:  θ_i = percentil 70 de la actividad en train  (por variable)
Capa fija:                    V_i[t] = α_i·V_i[t-1] + (1−α_i)·x̂_i[t]
                              spike_i[t] = 1 si V_i[t] ≥ θ_i, luego reset a 0

Integracion de la alerta:     E_i[t] = EMA de spike_i con τ_A = 12 h   (memoria: acumula "cuantos spikes recientes")
Capa que aprende:             I_A[t] = Σ w_i·E_i[t] + Σ v_j·ctx_j[t]    regresion logistica
                              P(lluvia) = σ(I_A[t] − θ_A),  θ_A=0.15 calibrado en validacion
```

- **Parametros libres:** 11 pesos + 6 `θ_i` (por busqueda) + `τ_A` (barrido en validacion, resulto 12 h).
- **La diferencia real con A:** la alerta ya no ve "cuanta humedad hay" (valor continuo) sino "la humedad disparo o no su alarma recientemente" (eventos binarios suavizados por `τ_A`).
- **Detalles medidos:** `θ_i ≈ [0.568, 0.574, 0.588, 0.593]`; tasa de disparo en train ≈ [3%, 3%, 5.6%, 13.6%] — los sensores informativos disparan poco (~3% de las horas), los falsos mas.

### 4.3. Modelo B2 — spikes instantaneos (sin integracion de la alerta)

**Identico a B pero la alerta NO tiene memoria `τ_A`:** las features son el spike binario del momento, sin acumular evidencia.

```
spike_i[t] = 1 si V_i[t] ≥ θ_i        (mismos θ_i que B)
I_A[t] = Σ w_i·spike_i[t] + contexto  (sin EMA, sin memoria)
```

- Sirve como experimento de control para aislar el efecto de la integracion `τ_A`.

### 4.4. Baseline — umbral fijo sobre una variable

**Filosofia:** regla simple de referencia: si la variable 0 supera un umbral fijo, alerta. Sin memoria temporal y sin combinar variables.

```
lluvia si x̂_0 > 0.70    (umbral calibrado en validacion)
```

---

## 5. Resultados: tabla comparativa (mejor / peor)

Metricas en test (tasa de lluvia en test: 7.9%):

| Modelo | Estructura | CSI | POD | FAR | Lectura |
| --- | --- | --- | --- | --- | --- |
| **A** (continuo + pesos) | filtros fijos + readout | **0.163** | 0.255 | **0.688** | El mas preciso: menos falsas alarmas |
| **B** (spikes integrados, V1) | spikes con θ_i + τ_A=12h | 0.166 | **0.332** | 0.752 | El que MAS lluvia detecta, pero con mas falsas alarmas |
| **B2** (spikes sin integracion) | spikes directos sin memoria | 0.069 | 0.123 | 0.862 | El PEOR: casi inutil |
| **Base** (umbral fijo X0) | una variable, un umbral | 0.123 | 0.313 | 0.832 | Referencia que todos los modelos LIF superan |

**Definiciones rapidas:**
- **CSI** (indice de calidad global): aciertos / (aciertos + falsas alarmas + lluvias perdidas). Maximo = 1, mejor cuanto mas alto. Combina todo en un numero.
- **POD** (probabilidad de deteccion): de cada 100 lluvias que hubo, cuantas aviso. B detecta 33%, A 26%, Base 31%.
- **FAR** (proporcion de falsas alarmas): de cada 100 alertas que dio, cuantas fueron falsas. A solo falla 69 de 100; B falla 75; Base 83. Cuanto mas bajo, mejor.

### Orden de mejor a peor (para predecir antes de que suceda)

1. **B y A empatan en CSI** (0.166 vs 0.163), con filosofias opuestas:
   - **A** = pocas falsas alarmas, pierde mas eventos.
   - **B** = avisa mas lluvias reales, a costa de avisar mas veces de mas.
2. **Base** los sigue (0.123): cualquier version LIF supera a la regla de un solo umbral.
3. **B2** es un fracaso (0.069): demuestra que **los spikes por si solos no sirven**; lo que los hace funcionar es la memoria `τ_A` de la alerta.

---

## 6. Cual es mejor para el objetivo

**Depende de que fallo es mas caro en el sistema de alerta:**

- Si el usuario (agricultor, comunidad) **deja de creer en el sistema cuando avisa de mas**, conviene **A** (FAR 0.688 es el mas bajo, menos falsas alarmas).
- Si lo prioritario es **no perderse ninguna lluvia** (p. ej. riesgo de inundacion), conviene **B** (POD 0.332, detecta el 30% mas de eventos que A).

**Recomendacion por defecto: Modelo A** como modelo principal del paper: mismo CSI que B, la mitad de parametros libres, sin `τ_A` que calibrar, y el FAR mas bajo (el mas fiable como alerta). **Modelo B** se reporta como variante spike equivalente con mejor deteccion y mejor interpretabilidad por variable ("el sensor de humedad dispara solo en su rango de alarma"), que es el claim que te interesaba evaluar. **B2 y Base** se reportan como controles (uno muestra por que la integracion es necesaria; el otro, que los modelos LIF superan a la regla simple).

---

## 7. Validacion del procedimiento (es valido o no)

### 7.1. Lo que SI esta bien hecho (valido)

1. **Division temporal de datos** (train→validacion→test en orden cronologico, sin barajar): respeta que la prediccion usa el pasado para predecir el futuro. Esto evita la fuga de informacion (leakage), el error metodologico mas comun en prediccion.
2. **Hiperparametros y calibracion SOLO en validacion, test intacto:** los `θ_i`, `τ_A` y `θ_A` se eligieron en validacion; el test solo se uso una vez al final. Metodologia correcta.
3. **Metricas adecuadas a un evento raro (CSI/POD/FAR), no accuracy:** la lluvia es ~8% de las horas; con accuracy un modelo que nunca avisara "acertaria" el 92%. Usar CSI/POD/FAR es lo correcto para predecir eventos raros (es la practica estandar en nowcasting, ver refs. 8-9 de `Diseno_Modelo_LIF.md`).
4. **El modelo aprende lo que debe:** los pesos de A (`[+0.63, +0.59, ~0, ~0]`) identifican exactamente las variables que importan. El procedimiento de entrenamiento funciona.
5. **Comparacion justa:** los 4 modelos se evaluaron sobre los mismos datos, misma etiqueta, misma division. La unica diferencia es la arquitectura. La ablation es controlada.
6. **El objetivo "antes de que suceda" se respeta:** la etiqueta es `y[t+1]` y las features usan datos hasta `t`.

### 7.2. Limitaciones (lo que hace que los numeros NO se puedan tomar como conclusion final)

1. **Datos sinteticos, no reales:** los datos son AR(1) artificiales con una etiqueta idealizada. Los resultados demuestran que el METODO funciona de punta a punta (pipeline correcto, aprendible, comparable), pero **no prueban nada sobre lluvia real de EDDF**. Todo hay que re-ejecutarlo con datos reales.
2. **Lead de 1 hora:** "antes de que suceda" aqui significa solo 1 hora de antelacion. Si el objetivo real es avisar con mas anticipacion (p. ej. 6 h), hay que cambiar la etiqueta a `y[t+6]` y re-calibrar `τ_m`.
3. **La etiqueta sintetica premia la persistencia:** "lluvia = 6 horas de valores altos" significa que el modelo aprende basicamente persistencia de anomalias. En lluvia real los precursores (caida de presion, subida de humedad) son mas variados; puede que el orden de A vs B cambie con datos reales.
4. **`τ_A = 12 h` de B se eligio en validacion con un barrido finito** (5 valores); el maximo quedo cerca del limite del barrido (CSI-val 0.224 @ 12h vs 0.189 @ 24h). No parece sobreajustado (test 0.166 ≈ val 0.227), pero conviene confirmar con datos reales.
5. **Solo se probo una familia de `τ_m`** (`[6,6,3,1]`). La sensibilidad de CSI a `τ_m` no se midio en esta ablation (esta pendiente para datos reales, §9 leccion 2 del diseno).
6. **Diferencia menor de codigo:** el `doy` se genera con ciclo de 366 dias pero el seno divide por 365.25. Irrelevante en sinteticos; unificar en datos reales.

### 7.3. Veredicto de validez

**El procedimiento es VALIDO para el objetivo**, con una condicion: valida que el diseno, el entrenamiento y la evaluacion estan bien planteados y que las arquitecturas se comportan de forma distinguible y explicable. Lo que NO es valido todavia es tomar los numeros como conclusion sobre lluvia real: falta ejecutar el mismo pipeline con datos EDDF.

---

## 8. Que modificar (recomendaciones concretas)

| # | Accion | Por que | Cuando |
| --- | --- | --- | --- |
| 1 | **Ejecutar el mismo pipeline con datos EDDF reales** (2020-2024) | Los numeros actuales son de datos sinteticos; lo unico que validan es el metodo | Antes de escribir el paper |
| 2 | **Decidir el punto de operacion (θ_A) segun el costo de la falsa alarma** | A y B empatan en CSI pero con trade-off POD/FAR opuesto; la eleccion es de producto, no tecnica | Antes del paper |
| 3 | **Si se quiere mas antelacion, cambiar la etiqueta a `y[t+k]`** (p. ej. k=3 o 6 h) y re-calibrar `τ_m` | "Antes de que suceda" con 1 h es muy corto para avisar | Si el objetivo lo exige |
| 4 | **Barrer `τ_m` por variable y reportar sensibilidad de CSI** | Confirmar que la eleccion de `τ_m=[6,6,3,1]` no es la que domina el resultado | En datos reales |
| 5 | **Mantener A como modelo principal, B como variante spike** | A: menor complejidad y menor FAR. B: mejor POD e interpretabilidad por variable | Decision ya tomada con la ablation |
| 6 | **Unificar el ciclo del `doy`** (366 vs 365.25) | Inconsistencia menor de codigo | Antes de datos reales |
| 7 | (Opcional) **Agregar `θ_i` por gradiente (LTMD) como tercer brazo de la ablation** | Completar la comparacion de la variante V1; hoy solo se probo por busqueda | Solo si el paper quiere ese claim |

**Lo que NO hay que modificar:** la metodologia (division temporal, calibracion en validacion, metricas CSI/POD/FAR, comparacion sobre los mismos datos) esta bien planteada y se mantiene igual.

---

## 9. Veredicto final

1. **Los 4 modelos** estan comparados sobre los mismos datos y el resultado es claro: A y B empatan en calidad global (CSI) con puntos de operacion opuestos; ambos superan al baseline; los spikes sin integracion (B2) no sirven.
2. **El procedimiento es valido** para predecir un evento de lluvia antes de que suceda (prediccion a 1 hora, sin fuga de informacion, calibracion correcta, metricas correctas).
3. **Para el objetivo "predecir antes de que suceda", la recomendacion es Modelo A** como base del paper (mas simple, menos falsas alarmas) y **Modelo B como variante spike equivalente e interpretable** que justifica la hipotesis que querias evaluar.
4. **El paso pendiente que decide todo:** repetir con datos EDDF reales. Los numeros sinteticos validan el metodo, no la lluvia.
