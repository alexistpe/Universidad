Resumen de la conversación hasta ahora
Contexto del proyecto
Carpeta de trabajo: /home/ale/Files/Proyectos/MYSOFT/OPENMETEO/
Usuario investigador que necesita datos meteorológicos crudos de estaciones reales argentinas para entrenar un modelo y presentar en un congreso. Requiere:
- 5 variables fundamentales: temperatura, humedad, presión, viento (dirección + velocidad), precipitación
- Datos crudos de sensor (no interpolados ni ajustados matemáticamente)
- Mínimo 5 años de datos horarios históricos
- Estaciones específicas: Ezeiza y Córdoba
- Fuente confiable y verificable para presentación académica
Trabajo realizado
1. Investigación inicial de fuentes argentinas (scripts de investigación ejecutados en bash/python)
- API Series de Tiempo Gob.Arg: Descartada (solo datos diarios, no sub-horarios)
- SMN WIS2 (http://w2b.smn.gob.ar/oapi): 121 estaciones SYNOP, datos 1-6h, solo desde feb 2026 (~5 meses), usa OGC API estándar con WIGOS IDs. Bueno para datos recientes verificables pero NO tiene 5+ años.
- INA Alerta5 (https://alerta.ina.gob.ar/a5/): ~130 estaciones con variables meteorológicas horarias, ~3 años de historia. Limitado.
- INTA SIGA (https://siga.inta.gob.ar/CdnaUV0iiERRpFQE.php): 394 estaciones agropecuarias, 10-min tiempo real (solo hoy), datos diarios históricos desde 1999-2000. Solo temp/humedad/precip (sin viento ni presión).
2. Scripts creados
- METEO.py (original, preexistente): Descarga Open-Meteo (grilla global interpolada)
- descargar_datos_unificado.py: Script unificado con 4 fuentes (Open-Meteo, SMN WIS2, INA Alerta5, INTA SIGA)
- meteostat.py (nuevo, el principal): Script independiente que usa la librería Meteostat para descargar datos crudos de 116 estaciones argentinas vía NOAA ISD
3. Investigación profunda de Meteostat (lo último que hicimos)
Se investigó a fondo el pipeline de datos de Meteostat para determinar si es apto para un paper académico:
Hallazgos clave sobre Meteostat:
- Fuente primaria: NOAA ISD (Integrated Surface Database) — archivo global de datos horarios de superficie del gobierno de EE.UU.
- Pipeline: SMN → WMO GTS → NOAA ISD → ISD Lite → Meteostat
- Transformaciones que aplica Meteostat (código fuente analizado en GitHub):
  - Escala décimas → unidades (temp: décimas °C → °C)
  - Convierte unidades (viento: m/s → km/h, después lo convertimos a m/s en el script)
  - Humedad relativa es CALCULADA (no medida): usa fórmula August-Roche-Magnus desde temperatura y punto de rocío
  - Elimina punto de rocío después del cálculo
  - Aplica validación de rangos (temp: -100°C a +65°C, presión: 850-1090 hPa)
  - Sistema de prioridad entre proveedores (ISD Lite tiene prioridad HIGH)
  - Por defecto incluye datos de modelo para rellenar vacíos (configurable)
- No es dato 100% crudo de sensor: Hay transformaciones de escala, unidades, y la humedad es calculada
- Sí es dato de estación real: No hay interpolación espacial (para consultas de estación), proviene de observaciones in-situ
- Citado en papers académicos: Scientific Data (Nature), Environmental Research Letters, Applied Energy, Scientific Reports, etc. La comunidad académica lo trata como "raw, non-interpolated observations in situ measurements"
- Ezeiza (87576): datos horarios desde 1957, Córdoba (87344): desde 1939
Estado actual
- El script meteostat.py está completo, funcional y probado:
  - python meteostat.py lista --buscar "Cordoba" — lista estaciones
  - python meteostat.py info 87344 — metadata + inventario + links verificación
  - python meteostat.py descarga --id 87344 --inicio 2024-01-01 --fin 2024-12-31 --variables temp,rhum,pres,wdir,wspd — descarga CSV
- Se verificó que Córdoba 2024 produce 8.761 registros horarios con 100% cobertura en temp, rhum, pres, wdir, wspd
Pendiente / A considerar
- El usuario estaba evaluando si Meteostat es suficientemente confiable para un congreso. La respuesta es: depende del nivel de "crudeza" requerido. Si necesita dato 100% crudo de sensor: usar SMN WIS2 directamente (pero solo 5 meses de datos). Si acepta transformaciones de unidades y humedad calculada: Meteostat es viable y ha sido usado en papers de Nature/Elsevier.
- La humedad relativa en Meteostat no es medida por sensor sino calculada por fórmula. Para un paper esto debe aclararse en la metodología.
- Alternativa: combinar SMN WIS2 (datos recientes crudos) + Meteostat (histórico), documentando las diferencias.
Archivos relevantes
- /home/ale/Files/Proyectos/MYSOFT/OPENMETEO/meteostat.py — script principal de Meteostat (352 líneas)
- /home/ale/Files/Proyectos/MYSOFT/OPENMETEO/descargar_datos_unificado.py — script unificado con 4 fuentes
- /home/ale/Files/Proyectos/MYSOFT/OPENMETEO/METEO.py — script original de Open-Meteo
- /tmp/meteostat_stations.db — base de datos SQLite de estaciones Meteostat (32MB)
- ~/.meteostat/ — caché de la librería Meteostat
