# Procesamiento de la senal: de la variable meteorologica al potencial de la neurona de alerta

**Proposito:** sintesis autocontenida del recorrido completo de la informacion en el modelo LIF. Desde la variable cruda hasta el potencial de membrana de la neurona de alerta: (1) transformacion y normalizacion de cada variable, (2) como entra a su neurona sensor como membrana, (3) como se interpreta el spike y se integra por canal, (4) como se combina todo (spikes + contexto) en la neurona de alerta, y (5) que representa cada variable en el modelo.

**Estado:** coherente con `Diseno_Modelo_LIF.md` (§2 y §2.8), `Definicion_Lluvia_y_Resultados_EDDF.md` (parametros y resultados reales) y el codigo `prototipos/prototipo_eddf_real.py`.

---

## 1. Vista general del pipeline

```
VARIABLE CRUDA (6)
  T [°C], HR [%], P [hPa], u y v [m/s], PRECIP [mm/h]     +  doy, hora

   │  1. Transformacion: viento → componentes u, v
   │  2. Normalizacion: anomalia estacional z → x̂ ∈ [0,1]  (PRECIP: min(prcp/1,1))
   ▼
NEURONA SENSOR i (una por variable)
   V_i[t] = α_i·V_i[t−1] + (1−α_i)·x̂_i[t]      ← membrana = integra con memoria τ_i
   S_i[t] = 1  si  V_i[t] ≥ θ_i ;  V_i[t] ← 0   ← spike (evento binario) + reset
   │
   │  5. La alerta integra CADA tren de spikes POR CANAL con su memoria τ_A
   ▼
NEURONA DE ALERTA (readout)
   E_i[t] = α_A·E_i[t−1] + (1−α_A)·S_i[t]       ← memoria por canal (E_i ∈ [0,1])
   ctx_j[t] = sin/cos(doy), sin/cos(hora)        ← contexto INSTANTANEO (sin memoria)
   I_A[t] = Σ_i w_i·E_i[t] + Σ_j v_j·ctx_j[t] + b  ← pre-activacion (potencial de la alerta)
   P = σ(I_A[t]) ;  lluvia si P ≥ θ_A            ← decision
```

Los numeros (1)-(5) son los pasos que se detallan en las secciones siguientes.

---

## 2. Tabla resumen: variable → transformacion → normalizacion → membrana

| Variable cruda | Unidad | Transformacion | Normalizacion → `x̂_i` (entrada) | `τ_i` (memoria) | `θ_i` (percentil 90) | Que representa en el modelo |
| --- | --- | --- | --- | --- | --- | --- |
| `temp` (T) | °C | — | anomalia estacional z → [0,1] | 3 h | 0.717 | anomalia termica persistente (peso ~0: apenas influye) |
| `rhum` (HR) | % | — | anomalia estacional z → [0,1] | 3 h | 0.695 | anomalia de humedad (precursor; peso +) |
| `pres` (P) | hPa | — | anomalia estacional z → [0,1] | 2 h | 0.734 | anomalia de presion (baja presion → lluvia; peso −) |
| `wdir`+`wspd` | °, m/s | descomposicion en `u = wspd·sin(wdir)`, `v = wspd·cos(wdir)` | anomalia estacional z → [0,1] para u y v | 1 h | 0.70 / 0.723 | direccion e intensidad del viento en componentes continuas (peso −) |
| `prcp` | mm/h | — | `min(prcp/1 mm/h, 1)` → [0,1] | 1 h | 0.089 | intensidad de lluvia actual (la mas rapida; DOMINA el modelo) |
| `doy`, `hora` | — | `sin/cos(2π·doy/365.25)`, `sin/cos(2π·hora/24)` | — (quedan en [−1,1]) | — | — | contexto temporal INSTANTANEO (no es neurona, no tiene memoria) |

**Normalizacion estacional (todas menos PRECIP):** `z = (x − μ_doy)/σ_doy` con `μ_doy, σ_doy` = climatologia del dia del ano (media 31 dias) calculada SOLO en el ajuste; luego `x̂ = 0.5 + clip(z, −3, 3)/6 ∈ [0,1]`. Esto define la variable como *anomalia respecto de lo tipico de ese dia*: mismo modelo para todo el ano.

**Transformacion del viento:** se hace ANTES de normalizar, para evitar el salto de 360°→0° y obtener dos senales continuas (`u`, `v`) que representan la misma magnitud vectorial sin discontinuidades.

---

## 3. De la variable a la membrana de su neurona sensor

Cada variable normalizada `x̂_i` alimenta SOLO a su neurona sensor `i`:

```
paso 2 →  x̂_i[t] ∈ [0,1]
paso 3 →  V_i[t] = α_i·V_i[t−1] + (1−α_i)·x̂_i[t]     con α_i = e^(−1/τ_i)
```

- La membrana `V_i` es la solucion de la EDO del LIF (`τ_i·dV/dt = −V + x̂_i`, ver §2 de `Diseno_Modelo_LIF.md`): integra la anomalia con olvido exponencial.
- La escala de entrada (0..1 vs unidades fisicas) NO cambia el resultado: la arquitectura es invariante a la escala (θ_i por percentil + readout z-score, experimento §2.8.4 de `Diseno_Modelo_LIF.md`).
- El valor de la membrana se interpreta como **"nivel de anomalia persistente"**: sube mientras la variable es anomalmente alta y decae con `τ_i` cuando vuelve a lo normal.

## 4. La memoria en las neuronas y como una entrada se suma al potencial acumulado

**La recurrencia es una combinacion convexa:** el potencial nuevo `V_i[t]` retiene una fraccion `α_i` del potencial anterior `V_i[t−1]` y absorbe una fraccion `(1−α_i)` del dato nuevo `x̂_i[t]`.

Expandida, se ve que resume TODA la historia con pesos que decaen exponencialmente:

```
V_i[t] = (1−α_i)·x̂_i[t] + (1−α_i)·α_i·x̂_i[t−1] + (1−α_i)·α_i²·x̂_i[t−2] + ...
```

| τ_i | 1 h | 2 h | 3 h | 6 h | 12 h |
| --- | --- | --- | --- | --- | --- |
| α_i = e^(−1/τ_i) | 0.37 | 0.61 | 0.72 | 0.85 | 0.92 |

Consecuencias de la memoria:
- Una entrada de hace `k` horas contribuye con peso `(1−α)·α^k`: cada hora la contribucion se multiplica por `α`.
- Si la entrada es constante `c`, la membrana converge a `c` (estado estacionario): la membrana no "acumula infinito", sino que se estabiliza en el valor persistente de la anomalia.
- El **reset** (cuando hay spike, `V_i ← 0`) es la unica forma de borrar la memoria del sensor; sin spike, el potencial anterior siempre pesa.

**Como "se divide por canal":** la memoria NO se comparte entre sensores en la capa sensor (cada variable tiene su neurona). En la alerta, la integracion `E_i` se hace **por canal** (`features_alerta` integra cada columna `S_i` de forma independiente con la misma `τ_A`): hay tantos acumuladores como sensores, cada uno recuerda "cuanto disparo SU sensor recientemente". Solo en la suma ponderada `I_A` se mezclan los canales. Como la integracion y la suma ponderada conmutan (ambas lineales), integrar por canal y luego ponderar es EQUIVALENTE a que la alerta integrara la suma ponderada de spikes directamente (docstring `prototipo_lif_spikes.py`).

## 5. Del spike a la neurona de alerta: el proceso de cada spike y del contexto

```
paso 4 (sensor):   V_i[t] ≥ θ_i  →  S_i[t] = 1  (y V_i ← 0)     [evento binario]
                   V_i[t] <  θ_i  →  S_i[t] = 0                  [sin evento]

paso 5 (alerta):   E_i[t] = α_A·E_i[t−1] + (1−α_A)·S_i[t]      τ_A = 1 h → α_A = 0.37
                   cada canal i integra SU tren de spikes

contexto:          ctx_j[t] = sin/cos(doy), sin/cos(hora)       [−1,1], SIN memoria
```

**Que "ve" la alerta de cada spike:** no el valor binario crudo, sino su huella integrada `E_i ∈ [0,1]`. Con `τ_A = 1 h`, un spike se ve asi en la membrana de la alerta:

| Horas desde el spike | E_i (lo que ve la alerta) |
| --- | --- |
| 0 (justo al disparar) | 0.63 |
| +1 h | 0.23 |
| +2 h | 0.09 |
| +3 h | 0.03 |

Si el sensor dispara varias horas seguidas, `E_i` sube: 0.63 → 0.86 → 0.95 → … hasta ~1 (un canal "saturado" = disparo continuo). El contexto, en cambio, entra con el valor del momento (el sin/cos del dia y la hora de `t`) sin guardar estado.

## 6. Como se combina todo en la neurona de alerta

```
paso 6:  I_A[t] = Σ_i w_i·E_i[t] + Σ_j v_j·ctx_j[t] + b     (potencial de la alerta)
paso 7:  P = σ(I_A[t]) = 1/(1 + e^(−I_A[t]))               (probabilidad)
         lluvia la proxima hora si  P ≥ θ_A                 (punto de operacion)
```

- `E_i` ya lleva la memoria (spikes integrados por canal); el contexto aporta la "etiqueta temporal" instantanea.
- Los pesos `w_i, v_j, b` se aprenden por regresion logistica sobre features **estandarizadas** (z-score), por eso los pesos reportados estan en unidades estandarizadas.
- `I_A` es un **unico escalar homogeneo**: el potencial de membrana de la alerta antes de la sigmoide. La decision `θ_A` (calibrado en validacion) fija cuanto evidencia se necesita.

**Ejemplo numerico** (pesos reales del Modelo B, `w = [−0.014, 0.015, −0.241, −0.03, −0.1, 0.987]`, contexto `v = [−0.054, 0.178, −0.05, −0.021]`): si en una hora disparan los canales de T, u y PRECIP (sin memoria previa, `E ≈ 0.63`) y el contexto vale `[0.14, 0.05, 0.1, 0.04]`:

```
I_A = (−0.014·0.63) + (−0.03·0.63) + (0.987·0.63) + v·ctx + b
    ≈ −0.009 − 0.019 + 0.624 − 0.007 + 0.009 − 0.005 − 0.001 + b
    ≈ 0.59 + b
```

El spike de PRECIP (peso 0.987) domina la evidencia; los demas apenas la mueven. (En el Modelo C se anade un canal extra: `nivel_precip = x̂_prcp` con peso 0.424, que da la intensidad graduada de la lluvia ademas del spike.)

## 6.1 Traza real de un evento (Modelo B, validacion EDDF)

Ejemplo con numeros reales (evento del 2026-01-29 05:00 a 17:00, generado por `prototipos/traza_evento_real.py`). Columna `spikes` = sensores en orden [T, HR, P, u, v, PRECIP]; `E` = memoria por canal (tau_A=1 h); `I_A` = logit exacto (pesos crudos, ver nota); `y_next` = llovio la hora siguiente.

| hora | prcp | x̂ (6 sens) | V (6 sens) | spikes | E (6 sens) | I_A | P | y_next |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 05:00 | 0.0 | [0.39 0.66 0.22 0.71 0.67 0.0] | [0.40 0.66 0.21 0.70 0.67 0.0] | 000100 | [0 0 0 0.63 0 0] | −3.82 | 0.02 | 0 |
| 06:00 | 0.0 | [0.38 0.67 0.22 0.66 0.65 0.0] | [0.40 0.66 0.22 0.67 0.66 0.0] | 000000 | [0 0 0 0.23 0 0] | −3.73 | 0.02 | 0 |
| 07:00 | 0.2 | [0.38 0.69 0.23 0.67 0.63 0.2] | [0.39 0.67 0.22 0.67 0.64 0.13] | 000001 | [0 0 0 0.09 0 0.63] | −0.80 | 0.31 | 0 |
| 08:00 | 0.2 | [0.38 0.69 0.24 0.68 0.65 0.2] | [0.39 0.67 0.23 0.68 0.64 0.17] | 000001 | [0 0 0 0.03 0 0.86] | +0.28 | 0.57 | 0 |
| 09:00 | 0.0 | [0.38 0.69 0.24 0.69 0.63 0.0] | [0.38 0.68 0.23 0.68 0.64 0.06] | 000000 | [0 0 0 0.01 0 0.32] | −2.21 | 0.10 | 0 |
| 10:00 | 0.1 | [0.38 0.70 0.24 0.70 0.64 0.1] | [0.38 0.69 0.24 0.69 0.64 0.09] | 000000 | [0 0 0 0 0 0.12] | −3.12 | 0.04 | 1 |
| 11:00 | 0.3 | [0.38 0.69 0.24 0.71 0.67 0.3] | [0.38 0.69 0.24 0.71 0.66 0.22] | 000101 | [0 0 0 0.63 0 0.68] | −0.71 | 0.33 | 1 |
| 12:00 | 0.4 | [0.38 0.69 0.25 0.67 0.64 0.4] | [0.38 0.69 0.24 0.69 0.65 0.33] | 000001 | [0 0 0 0.23 0 0.88] | +0.32 | 0.58 | 1 |
| 13:00 | 0.3 | [0.38 0.69 0.24 0.62 0.66 0.3] | [0.38 0.69 0.24 0.65 0.65 0.31] | 000001 | [0 0 0 0.09 0 0.96] | +0.70 | 0.67 | 1 |
| 14:00 | 0.5 | [0.37 0.72 0.25 0.64 0.66 0.5] | [0.38 0.70 0.25 0.64 0.66 0.43] | 010001 | [0 0.63 0 0.03 0 0.98] | +0.95 | 0.72 | 1 |
| 15:00 | 0.5 | [0.36 0.72 0.25 0.67 0.63 0.5] | [0.37 0.70 0.25 0.66 0.64 0.47] | 000001 | [0 0.23 0 0.01 0 0.99] | +0.94 | 0.72 | 1 |
| 16:00 | 0.3 | [0.37 0.70 0.25 0.65 0.61 0.3] | [0.37 0.70 0.25 0.66 0.62 0.36] | 000001 | [0 0.09 0 0 0 1.00] | +0.93 | 0.72 | 0 |
| 17:00 | 0.2 | [0.37 0.70 0.26 0.65 0.60 0.2] | [0.37 0.70 0.25 0.65 0.61 0.26] | 000001 | [0 0.03 0 0 0 1.00] | +0.92 | 0.72 | 1 |

Que se ve en los numeros:
- **El disparo viene de PRECIP (spike `...001`)**: con theta_prcp = 0.089 (el umbral mas bajo: dispara con lluvia casi cualquier cantidad). El canal v dispara una vez (05:00 y 11:00, `..1..`).
- **La memoria `E_5` acumula con tau_A=1 h**: 0.63 → 0.86 → 0.32 (lluvia se corto) → 0.68 → 0.88 → 0.96 → 0.98 → 0.99 → 1.00 (canal saturado = lluvia continua).
- **`I_A` cruza de negativo a positivo cuando `E_5` sube**: la alerta "enciente" (P≥0.21) mientras el canal de lluvia recuerda haber disparado. En 09:00 la lluvia se corto, `E_5` decae a 0.32 y la alerta se apaga (P=0.10); al volver la lluvia se reactiva.
- **El evento es un TP real** (P=0.72 en 14:00 con lluvia la hora siguiente): coincide con el diagnostico de que la mayoria de aciertos de B/C ocurren cuando ya esta lloviendo (persistencia dentro del propio modelo).

**Nota sobre los pesos "crudos":** `entrenar_logistico` estandariza las features (z-score) y reporta `w_std` en unidades estandarizadas (los de la tabla de §6). La columna `I_A` de la traza usa la conversion al espacio crudo `w_raw = w_std/sd`, `b_raw = b − Σ w_std·μ/sd`, de modo que `I_A = w_raw·E + v_raw·ctx + b_raw` es **exactamente** el logit de `P` (con pesos reales w_sens = [−0.156, 0.174, −2.599, −0.234, −0.741, 4.566] y v_ctx = [−0.053, 0.121, −0.013, −0.018]).

## 7. Que representa cada variable dentro del modelo

| Simbolo | Que representa | Significado meteorologico / de diseno |
| --- | --- | --- |
| `x̂_i` | anomalia normalizada de la variable | "cuanto se desvia de lo tipico del dia" — define el concepto de precursor |
| `V_i` | membrana del sensor (estado con memoria) | nivel de anomalia persistente; suaviza el ruido del sensor |
| `S_i` | spike del sensor (evento binario) | "la variable entro en su rango de alarma" |
| `E_i` | memoria de la alerta por canal | "cuanto ha disparado el sensor recientemente" (ultimas ~1-3 h) |
| `ctx_j` | sin/cos de dia y hora | epoca del ano y hora del dia, sin saltos de calendario |
| `I_A` | pre-activacion de la alerta | evidencia combinada (spikes integrados + contexto + sesgo) |
| `P` | probabilidad de lluvia la proxima hora | salida calibrable del modelo |
| `w_i` | peso sensor→alerta | que variable empuja (+) o frena (−) la lluvia |
| `v_j` | peso del contexto | amplitud y fase de la modulacion estacional/diurna |
| `θ_i` | umbral del sensor | sensibilidad de la variable (disparo facil o estricto) |
| `τ_i`, `τ_A` | memorias del sensor y de la alerta | cuanta historia recuerda cada neurona |

---

## 8. Referencia de codigo

| Paso | Funcion | Archivo |
| --- | --- | --- |
| 1. Transformacion viento + etiqueta | `cargar_datos` | `prototipo_eddf_real.py` |
| 2. Normalizacion estacional + contexto | `normalizar_estacional` | `prototipo_eddf_real.py` |
| 3. Membrana del sensor (EMA) | `capa_ema` | `prototipo_eddf_real.py` |
| 4. Spike + reset | `capa_sensores_spikes` | `prototipo_lif_spikes.py` |
| 5. Integracion por canal (memoria de la alerta) | `features_alerta` | `prototipo_lif_spikes.py` |
| 6-7. Readout y decision | `entrenar_logistico`, `puntuar`, `metricas` | `prototipo_lif.py` |
| Traza real de un evento (tabla §6.1) | `traza_evento_real` | `traza_evento_real.py` |
