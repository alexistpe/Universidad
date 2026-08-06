# Diseño del modelo LIF simplificado

**Proposito:** ser la guia tecnica para disenar y codificar el modelo LIF simplificado del proyecto. Responde, en orden, a: (1) que es un LIF y que permite hacer, (2) cuales son sus ecuaciones fundamentales y variables, (3) como se implementa en codigo, (4) como se conectan las neuronas sensor con la neurona de alerta, y (5) como funciona el entrenamiento y como se obtienen los valores de cada neurona.

**Alcance:** documento de diseno. No modifica el doc principal ni Notion. Complementa `Normalizacion.md` (preprocesamiento) y `Codificacion_Estacionalidad_Viento.md` (rate coding, estacionalidad, entrenamiento en dos etapas).

---

## Indice

1. Que es un LIF simplificado y que permite hacer
2. Ecuaciones fundamentales y variables del modelo
3. Componentes y parametros
4. Arquitectura: de los sensores a la neurona de alerta
5. Implementacion en codigo
6. Entrenamiento y obtencion de valores por neurona
7. Ejemplo numerico completo
8. Decisiones de diseno abiertas
9. Validacion del prototipo
10. Referencias

---

## 1. Que es un LIF simplificado y que permite hacer

El modelo **Leaky Integrate-and-Fire** (LIF) es la neurona artificial mas simple con memoria temporal (Gerstner et al., 2014; Burkitt, 2006). Se comporta como un circuito RC: acumula corriente de entrada en el potencial de membrana `V`, lo deja **filtrarse** (leak) exponencialmente, y cuando `V` supera un umbral `θ` **dispara** un spike y se reinicia.

"Simplificado" significa aqui que se usara la version discreta y de un solo compartimiento: sin dendritas, sin canales ionicos, sin plasticidad biologica. Solo tres operaciones por paso: una multiplicacion (fuga), una suma (integracion) y una comparacion (umbral). Eso es lo que la hace desplegable en hardware de gama baja.

**Que permite hacer concretamente en este proyecto:**

| Capacidad | Como la da el modelo |
| --- | --- |
| Deteccion de anomalias por variable | Cada neurona sensor integra su variable y dispara si esta "anomalamente alta/persistente" para la epoca del ano |
| Prediccion binaria de lluvia (proxima hora) | La neurona de alerta combina las anomalias ponderadas y dispara si la combinacion supera su umbral |
| Explicabilidad | Los pesos de la alerta indican que variable contribuye y con que signo a cada prediccion |
| Robustez al ruido de sensores baratos | La integracion con fuga es un promedio exponencial: suaviza el ruido de BME280/DHT22/pluviometro |
| Un solo modelo para todo el ano | Gracias a la normalizacion estacional (anomalias) + features de contexto temporal |
| Hardware de bajo costo | Solo sumas, productos y comparaciones (ver seccion 5): implementable en MicroPython/C |

**Analogia util para el paper:** cada neurona sensor es un **filtro IIR de primer orden** (pasa-bajos) sobre la anomalia de su variable. El modelo completo es un **banco de filtros fijos + regresion logistica** en la alerta. Esta es la manera tecnica de explicar "como funciona" sin perderse en biologia.

---

## 2. Ecuaciones fundamentales y variables del modelo

### 2.1. Forma continua (la definicion canonica)

La ecuacion diferencial del LIF es:

```
τ_m · dV/dt = −(V − V_rest) + R_m · I(t)
```

| Simbolo | Significado | Unidad | En este modelo |
| --- | --- | --- | --- |
| `V(t)` | Potencial de membrana | mV (relativo) | actividad de la variable (adimensional) |
| `V_rest` | Potencial de reposo | mV | 0 (escala normalizada) |
| `τ_m` | Constante de tiempo de membrana | s (u horas) | 2-4 h por variable (escala de precursores) |
| `R_m` | Resistencia de membrana | Ω | se absorbe en los pesos aprendidos |
| `I(t)` | Corriente de entrada | mA | proporcional a la variable normalizada |

La solucion dice lo esencial: `V` **tiende** a `V_rest + R_m·I` con constante `τ_m`. Si la entrada se mantiene, `V` sube asintoticamente hacia ella; si la entrada se corta, `V` decae exponencialmente con `τ_m`.

### 2.2. Disparo, reset y refractariedad

```
if V(t) >= θ:    emitir spike (s=1)
                 V(t) <- V_reset          (reset, tipicamente V_rest)
                 no recibir entrada durante t_ref   (periodo refractario)
```

### 2.3. Forma discreta (la que se codifica)

Con paso temporal `Δt` y **Euler implicito/explicito** (equivalentes si `Δt << τ_m`):

```
α = e^(−Δt/τ_m)                      (factor de fuga exacto)
V[t] = α·V[t-1] + (1−α)·(V_rest + R_m·I[t])
```

Con `V_rest = 0` y absorbiendo la escala en la corriente:

```
V[t] = α·V[t-1] + (1−α)·I[t]
```

Esta es la ecuacion que se implementa. `α` juega el papel de "cuanta memoria conserva el paso anterior".

### 2.4. Interpretacion clave: promedio movil exponencial (EMA)

Reordenando la ecuacion se ve que el LIF subumbral **es** un promedio movil exponencial:

```
V[t] = (1−α)·I[t] + (1−α)·α·I[t-1] + (1−α)·α²·I[t-2] + ...
```

Es decir: la actividad de la neurona sensor en el instante `t` resume **toda la historia** de la variable, con pesos que decaen exponencialmente. La constante `τ_m` controla cuanta historia: con `τ_m = 3 h`, la contribucion de hace 3 h pesa `e^(−1) ≈ 37%`; hace 6 h, `e^(−2) ≈ 14%`. Esto es exactamente lo que se quiere para capturar la evolucion de precursores (caida de presion, subida de humedad) en ventanas de 6-12 h.

### 2.5. Valores de α segun τ_m (paso horario)

| τ_m | 1 h | 2 h | 3 h | 4 h | 6 h | 12 h |
| --- | --- | --- | --- | --- | --- | --- |
| α = e^(−1/τ_m) | 0.37 | 0.61 | 0.72 | 0.78 | 0.85 | 0.92 |

---

## 3. Componentes y parametros

### 3.1. Neuronas del modelo

Con la descomposicion u/v del viento, la arquitectura queda:

```
6 neuronas sensor (una por variable normalizada):
    T, P (o ΔP), HR, u, v, PRECIP
+ 4 features de contexto temporal (sin/cos de doy y hora)  ← NO son LIF, entran al readout
+ 1 neurona de alerta (readout)
```

### 3.2. Parametros: fijos vs aprendidos

| Parametro | Simbolo | Valor/regla | Quien lo decide |
| --- | --- | --- | --- |
| Constante de tiempo | `τ_m,i` | 2-4 h por variable (T y HR mas lentas, P y PRECIP mas rapidas) | Fijado (literatura de precursores) |
| Umbral de disparo sensor | `θ_i` | Percentil de la actividad (p.ej. disparar ~5-10% del tiempo) o libre | Fijado o aprendido |
| Potencial de reposo | `V_rest` | 0 | Fijado |
| Reset | `V_reset` | 0 (reset total) | Fijado |
| Tasa maxima | `f_max` | 200 spikes/s | Fijado (doc principal) |
| Pesos sensor→alerta | `w_i` | m + 4 valores | **Aprendido** |
| Umbral de la alerta | `θ_A` | 1 valor | **Aprendido** |

Regla de oro del diseno: **lo que tiene interpretacion fisica se fija; lo que solo se puede aprender de los datos se aprende.** Esto mantiene el modelo con ~11-15 parametros libres (m + 1 + 4), entrenable con busqueda o regresion logistica sin GPU.

---

## 4. Arquitectura: de los sensores a la neurona de alerta

### 4.1. Flujo de datos

```
Variable cruda → transformacion (z-score estacional / ΔP / u/v / binaria)
  → x̂ ∈ [0,1]  (tras clip y min-max)
  → I[t] = x̂[t] · f_max        (rate coding)   O   I[t] = x̂[t]   (directo)
  → neurona sensor i: V_i[t] = α_i·V_i[t-1] + (1−α_i)·I_i[t]
  → actividad a_i[t] = V_i[t]  (+ spike si V_i >= θ_i)
  → sinapsis: I_A[t] = Σ_i w_i · a_i[t]  (+ Σ_j v_j · tiempo_j[t])
  → alerta:   V_A[t] = α_A·V_A[t-1] + (1−α_A)·I_A[t]
  → decision: si V_A[t_final] >= θ_A → lluvia la proxima hora
```

### 4.2. La conexion sensor → alerta (las sinapsis)

Cada neurona sensor `i` se conecta a la alerta a traves de **una sinapsis con peso `w_i`** (excitatoria si `w_i > 0`, inhibitoria si `w_i < 0`). La alerta recibe la **suma ponderada** de las actividades:

```
I_A[t] = w_1·a_1[t] + w_2·a_2[t] + ... + w_6·a_6[t] + v_1·doy_sin + v_2·doy_cos + v_3·hod_sin + v_4·hod_cos
```

En forma matricial: `I_A[t] = W^T · x[t]`, donde `W = [w_1..w_6, v_1..v_4]` y `x[t]` es el vector de features en `t`.

**Interpretacion meteorologica:** un `w_HR` grande y positivo significa "humedad anomala empuja a llover"; un `w_P` negativo (sobre la anomalia de presion) significa "presion subiendo empuja a no llover" (la lluvia suele venir con presion en caida, que es anomalia negativa). El signo y magnitud de cada peso es interpretable.

### 4.3. La neurona de alerta como LIF

Para ser coherentes con "6 neuronas LIF", la alerta tambien integra (con su propio `τ_A`, corto, 1-2 h) y dispara al superar `θ_A`. Pero como las features ya llevan memoria, la alerta puede **decidir al final de la ventana**:

- **Version binaria (hardware):** predice lluvia si `V_A[t_final] >= θ_A`.
- **Version probabilistico (calibracion):** `P(lluvia) = σ(V_A[t_final] − θ_A)` con la sigmoide `σ(x) = 1/(1+e^(−x))`. La sigmoide es la version suave del umbral: el umbral es `P ≥ 0.5`. Esto permite calibrar el umbral en validacion (seccion 6.3).

### 4.4. Rate coding (Poisson) vs inyeccion directa: puente teorico

Hay dos formas de alimentar las neuronas:

- **Camino A (rate coding, doc principal 7.3):** cada paso genera un tren de spikes de Poisson con tasa `λ = x̂·f_max`.
- **Camino B (inyeccion directa):** se inyecta directamente `I = x̂·f_max`.

La **equivalencia teorica** es lo que hace el diseno limpio: como el LIF es lineal (subumbral), el valor esperado de la membrana bajo Poisson **es** la membrana con inyeccion directa (la media del Poisson es `λ`). Es decir:

```
E[ V_A con rate coding ] = V_A con inyeccion directa
```

Por eso en la implementacion de referencia se usa la forma directa (determinista, reproducible, entrenable con regresion logistica), y el rate coding de Poisson queda como la **version de hardware** (o de ablation) del mismo modelo. Esto se puede citar con Herranz-Celotti & Rouat (2022) y la equivalencia promedio/EMD que ya se uso en `Normalizacion.md`.

**Consecuencia practica importante:** las constantes de escala (`f_max`, `R_m`) son factores constantes de un modelo lineal → **se absorben en los pesos aprendidos `w`**. No hay que "sintonizarlas" a mano para que las tasas sean comparables; la regresion logistica las acomoda sola. (Si se mantiene la version Poisson, si hay que fijar `f_max` igual en todas las variables, como ya esta decidido.)

---

## 5. Implementacion en codigo

### 5.1. La neurona LIF (pieza basica)

```python
import numpy as np

class NeuronaLIF:
    def __init__(self, tau_m, dt=1.0, theta=np.inf, v_rest=0.0, v_reset=0.0):
        self.alpha = np.exp(-dt / tau_m)   # factor de fuga
        self.theta = theta                 # umbral de disparo
        self.v_rest = v_rest
        self.v_reset = v_reset
        self.v = v_rest

    def paso(self, corriente):
        self.v = self.alpha * self.v + (1 - self.alpha) * (self.v_rest + corriente)
        spike = self.v >= self.theta
        if spike:
            self.v = self.v_reset
        return self.v, spike
```

`dt=1.0` significa **1 paso = 1 hora** (la frecuencia de los datos). Si se quisiera simular spikes con micro-pasos, se baja `dt` (p.ej. `dt=0.01` h) y `τ_m` se da en las mismas unidades.

### 5.2. El codificador de rate coding (Camino A)

```python
def rate_a_poisson(x_norm, f_max, dt_sim, rng):
    p = np.clip(x_norm, 0.0, 1.0) * f_max * dt_sim
    return (rng.random(p.shape) < p).astype(float)
```

Cada micro-paso produce 1 si hay spike (probabilidad `p`), 0 si no. El paso de la neurona se llama con `dt_sim` y con esta corriente.

### 5.3. El modelo completo

```python
class ModeloLluvia:
    def __init__(self, taus, thetas_sensores, w, theta_alerta, f_max=1.0):
        self.sensores = [NeuronaLIF(tau_m=t, theta=th) for t, th in zip(taus, thetas_sensores)]
        self.w = np.array(w)                      # pesos sensor->alerta + contexto temporal
        self.f_max = f_max
        self.alerta = NeuronaLIF(tau_m=1.5, theta=theta_alerta)

    def features(self, X):                        # X: (T_ventana, m) con x̂ en [0,1]
        T, m = X.shape
        A = np.zeros(T * m).reshape(T, m)
        for t in range(T):
            for i, sn in enumerate(self.sensores):
                A[t, i] = sn.paso(self.f_max * X[t, i])[0]
        return A

    def predecir(self, X, contexto=None):         # contexto: (4,) sin/cos doy y hora
        A = self.features(X)                       # actividades integradas
        ultimo = A[-1]                             # o np.mean(A[-k:], axis=0)
        s = ultimo @ self.w[: len(ultimo)]
        if contexto is not None:
            s = s + contexto @ self.w[len(ultimo):]
        proba = 1.0 / (1.0 + np.exp(-(s - self.alerta.theta)))
        return proba, A
```

Notas de la implementacion:
- Se usa la **actividad continua** (membrana subumbral) como feature de la alerta; el spike de la neurona sensor se puede usar aparte como "alarma por variable" o como feature binaria adicional.
- `predecir` evalua la alerta al final de la ventana (equivalente a la neurona de alerta integrando la suma).
- Todo es vectorizable: la capa de features es un filtro IIR aplicado a cada columna; `scipy.signal.lfilter` o `pandas .ewm()` lo hacen sin bucles.

### 5.4. Version vectorizada de la capa de features (referencia)

```python
def capa_features(X, alphas):
    A = np.empty_like(X)
    V = np.zeros(X.shape[1])
    for t in range(X.shape[0]):
        V = alphas * V + (1 - alphas) * X[t]
        A[t] = V
    return A
```

Con `alphas = np.exp(-1.0 / np.array(taus))`. Esta es la operacion equivalente a `pandas.ewm(alpha=1-alpha)` por columna. Se puede usar para construir la matriz de features de TODO el entrenamiento en un solo bucle, lista para la regresion logistica.

### 5.5. Pseudocodigo del pipeline completo

```
1. cargar datos horarios EDDF (2020-2024)
2. QC + (opcional) simulacion de sensores de bajo costo
3. transformaciones: z-score estacional (climatologia diaria, solo train),
   ΔP/Δt, u/v, precipitacion binaria
4. clip a [-3,3] y min-max a [0,1]  ->  x̂
5. features: A = capa_features(x̂, alphas)         (banco de filtros fijo)
6. contexto: doy_sin, doy_cos, hod_sin, hod_cos
7. X_readout = [A_final, contexto]; y = lluvia en la hora siguiente
8. entrenar W, θ_A  (seccion 6)
9. evaluar CSI/POD/FAR por estacion vs baseline de umbrales fijos
```

---

## 6. Entrenamiento y obtencion de valores por neurona

El entrenamiento sigue la separacion de `Codificacion_Estacionalidad_Viento.md` (Pregunta D): **dos etapas**.

### 6.1. Etapa fija (NO se entrena)

Se fijan por criterio fisico/estadistico:

- **τ_m por variable:** de la escala de precursores (2-4 h). Presion (señal rapida) y precipitacion (persistencia corta) con τ_m de 1-2 h; temperatura y humedad (señales lentas) con 3-4 h. Se reporta analisis de sensibilidad de CSI vs τ_m.
- **θ_i (umbrales de disparo de sensores):** opcion estadistica: el percentil 90-95 de la actividad en el train (disparan ~5-10% de las horas). Opcion aprendida: dejar como parametro de la busqueda.
- **V_rest = 0, V_reset = 0, f_max = 200.**

Estos valores se obtienen **solo del conjunto de entrenamiento** y se congelan.

### 6.2. Etapa aprendida (los parametros libres)

Parametros libres: `W = [w_1..w_6, v_1..v_4]` y `θ_A`.

El punto matematico que hace todo simple: **la alerta es lineal en las features**, asi que `P(lluvia) = σ(W^T·x + b)` es una **regresion logistica** (con `b = −θ_A`). Por lo tanto:

1. Se construye la matriz de features sobre el train: `X_train = [actividades finales de cada ventana | contexto]`.
2. Se minimiza la **binary cross-entropy (BCE)** entre `σ(W^T·x + b)` y la etiqueta `y` (llovio la proxima hora).
3. Se calibra el umbral de decision en validacion (no en train).

### 6.3. Opcion A (RECOMENDADA): regresion logistica + calibracion

```python
def entrenar_readout(X, y):
    X1 = np.column_stack([X, np.ones(len(X))])     # bias = -θ_A
    w = np.zeros(X1.shape[1])
    for _ in range(300):
        grad = X1.T @ (1/(1+np.exp(-X1@w)) - y)
        w -= 0.5 * grad / len(y)
    return w                                        # w[-1] == -θ_A

w = entrenar_readout(X_train, y_train)
proba_val = 1/(1+np.exp(-(X_val @ w[: -1] + w[-1])))
# calibrar θ_A sobre validacion maximizando CSI
```

La calibracion de `θ_A` es: probar varios umbrales en validacion y elegir el que maximiza **CSI** (no accuracy; la lluvia es rara). Con esto se obtiene el umbral de la alerta.

**Alternativa equivalente:** como el readout es logistico, `sklearn.linear_model.LogisticRegression` da el mismo resultado en una linea. La busqueda manual (bayesiana/random sobre `W` y `θ_A` maximizando CSI, `scipy.optimize`/`Optuna`) es la version "sin dependencias" del paper de bajo costo.

### 6.4. Opcion B: gradiente sustituto (baseline riguroso)

Si el paper quiere claim "SNN entrenado end-to-end", se entrena el LIF completo con gradiente sustituto (snnTorch, Norse, SpikingJelly): la funcion de disparo no es diferenciable, se aproxima con una recta en el gradiente. Mas costoso; se recomienda como comparativa, no como metodo principal.

### 6.5. Resumen: de donde sale cada valor de cada neurona

| Valor | Como se obtiene | Paso |
| --- | --- | --- |
| `α_i` (fuga de cada sensor) | `exp(−1/τ_m,i)` con τ_m fisico (2-4 h) | 6.1 |
| `θ_i` (umbral sensor) | percentil 90-95 de la actividad en train | 6.1 |
| `a_i[t]` (actividad) | filtro IIR sobre la variable normalizada | 5.4 |
| `w_i`, `v_j` | regresion logistica / busqueda (BCE) | 6.2-6.3 |
| `θ_A` | calibracion en validacion (maximizar CSI) | 6.3 |
| prediccion | `σ(W^T·x + b) >= 0.5` (o umbral calibrado) | 5.3 |

---

## 7. Ejemplo numerico completo

### 7.1. Configuracion (paso horario, directo)

- 3 variables de ejemplo para legibilidad: HR, dP, T. τ_m = [4, 2, 3] h → α = [0.78, 0.61, 0.72].
- `I[t] = x̂[t]` (directo; `f_max` absorbido en `w`).
- V_rest = 0. Umbrales sensor: θ = [0.5, 0.5, 0.5].

### 7.2. Evolucion de las membranas (3 horas)

| t | x̂_HR | x̂_dP | x̂_T | V_HR | V_dP | V_T |
| --- | --- | --- | --- | --- | --- | --- |
| t-2 | 0.5 | 0.3 | 0.4 | 0.11 | 0.12 | 0.11 |
| t-1 | 0.7 | 0.2 | 0.55 | 0.24 | 0.09 | 0.24 |
| t   | 0.8 | 0.1 | 0.60 | **0.36** | 0.09 | **0.34** |

Verificacion de un valor: `V_HR[t] = 0.78·0.24 + 0.22·0.8 = 0.187 + 0.176 = 0.36`. La humedad sube (persistencia); la caida de presion (`x̂_dP` bajo) se refleja en `V_dP` bajo; la temperatura apenas cambia.

### 7.3. Readout

Supongamos pesos aprendidos: `w = [w_HR=0.9, w_dP=−0.7, w_T=0.2]` y `b = −θ_A = −0.25`.

```
s = 0.9·0.36 − 0.7·0.09 + 0.2·0.34 = 0.324 − 0.063 + 0.068 = 0.329
P(lluvia) = σ(0.329 − 0.25) = σ(0.079) ≈ 0.52
```

Con `θ_A` calibrado en 0.25, este caso apenas cruza el umbral: humedad alta (peso grande positivo) gana sobre la presion en caida (peso negativo). Si en la hora siguiente la humedad siguiera subiendo, `V_HR` seguiria creciendo y `P` superaria claramente 0.5 → la alerta dispara.

### 7.4. Lectura

- Los pesos se interpretan: `w_HR` grande positivo (la humedad anomala es el motor), `w_dP` negativo (presion cayendo → anomalia baja → contribuye, porque el peso negativo multiplica un valor bajo).
- El umbral de la alerta fija "cuanta evidencia combinada se necesita".

---

## 8. Decisiones de diseno abiertas

A confirmar antes de codificar el modelo final:

1. **Feature de la alerta:** ¿actividad continua (membrana, recomendada) o spike binario del sensor (alarma por variable)? O ambas (actividad + tasa de spikes).
2. **La alerta integra o decide:** ¿`V_A` se evalúa al final de la ventana (recomendado) o se requiere un disparo en cualquier paso dentro de la ventana?
3. **τ_m por variable:** ¿se fijan individualmente (recomendado) o uno global con sensibilidad?
4. **Reset:** ¿`V_reset = 0` (recomendado) o `V_reset = θ − Δ` (reset parcial, mas biológico)?
5. **Umbrales θ_i:** ¿percentiles fijos (90-95) o libres en la busqueda?
6. **Feature de la ventana:** ¿actividad del ultimo paso, promedio de los ultimos k pasos, o maximo de la ventana?
7. **Version del codigo:** ¿forma directa determinista (base) + Poisson como ablation/hardware, o solo Poisson?
8. **f_max y micro-pasos:** si se usa Poisson, definir `dt_sim` y cuantos micro-pasos por hora (τ_m >> dt_sim).

---

## 9. Validacion del prototipo

El prototipo `prototipos/prototipo_lif.py` implementa la cadena completa con datos sinteticos (AR(1) estacionario, 4 variables, etiqueta = persistencia de 6 h de las 2 primeras + 5% de ruido) y se ejecuta con `python3 prototipo_lif.py`. Resultados:

- **Capa de features:** `τ_m = [6, 6, 3, 1]` h (alineados con la ventana de 6 h de la etiqueta). Los umbrales de disparo en el percentil 95 dan tasa de disparo del 5% por sensor, como se diseño.
- **Readout (regresion logistica sobre features estandarizadas):** pesos `w ≈ [+0.63, +0.59, ~0, ~0]` — positivos solo en las 2 variables informativas, ~0 en las 2 falsas (el modelo identifico correctamente que variables importan).
- **Calibracion:** umbral `θ_A = 0.2` elegido en validacion maximizando CSI (la lluvia es rara: tasa ~8% en test).
- **Test:** LIF `CSI=0.163, POD=0.255, FAR=0.688` vs baseline de umbral fijo `CSI=0.123, POD=0.313, FAR=0.832`. El LIF supera al baseline en CSI (+32%) y reduce FAR sustancialmente.

Lecciones para los datos reales de EDDF:
1. **Estandarizar features antes del readout** es necesario para que el GD converja (sin normalizar el readout se colapsaba a "predecir siempre lluvia").
2. **`τ_m` debe alinearse con la ventana de la etiqueta** (aqui 6 h); taus de 1-2 h dejaban la etiqueta casi sin señal. En datos reales se debe barrer `τ_m` y reportar sensibilidad de CSI.
3. Con una etiqueta desbalanceada, **calibrar `θ_A` en validacion** (no en train) y evaluar CSI/POD/FAR, no accuracy.

## 10. Referencias

1. **Gerstner, W.; Kistler, W. M.; Naud, R.; Paninski, L. (2014)**. *Neuronal Dynamics: From Single Neurons to Networks and Models of Cognition*. Cambridge University Press. — definicion del LIF, discretizacion, EMA.
2. **Burkitt, A. N. (2006)**. *A Review of the Integrate-and-Fire Neuron Model: I. Homogeneous Synaptic Input*. Biological Cybernetics, 95, 1-19. — revision de las variantes IF y su comportamiento.
3. **Gerstner, W.; Kistler, W. M. (2002)**. *Spiking Neuron Models*. Cambridge University Press.
4. **Herranz-Celotti, L.; Rouat, J. (2022)**. *On the role of direct inputs and spike rate in the LIF model* / encoding directo. arXiv:2202.00282. — inyeccion directa de corriente.
5. **Diehl, P. U.; Cook, M. (2015)**. *Unsupervised learning of digit recognition using spike-timing-dependent plasticity*. Frontiers in Computational Neuroscience, 9, 99. — practica de SNN, warm-up, readout lineal sobre features de spikes.
6. **Guo, W.; Fouda, M. E.; Eltawil, A. M.; Salama, K. N. (2021)**. *Neural Coding in Spiking Neural Networks: A Comparative Study for Robust Neuromorphic Systems*. Frontiers in Neuroscience, 15, 638474. — rate coding y su robustez.
7. **van Nieuwkoop, G.; Mehrkanoon, S. (2026)**. *Temporal Context Conditioning for Seasonality-Aware Precipitation Nowcasting of High-Intensity Rainfall*. arXiv:2606.09959. — contexto temporal (features sin/cos).
8. **Zeng, C.; Tian, Y.; Zheng, G.; Gao, Y. (2024)**. *How Much Can Time-related Features Enhance Time Series Forecasting?* arXiv:2412.01557. — features de tiempo en modelos lineales.
9. **Ko, J.; Lee, K.; Hwang, H.; Oh, S.-G.; Son, S.-W.; Shin, K. (2022)**. *Effective Training Strategies for Deep-learning-based Precipitation Nowcasting and Estimation*. Computers & Geosciences, 165, 105072. — desbalance de clases en nowcasting.

El prototipo ejecutable correspondiente esta en `prototipos/prototipo_lif.py`.

## Respuesta aclaraciones
Buenas preguntas. Respondo cada una apoyándome en Diseno_Modelo_LIF.md y en el código del prototipo validado.
1. ¿Qué es una regresión logística?
Es un modelo de clasificación binaria que predice la probabilidad de que una etiqueta y sea 1 (lluvia), a partir de una combinación lineal de features:
z = w₁·x₁ + w₂·x₂ + … + b        (logit)
P(lluvia) = σ(z) = 1/(1 + e^(−z))
- La parte w·x + b es lineal; la sigmoide la "aplasta" a (0,1), convirtiendo un valor real en una probabilidad.
- Se entrena minimizando el BCE (binary cross-entropy): penaliza poco cuando confía y acierta, mucho cuando confía y falla.
- La decisión es P ≥ 0.5, que equivale a w·x + b ≥ 0: la frontera de decisión es un hiperplano.
Por qué aparece aquí: la neurona de alerta del LIF es exactamente esto. La alerta recibe I_A = Σ wᵢ·aᵢ + Σ vⱼ·tⱼ y la "traducís" con la sigmoide a una probabilidad. Es el mismo bloque, dicho en el lenguaje de ML (doc §1, analogía "banco de filtros fijos + regresión logística").
2. ¿A qué hace referencia θ_A?
θ_A es el umbral de decisión de la neurona de alerta: el valor que V_A (la activación final) debe superar para predecir lluvia.
if V_A >= θ_A → lluvia en la próxima hora
En la versión probabilística, θ_A se absorbe dentro de la sigmoide como un "desplazamiento":
P = σ(V_A − θ_A),   decisión con P ≥ 0.5  ⇔  V_A ≥ θ_A
Es decir, no es un parámetro nuevo: en la regresión logística P = σ(w·x + b), el umbral es θ_A = −b. La diferencia entre versiones no es matemática, es de flujo de trabajo (punto 3).
En el prototipo validado, θ_A no quedó en 0.5: se calibró en validación a θ_A = 0.2 maximizando CSI. Eso es lo que la sección 6.3 del doc llama "calibrar en validación".
3. ¿Qué método de alerta es ideal y cuál es la diferencia?
| | Binaria (hardware) | Probabilística (calibración) |
|---|---|---|
| Decisión | V_A ≥ θ_A fijo | P = σ(V_A − θ_A), operas en la curva de probabilidad |
| θ_A | elegido una vez | barrido en validación (ROC/CSI vs umbral) |
| Uso | desplegar en el ESP32/MicroPython | investigación y evaluación |
Son el mismo modelo. La diferencia es dónde se fija el punto de operación:
- La binaria fija θ_A de una vez (o asume implícitamente 0.5).
- La probabilística deja θ_A libre para elegir el trade-off POD/FAR.
Cuál es ideal para este contexto: la probabilística con calibración en validación, porque la lluvia es un evento raro (en el prototipo, ~8% de las horas). Con un umbral fijo a 0.5 pierdes la capacidad de decidir "quiero más detección aunque tenga más falsas alarmas" (POD alto) o "quiero menos falsas alarmas aunque pierda eventos" (FAR bajo). Eso solo se obtiene barriendo el umbral. La binaria queda como la versión desplegable del mismo modelo, no como un modelo distinto.
4. Rate coding (Poisson) vs inyección directa: ¿por qué son equivalentes?
Son dos formas de alimentar las neuronas sensor (doc §4.4):
- Camino A (rate coding): para cada hora generás un tren de spikes de Poisson con tasa λ = x̂·f_max. Un valor alto de x̂ → muchos spikes; un valor bajo → pocos. Es estocástico.
- Camino B (inyección directa): inyectás la corriente directamente I = x̂·f_max. Es determinista.
Equivalencia: el LIF subumbral es lineal (V[t] = α·V[t−1] + (1−α)·I[t]). La media de un Poisson(λ) es λ. Entonces el valor esperado de la membrana bajo el tren de spikes es exactamente la membrana con inyección directa:
E[ V con rate coding ] = V con inyección directa
Por eso el prototipo usa la forma directa (reproducible, entrenable con regresión logística) y el Poisson queda como la versión de hardware/ablación del mismo modelo (se cita Herranz-Celotti & Rouat, 2022).
Consecuencia clave: como todo es lineal, f_max y R_m son constantes que se absorben en los pesos aprendidos w. No necesitás sintonizarlos a mano — la regresión logística los compensa sola. Eso lo confirma el prototipo: se entrenó sin ningún f_max y funcionó.
5. ¿Cómo defino f_max y por qué 200 spikes/s?
f_max es la tasa máxima de disparo: el valor normalizado x̂ = 1 (anomalía máxima) corresponde a λ = f_max spikes/s.
Cómo se define:
- Límite físico: si la neurona tiene período refractario t_ref ms, la tasa máxima alcanzable es 1000/t_ref. Con t_ref ≈ 2 ms (biológico) el techo es ~500 Hz. Es un tope duro: no se puede disparar más rápido que eso.
- 200 Hz (del doc principal §7.3) es una elección de convención: plausible biológicamente y cómodamente por debajo del techo físico. Es un valor "redondo" y conservador.
- Regla práctica: en la versión directa el valor exacto no importa (se absorbe en w). En la versión Poisson sí importa que sea el mismo para todas las variables, para que las tasas sean comparables (doc §4.4).
Si lo querés justificar en el paper: "tasa máxima de disparo de referencia de 200 Hz, por debajo del límite impuesto por el período refractario (~500 Hz)".
6. "doy" y el error 1464 vs 26280
doy = day of year (día del año, 1…366). Se usa para construir los features de contexto estacional:
doy_sin = sin(2π·doy/365.25)
doy_cos = cos(2π·doy/365.25)
A nivel de diseño: doy le da al modelo la "época del año" como variable cíclica (seno/coseno evitan la discontinuidad dic-ene), para que un solo modelo sirva todo el año — es lo que permite la normalización estacional (doc §1, tabla "un solo modelo para todo el año"). hora (hod, hour-of-day) hace lo mismo con el ciclo diario.
A nivel de código: el error vino de generar doy con np.tile(np.arange(1,367), anios//1+1)[:n]. Con anios=3, anios//1+1 = 4, así que la secuencia tiled tenía 366×4 = 1464 elementos, pero n = 3·8760 = 26280. Al hacer column_stack([doy, hora, …]) con hora de 26280 elementos, numpy crasheó: los vectores no tenían la misma longitud.
El arreglo usa aritmética modular:
doy  = (np.arange(n) % 366) + 1   # siempre de longitud n
hora = np.arange(n) % 24
Matiz de diseño que deja ver el bug: el doy se genera con ciclo de 366 días, pero el seno divide por 365.25 (el año astronómico). Hay una inconsistencia conceptual menor: el ciclo del feature debería ser un único valor (p. ej. 365.25 en ambos). En el prototipo es irrelevante; en los datos reales conviene unificarlo.
7. ¿Escala temporal de 1 h? ¿Cómo se modela el tiempo?
Sí: el paso de tiempo base es 1 hora (Δt = 1 h), en el prototipo y en el diseño:
- Datos: series horarias (n = anios × 8760 pasos). El prototipo sintetiza 3 años → 26280 horas.
- Neurona LIF: se actualiza una vez por hora, α = e^(−Δt/τ_m) = e^(−1/τ_m), con τ_m expresada en horas (doc §2.5, tabla con τ_m de 1 a 12 h). La memoria de cada neurona es "cuántas horas de historia retiene": con τ_m = 6 h, lo de hace 6 h pesa e^(−1) ≈ 37%.
- Etiqueta: "lluvia en la hora siguiente". El evento sintético usa persistencia de 6 h (6 pasos horarios promediados con np.convolve).
- Contexto temporal: doy (ciclo anual) y hora (ciclo diario) como features sin/cos — el tiempo entra como variables, no como red recurrente.
- Micro-pasos (solo versión Poisson): si se genera el tren de spikes, se simula con dt_sim << τ_m dentro de cada hora (decisión abierta nº 8 del doc). En la versión directa del prototipo no hace falta.
Resumen del modelo temporal: un reloj horario discreto, donde cada paso = 1 hora, las neuronas tienen memoria exponencial medida en horas, y el calendario (día del año / hora del día) entra por features cíclicas.
---
Esto es solo explicación — no modifiqué nada. Si querés, puedo planificar agregar esta sección de "preguntas frecuentes / glosario" al final de Diseno_Modelo_LIF.md (y unificar el ciclo de doy a 365.25 en el prototipo). ¿Lo hago?
