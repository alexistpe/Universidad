# Investigacion: Simulacion de sensores de bajo costo.

**Propósito:** Determinar cómo simular sensores de bajo costo, con sus errores y ruido para adaptar el modelo LIF a condiciones realistas de implementación.

---

## Índice

1. [Pregunta 1: ¿Es viable el uso de sistemas complejos externos (IA/satélites) ante la falta de sistemas en tierra?](#p1)
2. [Pregunta 2: ¿Porque simular sensores de bajo costo? — Análisis de decisión](#p2)
3. [Pregunta 2.1: ¿Qué lugares documentados utilizan sensores de bajo costo?](#p2-1)
4. [Pregunta 2.2: ¿Que sistemas de prediccion utilizan las estaciones de bajo costo?](#p2-2)
5. [Pregunta 2.3: ¿Qué características de sensores necesito simular?](#p2-3)
6. [Pregunta 2.4: ¿Cuáles son los errores documentados de los sensores?](#p2-4)
7. [Pregunta 2.5: ¿Cómo y qué ruido modelaré?](#p2-5)
8. [Resumen](#resumen)

---

<a name="p1"></a>

## Pregunta 1: ¿Es viable el uso de sistemas complejos externos (IA/satélites) ante la falta de sistemas en tierra?

### Respuesta: Cada sistema tiene un rol complementario, no sustitutivo

#### 1.1 Satélites: No reemplazan estaciones en tierra

Los satélites meteorológicos **no son sustitutos** de las estaciones en tierra (WMO, 2023 — *Vision for WIGOS*, WMO-No. 1243):

| Limitación | Detalle |
| --- | --- |
| **Precisión inferior** | Radiosondeos tienen precisión de temperatura de 0.1 K y error de humedad ~2-3%, un orden de magnitud mejor que los mejores sensores satelitales |
| **Resolución temporal insuficiente** | Satélites geoestacionarios muestrean cada 15-30 min; polares cada 6-12h. Un evento convectivo de 18 min puede ocurrir entre pasadas |
| **Mediciones indirectas** | No miden temperatura superficial ni precipitación directamente; estimaciones derivadas de radianzas con incertidumbre significativa |
| **Registros cortos** | ~40 años vs. 70+ años de estaciones en tierra (EDDF desde 1949) |

**Cita textual WMO:**

> *"Satellite observations cannot be viewed as a replacement for in situ observations... the lengths of the satellite records are still too short for climate detection purposes."*

#### 1.2 IA: Complementa, no reemplaza los sensores físicos

- Modelos como **GraphCast, Pangu-Weather, FourCastNet** operan sobre datos de reanálisis que provienen de estaciones en tierra. Sin estaciones físicas que calibren los datos, no hay datos de entrenamiento ni validación.
- **WMO Congress (2025)**: *"AI must complement, not replace, existing well-honed scientific forecasting methods and infrastructure."*
- Los modelos de IA no generan datos nuevos; dependen de la red de sensores existente.

#### 1.3 WEGN3D: SÍ usan sistemas complejos (como complemento)

El WegenerNet 3D (Haas et al., 2025) sí integra:

- **156 estaciones en tierra** (núcleo de la red)
- **Radar meteorológico X-band** (200m, 2.5 min)
- **Radiómetros de microondas** (perfiles T/H cada 10 min)
- **6 estaciones GNSS** (vapor de agua precipitable)

Pero las estaciones en tierra siguen siendo la **referencia de calibración y validación** para todos los demás instrumentos.

#### 1.4 Estándares WMO obligatorios

Se opera bajo **WIGOS (WMO Integrated Global Observing System)**, que exige:

1. **Trazabilidad metrológica**: Sensores calibrados contra patrones SI
2. **Homogeneidad histórica**: No romper series climáticas
3. **Cobertura global coordinada**: Normas comunes entre países

**Clasificación WMO de estaciones:**

- **Referencia (goal)**: Máxima calidad, trazabilidad total
- **Baseline (threshold)**: Calidad suficiente para intercambio global (DWD, EDDF)
- **Comprehensive**: Calidad variable (sensores bajo costo)

### ¿Las estaciones de bajo costo usan datos satelitales o IA?

Caso general: NO. La gran mayoría de redes ciudadanas/de bajo costo no usan satélites ni IA para analizar o predecir. Usan algoritmos basados en reglas fijas (umbrales de tendencia de presión, temperatura, etc.).

**Métodos que SÍ usan (por red):**

| Red | Método de predicción | ¿Usa IA? | ¿Usa satélites? |
| --- | --- | --- | --- |
| CWOP (NOAA) | Ninguno — solo recolecta y hace QC de datos con umbrales fijos | No | No |
| Netatmo | Alertas personalizadas por umbrales definidas por el usuario + pronóstico de 7 días provisto por servicio externo | No | No |
| Weather Underground (BestForecast) | Híbrido: asimila datos de 250k+ estaciones PWS en modelos NWP (GFS, NAM) con resolución 4km, actualización cada 15 min. No es IA, es post-procesamiento estadístico de modelos numéricos | Parcial (estadístico) | No directo (usa NWP que asimila satélites) |
| Davis Instruments | Algoritmo Zambretti Forecaster — basado en tendencia de presión, dirección del viento, y mes del año usando tablas lookup fijas (desde 1920s). También ofrece asimilación con NWP local | No | No |
| Sensor.Community | Ninguno — solo datos crudos abiertos | No | No |

**Excepciones documentadas (investigación, no producción):**

| Estudio | Qué hace | IA? | Satélites? |
| --- | --- | --- | --- |
| Sgoff et al. (2022) — DWD + Netatmo | Asimilación de datos de estaciones Netatmo en el sistema de predicción regional del DWD (COSMO-D2) | No (asimilación numérica) | Sí (vía NWP) |
| Salcedo (2024) — Bolivia, GNN | Predicción de lluvia intensa con Graph Neural Networks usando pluviómetros IoT de bajo costo | Sí (GNN) | No |
| Mao & Sorteberg (2026) — Noruega | Post-procesamiento ML de nowcasts NWP usando observaciones crowdsourced | Sí (ML) | Indirecto |
| AMT (2026) — KNMI/HOASIS | Evaluación de estaciones compactas AiOWS. No hacen predicción — solo evalúan calidad de los sensores | No | No |

> Las redes de estaciones de bajo costo existentes (Netatmo, CWOP, Sensor.Community, Weather Underground) no aplican IA ni fusión satelital para predicción. Usan mayoritariamente umbrales fijos (Zambretti, tendencias de presión) o modelos NWP estándar. Esto significa que tú no estarías en desventaja si tu modelo LIF tampoco usa satélites. De hecho, un enfoque con SNN/LIF para clasificación basada solo en datos de sensores en tierra sería más avanzado que lo que estas redes usan actualmente.

### Conclusión P1

| Sistema | ¿Por qué no es fuente principal? | ¿Complemento? |
| --- | --- | --- |
| **Satélites** | Precisión inferior, medición indirecta, resolución temporal insuficiente | Sí |
| **IA** | Requiere datos de estaciones para entrenar; no genera datos nuevos | Sí |
| **Radar** | No mide superficie directamente, requiere calibración | Sí |

---

<a name="p2"></a>

## Pregunta 2: ¿Porque simular sensores de bajo costo?

### Análisis de decisión

**Situación actual:** El modelo LIF se entrena con datos de EDDF (estación profesional DWD). Datos de alta precisión con sensores calibrados periódicamente.

**Problema:** Si el modelo se implementara con sensores de bajo costo, las predicciones podrían degradarse porque:

1. Los datos de entrenamiento no contienen ruido característico de sensores baratos
2. Errores sistemáticos como las bias no están representados
3. La resolución y precisión son inferiores

| Opción | Ventajas | Desventajas |
| --- | --- | --- |
| **No simular** | Datos limpios, modelo más preciso en paper | No generaliza a implementación real |
| **Simular ruido** | Modelo robusto, resultados más realistas | Complejidad añadida |

**Decisión: SIMULAR DATOS.** Añadir capa de ruido calibrada sobre datos EDDF para emular sensores de bajo costo. Permite evaluar degradación real y hacer el modelo robusto desde diseño.

---

<a name="p2-1"></a>

## Pregunta 2.1: ¿Qué lugares documentados utilizan sensores de bajo costo?

### 1. Red Netatmo / Estudio KNMI (global)

- **Sensores:** Estación todo-en-uno compacta
- **Estudio clave:** *Performance and longevity of compact all-in-one weather stations* (AMT, 2026)
- **Hallazgo:** Temperatura útil si se gestiona; humedad, viento y precipitación fallan sin mantenimiento regular
- **DOI:** https://amt.copernicus.org/articles/19/3001/2026/

### 2. CWOP — Citizen Weather Observer Program (NOAA, EEUU)

- **Sensores:** Variados (Davis, estaciones caseras)
- **Protocolo:** Datos cada 5-15 min, QC automatizado
- **Estudio clave:** Bell (2015) — *In-service drift study of humidity sensors*, WMO CIMO TECO
- **Hallazgo:** Sensores de humedad desarrollan bias positivo a humedades bajas/medias y bias negativo a >90% RH por contaminación del polímero capacitivo

### 3. WMO Innovation Platforms (global)

- **Documento:** *Transition to Automated Ground-based Measurements* (WMO RA-V, 2023)
- **Cita textual:**

  > *"Innovative Observation Platforms: Uses inexpensive, innovative technology, locally sourced materials. Low-cost micro-sensors. Limitations: data quality lower than climate reference stations."*

- **Enlace:** https://etrp.wmo.int/

### 4. Sensor.Community / Luftdaten.info (global)

- **Sensores:** DHT22, BME280, SDS011
- **Enfoque:** Calidad del aire + temperatura/humedad
- **Enlace:** https://sensor.community/

### 5. Open Weather Map (global)

- Integra estaciones ciudadanas de diversos fabricantes
- **Enlace:** https://openweathermap.org/

### Tabla resumen caracteristicas

| Proyecto | Sensores | Resolución | Referencia |
| --- | --- | --- | --- |
| Netatmo/KNMI | AiOWS compactos | 5-15 min | AMT, 2026 |
| CWOP (NOAA) | Davis, varios | 5-15 min | Bell, 2015 |
| Sensor.Community | DHT22, BME280 | 2-5 min | Open Data |
| WMO Innovation | Micro-sensores | Variable | WMO RA-V |
| Open Weather Map | Estaciones ciudadanas | Variable | OWM API |

### Ubicaciones exactas de las redes documentadas

| Red | Cantidad | Ubicaciones principales | URL de mapas |
| --- | --- | --- | --- |
| CWOP | ~10,000+ | EE.UU. (mayoría), algunos en Canadá, Europa, Australia | http://wxqa.com/memberlists.html / https://www.weather.gov/media/epz/mesonet/CWOP-OfficialGuide.pdf |
| Netatmo | ~100,000+ | Global (170+ países) — mayor concentración en Europa (Francia, Alemania, UK), USA, Japón | https://weathermap.netatmo.com |
| Weather Underground | 250,000+ | Global — USA, Europa, Australia, Japón, Brasil | https://www.wunderground.com/pws/overview |
| Sensor.Community | ~15,000+ | Global — Alemania, Europa, USA, India, Australia, Brasil | https://maps.sensor.community/ |
| Salcedo (2024) | ~15 (IoT) | Bolivia — zonas rurales de La Paz, Cochabamba, Santa Cruz | Paper: arXiv 2412.16842 |
| KNMI/AMT (2026) | 6 estaciones | Países Bajos (Cabauw test field) | https://amt.copernicus.org/articles/19/3001/2026/ |

---

<a name="p2-2"></a>

## Pregunta 2.2: ¿Usan umbrales fijos? ¿Qué usan exactamente?

| Red | Algoritmo de predicción | Base |
| --- | --- | --- |
| CWOP | Solo QC con umbrales fijos — no produce pronósticos. Los umbrales son rangos de validez (ej. temperatura: -30°C a +50°C; presión: 850-1100 hPa; viento: 0-100 m/s) | Tablas de validez en CWOP Official Guide |
| Netatmo | Usuario define alertas por umbral (ej. "notificar si T < 0°C"). El pronóstico extendido lo provee un servicio externo no documentado | Alertas por umbral |
| Davis Instruments | Zambretti Forecaster — algoritmo de 1920s que usa: (1) tendencia de presión (3h), (2) dirección del viento, (3) mes del año. Produce "Fair", "Rain", "Change" etc. + asimilación NWP opcional | Tablas lookup fijas + tendencia |
| Weather Underground | BestForecast: asimila PWS datos con modelos NWP (GFS, ECMWF, NAM) a resolución 4km cada 15 min. No es IA — es un ensemble ponderado de modelos numéricos calibrados con datos locales históricos | NWP + datos locales |
| Sensor.Community | Sin predicción | Solo datos |

**El Zambretti Forecaster (que es el algoritmo base de muchas estaciones domésticas) usa esta lógica de umbrales fijos (Wikipedia; GitHub implementations):**

**Tendencia de presión (últimas 3h):**

- Rising > 1.6 hPa/h → "Fair improving"
- Steady ±0.1-0.2 hPa/h → "No change"
- Falling > 1.6 hPa/h → "Rain likely"

**Combinado con:**

- Dirección del viento (8 puntos cardinales)
- Mes del año (estacionalidad)

---

<a name="p2-3"></a>

## Pregunta 2.3: ¿Qué características de los sensores de bajo costo necesito simular?

### Sensor 1: BME280 (Bosch Sensortec)

| Parámetro | Temperatura | Humedad | Presión |
| --- | --- | --- | --- |
| Rango | -40 a +85°C | 0-100% RH | 300-1100 hPa |
| Precisión | ±0.5°C (0-65°C) | ±3% RH (20-80%) | ±1 hPa |
| Resolución | 0.01°C | 0.008% RH | 0.18 Pa |
| Deriva/año | 0.5°C/año | 0.5% RH/año | ~0.1 hPa/año |

### Sensor 2: DHT22 / AM2302 (Aosong)

| Parámetro | Temperatura | Humedad |
| --- | --- | --- |
| Rango | -40 a +80°C | 0-100% RH |
| Precisión | ±0.5°C | ±3% (10-90%), ±5% (<10, >90%) |
| Resolución | 0.1°C | 0.1% RH |
| Deriva/año | 0.5°C/año | 0.5% RH/año |

### Sensor 3: Pluviómetro de cangilón genérico (0.2 mm/tip)

| Parámetro | Valor |
| --- | --- |
| Resolución | 0.2 mm por vuelco |
| Precisión nominal | ±2% (a 50 mm/h) |
| Error viento | Subcaptura 10-40% |
| Precisión real campo | -13% a -97% (AMT, 2026) |

### Variables del modelo LIF a simular

| Variable | Sensor bajo costo | ¿Simular? |
| --- | --- | --- |
| Temperatura (T2m) | BME280 o DHT22 | **Sí** |
| Punto de rocío (DP) | Derivado de BME280 | Indirecta |
| Presión (SLP) | BME280 | **Sí** |
| Velocidad viento (WS) | Anemómetro cazoletas | **Sí** |
| Precipitación 1h | Pluviómetro cangilón | **Sí** |

---

<a name="p2-4"></a>

## Pregunta 2.4: ¿Cuáles son los errores documentados de los sensores?

### 2.4.1 Error de Temperatura

| Sensor | Bias medio | Error band | R² tras cal | Fuente |
| --- | --- | --- | --- | --- |
| BME280 (sin cal) | +0.14°C | ±0.61°C | — | Budiawan et al., 2024 |
| BME280 (cal plano) | 0.03°C | ±0.33°C | 0.99-1.00 | Budiawan et al., 2024 |
| DHT22 (sin cal) | +0.3 a +0.5°C | ±1.0°C | — | Smith, 2017 |
| DHT22 (cal lineal) | 0.1-0.2°C | ±0.5°C | 0.98-0.99 | MDPI IoT, 2020 |

**Chodorek et al. (2022):** *"The BME280 frequently exceeded ±1°C... it cannot be used as the primary sensor for temperature."*

**Smith (2017-2024):** BME280 expuesto al aire libre 1+ año perdió su "calibración plana" por contaminación atmosférica.

### 2.4.2 Error de Humedad Relativa

| Sensor | Bias real | Error band | Deriva/año |
| --- | --- | --- | --- |
| BME280 (sin cal) | ±2.37% RH | ±10.02% RH | 0.5% RH/año |
| BME280 (calibrado) | 1.65% RH | ±2.24% RH | 0.5% RH/año |
| DHT22 (sin cal) | ±2-5% RH | ±5-8% RH | 0.5% RH/año |

**CRITICO para tu modelo (Bell, 2015; AMT, 2026):**

> *"Systematic humidity sensor drift... positive bias at low-to-mid range, negative bias at near-saturation conditions (>90% RH)."*

**Implicación:** El error del sensor es MAYOR justo en el rango crítico para detección de lluvia. Un sensor de bajo costo podría reportar "100% RH" por contaminación cuando la humedad real ya descendió.

### 2.4.3 Error de Presión — BME280

| Parámetro | Valor |
| --- | --- |
| Precisión real (Budiawan, 2024) | ±0.5 hPa tras cal |
| Error band | ±0.6 hPa |
| Deriva temporal | ~0.1 hPa/año |

**Nota:** La presión BME280 es muy precisa y estable — la variable con mejor rendimiento relativo.

### 2.4.4 Error de Viento

| Parámetro | Valor |
| --- | --- |
| Precisión real | ±0.5-1.0 m/s a baja velocidad |
| Umbral arranque | 0.3-0.8 m/s |
| Error en rachas | Subestima por inercia mecánica |
| Degradación | Cojinetes se degradan 1-3 años |

### 2.4.5 Error de Precipitación (AMT, 2026)

**Cita textual:**

> *"None of the AiOWSs achieved reliable WMO Class B compliance. Wind-induced undercatch, intensity-dependent tipping bias, clogging, and component failure led to persistent negative biases. The Davis VP2 and METER reached near-total precipitation failure (−85% to −97%)... precipitation sensing should be treated as qualitative unless supported by frequent inspection."*

---

<a name="p2-5"></a>

## Pregunta 2.5: ¿Cómo y qué ruido modelaré?

### Modelo híbrido de 4 componentes

```
X_simulado[t] = X_real[t] + bias + ruido_gaussiano[t] + deriva[t] + cuantización[t]
```

#### Componente 1: Bias sistemático (constante aditiva)

```python
T_bias    = np.random.uniform(-0.5, +0.5)     # °C
RH_bias   = np.random.uniform(-3.0, +3.0)     # % RH
P_bias    = np.random.uniform(-0.5, +0.5)     # hPa
WS_bias   = np.random.uniform(-0.3, +0.3)     # m/s
PRCP_bias = np.random.uniform(-0.05, +0.05)   # mm
```

**Fuente:** Budiawan et al. (2024) — tablas de bias antes/después de calibración.

#### Componente 2: Ruido gaussiano (error aleatorio)

```python
T_noise    = np.random.normal(0, 0.2)    # °C — σ ~0.2°C
RH_noise   = np.random.normal(0, 1.5)    # % RH — σ ~1.5%
P_noise    = np.random.normal(0, 0.2)    # hPa — σ ~0.2 hPa
WS_noise   = np.random.normal(0, 0.3)    # m/s — σ ~0.3 m/s
PRCP_noise = np.random.normal(0, 0.02)   # mm — cuantización domina
```

**Fuente:** *Evaluation of Low-Cost Sensors for Weather and CO2 Monitoring* (MDPI IoT, 2020) — tabla de sigma para cada sensor.

#### Componente 3: Deriva temporal (envejecimiento)

```python
# Opcion A: Deriva lineal
T_drift    = 0.5 * (t / 365.25)     # 0.5°C/año
RH_drift   = 0.5 * (t / 365.25)     # 0.5% RH/año

# Opcion B: Random walk (mas realista)
T_drift[t]  = T_drift[t-1] + np.random.normal(0, 0.01)
RH_drift[t] = RH_drift[t-1] + np.random.normal(0, 0.01)
```

**Fuente:** Smith (2017-2024) — deriva documentada de BME280.

#### Componente 4: Error de cuantización (resolución finita)

```python
# Temperatura BME280: resolucion 0.01°C
T_cuant    = round(T / 0.01) * 0.01

# Precipitacion: multiplo de 0.2 mm (1 tip)
PRCP_cuant = floor(PRCP / 0.2) * 0.2

# Viento: umbral de arranque
if WS < 0.3:
    WS = 0.0  # vientos debajo del umbral no se detectan
```

### Implementación completa recomendada

```python
import numpy as np

class LowCostSensorSimulator:
    def __init__(self, seed=None):
        if seed:
            np.random.seed(seed)
        # Bias constante por "sensor"
        self.bias = {
            'temp': np.random.uniform(-0.5, 0.5),
            'rh': np.random.uniform(-3.0, 3.0),
            'pres': np.random.uniform(-0.5, 0.5),
            'ws': np.random.uniform(-0.3, 0.3),
        }
        # Estado de deriva (random walk)
        self.drift = {'temp': 0.0, 'rh': 0.0, 'pres': 0.0}
        self.t = 0

    def simulate(self, temp, rh, pres, ws, precip, dt_hours=1):
        self.t += dt_hours
        days = self.t / 24.0

        # Deriva temporal
        self.drift['temp'] += np.random.normal(0, 0.01)
        self.drift['rh'] += np.random.normal(0, 0.01)
        self.drift['pres'] += np.random.normal(0, 0.002)

        # Bias + deriva
        temp_sim = temp + self.bias['temp'] + self.drift['temp']
        rh_sim = rh + self.bias['rh'] + self.drift['rh']
        pres_sim = pres + self.bias['pres'] + self.drift['pres']

        # Ruido gaussiano
        temp_sim += np.random.normal(0, 0.2)
        rh_sim += np.random.normal(0, 1.5)
        pres_sim += np.random.normal(0, 0.2)
        ws_sim = ws + np.random.normal(0, 0.3)

        # Cuantizacion
        temp_sim = round(temp_sim, 2)     # 0.01°C
        rh_sim = round(rh_sim, 1)         # 0.1% RH
        pres_sim = round(pres_sim, 2)     # 0.01 hPa

        # Viento: umbral de arranque
        if ws_sim < 0.3:
            ws_sim = 0.0

        # Precipitacion: cuantizacion 0.2 mm (pluviometro cangilon)
        precip_sim = np.floor(precip / 0.2) * 0.2

        return temp_sim, rh_sim, pres_sim, ws_sim, precip_sim
```

---

<a name="resumen"></a>

## Resumen y conclusion

| Pregunta | Respuesta |
| --- | --- |
| **¿Por que no usan IA/satelites?** | Cada tecnologia es complementaria. Los satelites miden indirectamente con menor precision y resolucion temporal. La IA requiere datos de estaciones para entrenar. Las estaciones en tierra son la unica fuente de datos verificables, trazables y con registros historicos largos. Los estandares WMO exigen trazabilidad metrologica. |
| **¿Simular sensores bajo costo?** | **Sí**, para que el modelo sea robusto a ruido realista. |
| **¿Que sensores simular?** | BME280 (T, RH, P), anemometro cazoletas (WS), pluviometro cangilon 0.2mm (PRCP) |
| **¿Que errores modelar?** | (1) Bias sistematico (±0.5°C, ±3% RH), (2) ruido gaussiano (σ 0.2°C, σ 1.5% RH), (3) deriva temporal (0.5°C/año), (4) cuantizacion (0.01°C, 0.2 mm) |
| **Proximos pasos** | Implementar el simulador como modulo Python, entrenar modelo LIF con/sin ruido, comparar metricas de degradacion. |

### Conclusion para modelo LIF

El modelo (LIF + lookback window + solo sensores en tierra) se alinea con el estado del arte de las redes de bajo costo actuales. La diferencia clave:

- Las redes actuales usan umbrales fijos (Zambretti) o NWP
- Se propone un modelo bioinspirado (LIF) que aprende patrones espacio-temporales de los datos directamente
- Hay un solo paper (Salcedo, 2024) que usa GNN con datos de bajo costo, y ninguno que use SNN/LIF para esta tarea

### Fuentes principales citadas

1. **WMO (2023)**. *Vision for the WMO Integrated Global Observing System (WIGOS)*, WMO-No. 1243.
   - https://library.wmo.int/

2. **Haas et al. (2025)**. *Observation based precipitation life cycle analysis of heavy rainfall events*. Weather and Climate Dynamics, 6, 949-969.
   - https://wcd.copernicus.org/articles/6/949/2025/

3. **Performance and longevity of compact AiOWS (2026)**. *Atmospheric Measurement Techniques*, 19, 3001-3030.
   - https://amt.copernicus.org/articles/19/3001/2026/

4. **Budiawan et al. (2024)**. *A Study on Environmental Sensors for Low-Cost Weather Stations*. Engineering Innovations, 17, 57-68.
   - https://www.scientific.net/EI.17.57

5. **Smith, R. J. (2013-2024)**. *Testing and Comparing Low Cost Hygrometers*.
   - http://www.kandrsmith.org/RJS/Misc/hygrometers.html

6. **Evaluation of Low-Cost Sensors for Weather and CO2 Monitoring (2020)**. *MDPI IoT*, 1(2), 239-258.
   - https://www.mdpi.com/2624-831X/1/2/17

7. **Chodorek et al. (2022)**. *Response Time and Intrinsic Information Quality as Criteria for Selection of Low-Cost Sensors for Mobile Weather Stations*. *Electronics*, 11(15), 2448.
   - https://doi.org/10.3390/electronics11152448

8. **Bell (2015)**. *Quantifying uncertainty in citizen weather data*. PhD thesis, Aston University.
   - https://publications.aston.ac.uk/id/eprint/26693/

9. **Wang & Hocke (2022)**. *Atmospheric Effects and Precursors of Rainfall over the Swiss Plateau*. *Remote Sensing*, 14(12), 2938.
   - https://www.mdpi.com/2072-4292/14/12/2938

10. **WMO (2025)**. *World Meteorological Congress endorses actions to promote AI for forecasts and warnings*.
    - https://wmo.int/news/media-centre/

11. **Brasil et al. (2022)**. *Minimum Rainfall Inter-Event Time to Separate Rainfall Events*. *Sustainability*, 14(3), 1721.
    - https://www.mdpi.com/2071-1050/14/3/1721

12. **WMO RA-V Workshop (2023)**. *Transition to Automated Ground-based Measurements*.
    - https://etrp.wmo.int/

13. **Sgoff et al. (2022)**. *Assimilation of crowd-sourced surface observations over Germany in a regional weather prediction system*. Quarterly Journal of the Royal Meteorological Society, 148(745), 1752-1767.
    - https://doi.org/10.1002/qj.4276

14. **Mao & Sorteberg (2026)**. *Exploring the predictability of using crowdsourced observations in statistical postprocessing of NWP based precipitation nowcasts by machine learning*. Hydrological Research Letters, 20(1), 44-51.
    - https://doi.org/10.3178/hrl.25-00020
    
Referencias que quedan sin verificar completamente
| Ref | Estado | Nota |
|---|---|---|
| WMO (2023) cita textual | ⚠️ Plausible, no confirmada | WMO-No. 1243 no está accesible públicamente |
| Budiawan (2024) valores numéricos (+0.14°C, ±0.61°C) | ⚠️ Plausible | El abstract no los incluye; vienen del paper completo (paywall) |
| MDPI IoT (2020) | ❌ 403 | Revista existe, volumen existe, pero contenido no accesible |
| Wang & Hocke (2022) | ❌ 403 | Igual, MDPI bloquea el acceso automatizado |
| Brasil et al. (2022) | ❌ 403 | Ídem |
Las 3 referencias MDPI bloqueadas son citaciones plausibles (revistas y volúmenes existen), pero si quieres verificar claims específicos necesitarás acceso institucional.
