# ModeloLIF-DeteccionLluvia

Debilidad: Se debe llamar "modelo LIF simplificado inspirado en neurociencia computacional" y no "red neuronal de picos" ni "SNN”

> Uso de redes LIF (Integración y Disparo con Fugas) para procesar datos solo cuando son necesarios, ahorrandose computo innesesario a comparacion de las redes ANN para deteccion de cambios.
> 

# Plantear el QUE, y luego el COMO:

#### Que:

Consiste en plantear la propuesta, el QUE se quiere hacer, con su correcta metodologia de aplicacion.

#### Como:

Consiste en desarrollar la propuesta, aplicando la metodologia, realizando las pruebas y documentandolas. Identificando los puntos a expandir y fundamentar para el correcto desarrollo.

#### Luego se obtienen los datos producidos en el proyecto, y se recolectan y organizan los resultados obtenidos y se produce la conclusion final.

## QUE:

Se plantea la necesidad de detecciones de tormentas en zonas locales.

Se propone una solucion utilizando un modelo matematico bioinspirado (LIF), aportando:

- **Precision:** Solo alerta cuando las condiciones realmente se confirmaron, evitando falsos positivos. (Caracteristica modelo LIF)
- **Bajo costo:** Permite utilizar el modelo y sensores con poco capital.
- **Solucion de un problema real:** Una necesidad real resuelta a bajo costo con alta precision.

Para su aplicacion utilizaremos la tegnologia bioinspirada llamada LIF. Esta tegnologica consiste en Integracion y disparo con fugas, consiste en un modelo matematico para simular neuronas biologicas en su fucionamiento basico, sin embargo utilizaremos una version simplificada del mismo, donde simularemos una unica neurona con parametros simples para el experimento en cuestion.

---

## Propuesta antigua:

- Sistema de alerta temprana de tormentas locales basado en LIF y sensores de bajo costo. (**Modelo de Alerta de Bajo Costo**).
    - **Estudio comparativo de un algoritmo bioinspirado (LIF) frente a una red densa o un umbral fijo**
    - **Componentes:**
        1. **Sensores**: 3–5 estaciones meteorológicas pequeñas (temperatura, humedad, presión
        atmosférica, intensidad de lluvia) conectadas a una Raspberry Pi o
        similar.
        2. **Red SNN simplificada**: Implementada con **snnTorch** (Python) o **Norse**, entrenada con datos históricos de tormentas en tu región (puedes usar datos públicos de estaciones meteorológicas).
        3. **Salida**: Alerta visual / sonora / mensaje cuando se detecte riesgo de tormenta o granizo en los próximos 30–60 minutos.
    - **Mediciones:**
        - **Precisión** de la LIF (porcentaje de tormentas detectadas correctamente).
        - **Falsas alarmas** (cuántas alertas sin tormenta).
        - **Consumo energético** estimado comparado con una red densa tradicional.
        - **Latencia** desde la lectura de los sensores hasta la alerta.
    - **Pasos:**
        - **Dataset:** Datos históricos de clima (hay miles en Kaggle) que tengan el registro de una tormenta minuto a minuto.
        - **Simulación:** Script donde "inyectás" esos datos a tu neurona programada.
        - **Ajuste:** Manejar *leak* (el agujerito del balde).
            - Si el agujero es muy grande, la neurona es muy "escéptica" y no avisa nunca.
            - Si el agujero es muy chico, es muy "asustadiza" y tira alertas falsas por cualquier brisa.

## Problema/concepto:

- Base teorica
    
    Los sistemas actuales utilizan redes continuas ANN, que son utiles para CPU actuales, sin embargo a comparacion de las redes SNN donde estas se activan cuando es necesario y lo realizan por pulsos, las ANN terminan siendo increiblemente ineficientes, siendo hasta 100 o 1000 veces mas ineficientes que una SNN con el hardware adecuado.
    
    Ademas de eso, las SNN tienen la capacidad nativa de manejar la incertidumbre con cautela, evitando por completo las alucinaciones y solo avanzando si la red esta segura de ello.
    
- Prediccion climatica para tormentas a bajo costo mediante el uso de LIF simplificado.
    
    Se requiere predecir el clima local ante el posible evento de una tormenta. Se necesita un sistema capaz de predecir con exactitud tormentas con la menor cantidad de falsos positivos y a bajo costo.
    
    - Predecir tormenta (clima)
        - Horas/minutos antes.
        - Sin falsos positivos.
        - A bajo costo.

## Herramientas/Teorias:

| **snnTorch** | Python/PyTorch | Entrenamiento con surrogate gradient |
| --- | --- | --- |
| **Norse** | Python/PyTorch | SNN research con LIF neuronas |

**Funcionamiento:** Las neuronas actúan como un **Filtro Pasa-Bajo** natural. El ruido aleatorio no tiene la coherencia temporal para hacer que la neurona dispare. **Solo las señales reales (coherentes) logran vencer el umbral θ.**

## Investigacion antigua:

### Estructura del paper

**Definir problema:** Necesidad de prediccion climatica para tormentas locales a bajo costo.

**Definir propuesta:** Sistema de prediccion temprana de tormentas locales a bajo costo.

**Definir herramientas a utilizar:** Utilizar el modelo matematico LIF simplificado (**Leaky Integrate-and-Fire**)

---

#### Profundizar el analisis: ¿Que implica la realizacion de este modelo?

**Preguntas:**

- ¿Como lograra predecir una tormenta este modelo, que se le necesita especificar?
    
    Se modela una unica neurona LIF que permita avisar cuando los factores correspondientes sucedan.
    
    El sistema LIF modela una neurona biologica, basandose en 3 parametros:
    
    - **Fuga:** La carga que pierde por segundo.
    - **Limite:** El umbral que debe superar para realizar un spike.
    - **Pesos/pulsos:** Permiten “cargar” la neurona enviando pulsos. (Fundamentar 3 factores determinantes para la prediccion de tormentas):
        - Humedad
        - Temperatura
        - Presion
- ¿Que fuentes se utilizaran para la obtencion de los datos?
    - ….
- ¿El paper se basa en una demostracion potencial de uso o de una comparacion con otros modelos de prediccion?
- ¿Cuales son sus limites?
    - ¿Se modela la alarma?
    - ¿Se prueba/crea empiricamente?

### Hecho hasta ahora.

- **Arquitecturas alternativas de IA**
    
    # Informe Técnico: RWKV, SNN y Spike-GPT - Arquitecturas Alternativas para IA
    
    ## Resumen Ejecutivo
    
    Este informe analiza tres arquitecturas de inteligencia artificial que representan alternativas al paradigma dominante de los Transformers: **RWKV** (Red Neuronal Recurrente moderna), **SNN** (Spiking Neural Networks, inspiradas en el cerebro biológico) y **Spike-GPT** (la convergencia de ambas). El documento aborda su fundamento teórico, estado actual de desarrollo, nivel de complejidad para su implementación, y la posibilidad de simularlos sin hardware especializado. La información está actualizada a 2026 e incluye los últimos avances presentados en conferencias como ICLR 2025 y GDC 2026.
    
    ## 1. Modelo RWKV: Recurrent Neural Networks Modernas
    
    ### 1.1 ¿Qué es RWKV?
    
    RWKV (Receptance Weighted Key Value) es una arquitectura de red neuronal recurrente (RNN) diseñada como una alternativa eficiente a los Transformers. Su nombre proviene de sus cuatro componentes fundamentales: **R**eceptance, **W**eight, **K**ey, **V**alue .
    
    A diferencia de los Transformers, que requieren memoria cuadrática con respecto a la longitud de la secuencia (complejidad O(n²)), RWKV mantiene un **estado de tamaño fijo** que se actualiza secuencialmente, logrando complejidad lineal O(n) . Esto lo hace significativamente más eficiente para procesar secuencias largas.
    
    ### 1.2 Características Clave
    
    | Característica | Descripción |
    | --- | --- |
    | **Arquitectura** | RNN con estado de tamaño fijo |
    | **Complejidad** | O(n) en tiempo y memoria (vs O(n²) de Transformers) |
    | **Entrenamiento** | Paralelizable como Transformer, inferencia recurrente |
    | **Aplicación Principal** | Procesamiento de lenguaje natural eficiente |
    
    ### 1.3 Estado Actual de Investigación (2026)
    
    La investigación en RWKV ha avanzado significativamente. El framework **DREAMSTATE** (Diffusing States and Parameters for Recurrent Large Language Models), presentado en enero 2026, explora las propiedades representacionales del estado interno de RWKV .
    
    **Hallazgos clave de DREAMSTATE:**
    
    - El estado interno de RWKV tiene una estructura representacional que puede ser modelada y editada
    - Utiliza un **Diffusion Transformer (DiT)** para modelar la manifold de probabilidad del estado
    - Propone una arquitectura híbrida donde los parámetros WKV se generan dinámicamente a partir de contexto global variable
    - Validación experimental mediante visualizaciones t-SNE y experimentos de generación controlada
    
    El código de DREAMSTATE está disponible públicamente en Hugging Face .
    
    ## 2. SNN: Spiking Neural Networks (Redes Neuronales con Picos)
    
    ### 2.1 Fundamentos Teóricos
    
    Las Spiking Neural Networks (SNN) representan la tercera generación de redes neuronales, inspiradas directamente en el funcionamiento del cerebro biológico . A diferencia de las ANN tradicionales que procesan valores continuos, las SNN operan mediante **eventos discretos llamados "spikes" (picos o pulsos)** .
    
    ### 2.1.1 Comparativa ANN vs SNN
    
    | Aspecto | ANN (Tradicional) | SNN (Neuromórfica) |
    | --- | --- | --- |
    | **Unidad de información** | Valor continuo (ej: 0.372) | Spike binario (0 o 1) |
    | **Tiempo** | Procesamiento síncrono por capas | Procesamiento asíncrono, dependiente del tiempo |
    | **Computación** | Operaciones matriciales densas | Event-driven (solo cuando hay spikes) |
    | **Energía** | Alta (GPU) | Ultra-baja (microjulios por inferencia) |
    | **Memoria** | Pesos estáticos | Estado dinámico (membrana) + pesos |
    
    ### 2.1.2 Modelo de Neurona: Leaky Integrate-and-Fire (LIF)
    
    El modelo más utilizado en SNN es el **LIF (Leaky Integrate-and-Fire)**, que simula el comportamiento de una neurona biológica en tres etapas :
    
    1. **Integrate (Integración)**: Cuando recibe spikes de entrada, el potencial de membrana aumenta.
    2. **Leaky (Fuga)**: Con el tiempo, el potencial se "filtra" (decae) si no hay estímulos.
    3. **Fire (Disparo)**: Si el potencial supera un umbral, la neurona emite un spike y el potencial se reinicia.
    
    Esta dinámica temporal permite a las SNN procesar naturalmente información con componente temporal, a diferencia de las ANN que requieren mecanismos adicionales como positional encoding .
    
    ### 2.2 Métodos de Codificación
    
    Para convertir datos de entrada (como imágenes o texto) a spikes, se utilizan dos enfoques principales :
    
    | Método | Descripción | Ventajas |
    | --- | --- | --- |
    | **Rate Coding** | La intensidad se traduce en frecuencia de spikes. Mayor valor = más spikes por unidad de tiempo | Simple, robusto, ampliamente utilizado |
    | **Temporal Coding** | La intensidad se traduce en el momento del spike. Mayor valor = spike más temprano | Más eficiente, menos spikes, información más densa |
    
    Además, las SNN pueden integrarse directamente con sensores neuromórficos como **event cameras (DVS)**, que generan spikes ante cambios en la escena, eliminando la necesidad de codificación .
    
    ### 2.3 Estrategias de Entrenamiento
    
    El principal desafío de las SNN es su **no diferenciabilidad**: la función de activación (spike) es una función escalón, cuya derivada es cero o infinita, lo que imposibilita el uso directo de backpropagation .
    
    Existen tres enfoques principales para entrenar SNN:
    
    ### 2.3.1 Surrogate Gradient (Gradiente Sustituto)
    
    Es la técnica más exitosa actualmente. Durante el forward pass, se usa la función de spike real (no diferenciable). Durante el backward pass, se reemplaza la derivada con una aproximación suave .
    
    **Resultados:** SNN entrenadas con gradiente sustituto alcanzan una precisión **dentro del 1-2% de las ANN equivalentes** en benchmarks de imagen como CIFAR-10 e ImageNet .
    
    ### 2.3.2 ANN-to-SNN Conversion
    
    Consiste en entrenar una ANN convencional y luego convertir sus pesos a una SNN equivalente. Este método evita el problema de entrenamiento directo .
    
    **Limitaciones:** Requiere más tiempo de simulación y más spikes por inferencia, pero es el enfoque más maduro para aplicaciones prácticas.
    
    ### 2.3.3 STDP (Spike-Timing Dependent Plasticity)
    
    Un mecanismo biológicamente plausible donde la conexión entre dos neuronas se fortalece si la pre-sináptica dispara justo antes que la post-sináptica . Es un aprendizaje **no supervisado** y local, ideal para sistemas que deben adaptarse en tiempo real.
    
    **Ventajas:** Consumo energético extremadamente bajo (hasta 5 milijulios por inferencia) .
    **Desventajas:** Convergencia más lenta y precisión menor que los métodos supervisados.
    
    ### 2.4 Hardware Neuromórfico para SNN
    
    Las SNN están diseñadas para ejecutarse en hardware especializado que aprovecha su naturaleza event-driven:
    
    | Plataforma | Desarrollador | Características |
    | --- | --- | --- |
    | **Loihi 2** | Intel | Investigación neuromórfica, soporte para modelos MatMul-free |
    | **TrueNorth** | IBM | 1 millón de neuronas, 256 millones de sinapsis |
    | **SpiNNaker** | Universidad de Manchester | Simulación a gran escala de redes neuronales |
    | **DYNAP-CNN** | SynSense | Hardware para redes convolucionales con spikes |
    
    Estos chips logran consumos de energía de **2-20 watts** para modelos que en GPU consumirían cientos de watts .
    
    ## 3. Spike-GPT: Convergencia de RWKV y SNN
    
    ### 3.1 ¿Qué es Spike-GPT?
    
    Spike-GPT es un modelo de lenguaje generativo que combina la arquitectura eficiente de **RWKV** con la naturaleza **event-driven de las SNN**. Fue presentado en ICLR 2025 por Rui-Jie Zhu, Qihang Zhao, Jason Eshraghian y Guoqi Li .
    
    ### 3.2 Arquitectura y Escalado
    
    | Parámetro | Valor |
    | --- | --- |
    | **Variante pequeña** | 46 millones de parámetros |
    | **Variante grande** | 216 millones de parámetros |
    | **Arquitectura base** | RWKV modificado (atención reemplazada) |
    | **Activación** | Unidades de spike binarias y event-driven |
    
    Al momento de su lanzamiento, Spike-GPT fue el **SNN más grande entrenado con backpropagation** .
    
    ### 3.3 Complejidad Computacional
    
    Spike-GPT logra reducir la complejidad cuadrática O(T²) de los Transformers a **complejidad lineal O(T)**, donde T es la longitud de la secuencia. Esto se logra procesando los tokens secuencialmente, como una RNN, en lugar de procesar toda la secuencia en paralelo .
    
    ### 3.4 Eficiencia Energética
    
    Según los autores, Spike-GPT requiere **32.2× menos operaciones** cuando se ejecuta en hardware neuromórfico que aprovecha la naturaleza sparse y event-driven de las activaciones .
    
    ### 3.5 Evolución: Ouro (2026)
    
    Jason Eshraghian (UCSC Neuromorphic Computing Group) presentó en marzo 2026 **Ouro**, un modelo de razonamiento latente entrenado end-to-end que evoluciona los principios de Spike-GPT .
    
    **Características de Ouro:**
    
    - **2 mil millones de parámetros** (aproximadamente)
    - Corre en hardware neuromórfico a **2 watts**
    - Supera a modelos de Meta y Google en el rango de ~10B parámetros
    - "Pega 5 veces por encima de su peso" (performance relativa)
    
    ### 3.6 Estado Actual
    
    Spike-GPT y sus derivados representan la frontera de investigación en SNN para lenguaje. Aunque competitivos, aún no igualan el rendimiento de los grandes modelos comerciales (GPT-5, Claude) en benchmarks de lenguaje general, pero la brecha se está cerrando rápidamente .
    
    ## 4. Complejidad de Crear una SNN vs ANN
    
    ### 4.1 Dificultad Relativa
    
    | Aspecto | ANN | SNN | Diferencia |
    | --- | --- | --- | --- |
    | **Conceptos básicos** | Simple (matrices + activaciones) | Compleja (LIF, tiempo, spikes, codificación) | SNN requiere comprensión de dinámica temporal |
    | **Frameworks** | Maduros (PyTorch, TF, JAX) | Emergentes (snnTorch, Norse, Lava) | ANN tiene ecosistema más desarrollado |
    | **Entrenamiento** | Backpropagation estándar | Surrogate gradient, STDP, o conversión | SNN requiere técnicas especializadas |
    | **Debugging** | Visualización de pérdidas/gradientes | Visualización de spikes, potencial de membrana | Más complejo en SNN |
    | **Documentación** | Abundante | Limitada, principalmente académica | ANN tiene mejor soporte |
    
    ### 4.2 Principales Problemas en el Desarrollo SNN
    
    ### 4.2.1 La "Maldición de la No-Diferenciabilidad"
    
    Es el obstáculo fundamental. Mientras que las ANN tienen funciones de activación continuas y diferenciables, la función de spike es una **función escalón** con derivada cero en casi todo su dominio e indefinida en el punto de cambio .
    
    **Impacto:** No se puede aplicar backpropagation directamente. Se requieren aproximaciones (surrogate gradient) que introducen complejidad adicional y pueden afectar la convergencia.
    
    ### 4.2.2 Simulación Temporal Costosa
    
    Las SNN requieren simular la evolución temporal de las neuronas durante múltiples pasos de tiempo (time steps). Una imagen de entrada puede necesitar decenas o cientos de pasos para ser procesada .
    
    **Comparación:**
    
    - **ANN**: 1 forward pass → resultado
    - **SNN**: 100-200 time steps → resultado
    
    Esto hace que el entrenamiento de SNN sea **10-100 veces más lento** que ANN equivalentes en hardware convencional.
    
    ### 4.2.3 Falta de Estandarización en Software
    
    A diferencia de ANN donde PyTorch/TensorFlow son estándares de facto, las SNN tienen múltiples frameworks incompatibles: snnTorch, Norse, Lava, Nengo, etc. .
    
    ### 4.2.4 Hardware Heterogéneo
    
    El hardware neuromórfico (Loihi, SpiNNaker) no es estándar y cada plataforma tiene su propia API y limitaciones. No hay un "GPU para SNN" unificado .
    
    ### 4.3 ¿Cuánto Cuesta Desarrollar una SNN?
    
    **Para investigación académica:**
    
    - Curva de aprendizaje: 3-6 meses para dominar conceptos y frameworks
    - Código base: 5,000-20,000 líneas para un modelo funcional
    - Dependencia de colaboración con hardware especializado
    
    **Para producción industrial:**
    
    - Actualmente limitada a casos de uso muy específicos (bajo consumo)
    - La mayoría adopta ANN-to-SNN conversion para evitar complejidad de entrenamiento
    - Empresas con hardware neuromórfico propio (Intel, IBM) tienen ventaja competitiva
    
    ## 5. Simulación de SNN sin Hardware Físico
    
    ### 5.1 Respuesta Corta
    
    **Sí, es perfectamente posible programar y probar SNN sin tener hardware neuromórfico.** Existen múltiples simuladores que permiten desarrollar, entrenar y evaluar SNN completamente en software .
    
    ### 5.2 Plataformas de Simulación SNN
    
    ### 5.2.1 Specksim (Recomendado para DYNAP-CNN)
    
    Specksim es un simulador de alto rendimiento para SNN convolucionales, escrito en C++ con bindings a Python. Está diseñado para emular el comportamiento del hardware DYNAP-CNN .
    
    **Características:**
    
    - Simulación completamente **event-based**
    - Conversión directa de modelos ANN a SNN via `sinabs`
    - Soporte para `torch.nn.Sequential` y capas spiking (`IAF`, `IAFSqueeze`)
    - Entrada/salida en formato de eventos (x, y, t, p)
    
    **Limitaciones importantes:**
    
    - **Solo inferencia, no entrenamiento**
    - No soporta biases
    - Procesamiento breadth-first vs depth-first del hardware real
    - No es tiempo real (hay delays en simulaciones complejas)
    
    ### 5.2.2 RAVSim (Real-Time SNNs Model Analyzing and Visualizing Experimentation)
    
    RAVSim es un simulador interactivo implementado en LabVIEW que permite:
    
    - Modificar parámetros de entrada y modelo en **tiempo real**
    - Visualizar comportamiento de SNN
    - Definir arquitectura completamente en software sin necesidad de re-sintetizar hardware
    
    **Ventaja clave:** Excelente para **experimentación interactiva** y enseñanza.
    
    ### 5.2.3 Otros Frameworks
    
    | Framework | Plataforma | Propósito |
    | --- | --- | --- |
    | **snnTorch** | Python/PyTorch | Entrenamiento con surrogate gradient |
    | **Norse** | Python/PyTorch | SNN research con LIF neuronas |
    | **Lava** | Python/Intel | Desarrollo para Loihi, con simulación software |
    | **Nengo** | Python | Modelado a gran escala, conexión con hardware |
    | **Brian2** | Python | Simulación biológicamente detallada |
    
    ### 5.3 Flujo de Trabajo Típico
    
    ```
    1. Entrenar ANN en PyTorch (opcional)
          ↓
    2. Convertir a SNN con sinabs (si aplica)
          ↓
    3. Cuantizar pesos para hardware (discretize=True)
          ↓
    4. Simular con Specksim (modo software)
          ↓
    5. Validar comportamiento y métricas
          ↓
    6. (Opcional) Desplegar en hardware real
    ```
    
    ### 5.4 Limitaciones de la Simulación
    
    1. **No es tiempo real**: Simular millones de eventos en software tiene latencia, especialmente para redes grandes
    2. **Aproximaciones de hardware**: El comportamiento exacto de los chips neuromórficos (latencia de core, encolado de eventos) es difícil de emular perfectamente
    3. **Sin entrenamiento en simulación**: Muchos simuladores son solo para inferencia
    4. **Modelos de neuronas limitados**: No todos los simuladores soportan todos los tipos de neuronas
    
    ## 6. Conclusiones y Recomendaciones
    
    ### 6.1 Resumen de Hallazgos
    
    | Tecnología | Estado | Complejidad | Recomendación |
    | --- | --- | --- | --- |
    | **RWKV** | Maduro, en investigación activa | Baja (similar a RNN) | Excelente para proyectos de LLM eficientes |
    | **SNN (general)** | Emergente, alto potencial | Alta | Recomendado para edge AI y bajo consumo |
    | **Spike-GPT** | Prototipo académico | Muy alta | Para investigación avanzada |
    | **Simulación SNN** | Madura | Media | Perfectamente viable sin hardware |
    
    ### 6.2 Para tu Proyecto CNEISI
    
    Dado tu hardware (GT 1030, Ryzen 3400G, 16GB RAM):
    
    1. **RWKV es viable** - Puedes ejecutar modelos pequeños en CPU/GPU limitada
    2. **Simulación SNN con Specksim** - Funciona en CPU, no requiere GPU potente
    3. **Spike-GPT** - Probablemente muy demandante para tu hardware actual
    
    ### 6.3 Recomendación de Enfoque
    
    Si tu interés es presentar en CNEISI, te sugiero:
    
    **Opción A (Menor riesgo)**: Desarrollar un agente basado en **RWKV** con herramientas como `smolagents` o `Ollama`, enfocado en testing de videojuegos o ciberseguridad.
    
    **Opción B (Mayor impacto académico)**: Implementar una **SNN en simulación** (Specksim) para un caso de uso específico, documentando la complejidad y comparando con ANN equivalente.
    
    **Opción C (Innovación pura)**: Trabajar con Spike-GPT como base teórica, proponiendo una mejora o adaptación para tu dominio de aplicación.
    
    ### 6.4 Recursos Recomendados
    
    - **Código Spike-GPT**: [https://github.com/ridgerchu/SpikeGPT](https://github.com/ridgerchu/SpikeGPT)
    - **DREAMSTATE**: [https://huggingface.co/2dgx41s/DreamState](https://huggingface.co/2dgx41s/DreamState)
    - **Specksim**: Documentación en [sinabs.readthedocs.io](http://sinabs.readthedocs.io/)
    - **snnTorch**: [https://github.com/jeshraghian/snntorch](https://github.com/jeshraghian/snntorch)
    
    ---
    
    *Informe preparado con información actualizada a abril 2026, basado en publicaciones de arXiv, ICLR 2025, y presentaciones del UCSC Neuromorphic Computing Group.*
    
- **Informe de SNN**
    
    ## SNN: Spiking Neural Networks (Redes Neuronales con Picos)
    
    ### 2.1 Fundamentos Teóricos
    
    Las Spiking Neural Networks (SNN) representan la tercera generación de redes neuronales, inspiradas directamente en el funcionamiento del cerebro biológico . A diferencia de las ANN tradicionales que procesan valores continuos, las SNN operan mediante **eventos discretos llamados "spikes" (picos o pulsos)** .
    
    ### 2.1.1 Comparativa ANN vs SNN
    
    | Aspecto | ANN (Tradicional) | SNN (Neuromórfica) |
    | --- | --- | --- |
    | **Unidad de información** | Valor continuo (ej: 0.372) | Spike binario (0 o 1) |
    | **Tiempo** | Procesamiento síncrono por capas | Procesamiento asíncrono, dependiente del tiempo |
    | **Computación** | Operaciones matriciales densas | Event-driven (solo cuando hay spikes) |
    | **Energía** | Alta (GPU) | Ultra-baja (microjulios por inferencia) |
    | **Memoria** | Pesos estáticos | Estado dinámico (membrana) + pesos |
    
    ### 2.1.2 Modelo de Neurona: Leaky Integrate-and-Fire (LIF)
    
    El modelo más utilizado en SNN es el **LIF (Leaky Integrate-and-Fire)**, que simula el comportamiento de una neurona biológica en tres etapas :
    
    1. **Integrate (Integración)**: Cuando recibe spikes de entrada, el potencial de membrana aumenta.
    2. **Leaky (Fuga)**: Con el tiempo, el potencial se "filtra" (decae) si no hay estímulos.
    3. **Fire (Disparo)**: Si el potencial supera un umbral, la neurona emite un spike y el potencial se reinicia.
    
    Esta dinámica temporal permite a las SNN procesar naturalmente información con componente temporal, a diferencia de las ANN que requieren mecanismos adicionales como positional encoding .
    
    ### 2.2 Métodos de Codificación
    
    Para convertir datos de entrada (como imágenes o texto) a spikes, se utilizan dos enfoques principales :
    
    | Método | Descripción | Ventajas |
    | --- | --- | --- |
    | **Rate Coding** | La intensidad se traduce en frecuencia de spikes. Mayor valor = más spikes por unidad de tiempo | Simple, robusto, ampliamente utilizado |
    | **Temporal Coding** | La intensidad se traduce en el momento del spike. Mayor valor = spike más temprano | Más eficiente, menos spikes, información más densa |
    
    Además, las SNN pueden integrarse directamente con sensores neuromórficos como **event cameras (DVS)**, que generan spikes ante cambios en la escena, eliminando la necesidad de codificación .
    
    ### 2.3 Estrategias de Entrenamiento
    
    El principal desafío de las SNN es su **no diferenciabilidad**: la función de activación (spike) es una función escalón, cuya derivada es cero o infinita, lo que imposibilita el uso directo de backpropagation .
    
    Existen tres enfoques principales para entrenar SNN:
    
    ### 2.3.1 Surrogate Gradient (Gradiente Sustituto)
    
    Es la técnica más exitosa actualmente. Durante el forward pass, se usa la función de spike real (no diferenciable). Durante el backward pass, se reemplaza la derivada con una aproximación suave .
    
    **Resultados:** SNN entrenadas con gradiente sustituto alcanzan una precisión **dentro del 1-2% de las ANN equivalentes** en benchmarks de imagen como CIFAR-10 e ImageNet .
    
    ### 2.3.2 ANN-to-SNN Conversion
    
    Consiste en entrenar una ANN convencional y luego convertir sus pesos a una SNN equivalente. Este método evita el problema de entrenamiento directo .
    
    **Limitaciones:** Requiere más tiempo de simulación y más spikes por inferencia, pero es el enfoque más maduro para aplicaciones prácticas.
    
    ### 2.3.3 STDP (Spike-Timing Dependent Plasticity)
    
    Un mecanismo biológicamente plausible donde la conexión entre dos neuronas se fortalece si la pre-sináptica dispara justo antes que la post-sináptica . Es un aprendizaje **no supervisado** y local, ideal para sistemas que deben adaptarse en tiempo real.
    
    **Ventajas:** Consumo energético extremadamente bajo (hasta 5 milijulios por inferencia) .
    **Desventajas:** Convergencia más lenta y precisión menor que los métodos supervisados.
    
    - **Manejo de incertidumbre** por parte de las SNN a comparacion de las ANN
        
        ### **1. Acumulación de Evidencia (El factor tiempo)**
        
        En una ANN, vos le das una imagen y, en un solo paso matemático, te devuelve un número (ej. "90% perro"). Si la imagen es ruidosa, la ANN igual te va a tirar un número, aunque sea fruta.
        
        En una **SNN**, la neurona funciona por acumulación. El potencial de membrana V(t) va subiendo a medida que recibe pulsos:
        
        τmdtdv=−(v(t)−vrest)+R⋅I(t)
        
        - **Si el estímulo es claro:** El potencial llega rápido al umbral θ y la neurona dispara al toque.
        - **Si el estímulo es incierto (ruido):** El potencial sube y baja erráticamente. La neurona "espera" a recibir más confirmación antes de disparar.
        
        **Esa demora es la representación física de la incertidumbre.** En sistemas, esto es oro: podés medir la duda del modelo simplemente viendo cuánto tarda en responder.
        
        ---
        
        ### **2. El Silencio como Información (Sparsity)**
        
        Las ANN sufren del problema de que "siempre tienen algo que decir". Incluso si el input es basura, las neuronas activan sus pesos y generan una salida.
        
        En las **SNN**, si la señal no es lo suficientemente fuerte o coherente para vencer al "umbral de disparo", la neurona se queda en **silencio**.
        
        - En una red de defensa o un sensor de satélite, que un nodo no dispare es un mensaje de: *"No tengo suficiente información para validar este evento"*.
        - Esto evita que el error se propague por las capas superiores del grafo, algo que en las ANN genera alucinaciones o clasificaciones erróneas.
        
        ---
        
        ### **3. Jitter y Variabilidad (Bayesian Brain)**
        
        Existe una teoría llamada el **Cerebro Bayesiano**, que dice que nuestras neuronas representan distribuciones de probabilidad, no valores fijos. Las SNN son geniales para esto:
        
        - **Variabilidad del pulso:** La "incertidumbre" se puede codificar en el *jitter* (la variación temporal) de los pulsos.
        - Si los pulsos son rítmicos y constantes, hay alta certeza.
        - Si los pulsos son erráticos, el sistema está informando que hay alta varianza (duda).
        
        Las ANN necesitan capas complejas (como las Bayesian Neural Networks) para hacer esto, lo que consume muchísima memoria. La SNN lo hace "gratis" por su propia física.
        
    
    ### 2.4 Hardware Neuromórfico para SNN
    
    Las SNN están diseñadas para ejecutarse en hardware especializado que aprovecha su naturaleza event-driven:
    
    | Plataforma | Desarrollador | Características |
    | --- | --- | --- |
    | **Loihi 2** | Intel | Investigación neuromórfica, soporte para modelos MatMul-free |
    | **TrueNorth** | IBM | 1 millón de neuronas, 256 millones de sinapsis |
    | **SpiNNaker** | Universidad de Manchester | Simulación a gran escala de redes neuronales |
    | **DYNAP-CNN** | SynSense | Hardware para redes convolucionales con spikes |
    
    Estos chips logran consumos de energía de **2-20 watts** para modelos que en GPU consumirían cientos de watts .
    
- **Biografia.**
    
    https://arxiv-org.translate.goog/html/2302.13939v5?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc
    
    - **Código Spike-GPT**: [https://github.com/ridgerchu/SpikeGPT](https://github.com/ridgerchu/SpikeGPT)
    - **DREAMSTATE**: [https://huggingface.co/2dgx41s/DreamState](https://huggingface.co/2dgx41s/DreamState)
    - **Specksim**: Documentación en [sinabs.readthedocs.io](https://sinabs.readthedocs.io/)
    - **snnTorch**: [https://github.com/jeshraghian/snntorch](https://github.com/jeshraghian/snntorch)

### Descripcion problema-solucion.

- Prediccion climatica a bajo costo.
    
    Se requiere predecir el comienzo de una tormenta horas antes de que empiece, de forma localizada y precisa. Preferentemente a bajo costo.
    
    **Problema:** Ineficiencia energética y falsas alarmas de las ANN tradicionales en dispositivos de borde (*Edge Computing*) para predicción climática.
    **Solucion**: Uso de **Redes Neuronales de Picos (SNN)** basadas en el modelo **LIF** (*Leaky Integrate-and-Fire*) para procesar datos meteorológicos temporales.
    

### Metodologia para afrontarlo.

- Prediccion climatica a bajo costo. (Revision)
    
    Se propone el uso de un sistema con SNN (spike neural networks), para crear una red capaz de identificar multiples patrones entre diferentes variables y gracias a ello plasmarlo en una notificacion de alerta.
    Simulación digital utilizando datasets históricos de la región (Kaggle/SMN), convirtiendo variables continuas en ráfagas de impulsos (*spikes*).
    
    **Qué medir:**
    
    - **Precisión** de la SNN (porcentaje de tormentas detectadas correctamente).
    - **Falsas alarmas** (cuántas alertas sin tormenta).
    - **Consumo energético** estimado comparado con una red densa tradicional.
    - **Latencia** desde la lectura de los sensores hasta la alerta.
    - **Comparacion con modelos estandares.**
    
    #### **Paso A: La "Materia Prima" (El Dataset)**
    
    Buscás en Kaggle o en el sitio del **Servicio Meteorológico Nacional (SMN)** datos históricos de Villa María o Córdoba. Necesitás un CSV con columnas de: `Temperatura`, `Humedad`, `Presión` y `Evento` (1 si hubo tormenta, 0 si no).
    
    #### **Paso B: El "Traductor" (Encoding)**
    
    Las SNN no entienden el número "1013 hPa". Tenés que convertir ese número en pulsos.
    
    - **Rate Encoding:** Si la presión baja mucho, mandás más pulsos por segundo. Si está estable, mandás pocos.
    - **Latency Encoding:** El sensor que detecta el cambio más brusco manda el pulso "primero". El orden de los pulsos le dice a la SNN qué está pasando.
    
    #### **Paso C: El "Inyector" (Loop de Simulación)**
    
    En tu código de Python (con `snnTorch`), creás un bucle que lea una fila del CSV por vez:
    
    1. Leés la fila del minuto t=100.
    2. La convertís a spikes.
    3. Se la pasás a la neurona.
    4. La neurona actualiza su potencial de membrana V.
    5. Repetís para el minuto t=101.
    
    Mediante la formula: V[t]=V[t−1]⋅fuga+entrada creas el sistema de SNN.
    
    - **La Fórmula del Potencial de Membrana (Discreta)**
        
        No usás la ecuación diferencial continua, sino su versión por pasos de tiempo. La fórmula básica para actualizar el "balde" es:
        
        V[t+1]=V[t]⋅β+X[t]
        
        Donde:
        
        - V[t+1] es el potencial nuevo.
        - V[t] es el potencial anterior.
        - β es tu factor de **leak** (decaimiento).
        - X[t] es la entrada del sensor en ese momento.
        
        ![image.png](ModeloLIF-DeteccionLluvia/image.png)
        
    
    ### **El flujo de trabajo (Pruebas python, implementacion en C++)**
    
    En la industria y en el **CNEISI**, lo que más se valora es este flujo:
    
    1. **Entrenamiento en Python:** Usás `snnTorch` o `Norse` en tu PC con los datos de Kaggle para encontrar el "punto justo" de tu umbral y tu fuga.
    2. **Exportación de Pesos:** Una vez que sabés que con un umbral de 1.5 y una fuga de 0.95 detectás la tormenta, anotás esos números.
    3. **Implementación en C++:** Programás el sensor real con esos valores fijos. Esto se llama **Inferencia en el Borde** (*Edge Inference*).

### Pruebas y resultados.

- Prediccion climatica a bajo costo.
    
    Precisión diagnóstica, tasa de falsas alarmas, latencia de respuesta y eficiencia energética teórica.
    
    #### Medir y comprar entre SNN y sistemas actuales:
    
    - **Precisión** de la SNN (porcentaje de tormentas detectadas correctamente).
    - **Falsas alarmas** (cuántas alertas sin tormenta).
    - **Consumo energético** estimado comparado con una red densa tradicional.
    - **Latencia** desde la lectura de los sensores hasta la alerta.
    
    #### Comparar eficiencia en Python vs C++
    

### Conclusiones.

**Impacto:** Sistema de bajo costo y alta autonomía ideal para zonas rurales o infraestructura civil crítica.

---

# Base

- **GUIA DE REFERENCIA.**
    
    # Guía para la Formalización de tu Propuesta de Investigación con SNN LIF para Predicción de Tormentas Locales
    
    ## Introducción: El momento de pasar de la idea al planteamiento
    
    Has dado con una idea que tiene potencial real de convertirse en un trabajo de investigación sólido. El desafío ahora es dejar de "dar vueltas alrededor de la idea" y empezar a construir una propuesta concreta, con límites claros, fundamentos sólidos y un plan viable.
    
    Lo que buscas es exactamente esto: una base completa sobre la cual construir. Vamos a estructurarlo en **tres fases progresivas**:
    
    1. **Formalización de la idea de investigación** (¿qué vas a investigar realmente?)
    2. **Delimitación del proyecto** (¿dónde empieza y dónde termina tu trabajo?)
    3. **Preparación de la propuesta para CNEISI** (lo mínimo que necesitas tener definido antes de escribir una línea de código)
    
    Cada fase incluye **preguntas guía, decisiones concretas y una plantilla para que completes**.
    
    ---
    
    ## Fase 1: Formalización de la Idea de Investigación
    
    Tu idea base está clara: usar un modelo LIF (Leaky Integrate-and-Fire) simplificado para detectar tormentas locales con bajo costo. Ahora hay que convertir esa idea general en una **pregunta de investigación precisa**, respaldada por un **estado del arte** que justifique por qué vale la pena explorarla.
    
    ### 1.1 Definir la pregunta de investigación
    
    Una buena pregunta de investigación debe ser **específica, respondible empíricamente y no trivial**. Tu pregunta actual es:
    
    > "¿Se puede predecir tormentas locales con un modelo LIF simplificado?"
    > 
    
    Esta pregunta es demasiado abierta. Te propongo refinarla en una dirección más concreta:
    
    > **Pregunta propuesta:** "¿Es posible detectar patrones de tormenta local en datos de sensores de bajo costo utilizando un modelo de neurona LIF como detector de anomalías temporal, logrando una tasa de falsos positivos inferior a los métodos tradicionales basados en umbrales fijos?"
    > 
    
    **¿Por qué esta formulación?**
    
    | Componente | Qué aporta |
    | --- | --- |
    | "detectar patrones de tormenta" | Acota a detección (no predicción a largo plazo) |
    | "datos de sensores de bajo costo" | Define el dominio operativo |
    | "modelo LIF como detector de anomalías" | Especifica el mecanismo concreto |
    | "tasa de falsos positivos inferior a umbrales fijos" | Define la métrica de éxito y el baseline de comparación |
    
    **Tu tarea:** Escribe tu propia pregunta de investigación. Puedes empezar desde esta propuesta y ajustarla a lo que realmente quieras responder.
    
    ### 1.2 Fundamentar por qué LIF es relevante
    
    Para un paper académico, no basta con decir "uso LIF porque es bioinspirado". Necesitas mostrar que hay una **base teórica y resultados previos** que respaldan su idoneidad para este tipo de problema.
    
    **Lo que la investigación actual dice sobre SNN y detección de anomalías:**
    
    | Hallazgo Clave | Fuente |
    | --- | --- |
    | Las SNN capturan cambios en señales temporales y reducen consumo de recursos en comparación con ANN, aunque tradicionalmente sacrifican algo de rendimiento | Zhang et al. (2025) |
    | Modelos híbridos spiking con codificación de frecuencia de primer spike alcanzan rendimiento superior en detección de anomalías con **5.04× menor consumo energético** que su equivalente ANN | Zhang et al. (2025) |
    | El modelo LIF ha sido aplicado exitosamente a forecasting de series temporales ambientales (irradiancia solar) | Alharbi & Ahmed, IEEE Access (2024) |
    | La versión cuántica QLIF (Quantum Leaky Integrate-and-Fire) ha demostrado mejoras del **15.4% en MSE** y convergencia hasta **94% más rápida** para forecasting climático | Marchisio et al., arXiv (mayo 2026) |
    
    **Lo que esto significa para tu propuesta:** Tu enfoque no es "inventar algo nuevo", sino **aplicar una técnica que ya ha mostrado ventajas en dominios similares a un problema concreto** (tormentas locales), con un giro original: usar una versión simplificada (una neurona) y evaluar su eficacia vs. un baseline sencillo. Esto es perfectamente válido para un congreso estudiantil.
    
    **Tu tarea:** Resume en 3-5 líneas por qué el modelo LIF es una opción pertinente para tu problema.
    
    ### 1.3 Definir la contribución esperada
    
    Un buen proyecto de investigación no solo "hace algo", sino que **aporta algo** al conocimiento o a la práctica. Tu contribución podría ser:
    
    | Tipo de Contribución | Posible enunciado |
    | --- | --- |
    | **Metodológica** | Mostrar cómo adaptar un modelo LIF para detección de anomalías en datos climáticos de bajo costo |
    | **Empírica** | Generar evidencia comparativa (LIF vs umbral fijo) en un dominio específico (tormentas locales) |
    | **Práctica** | Demostrar la viabilidad técnica de un sistema de alerta de bajo costo implementable en hardware de gama baja |
    
    **Tu tarea:** Define cuál será la principal contribución de tu trabajo. Sé honesto con el alcance: para un proyecto de primer año, la contribución práctica y la evidencia empírica son los caminos más realistas.
    
    ### 1.4 Contextualizar vs. métodos existentes
    
    Para que tu trabajo tenga "originalidad acotada" (como exige el CNEISI), necesitas mostrar que tu propuesta se diferencia de lo que ya existe.
    
    **Alternativas existentes en el mercado/sector:**
    
    | Alternativa | Fortalezas | Debilidades |
    | --- | --- | --- |
    | Estaciones meteorológicas comerciales (Davis, Oregon Scientific) | Precisión, confiabilidad | Costo elevado (>USD 500) |
    | Datos satelitales + IA (ECMWF AIFS, modelos ML) | Gran cobertura geográfica, alta precisión | Infraestructura masiva, no localizable |
    | Métodos de umbral fijo (ej. "alerta si presión baja 5 hPa") | Simple, bajo costo | Altas tasas de falsas alarmas |
    
    **Tu diferenciación:** Un sistema de bajo costo que utiliza un modelo bioinspirado para reducir falsas alarmas en comparación con métodos de umbral simple, manteniendo la simplicidad operativa.
    
    **Tu tarea:** Escribe un párrafo que describa brevemente cómo tu propuesta se diferencia de las alternativas existentes.
    
    ---
    
    ## Fase 2: Delimitación del Proyecto
    
    Aquí es donde muchos proyectos se desvían: no definir qué **NO** van a hacer. Un proyecto bien delimitado es más fácil de ejecutar y defender.
    
    ### 2.1 Alcance geográfico y temporal
    
    | Dimensión | Preguntas a responder |
    | --- | --- |
    | **Geográfica** | ¿Una ubicación fija? ¿Múltiples ubicaciones? ¿Datos reales de tu región o dataset público? |
    | **Temporal** | ¿Qué horizonte de predicción buscas? (15 min, 1 hora, 6 horas) |
    | **Estacional** | ¿Datos de todas las estaciones o solo tormentas de verano? |
    
    **Recomendación:** Empieza con **una ubicación fija y horizonte corto (15-30 minutos)** . Esto reduce la complejidad y te permite demostrar concepto.
    
    **Tu tarea:** Define claramente los límites geográficos y temporales de tu experimento.
    
    ### 2.2 Alcance tecnológico
    
    | Componente | Decisión a tomar |
    | --- | --- |
    | **Sensores** | ¿Simularás datos o usarás sensores reales (Raspberry Pi + sensores económicos)? |
    | **Modelo LIF** | ¿Neurona única o red pequeña? ¿Qué parámetros (tau_membrana, umbral, reinicio)? |
    | **Baseline** | ¿Contra qué compararás tu modelo? (ej. umbral fijo de presión, media móvil) |
    | **Implementación** | ¿Python puro? ¿Usarás snnTorch/Norse? |
    
    **Recomendación para tu hardware (GT 1030, Ryzen 3400G):** Una neurona LIF en Python puro es perfectamente viable y te permite mantener el control total sobre los parámetros. Puedes simular los sensores con datos públicos del Servicio Meteorológico Nacional (SMN) o usar datasets abiertos (ej. NOAA, Meteostat).
    
    **Tu tarea:** Define la pila tecnológica que usarás y justifica por qué es adecuada para tu objetivo.
    
    ### 2.3 Limitaciones explícitas (lo que NO harás)
    
    Declarar limitaciones no es una debilidad — es una muestra de honestidad académica y te protege de críticas sobre lo que no cubriste.
    
    **Limitaciones a considerar:**
    
    - No se realizará predicción de largo plazo (>2 horas)
    - No se incluirán datos satelitales (solo sensores terrestres)
    - No se entrenará una red multicapa compleja (solo neurona única)
    - No se implementará en hardware embebido real (solo simulación)
    - No se incluirán todos los tipos de tormenta (solo tormentas convectivas de verano)
    - No se optimizará para latencia extrema
    
    **Tu tarea:** Redacta una lista de 4-6 limitaciones explícitas de tu proyecto.
    
    ---
    
    ## Fase 3: Preparación de la Propuesta para CNEISI
    
    Un paper necesita estructura. Para empezar a escribir, necesitas tener claras al menos **cuatro secciones fundamentales**.
    
    ### 3.1 Resumen (Abstract)
    
    Redacta un párrafo inicial de prueba. Debe incluir: contexto/problema, enfoque propuesto, método, resultados esperados, contribución.
    
    **Plantilla:**
    
    > "La detección temprana de tormentas locales sigue siendo un desafío en zonas con recursos limitados, donde los sistemas comerciales son costosos y los métodos de umbral simple producen altas tasas de falsas alarmas. Este trabajo propone un sistema de alerta temprana de bajo costo basado en un modelo de neurona LIF (Leaky Integrate-and-Fire) simplificado, aplicado como detector de anomalías en series temporales de variables atmosféricas (presión, temperatura, humedad). A diferencia de las redes neuronales tradicionales, el modelo LIF procesa datos de forma event-driven, lo que permite un cómputo eficiente en hardware de gama baja. Se simulará el modelo utilizando datos del SMN [o dataset específico] y se comparará su tasa de detección y falsos positivos contra un baseline de umbrales fijos. Se espera demostrar que el enfoque LIF reduce significativamente las falsas alarmas manteniendo una sensibilidad competitiva, validando su viabilidad como base para sistemas de alerta descentralizados y de bajo costo."
    > 
    
    ### 3.2 Metodología (diseño experimental)
    
    Define paso a paso cómo ejecutarás tu experimento:
    
    | Paso | Qué debes definir |
    | --- | --- |
    | **1. Adquisición de datos** | ¿De dónde obtienes los datos? ¿Qué variables usas? ¿Frecuencia de muestreo? |
    | **2. Preprocesamiento** | Normalización, detección de outliers, ventanas temporales |
    | **3. Definición del modelo LIF** | Ecuación de membrana, parámetros, cómo se codifica la entrada a spikes |
    | **4. Definición del baseline** | ¿Qué regla de umbral usarás para comparar? |
    | **5. Protocolo de evaluación** | ¿Cómo medirás éxito? ¿Qué métricas? (precisión, recall, F1, tasa de falsos positivos) |
    
    **Tu tarea:** Escribe un borrador de los 5 pasos anteriores, con el nivel de detalle que te permita empezar a programar.
    
    ### 3.3 Resultados esperados
    
    En un proyecto de investigación, no tienes que tener los resultados antes de proponerlo. Pero sí debes tener **expectativas fundamentadas** sobre lo que encontrarás.
    
    **Ejemplo de resultados esperados:**
    
    > "Se espera que el modelo LIF alcance una tasa de falsos positivos ≤ 15% para el conjunto de datos de prueba, significativamente inferior a la del baseline de umbral fijo (estimada en 30-40%). En cuanto a sensibilidad (tasa de tormentas detectadas), se espera que el modelo LIF se mantenga en rangos aceptables (≥ 80%). La principal ventaja esperada será la reducción de alarmas espurias, no necesariamente una mejora en la detección pura."
    > 
    
    ### 3.4 Plan de trabajo
    
    Define un cronograma tentativo. Para un proyecto de 2-3 meses:
    
    | Semana | Actividad |
    | --- | --- |
    | 1-2 | Obtención y exploración de datos |
    | 3-4 | Implementación del baseline (umbral fijo) |
    | 5-6 | Implementación del modelo LIF |
    | 7-8 | Experimentación y ajuste de parámetros |
    | 9 | Análisis de resultados y documentación |
    | 10-12 | Redacción del paper |
    
    ---
    
    ## Checklist de preguntas críticas (antes de empezar a codificar)
    
    Para consolidar tu propuesta, asegúrate de poder responder **afirmativamente** estas preguntas:
    
    | # | Pregunta | ¿Puedes responderla? |
    | --- | --- | --- |
    | 1 | ¿Tienes acceso a datos climáticos históricos (públicos o propios) que incluyan tormentas documentadas? |  |
    | 2 | ¿Has definido qué constituye "tormenta" en tu experimento (condición umbral de variables)? |  |
    | 3 | ¿Conoces la ecuación del modelo LIF y puedes implementarla en Python? |  |
    | 4 | ¿Has decidido cómo codificarás la entrada continua (presión, temp, humedad) a spikes? |  |
    | 5 | ¿Tienes un baseline claro para comparar? |  |
    | 6 | ¿Has identificado una métrica de éxito principal (ej. F1 score, tasa de falsos positivos)? |  |
    | 7 | ¿Tu hardware puede ejecutar las simulaciones necesarias? |  |
    | 8 | ¿Has identificado qué NO vas a hacer (limitaciones explícitas)? |  |
    | 9 | ¿Tienes un plan B si el modelo LIF no supera al baseline? (¿qué contribución ofreces entonces?) |  |
    | 10 | ¿Puedes explicar tu proyecto en 2 minutos a un compañero y que entienda qué aporta? |  |
    
    ---
    
    ## Conclusión: El esqueleto de tu propuesta
    
    Tu propuesta completa debe contener, en este orden:
    
    1. **Título tentativo** (que refleje tu pregunta de investigación)
    2. **Resumen** (contexto, enfoque, método, contribución)
    3. **Introducción y motivación** (por qué es importante el problema)
    4. **Estado del arte breve** (qué se ha hecho, qué falta)
    5. **Pregunta de investigación** (concreta, específica)
    6. **Metodología** (pasos detallados)
    7. **Resultados esperados** (hipótesis fundamentada)
    8. **Limitaciones** (lo que no se aborda)
    9. **Plan de trabajo** (cronograma)
    10. **Referencias iniciales** (3-5 fuentes clave)
    
    Con esto, tienes una base sólida para empezar a codificar sabiendo exactamente **qué** estás probando y **por qué**. Ya no estarás "dando vueltas" — estarás ejecutando un plan con propósito definido.
    
    **¿Por cuál de estas secciones quieres empezar a trabajar concretamente?** Podemos redactar juntos el título, refinar la pregunta, o definir la metodología paso a paso.
    
    ## Introducción: El momento de pasar de la idea al planteamiento
    
    Has dado con una idea que tiene potencial real de convertirse en un trabajo de investigación sólido. El desafío ahora es dejar de "dar vueltas alrededor de la idea" y empezar a construir una propuesta concreta, con límites claros, fundamentos sólidos y un plan viable.
    
    Lo que buscas es exactamente esto: una base completa sobre la cual construir. Vamos a estructurarlo en **tres fases progresivas**:
    
    1. **Formalización de la idea de investigación** (¿qué vas a investigar realmente?)
    2. **Delimitación del proyecto** (¿dónde empieza y dónde termina tu trabajo?)
    3. **Preparación de la propuesta para CNEISI** (lo mínimo que necesitas tener definido antes de escribir una línea de código)
    
    Cada fase incluye **preguntas guía, decisiones concretas y una plantilla para que completes**.
    
    ---
    
    ## Fase 1: Formalización de la Idea de Investigación
    
    Tu idea base está clara: usar un modelo LIF (Leaky Integrate-and-Fire) simplificado para detectar tormentas locales con bajo costo. Ahora hay que convertir esa idea general en una **pregunta de investigación precisa**, respaldada por un **estado del arte** que justifique por qué vale la pena explorarla.
    
    ### 1.1 Definir la pregunta de investigación
    
    Una buena pregunta de investigación debe ser **específica, respondible empíricamente y no trivial**. Tu pregunta actual es:
    
    > "¿Se puede predecir tormentas locales con un modelo LIF simplificado?"
    > 
    
    Esta pregunta es demasiado abierta. Te propongo refinarla en una dirección más concreta:
    
    > **Pregunta propuesta:** "¿Es posible detectar patrones de tormenta local en datos de sensores de bajo costo utilizando un modelo de neurona LIF como detector de anomalías temporal, logrando una tasa de falsos positivos inferior a los métodos tradicionales basados en umbrales fijos?"
    > 
    
    **¿Por qué esta formulación?**
    
    | Componente | Qué aporta |
    | --- | --- |
    | "detectar patrones de tormenta" | Acota a detección (no predicción a largo plazo) |
    | "datos de sensores de bajo costo" | Define el dominio operativo |
    | "modelo LIF como detector de anomalías" | Especifica el mecanismo concreto |
    | "tasa de falsos positivos inferior a umbrales fijos" | Define la métrica de éxito y el baseline de comparación |
    
    **Tu tarea:** Escribe tu propia pregunta de investigación. Puedes empezar desde esta propuesta y ajustarla a lo que realmente quieras responder.
    
    ### 1.2 Fundamentar por qué LIF es relevante
    
    Para un paper académico, no basta con decir "uso LIF porque es bioinspirado". Necesitas mostrar que hay una **base teórica y resultados previos** que respaldan su idoneidad para este tipo de problema.
    
    **Lo que la investigación actual dice sobre SNN y detección de anomalías:**
    
    | Hallazgo Clave | Fuente |
    | --- | --- |
    | Las SNN capturan cambios en señales temporales y reducen consumo de recursos en comparación con ANN, aunque tradicionalmente sacrifican algo de rendimiento | Zhang et al. (2025) |
    | Modelos híbridos spiking con codificación de frecuencia de primer spike alcanzan rendimiento superior en detección de anomalías con **5.04× menor consumo energético** que su equivalente ANN | Zhang et al. (2025) |
    | El modelo LIF ha sido aplicado exitosamente a forecasting de series temporales ambientales (irradiancia solar) | Alharbi & Ahmed, IEEE Access (2024) |
    | La versión cuántica QLIF (Quantum Leaky Integrate-and-Fire) ha demostrado mejoras del **15.4% en MSE** y convergencia hasta **94% más rápida** para forecasting climático | Marchisio et al., arXiv (mayo 2026) |
    
    **Lo que esto significa para tu propuesta:** Tu enfoque no es "inventar algo nuevo", sino **aplicar una técnica que ya ha mostrado ventajas en dominios similares a un problema concreto** (tormentas locales), con un giro original: usar una versión simplificada (una neurona) y evaluar su eficacia vs. un baseline sencillo. Esto es perfectamente válido para un congreso estudiantil.
    
    **Tu tarea:** Resume en 3-5 líneas por qué el modelo LIF es una opción pertinente para tu problema.
    
    ### 1.3 Definir la contribución esperada
    
    Un buen proyecto de investigación no solo "hace algo", sino que **aporta algo** al conocimiento o a la práctica. Tu contribución podría ser:
    
    | Tipo de Contribución | Posible enunciado |
    | --- | --- |
    | **Metodológica** | Mostrar cómo adaptar un modelo LIF para detección de anomalías en datos climáticos de bajo costo |
    | **Empírica** | Generar evidencia comparativa (LIF vs umbral fijo) en un dominio específico (tormentas locales) |
    | **Práctica** | Demostrar la viabilidad técnica de un sistema de alerta de bajo costo implementable en hardware de gama baja |
    
    **Tu tarea:** Define cuál será la principal contribución de tu trabajo. Sé honesto con el alcance: para un proyecto de primer año, la contribución práctica y la evidencia empírica son los caminos más realistas.
    
    ### 1.4 Contextualizar vs. métodos existentes
    
    Para que tu trabajo tenga "originalidad acotada" (como exige el CNEISI), necesitas mostrar que tu propuesta se diferencia de lo que ya existe.
    
    **Alternativas existentes en el mercado/sector:**
    
    | Alternativa | Fortalezas | Debilidades |
    | --- | --- | --- |
    | Estaciones meteorológicas comerciales (Davis, Oregon Scientific) | Precisión, confiabilidad | Costo elevado (>USD 500) |
    | Datos satelitales + IA (ECMWF AIFS, modelos ML) | Gran cobertura geográfica, alta precisión | Infraestructura masiva, no localizable |
    | Métodos de umbral fijo (ej. "alerta si presión baja 5 hPa") | Simple, bajo costo | Altas tasas de falsas alarmas |
    
    **Tu diferenciación:** Un sistema de bajo costo que utiliza un modelo bioinspirado para reducir falsas alarmas en comparación con métodos de umbral simple, manteniendo la simplicidad operativa.
    
    **Tu tarea:** Escribe un párrafo que describa brevemente cómo tu propuesta se diferencia de las alternativas existentes.
    
    ---
    
    ## Fase 2: Delimitación del Proyecto
    
    Aquí es donde muchos proyectos se desvían: no definir qué **NO** van a hacer. Un proyecto bien delimitado es más fácil de ejecutar y defender.
    
    ### 2.1 Alcance geográfico y temporal
    
    | Dimensión | Preguntas a responder |
    | --- | --- |
    | **Geográfica** | ¿Una ubicación fija? ¿Múltiples ubicaciones? ¿Datos reales de tu región o dataset público? |
    | **Temporal** | ¿Qué horizonte de predicción buscas? (15 min, 1 hora, 6 horas) |
    | **Estacional** | ¿Datos de todas las estaciones o solo tormentas de verano? |
    
    **Recomendación:** Empieza con **una ubicación fija y horizonte corto (15-30 minutos)** . Esto reduce la complejidad y te permite demostrar concepto.
    
    **Tu tarea:** Define claramente los límites geográficos y temporales de tu experimento.
    
    ### 2.2 Alcance tecnológico
    
    | Componente | Decisión a tomar |
    | --- | --- |
    | **Sensores** | ¿Simularás datos o usarás sensores reales (Raspberry Pi + sensores económicos)? |
    | **Modelo LIF** | ¿Neurona única o red pequeña? ¿Qué parámetros (tau_membrana, umbral, reinicio)? |
    | **Baseline** | ¿Contra qué compararás tu modelo? (ej. umbral fijo de presión, media móvil) |
    | **Implementación** | ¿Python puro? ¿Usarás snnTorch/Norse? |
    
    **Recomendación para tu hardware (GT 1030, Ryzen 3400G):** Una neurona LIF en Python puro es perfectamente viable y te permite mantener el control total sobre los parámetros. Puedes simular los sensores con datos públicos del Servicio Meteorológico Nacional (SMN) o usar datasets abiertos (ej. NOAA, Meteostat).
    
    **Tu tarea:** Define la pila tecnológica que usarás y justifica por qué es adecuada para tu objetivo.
    
    ### 2.3 Limitaciones explícitas (lo que NO harás)
    
    Declarar limitaciones no es una debilidad — es una muestra de honestidad académica y te protege de críticas sobre lo que no cubriste.
    
    **Limitaciones a considerar:**
    
    - No se realizará predicción de largo plazo (>2 horas)
    - No se incluirán datos satelitales (solo sensores terrestres)
    - No se entrenará una red multicapa compleja (solo neurona única)
    - No se implementará en hardware embebido real (solo simulación)
    - No se incluirán todos los tipos de tormenta (solo tormentas convectivas de verano)
    - No se optimizará para latencia extrema
    
    **Tu tarea:** Redacta una lista de 4-6 limitaciones explícitas de tu proyecto.
    
    ---
    
    ## Fase 3: Preparación de la Propuesta para CNEISI
    
    Un paper necesita estructura. Para empezar a escribir, necesitas tener claras al menos **cuatro secciones fundamentales**.
    
    ### 3.1 Resumen (Abstract)
    
    Redacta un párrafo inicial de prueba. Debe incluir: contexto/problema, enfoque propuesto, método, resultados esperados, contribución.
    
    **Plantilla:**
    
    > "La detección temprana de tormentas locales sigue siendo un desafío en zonas con recursos limitados, donde los sistemas comerciales son costosos y los métodos de umbral simple producen altas tasas de falsas alarmas. Este trabajo propone un sistema de alerta temprana de bajo costo basado en un modelo de neurona LIF (Leaky Integrate-and-Fire) simplificado, aplicado como detector de anomalías en series temporales de variables atmosféricas (presión, temperatura, humedad). A diferencia de las redes neuronales tradicionales, el modelo LIF procesa datos de forma event-driven, lo que permite un cómputo eficiente en hardware de gama baja. Se simulará el modelo utilizando datos del SMN [o dataset específico] y se comparará su tasa de detección y falsos positivos contra un baseline de umbrales fijos. Se espera demostrar que el enfoque LIF reduce significativamente las falsas alarmas manteniendo una sensibilidad competitiva, validando su viabilidad como base para sistemas de alerta descentralizados y de bajo costo."
    > 
    
    ### 3.2 Metodología (diseño experimental)
    
    Define paso a paso cómo ejecutarás tu experimento:
    
    | Paso | Qué debes definir |
    | --- | --- |
    | **1. Adquisición de datos** | ¿De dónde obtienes los datos? ¿Qué variables usas? ¿Frecuencia de muestreo? |
    | **2. Preprocesamiento** | Normalización, detección de outliers, ventanas temporales |
    | **3. Definición del modelo LIF** | Ecuación de membrana, parámetros, cómo se codifica la entrada a spikes |
    | **4. Definición del baseline** | ¿Qué regla de umbral usarás para comparar? |
    | **5. Protocolo de evaluación** | ¿Cómo medirás éxito? ¿Qué métricas? (precisión, recall, F1, tasa de falsos positivos) |
    
    **Tu tarea:** Escribe un borrador de los 5 pasos anteriores, con el nivel de detalle que te permita empezar a programar.
    
    ### 3.3 Resultados esperados
    
    En un proyecto de investigación, no tienes que tener los resultados antes de proponerlo. Pero sí debes tener **expectativas fundamentadas** sobre lo que encontrarás.
    
    **Ejemplo de resultados esperados:**
    
    > "Se espera que el modelo LIF alcance una tasa de falsos positivos ≤ 15% para el conjunto de datos de prueba, significativamente inferior a la del baseline de umbral fijo (estimada en 30-40%). En cuanto a sensibilidad (tasa de tormentas detectadas), se espera que el modelo LIF se mantenga en rangos aceptables (≥ 80%). La principal ventaja esperada será la reducción de alarmas espurias, no necesariamente una mejora en la detección pura."
    > 
    
    ### 3.4 Plan de trabajo
    
    Define un cronograma tentativo. Para un proyecto de 2-3 meses:
    
    | Semana | Actividad |
    | --- | --- |
    | 1-2 | Obtención y exploración de datos |
    | 3-4 | Implementación del baseline (umbral fijo) |
    | 5-6 | Implementación del modelo LIF |
    | 7-8 | Experimentación y ajuste de parámetros |
    | 9 | Análisis de resultados y documentación |
    | 10-12 | Redacción del paper |
    
    ---
    
    ## Checklist de preguntas críticas (antes de empezar a codificar)
    
    Para consolidar tu propuesta, asegúrate de poder responder **afirmativamente** estas preguntas:
    
    | # | Pregunta | ¿Puedes responderla? |
    | --- | --- | --- |
    | 1 | ¿Tienes acceso a datos climáticos históricos (públicos o propios) que incluyan tormentas documentadas? |  |
    | 2 | ¿Has definido qué constituye "tormenta" en tu experimento (condición umbral de variables)? |  |
    | 3 | ¿Conoces la ecuación del modelo LIF y puedes implementarla en Python? |  |
    | 4 | ¿Has decidido cómo codificarás la entrada continua (presión, temp, humedad) a spikes? |  |
    | 5 | ¿Tienes un baseline claro para comparar? |  |
    | 6 | ¿Has identificado una métrica de éxito principal (ej. F1 score, tasa de falsos positivos)? |  |
    | 7 | ¿Tu hardware puede ejecutar las simulaciones necesarias? |  |
    | 8 | ¿Has identificado qué NO vas a hacer (limitaciones explícitas)? |  |
    | 9 | ¿Tienes un plan B si el modelo LIF no supera al baseline? (¿qué contribución ofreces entonces?) |  |
    | 10 | ¿Puedes explicar tu proyecto en 2 minutos a un compañero y que entienda qué aporta? |  |
    
    ---
    
    ## Conclusión: El esqueleto de tu propuesta
    
    Tu propuesta completa debe contener, en este orden:
    
    1. **Título tentativo** (que refleje tu pregunta de investigación)
    2. **Resumen** (contexto, enfoque, método, contribución)
    3. **Introducción y motivación** (por qué es importante el problema)
    4. **Estado del arte breve** (qué se ha hecho, qué falta)
    5. **Pregunta de investigación** (concreta, específica)
    6. **Metodología** (pasos detallados)
    7. **Resultados esperados** (hipótesis fundamentada)
    8. **Limitaciones** (lo que no se aborda)
    9. **Plan de trabajo** (cronograma)
    10. **Referencias iniciales** (3-5 fuentes clave)
    
    Con esto, tienes una base sólida para empezar a codificar sabiendo exactamente **qué** estás probando y **por qué**. Ya no estarás "dando vueltas" — estarás ejecutando un plan con propósito definido.
    
    **¿Por cuál de estas secciones quieres empezar a trabajar concretamente?** Podemos redactar juntos el título, refinar la pregunta, o definir la metodología paso a paso.
    

Se habla de un trabajo e investigacion.

Para plantear la base debemos responder 3 preguntas fundamentales, que van a ir dando forma al trabajo a realizar:

1. **Formalización de la idea de investigación** (¿qué vas a investigar realmente?)
2. **Delimitación del proyecto** (¿dónde empieza y dónde termina tu trabajo?)
3. **Preparación de la propuesta para CNEISI** (lo mínimo que necesitas tener definido antes de escribir una línea de código)

# Entrega del PAPER: 28/08/26

[Pendiente](ModeloLIF-DeteccionLluvia/Pendiente%2038b3a6e010e380cd92c1f7b943230814.csv)

## **1) PREGUNTA DE INVESTIGACION**

Se divide en 2 frentes diferentes:

- **Pregunta:** Se propone una pregunta de investigacion para constestar. Permitiendo una respuesta concreta y/o comparativa.
- **Desarrollo:** Se propone directamente el modelo a realizar, con su correspondiente analisis de efectividad.

1. Una buena pregunta de investigación debe ser **específica, respondible empíricamente y no trivial**.
    
    puntos fundamentales que quiero abacar con esta investigacion:
    
    - Deteccion de eventos de lluvia locales (deteccion de patrones del evento).
    - Sistemas de Alerta Temprana (busca aclarar el rango de tiempo a funcionar).
    - Utilizacion del modelo LIF simplificado.
    - Comparacion de falsos positivos con un modelo tradicional de umbrales fijos.
    
    Una vez detectado los puntos fundamentales a tratar podemos formular una pregunta consisa.
    
    - **Analisis de preguntas.**
        - **¿Puede un modelo matematico LIF simplificado detectar patrones de tormentas locales para la deteccion de anomalias temorales mediante datos provenientes de sensores de bajo costo, produciendo una menor tasa de falsos positivos a comparacion de un modelo tradicional basado en umbrales fijos?**
        
        **¿Porque esta pregunta es valida?**
        
        | **Frase** | **Aporte** |
        | --- | --- |
        | modelo matematico LIF simplificado | Impone el modelo matematico que se utilizara. |
        | detectar patrones de tormentas locales para la deteccion de anomalias temporales | Impone el objetivo para el modelo matematico. |
        | datos provenientes de sensores a bajo costo | Indicar el origen de los datos evaluados. |
        | produciendo una menor tasa de falsos positivos a comparacion de un modelo tradicional basado en umbrales fijos | Impone la metrica de exito junto a la comparacion fundamental de la investigacion. |
        
        **Reformulacion y intercambio de terminos:**
        
        - **¿Puede un modelo matematico LIF simplificado funcionar como un componente de un sistema de Alerta Temprana para tormentas mediante patrones climaticos locales, produciendo una menor tasa de falsos positivos a comparacion de un modelo tradicional basado en umbrales fijos?**
        
        | **Frase** | **Aporte** |
        | --- | --- |
        | modelo matematico LIF simplificado | Modelo matematico que se utilizara. |
        | **funcionar como un sistema de Alerta Temprana parcial para tormentas detecando patrones climaticos locales** | Objetivo de uso del modelo matematico LIF simplificado. Con aclaracion de cubrir “parcialmente” a un sistema de alerta temprana, centrandose en el pilar 2. |
        | produciendo una menor tasa de falsos positivos a comparacion de un modelo tradicional basado en umbrales fijos | Metrica de exito y comparacion fundamental de la investigacion. |
    - **Pregunta candidata: Analisis.**
        
        Reformulacion y correciones de errores, redundancia u ambiguedad:
        
        **Pregunta concreta y completa:**
        
        #### **¿Es un modelo LIF (Leaky Integrate-and-Fire) simplificado superior a un modelo de umbrales fijos tradicional en la deteccion de eventos de lluvia locales con al menos 30 minutos de anticiapacion, con una tasa de falsos positivos menor sin sacrificar sensibilidad?**
        
        - **Otras propuestas candidatas:**
            - ¿Puede un modelo LIF (Leaky Integrate-and-Fire) simplificado lograr una tasa de falsos positivos menor que un sistema de umbrales fijos, sin sacrificar sensibilidad en la deteccion de eventos de lluvia locales con al menos 30 minutos de anticipacion?
            - Comparacion modelo LIF (Leaky Integrate-and-Fire) simplificado con un modelo tradicional de umbrales fijos para la dereccion de eventos de lluvia locales.
            - Modelo matematico LIF (Leaky Integrate-and-Fire) para la prediccion de eventos de lluvia locales.
        
        | Frase | Aporte |
        | --- | --- |
        | **modelo LIF (Leaky Integrate-and-Fire) simplificado** | Modelo propuesto |
        | **tasa de falsos positivos menor que un sistema de umbrales fijos** | Punto de comparacion principal propuesto |
        | **sin sacrificar sensibilidad** | Aclaracion de sistema util |
        | **deteccion de** eventos de lluvia | Proposito de los modelos |
        | **con al menos 30 minutos de anticipacion** | especifica el tiempo minimo para la prediccion |
        
        #### **Puntos fundamentales de la pregunta propuesta:**
        
        - Esta pregunta permite esbosar el **tema fundamental** a tratar, planteando la principal comparacion con los modelos tradicionales utilizados basados en umbrales fijos, con un modelo dinamico basado en el modelo matematico simplificado: LIF.
        - La pregunta plantea la **metrica de exito** principal a evaluar, la cual es la tasa de falsos positivos en la deteccion de patrones climaticos locales de tormentas.
        - Esta investigacion busca **contestar** si el modelo matematico LIF simplificado es una alternativa superior a modelos tradicionales basados en umbrales fijos para la prediccion temprana de tormentas locales. (Los falsos positivos son el principal problema de las SAT).

### ¿Que se quiere lograr con la investigacion? - Puntos fundamentales

- Determinar si un modelo matematico LIF simplificado tiene la capacidad de predecir tormentas de forma fiable.
- Comparar si el modelo es capaz de predecir tormentas de forma mas efectiva que un modelo por umbrales fijos tradicional.
    - Investigar y adaptar un modelo LIF simplificado (UTILIZAR un concepto ya expandido y probado).
    - Investigar y recolectar datos de eventos de lluvia locales.
    - Investigar y obtener modelos tradicionales de umbrales fijos para la comparacion.

### **Hipótesis**

El modelo LIF es más preciso que el umbral fijo, generando una menor cantidad de falsos positivos en alertas de tormentas (porque tiene memoria temporal y decaimiento, puede distinguir entre una lectura aislada y una tendencia acumulada), pero más simple que un modelo de ML completo.

### Contribucion de la investigacion:

Esta investigacion aporta de las siguietes maneras:

| Tipo de Contribución | Enunciado |
| --- | --- |
| **Metodológica** | Mostrar cómo adaptar un modelo LIF para detección de anomalías en datos climáticos para eventos de lluvia. |
| **Empírica** | Generar evidencia comparativa (LIF vs umbral fijo) en un dominio específico (Eventos de lluvia locales) |
| **Práctica** | Demostrar la viabilidad técnica de un sistema de alerta de bajo costo implementable en hardware simple determinado como sensores de tierra que miden humedad, temperatura, presion y un sensor de viento Mecánico. |

---

## 2) INVESTIGACION DE BIBLIOGRAFIA: Justificar sobre la utilizacion del modelo LIF: Anexos

- Determinan las investigaciones previas que certifican los fundamentos para la utilizacion efectiva del modelo matematico LIF.
    - Se determinan las investigaciones que certifican el porque el modelo matematico LIF resulta ultil, efectivo y aplicable.
- Determinar evento a predecir (evento de lluvia).
    - Investigacion en diversas fuentes sobre las definicion concreta del evento y factores con sus variables esenciales para predecirlo.
- Determinar modelo comparativo (umbrales fijos).

---

### **Sintesis de Conceptos basicos del modelo:**

#### **Conceptos basicos:**

- **SNN:** Se refiere a redes neuronales pico, aqui la informacion se representa mediante trenes de pulsos discretos de tiempo, donde justamente esta variable (el tiempo) permite representar la informacion al variar en el envio de los pulsos. Su forma de comunicacion es similar a como se comunica las neuronas biologicas
- **ANN:** Hace referencia a las redes neuronales artificiales, las cuales se representan mediante activaciones continuas, su escructura consiste en nodos conectados entre diferentes capas (entrada-oculta/proceso-salida). Aprenden mediante ajustar los pesos de sus conexiones entre ellas.
- **Generaciones: Existen 3 generaciones: segun Maass (1997)**
    - **Primera:** Señal estatica, utilizada en funciones booleanas.
    - **Segunda:** Valor continuo sin temporalidad, aproximador universal de funciones.
    - **Tercera:** Pulsos binarios con temporalidad incluida, mas potente que la segunda generacion con menos neuronas.

#### **¿En que consiste el modelo planteado? Contexto del modelo.**

- Las Spiking Neural Networks (SNN) representan la tercera generación de redes neuronales, inspiradas directamente en el funcionamiento del cerebro biológico. A diferencia de las ANN tradicionales que procesan valores continuos (segunda generacion, tranformer y gpt), las SNN operan mediante **eventos discretos llamados "spikes" (picos o pulsos)**.

#### **¿Como funciona? Concepto del modelo matematico.**

- El modelo más utilizado en SNN es el **LIF (Leaky Integrate-and-Fire),** el cual utilizare en esta investigacion de forma simplificada, permite simular el comportamiento de una neurona biológica en tres etapas:
    - **Integrate (Integración)**: Cuando recibe spikes de entrada, el potencial de membrana aumenta.
    - **Leaky (Fuga)**: Con el tiempo, el potencial se "filtra" (decae) si no hay estímulos.
    - **Fire (Disparo)**: Si el potencial supera un umbral, la neurona emite un spike y el potencial se reinicia.
- Esta dinámica temporal permite a las SNN procesar naturalmente información con componente temporal, a diferencia de las ANN que requieren mecanismos adicionales como positional encoding, ya que procesan todo al mismo tiempo, y necesitan un mecanismo que les permita simular de forma artificial el **orden temporal**.
- La neurona LIF en particular es matemáticamente un detector de cambios para procesos de Poisson compuestos.
- La neurona solo se activa cuando recibe los suficientes pulsos para generar un spike, permitiendo que este gasto de energia sea utilizado solo cuando sea completamente necesario.

#### **¿Como se aplica? Estructural y matematicamente.**

- Las redes SNN no son un simple encadenamiento de neuronas LIF, sino que tiene una estructura compleja que las sostiene.
    
    **Componentes estructurales:**
    
    - **Capa de entrada / codificación:** convierte datos del mundo real (señales continuas, imágenes, series temporales) en trenes de spikes.
    - **Neuronas LIF (u otras variantes):** integran spikes entrantes, decaen, y disparan cuando alcanzan el umbral. Cada conexión sináptica tiene un peso w_ij que pondera el spike recibido.
    - **Sinapsis con dinámica temporal:** los spikes no se transmiten instantáneamente — la corriente sináptica tiene su propia constante de tiempo τ_s que determina cuánto dura el efecto de cada spike en el potencial postsináptico.
    - **Capa de salida / decodificación:** convierte el tren de spikes de salida en una decisión o valor. Las dos estrategias principales son contar spikes en una ventana temporal (rate decoding) o medir el tiempo al primer spike (temporal decoding).
- **La ecuación fundamental del LIF**
    - El modelo LIF moderno (Gerstner et al., 2014) se describe con una EDO de primer orden lineal. Esta es la ecuación central de todo el campo:
    τ_m · (dV/dt) = -(V(t) - V_rest) + R · I(t)
    - Con condición de disparo y reset:
    Si V(t) ≥ V_threshold → emite spike → V(t) := V_reset
- **Descripcion de los valores:**
    
    ![image.png](ModeloLIF-DeteccionLluvia/image%201.png)
    
- **Período refractario y período de gracia**
    - Tras emitir un spike, la neurona biológica entra en un período refractario durante el cual no puede disparar de nuevo, independientemente de la corriente entrante. El período refractario absoluto (~2ms en neuronas biológicas) previene que una neurona dispare dos spikes tan seguidos que sean indistinguibles. El período refractario relativo (varios ms) aumenta el umbral temporalmente, haciendo más difícil el disparo.
    En implementaciones de software, se modela con un contador de pasos post-spike durante el cual V se fija en V_reset sin procesar entradas
- **Variabilidad neuronal: Diferencia con el modelo simplificado (determinisitico)**
    - Una neurona biológica real no dispara con intervalos perfectamente regulares bajo corriente constante — exhibe variabilidad estocástica. Stein (1965) propone modelar la actividad de picos como un proceso puntual con corriente de entrada aleatoria, analizando la distribución de intervalos entre spikes (ISI). Stein (1967) extiende esto a modelos con múltiples fuentes de ruido. Gerstein y Mandelbrot (1964) proponen el 'random walk model': el potencial de membrana realiza una caminata aleatoria hasta cruzar el umbral — el primer modelo estocástico de actividad neuronal.
    - Estos trabajos hablan sobre la diferencia entre las neuronas biologicas, y su naturaleza estocastica y probabilistica, por eso implementando ruido a la señal generada, se busca lograr una mayor robustez en el modelo ante pequeñas fluctuaciones, y volviendolo mas resiliente por esa caracteristica probabilistica.
    - El **modelo** **LIF** planteado para esta **investigacion** sera **deterministico**, osea no se le añadira **ruido** a la lectura debido a su **formato simplificado.**

#### **¿En que resulta util o diferente en este caso? Justificacion de la utilizacion.**

- **Eficiencia energetica:**
    - En una ANN densa, todas las neuronas computan en cada paso de tiempo, independientemente de si hay señal. En una SNN, una neurona solo 'gasta energía' cuando recibe o emite un spike. En señales esparsas (como datos de sensores en reposo), la actividad de spikes es muy baja, y el consumo energético cae proporcionalmente. Los papers de hardware (Loihi, TrueNorth, Xylo) reportan reducciones de 1 a 3 órdenes de magnitud en consumo respecto a GPU equivalente.
- **Codificación de información en spikes:**
    - Para representar una señal continua (temperatura, presion, etc…) como un “tren” de spikes es el problema fundamental en estos modelos. Por eso se exponen diferentes enfoqus posibles:
    - Tabla:
        
        ![image.png](ModeloLIF-DeteccionLluvia/image%202.png)
        
- Existen otros modelos aparte de LIF, sin embargo este es el que permite representar de forma solida y eficiente las señales necesarias, sin agregar complejidad extra innecesaria al modelo.
    
    ![image.png](ModeloLIF-DeteccionLluvia/image%203.png)
    
- **No necesita entrenamiento exaustivo.**
    - Si bien se necesita una serie de pruebas para determinar el valor ideal para las variables del modelo, no se realizara un entrenamiento exaustivo como el “Surrogate Gradient Learning”, los valores de las variables utilizadas se ajustaran manualmente o por “grid search”, debido a la simplicidad del modelo. El paper de Maass (1997) permite explicar el potencial computacional y capacidad subyacente de este modelo sin necesitar entrenamiento previo.

#### Definicion del modelo a utilizar

- El modelo es un LIF de una sola neurona con parámetros fijos (deterministico), sin aprendizaje, implementado en Python, usando rate coding (frecuencia de disparo) implícito. Esto es exactamente lo que EONS y Vacuum Spiker usan como arquitectura mínima para detección binaria en series temporales. 
La diferencia original del trabajo es el dominio de aplicación (variables climáticas argentinas del SMN) y la comparación directa contra un detector de umbral estático como punto de partida para la evaluacion.
- **Tabla comparativa:**

![image.png](ModeloLIF-DeteccionLluvia/image%204.png)

---

### Sinstesis del evento y modelo comparativo.

#### Qué son los modelos de umbral fijo

Un Sistema de umbral fijo de alertas para tormentas/eventos de lluvia funciona con una dinámica muy simple, si se dan las condiciones, lanza una alerta, sino no.

Se guían por variables meteorológicas que al identificar que cruzan un valor predeterminado impuesto, lanza la alerta.

No hay memoria, no hay contexto temporal, no hay acumulación de señales.
La implementación más común compara la tasa de caída de presión barométrica contra un umbral máximo: si ΔP actual ≥ ΔP_MAX, se activa la alarma. Si es menor, el sistema regresa a leer el sensor. 

En forma generalizada, el mismo principio aplica a temperatura, humedad, velocidad del viento y reflectividad de radar: **cada variable tiene su número, y ese número no cambia con el contexto**.
La lógica interna es exactamente esta:
```SI temperatura > T_umbral   Y humedad > H_umbral   Y presión < P_umbral ENTONCES → emitir alerta```
Cada variable se evalúa de forma independiente en el momento actual. No importa cómo llegó ahí, cuánto tiempo lleva subiendo, ni si viene de un pico aislado o de una tendencia sostenida. Eso es el problema central.

- **Medida de desempeño:**
El SMN utiliza 2 medidas clave para medir el desempeño de los modelos de prediccion utilizados.
    - **POD (Probability of Detection - Probabilidad de Detección).**
        - Mide la capacidad de un sistema para detectar correctamente un evento que sí ocurrió.
        - Se calcula como: `Aciertos / (Aciertos + Fallas)`.
    - **FAR (False Alarm Ratio - Relación de Falsas Alarmas)**:
        - Es el indicador que buscas y se define como `Falsas Alarmas / (Aciertos + Falsas Alarmas)`
        - Un FAR de 0 es perfecto (sin falsas alarmas) y de 1 es pésimo.
    - https://repositorio.smn.gob.ar/bitstream/handle/20.500.12160/3138/Nota_Tecnica_SMN_alertas_2025-204.pdf?sequence=3&isAllowed=y#6#1
    - https://repositorio.smn.gob.ar/bitstream/handle/20.500.12160/2167/Nota_Tecnica_SMN_2022-130.pdf?sequence=3&isAllowed=y#2#2
    - https://repositorio.smn.gob.ar/bitstream/handle/20.500.12160/2724/Nota_Tecnica_SMN_2024-167.pdf?sequence=1&isAllowed=y
    - https://repositorio.smn.gob.ar/bitstream/handle/20.500.12160/1723/Nota_Tecnica_SMN_2021-109.pdf?sequence=1&isAllowed=y
- La tasa de falsos positivos y las medidas de exitos propuestas varian mucho entre regiones, debido a la modificacion de variables locales utilizadas para la prediccion, como la presion, temperatura, humedad, etc…
- Los sistemas de umbral fijo siguen siendo el estándar operacional en estaciones meteorológicas locales sin cobertura de radar, especialmente en países en desarrollo. Los sistemas avanzados (WoFS ML, GenCast) requieren modelos numéricos de alta resolución, clusters de cómputo, y datos de múltiples fuentes — inaccesibles para implementaciones locales de bajo costo.
    - [https://ws2.smn.gob.ar/sites/default/files/Umbrales.pdf](https://ws2.smn.gob.ar/sites/default/files/Umbrales.pdf)

#### Como se predice un evento de lluvia

**¿Que es una evento de lluvia?**

- Un **evento de lluvia** (rainfall event) es cualquier episodio en que la precipitación líquida alcanza el suelo con una intensidad y duración medibles. La Organización Meteorológica Mundial (OMM) define la lluvia como precipitación de partículas de agua líquida con diámetro superior a 0,5 mm, o gotas más pequeñas muy dispersas (WMO, 2017). No se exige actividad eléctrica, granizo ni viento fuerte; basta la existencia de lluvia mensurable.
- Para el analisis, utilizaremos la precipitacion como nuestra metrica para determinar si se efectuo o no el evento, si sobrepasa cierto valor asignado.
- Desde el punto de vista operativo, un evento de lluvia se registra cuando:
- Un **pluviómetro** acumula una cantidad ≥ 0,2 mm (umbral común para “día de lluvia” en climatología, p. ej., OMM, 2011).
- Un observador o un sistema automático codifica **tiempo presente** como lluvia (códigos WW 20‑29, 50‑99 sin TS) o **METAR** como RA, SHRA, DZ**,** etc…

| Tipo | Mecanismo de ascenso | Nube principal | Intensidad típica |
| --- | --- | --- | --- |
| **Estratiforme** | Ascenso lento y extendido (frentes cálidos, circulaciones de gran escala) | Nimbostratus (Ns) | Continua, moderada a débil |
| **Convectiva** | Ascenso rápido y localizado (inestabilidad, calentamiento diurno) | Cumulonimbus (Cb), Cumulus congestus | Chubascos intensos, a menudo acompañados de tormenta |

Las definiciones científicas estándar (AMS, 2023; WMO, 2017) separan claramente *lluvia* (fenómeno hídrico) de *tormenta* (fenómeno eléctrico dentro de un cumulonimbus). Por tanto, **todo evento de tormenta implica lluvia (salvo tormentas secas), pero no todo evento de lluvia es tormenta**.

**Referencias:**

- **WMO. (2017). *International Cloud Atlas*.**
- **American Meteorological Society. (2023). “Rain”. *Glossary of Meteorology*.**
- **Houze, R. A. (2014). *Cloud Dynamics*. Academic Press.**

**¿De que variables depende la formacion y efectuacion de un evento de lluvia?**

- Para cualquier evento de lluvia, se necesitan tres situaciones fundamentales para su efectuacion: (Doswell et al., 1996; Houze, 2014):
1. **Humedad suficiente en la columna atmosférica** – expresada como humedad específica, razón de mezcla o punto de rocío en capas bajas y medias.
2. **Mecanismo de ascenso** – necesario para enfriar el aire y condensar el vapor.
3. **Proceso de precipitación** – formación de gotas por coalescencia (lluvia cálida) o por fase hielo (efecto Bergeron‑Findeisen) (Rogers & Yau, 1989).

Existen multiples dispositivos para medir e identificar esta variables y situaciones. Sin embargo, en este modelo utilizare los esenciales para una prediccion confiable, sin extenderse a modelos mas complejos de analisis. Se busca una prediccion “nowcasting”, de muy corto plazo (0-3 horas) utilizando sensores terrestres.

- **Variables esenciales para la prediccion en eventos de lluvia:**

| Variable de superficie | Rol físico en la lluvia |
| --- | --- |
| **Presión atmosférica (tendencia)** | Descensos de presión (0,5‑2 hPa/h) señalan la aproximación de un sistema de ascenso organizado (frente, baja térmica, línea de inestabilidad). La caída bárica es un precursor estadístico robusto de lluvia en las siguientes 1‑3 h, tanto estratiforme como convectiva (Sanders & Doswell, 1995). |
| **Temperatura del aire** | Influye en la capacidad de retención de vapor (Clausius‑Clapeyron). Temperaturas altas favorecen la lluvia convectiva si hay humedad; en lluvia estratiforme, la temperatura ayuda a distinguir nieve/agua.
Craven, J. P., & Brooks, H. E. (2004). *Baseline climatology of sounding-derived parameters associated with deep, moist convection*. |
| **Humedad (punto de rocío / HR)** | Variable crítica. Punto de rocío en superficie ≥ 12‑15 °C es un umbral frecuente para lluvia significativa en latitudes medias (Craven & Brooks, 2004). La HR alta indica cercanía a la saturación, facilitando la condensación si hay ascenso. |
| **Viento (dirección y velocidad)** | Identifica convergencia en superficie (choque de flujos), que es el mecanismo de  disparo más directo. La convergencia cuantificada por la divergencia  negativa (∇·V < 0) está fuertemente correlacionada con el inicio de la precipitación (Byers & Braham, 1949; Wilson & Schreiber, 
1986). |
- **Variables extras, necesarias para una precisa prediccion sobre el evento de lluvia:**

| Variable adicional | Por qué es fundamental | Cómo se mide (fuera de su estación) |
| --- | --- | --- |
| **Agua precipitable (PWAT)** | La
 cantidad total de vapor de agua en la columna atmosférica. Sin ella, la
 lluvia es imposible independientemente de lo que marquen los sensores 
de superficie. | Radiosondeo, GPS-Met, reanálisis (ERA5) |
| **CAPE (Energía Potencial Convectiva Disponible)** | Mide
 la inestabilidad real de la columna. Valores altos (> 1000 J/kg) 
convierten una simple lluvia en lluvia convectiva intensa. | Radiosondeo, reanálisis |
| **Cizalladura vertical del viento (0-6 km)** | Determina la organización y duración de los sistemas precipitantes. Sin cizalladura, la lluvia convectiva es pulsante y breve. | Radiosondeo, perfilador de viento, reanálisis |
| **Convergencia de humedad integrada** | La convergencia del flujo de humedad en toda la columna (no solo en superficie) es el predictor más directo de lluvia. | Radiosondeo + viento en capas, reanálisis |
| **Temperatura de brillo (satélite IR)** | Detecta el enfriamiento de los topes nubosos (nubes profundas = lluvia probable). | GOES-16 (cada 10 min), de acceso libre |
| **Reflectividad radar (Z)** | El mejor predictor de lluvia inminente (0-30 min) porque detecta directamente las gotas en formación. | Radares del SMN o de la red INVAP (Argentina) |
- Como se aclaro anteriormente, en este proyecto solo se utilizaran las variables esenciales, debido a la simplicidad del modelo propuesto.

**¿Con que precision se predice tormentas segun la interpretacion de estas variables?**

La predicción de **ocurrencia de lluvia** (sí/no) a partir de observaciones horarias de presión, temperatura,  humedad y viento ha sido evaluada en múltiples trabajos de nowcasting. La métrica estándar es la **probabilidad de detección (POD)**, la **tasa de falsas alarmas (FAR)** y el **índice de éxito crítico (CSI)**.

### Síntesis de resultados documentados

| Horizonte | POD (aciertos) | FAR (falsas alarmas) | CSI | Método | Referencia |
| --- | --- | --- | --- | --- | --- |
| 0‑1 h | 0,82–0,91 | 0,18–0,30 | 0,55–0,70 | Regresión logística / Random forest con P, T, HR, viento | Manzato (2010), Tyagi et al. (2012), Babu et al. (2019) |
| 1‑2 h | 0,72–0,85 | 0,25–0,40 | 0,45–0,60 | Redes neuronales, árboles de decisión con los mismos predictores horarios | Babu et al. (2019), Rajeevan et al. (2012) |
| 2‑3 h | 0,60–0,75 | 0,35–0,50 | 0,35–0,50 | Similar, añadiendo tendencias horarias | Sen Roy & Balling (2004), Paras et al. (2007) |
- Con los cuatro sensores se alcanza una capacidad de detección del 70‑90% para lluvia en la próxima hora, con una tasa de falsa alarma del
20‑40%. Lo convierte en un sistema operativamente util para la alerta temprana.
- La habilidad predictiva cae gradualmente después de las 2 horas porque los procesos de mesoescala (advección de humedad en capas medias,
forzamiento dinámico en altura) escapan a las mediciones puramente superficiales (Doswell, 1987; Wilson & Roberts, 2006).
- La inclusión del **viento** mejora el CSI entre 0,08 y 0,12 respecto a modelos que solo usan P, T y HR (temperatura, presion y humedad), porque permite detectar convergencia precursora (Tyagi et al.,2012).
- Los estudios que han construido predictores de lluvia o tormenta con datos de estaciones sinópticas (1 observación por hora) demuestran que esta frecuencia **es suficiente para horizontes de 1‑3 horas**, aunque con limitaciones. Permitiendo entrenar un modelo predictor con datos entregados en una frecuencia de 1h como minimo viable.
    - Sin embargo, se determina por diversos estudios que para un rango de tiempo menor (30m - 10m) se obtiene una mayor precision en la prediccion de eventos de lluvia.
    - **Wilson, J. W., & Schreiber, W. E. (1986)** – *Initiation of convective storms at radar-observed boundary-layer convergence lines*
    - **Mueller, C., et al. (2003)** – *NCAR Auto‑Nowcast System*

**Referencias:**

- **Doswell, C. A., Brooks, H. E., & Maddox, R. A. (1996).** Flash Flood Forecasting: An Ingredients‑Based Methodology.
- **Wilson, J. W., & Roberts, R. D. (2006).** Summary of Convective Storm Initiation and Evolution during IHOP_2002.
- **Luk, K. C., Ball, J. E., & Sharma, A. (2001).** An application of artificial neural networks for rainfall forecasting. *Mathematical and Computer Modelling*
- **Nayak, M. A., Krishnan, A., & Sen Roy, S. (2013).** Nowcasting of rainfall over Mumbai using support vector regression with surface meteorological data
- **Tyagi, B., Krishna, P. M., & Kumar, A. (2012).** *Nowcasting of thunderstorms using surface meteorological data*

### Originalidad del modelo: ¿Que aporta de diferente a lo que ya hay?

#### Alternativas principales al modelo LIF (Situacion actual)

Las estaciones meteorologias e instituciones externas que preveen el clima, utilizan modelos que resultan precisos a costa de maximizar la infrestructura.

**Datos satelitales:** Gran cobertura geografica brindando alta precision a costa de un gran gasto en la infrestructura, y delegando la localizacion y prediccion a corto plazo.

**Infrestructura terrestre:** Brinda alta precision y confiabilidad local pero produciendo un costo elevado al construir y mantener la infrestructura.

**Metodos de umbrales fijos:** Simples y baratos de implementar, pero generando una baja precision aumentando apleamente la tasa de falsas alarmas.

#### Propuesta y puntos clave

El modelo LIF adaptado a las tormentas plantea equilibrar alta precision con el bajo costo de la infrestructura necesaria.

Permite en base a sensores de bajo costo (comparado a la infrestructura terrestre u orbital de las estaciones meteorologicas) y un modelo matematico adaptado, poder brindar un modelo simple y barato de implementar con una precision mayor al umbral fijo.

### Delimitación del Proyecto:

#### Que se va a hacer

Se quiere desarrollar un modelo predictor de eventos de lluvia basado en el modelo matematico LIF (Que son redes neuronales pico en su version simplificada).

**Se plantean los siguientes requisitos:**

- Origen de los datos.
- Precision de los datos / metodos de recoleccion.
- Ubicaciones a predecir por el modelo.
- Rango de prediccion.
- Epoca del año.
- Lenguaje y programa de implementacion.
- Tipos de lluvia.
- Modelo comparativo.
- Datos a utilizar.
- Modelo a desarrollar.
- Ciclo dia y noche.

**Puntos principales:**

| **Dimension** | **Atributo** | **Dato** |
| --- | --- | --- |
| Geografia | Ubicacion fija. | Aeropuerto Internacional Ingeniero Aeronáutico Ambrosio Taravella, Cordoba, Argentina. |
| Rango | Horizonte a muy corto plazo. | 1h antes del evento de lluvia. |
| Epoca del año | Completa | Se entrenara el modelo para que sea capaz de adaptarse a todo el año, utilizando tecnicas de transformacion y normalizacion de datos, agregando neuronas extras. |
| Proveedor | Externo | Se utilizara un proveedor que permita acceder a los datos de forma directa y eficaz para el entrenamiento. No seran datos extraidos de forma particular, sino que se utilizaran datos provistos por la institucion dueña de la infrestructura. https://open-meteo.com/ |
| Evento | Evento de Lluvia | Se buscara predecir unicamente eventos de lluvia que provoquen precipitaciones. |
| Implementaciontecnica | Accesible y simple | Se eligira un lenguaje y IDE que permita extraer los datos de forma sencilla y eficaz, entrenar el modelo LIF a desarrollar y brindar correctamente los resultados extraidos del modelo. 
Se buscara algo eficaz y sencillo de trabajar que sea util para la investigacion debido al interes centrado en la comparativa y no en la implementacion eficiente u optimizacion del programa final. |
| Modelo comparativo | Umbrales fijos | Se utilizara un modelo tradicional basado en umbrales fijos especificado en metodologia para comparar la precision del modelo LIF simplificado. |
| Variables | 6 datos principales | Se extraeran 6 datos fundamentales de los sensores brindados por el proveedor, que permitan entrenar el modelo, estos son: Temperatura, presion, humedad, precipitacion, viento (velocidad|direccion).
Se utilizara la precipitacion como confirmacion de que ocurrio la lluvia, con el objetivo de utilizarlo como feedback en el entrenamiento del modelo (Metrica de exito). |
| Modelo a desarrollar | Basico y determinista | El modelo matematico LIF a utilizar representara una red minima de apenas 6 neuronas que representaran individualmente cada sensor especificado (Temperatura, presion, humedad, viento (velocidad|direccion), evento de lluvia (Neurona de alerta)). Se utilizara la ecuacion diferencial ordinaria que representa al comportamiento de una neurona, y se ajustaran los valores de cada una de las 6 neuronas individualmente en el “entrenamiento”.
Se ajustaran los valores con el entrenamiento que permita maximizar la precision y simplicidad de ejecucion. |
| Precision de los datos | Alta para el entrenamiento. | Debido a las limitantes de acceso confiable a datos historicos disponibles en sensores especificos de bajo costo se decidio:
  • Utilizar datos de estaciones que forman parte del SMN para la recoleccion de datos gracias a su facil acceso, obtenidos con dispositivos profecionales que cumplen los estandares de la MMO.
  • Posteriormente se añadira ruido a estos datos precisos para simular los datos de un sensor de bajo costo.
  • Se entrenaran 2 instancias del modelo LIF para comprobar su adaptacion a las diferentes precisiones en los datos disponibles.  |
| Ciclo dia y noche | Se analizara las 24h | Las variables de lluvia pueden variar entre las horas diurnas y nocturans, sin embargo el modelo sera entrenado con ambas. Contendra ciertas neuronas especializadas en identificar estos cambios horarios para una mayor precision. |

#### Que NO se va a hacer

Se detallan las caracteristicas y areas que NO va a abordar esta investigacion:

- NO se entrenara un mismo modelo para multiples ubicaciones diferentes.
- NO se desarrollara para rangos de predicion de mas de una hora antes del evento de lluvia. Aunque pueda lograr una prediccion de un rango mayor.
- NO se predeciran tormentas. Solo se predeciran eventos de lluvia especificados en la metodologia.
- NO se utilizaran datos mas complejos a los especificados, como imagenes satelitales. Solo se utilizaran 5 sensores terrestres determinados como:  Temperatura del aire, presion atmosferica, humedad relativa, precipitacion, viento (velocidad|direccion).
- NO se entrenara un modelo nocturno y otro diurno, solo e entrenara un unico modelo capaz de identificar este evento de lluvia tanto de dia como de noche.
- NO se entrenaran multiples modelos para cada estacion del año.
- NO incorporara un sistema de alerta temprana que se comunique con organismos, autoridades, ciudadanos o cualquier infrestructura de alerta compleja . Solo se alertara de forma simbolica en el software desarrollado.
- NO se utilizaran sensores personales para los datos utilizados en el entrenamiento, analisis u desarrollo. Se utilizaran datos de un proveedor externo debido a las limitaiones tecnicas. Se especifica el modo de analisis en la metodologia.
- NO se implementara en hardware embebido real. Solo se simulara por software.
- NO se desarrollara un modelo probabilistico. Se utilizara el modelo matematico LIF deterministico que representara una red neuronal de tercera generacion simplificada.
- NO se centrara optimizar la latencia de los dispositivos u otro atributo tecnico relacionado. Se centrara en desarrollar un modelo teorico predictivo util.
- NO se comparara el modelo LIF simplificado a desarrollar con modelos mas complejos y avanzados que sean diferentes al modelo tradicional de umbrales fijos especificado en la metodologia.
- NO medira intensidad de la lluvia. Solo mide el evento de lluvia determinado en la metodologia.

---

### Investigacion redes SNN (redes neuronales pico)

| **Tema** | **Contexo** | **Autores principales** | **Anexos principales.** |
| --- | --- | --- | --- |
| ¿**Que son las ssn**, redes neuronales de pico? | Qué son las redes neuronales de pico (SNN) y por qué se las llama "tercera generación". Las Spiking Neural Networks son modelos computacionales en los que la información no se representa mediante activaciones continuas (como en un perceptrón multicapa) sino mediante trenes de pulsos discretos en el tiempo, de manera análoga a cómo se comunican las neuronas biológicas. La referencia fundacional que formaliza esta clasificación es Wolfgang Maass, quien en 1997 publicó el trabajo que ubicó a las SNN como una tercera generación de modelos de redes neuronales, posterior a las redes basadas en neuronas de McCulloch-Pitts (compuertas de umbral) y a las redes basadas en unidades sigmoideas (el perceptrón multicapa clásico). 
El trabajo compara el poder computacional de las redes de neuronas pico con el de otros modelos de redes neuronales basados en neuronas de McCulloch-Pitts y en compuertas sigmoideas, mostrando que las primeras son, en relación con la cantidad de neuronas necesarias, computacionalmente más potentes (Una sola neurona de tercera generacion puede computar cualquier funcion booleana, mientras que a una neurona de segunda generacion se le haria imposible debido a las capas ocultas necesarias). 
Un resultado particularmente citado de ese mismo trabajo es que existe una función biológicamente relevante que puede ser computada por una sola neurona de pico (con valores biológicamente razonables de sus parámetros), pero que requeriría cientos de unidades ocultas en una red sigmoidea. 

Este dato no es menor: es el sustento formal de que una **neurona única**, bien parametrizada, puede tener capacidad de cómputo no trivial — no es una simplificación ingenua, es una elección con respaldo teórico.

Las compuertas de McCulloch-Pitts son binarias y atemporales, las unidades sigmoideas permiten gradientes continuos pero siguen siendo atemporales en su forma estándar, y las neuronas de pico incorporan el tiempo como dimensión computacional explícita: no solo importa si una neurona dispara, sino cuándo.

El trabajo establece que los modelos de tercera generación no son solo una curiosidad biológica, sino que poseen un poder computacional estrictamente superior en tareas donde el tiempo es una variable esencial. Con esto se inaugura un nuevo paradigma en el modelado neuronal y se sientan las bases teóricas para el desarrollo de hardware neuromórfico y nuevos sistemas de inteligencia artificial temporal. | Wolfgang Maass | https://www.sciencedirect.com/science/article/abs/pii/S0893608097000117 |
| **Efectividad del modelo simplificado**: Origen de la excitabilidad neuronal | Louis Lapicque, nacido el 1 de agosto de 1866, fue pionero en el campo de la excitabilidad neural, y una de sus principales contribuciones fue proponer el modelo de integración y disparo de la neurona en un artículo publicado en 1907. En ese estudio de 1907, Lapicque introduce un modelo del nervio que compara con datos obtenidos de estimulación de nervio de rana, modelo basado en un circuito capacitor simple, que formaría la base de modelos posteriores de membrana. Es decir: el modelo es anterior en 45 años al descubrimiento del mecanismo iónico real del potencial de acción (Hodgkin y Huxley, 1952). Lapicque no sabía *por qué* disparaba una neurona — pero logró un modelo predictivo igual. 

Esto es un dato fuerte para argumentar metodológicamente por qué un modelo simplificado (sin conocer todo el detalle biofísico subyacente) puede ser válido para predicción de eventos: el valor de un modelo no depende de captar el mecanismo completo, sino de capturar la dinámica relevante para la tarea.

Este modelo sigue siendo, más de un siglo después, uno de los más populares en neurociencia computacional, tanto para estudios celulares como de redes, y para neurociencia matemática. La redescubierta y modernización del modelo original de Lapicque hacia su forma "leaky" (con fuga) actual ocurrió recién a partir de la década de 1960, según documenta el trabajo centenario de Brunel y van Rossum (2007) que reconstruye la genealogía completa del modelo. | Louis Lapicque | https://library.uthscsa.edu/2014/06/the-louis-lapicque-papers/
https://www.researchgate.net/publication/5876908_Lapicque's_1907_paper_From_frogs_to_integrate-and-fire |
| Modelo LIF (Leaky integrate and fire) | El modelo Leaky Integrate-and-Fire es una extensión del modelo original de Integrate-and-Fire introducido por Lapicque en 1907, basado en observaciones experimentales sobre el axón gigante de calamar, y que respecto del modelo IF original incluye un término de fuga que evita que el potencial crezca indefinidamente, siendo versátil y ampliamente usado en neurociencia computacional. El "axón gigante de calamar" es justamente el sistema sobre el que Hodgkin y Huxley construyeron su modelo biofísico detallado de 1952 — el LIF es, en cierto sentido, la versión reducida y tratable analíticamente de esa dinámica iónica completa. [ResearchGate](https://www.researchgate.net/publication/5876908_Lapicque's_1907_paper_From_frogs_to_integrate-and-fire) | Richard B. Stein | https://pubmed.ncbi.nlm.nih.gov/14268952/
https://www.sciencedirect.com/science/article/abs/pii/S0303264706000475
https://www.researchgate.net/publication/14100224_Computing_with_the_Leaky_Integrate-and-Fire_Neuron_Logarithmic_Computation_and_Multiplication
https://link.springer.com/article/10.1007/s00422-007-0190-0 |
| Base matematica | La derivación estándar parte de modelar la membrana neuronal como un circuito RC en paralelo: una resistencia R (que representa los canales iónicos de fuga) y un capacitor C (que representa la bicapa lipídica de la membrana, que separa cargas). La corriente en el capacitor C está dada por I_C = dQ/dt = d(CV)/dt = C·dV/dt, para una carga Q y capacitancia C; la corriente en la resistencia R está dada por la ley de Ohm como I_R = V/R; y por conservación de la energía, la suma de todas las corrientes del capacitor, la resistencia, y cualquier corriente restante debe ser cero. 

τmdtdV(t)=−(V(t)−Vrest)+R⋅I(t)

El modelo LIF simula una **neurona biológica** reduciéndola a un **circuito eléctrico RC** (Resistencia-Capacitor) recontra **básico**.
****Cuando llevás estos modelos a la práctica en ingeniería de software, la R, la C y la I pierden su significado eléctrico literal y se transforman en **abstracciones matemáticas ajustables**.

donde U_i(t) es el potencial de membrana en el instante t, U_rest es el potencial de reposo, τ_mem es la constante de tiempo de membrana, I_i es la corriente inyectada en la neurona y R es la resistencia, siendo el término -(U_i - U_rest) el término de fuga que conduce el potencial hacia el reposo. El parámetro τ_m es la constante de tiempo de membrana, R_m es la resistencia de membrana y C_m es la capacitancia de membrana, relacionadas como τ_m = R_m·C_m. 

La condición de disparo y reseteo se define aparte de la ecuación diferencial: cuando el potencial de membrana alcanza el umbral de disparo ϑ, la neurona genera un potencial de acción; la dinámica neuronal que genera ese potencial de acción no es tratada por el modelo integrate-and-fire, que simplemente define el instante t en el cual ocurre v(t)=ϑ. Después de que se genera un pico postsináptico, el potencial de membrana cambia instantáneamente al valor de reset v_rs, y típicamente se añade un período refractario absoluto τ_abs durante el cual el potencial queda fijo en ese valor de reset antes de reanudar la integración.

Esto da las **tres reglas** que, junto con la ecuación diferencial, definen completamente al modelo (formulación estándar usada también en el trabajo de Gao et al. 2022 y en el material de Cuomo et al.): cuando el potencial de membrana supera el umbral fijo V_threshold se dispara instantáneamente un potencial de acción, el potencial se fija instantáneamente al valor de reset V_reset, y el disparo de otro potencial de acción queda prohibido durante un período refractario absoluto dado. | Romain Zimmer, Thomas Pellegrini2, Srisht Fateh Singh1, and Timothée Masquelie | https://arxiv.org/pdf/1911.10124 |
| Modelo LIF como filtro: Simulacion | Para corriente constante I(t) = I, la ecuación tiene solución exponencial cerrada. El valor asintótico del potencial de membrana es RI: si ese valor es menor que el umbral de disparo V_th, no se puede generar ningún pico; si en cambio RI > V_th, la neurona genera picos periódicamente. Esto es clave conceptualmente: el LIF no responde a *cualquier* estímulo, sino solo a aquellos cuya intensidad sostenida supera un punto de equilibrio determinado por la relación entre la corriente de entrada y la resistencia de membrana. Por debajo de ese punto, el sistema simplemente no dispara — actúa como filtro pasa-alto en intensidad y, simultáneamente, como filtro pasa-bajo en frecuencia temporal gracias al término de fuga, que descarta fluctuaciones rápidas y solo "recuerda" estímulos sostenidos en una ventana de orden τ_m.

Esta doble propiedad (umbral de intensidad + memoria temporal limitada por τ_m) es exactamente el comportamiento que necesitás justificar matemáticamente para tu modelo de detección de tormentas: la fuga descarta ruido transitorio de sensor, y el umbral descarta fluctuaciones que no acumulan suficiente "evidencia" sostenida. | Lindner, Benjamin;
Rubén Moreno-Bote and Néstor Parga | https://www.cns.nyu.edu/~eorhan/notes/lif-neuron.pdf
https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.92.028102
https://ui.adsabs.harvard.edu/abs/2014ican.conf..249L/abstract |

### Referencias iniciales.

1. **Lapicque, L.** (1907). Recherches quantitatives sur l'excitation électrique des nerfs traitée comme une polarisation. *Journal de Physiologie et de Pathologie Générale*
2. **Brunel, N., & van Rossum, M. C. W.** (2007). Lapicque's 1907 paper: From frogs to integrate-and-fire. *Biological Cybernetics*
3. **Abbott, L. F.** (1999). Lapicque's introduction of the integrate-and-fire model neuron (1907). *Brain Research Bulletin*
4. **Maass, W.** (1997). Networks of spiking neurons: The third generation of neural network models. *Neural Networks*, *10*(9), 1659–1671.
5. **Stein, R. B.** (1965). A theoretical analysis of neuronal variability. *Biophysical Journal*
6. **Stein, R. B.** (1967). Some models of neuronal variability. *Biophysical Journal*
7. **Gerstein, G. L., & Mandelbrot, B.** (1964). Random walk models for the spike activity of a single neuron. *Biophysical Journal*
8. **Gerstner, W., Kistler, W. M., Naud, R., & Paninski, L.** (2014). *Neuronal dynamics: From single neurons to networks and models of cognition*. Cambridge University Press.
9. **Gerstner, W., & Kistler, W. M.** (2002). *Spiking neuron models: Single neurons, populations, plasticity*. Cambridge University Press.

### Preprints y Documentos Técnicos

**1. Plesser, H. E., & Geisel, T.** (2001). Signal selection based on stochastic resonance.
**2. Bulsara, A., et al.** (1998). Markov analysis of stochastic resonance in periodically driven integrate-fire neuron.
**3. Vázquez, I. X., Sedano, J., Afzal, M., & García-Vico, Á. M.** (2025). Vacuum Spiker: A spiking neural network-based model for efficient anomaly detection in time series.

---

## 3) METODOLOGIA Y APLICACION

Aqui se expandira los pasos a realizar y la dinamica que tendra esta investigacion para lograr responder esta pregunta.

### **Lo que se busca responeder en esta investigacion es:**

- La capacidad del modelo LIF simplificado para predecir eventos de lluvia en entornos locales en base a la recoleccion de datos con diversos sensores.

### Metodologia basica (antigua):

- **Recolectar los datos necesarios.**
    - Identificar las variables que el modelo LIF utilizara para la prediccion.
    - Identificar instituciones meteorologicas con datos de sensores publicos.
    - Determinar zona especifica para la recoleccion de datos.
        - Descargar los analisis diarios con las variables necesarias.
- **Diseñar el modelo LIF.**
    - Identificar estructura del modelo a diseñar.
        - Determinar estructura de un modelo LIF funcional.
        - Determinar ecuaciones a utilizar.
        - Determinar la forma de utilizacion de las variables recolectadas.
    - Plantear programa a utilizar para la construccion del modelo LIF.
        - Determinar necesidades para la implementacion.
        - Determinar viabilidad en la exposicion a datos.
    - Analizar metodo de entrenamiento a utilizar.
        - Determinar objetivos a conseguir.
        - Identificar flujo de la informacion.
        - Determinar metodo que permita ajustar las variables del modelo identificadas.
        - Aplicar metodo para ajustar las variables del modelo.
- **Evaluar el modelo LIF.**
    - Analizar la tasa de exitos y fracasos mediante las medidas propuestas de FAR y POD.
    - Diseñar modelo sobre umbrales fijos
        - Determinar umbrales fijos propuestos para esa zona.
        - Utilizar algoritmo simple para el modelo de umbrales fijos.
        - Realizar pruebas para determinar tasa de exito y fracaso en el modelo de umbrales fijos.
        - Comparar tasas de exito y fracaso con las del modelo LIF.

---

## Metodología Preguntas Fundamentales.

### Aclaracion: No gastes tanto tiempo en justificar y aclarar formatos particulares. Centrate en avanzar en la estructura del modelo.

- Aclara los puntos fundamentales que te permitan estructurar el modelo. No gastes tiempo en aclarar estandares, fuentes o cuestiones externas. **CENTRATE EN EL DESARROLLO Y LA ESTRUCTURA.** PUNTO.

Se define el paso a paso de como se desarrollara y evaluara el proyecto:

#### Adquisicion de datos:

Se explica cuales, porque y de que forma se obtendran los datos necesarios para el proyecto.

- **¿Que variables se necesitan?**
    
    Se necesitan variables minimas para una correcta prediccion del clima, se pueden determinar como 6 variables principales.
    
    - **Humedad:** La humedad del aire se refiere a la cantidad de vapor de agua presente en la atmósfera.
        - **Para aplicaciones depredicción meteorológica**, la medida más utilizada es la Humedad Relativa (HR) , definida por la OMM como la relación entre la presión de vapor de agua real en el aire y la presión de vapor de saturación (la máxima que el aire podría contener a esa temperatura y presión), expresada como porcentaje.
        - **Unidades de medida:** Porcentaje (%), que varía entre 0% (aire completamente seco) y 100% (aire saturado).
    - **Presion:** Es la fuerza ejercida por unidad de área sobre una superficie determinada, envirtud del peso de la columna de aire que se encuentra sobre ella.
        - Es equivalente al peso de una columna vertical de aire que se extiende desde la superficie hasta el límite exterior de la atmósfera.
        - **Unidades de medida:** Hectopascal (hPa) (A utilizar) o milibar (mb), donde 1 hPa = 1 mb. El valor de referencia a nivel del mar es 1013.25 hPa
    - **Temperatura de Aire:** Es la magnitud física que indica el grado de agitación molecular (energía cinética promedio) de las partículas que componen el aire en un lugar y momento determinados.
        - **En términos operativos**, se define como la temperatura indicada por un termómetro expuesto al aire, en un lugar resguardado de la radiación solar directa.
        - **Unidades de medida:** Grados Celsius (°C) (A utilizar), grados Fahrenheit (°F) o Kelvin (K).
    - **Viendo (Direccion y velocidad):** Es el movimiento horizontal del aire a través de la superficie de la Tierra. Se describe mediante dos componentes fundamentales:
        - **Dirección del viento:** Se define por convención como la dirección de origen del viento (de dónde viene).
            - **Unidades de medida:** Se mide en grados (°), donde 0° o 360° es el Norte, 90° el Este, 180° el Sur y 270° el Oeste.
        - **Velocidad del viento:** Es la rapidez con la que la masa de aire se desplaza horizontalmente.
            - **Unidades de medida:** Se mide en metros por segundo (m/s), kilómetros por hora (km/h) (A utilizar) o nudos (kn)
    - **Precipitaciones:** Se define como el producto líquido o sólido de la condensación del vapor de agua que cae de las nubes y alcanza la superficie terrestre.
        - Las **formas de precipitación** incluyen lluvia, llovizna, nieve, granos de nieve, granizo, etc..
        - **Unidades de medida:** Milímetros (mm) de altura de agua acumulada sobre una superficie horizontal (A utilizar). También se mide como lámina de agua (litros por metro cuadrado, L/m²), que es equivalente.
    
    **Fuentes:** 
    
    https://library.wmo.int/es/records/item/68714-guia-de-instrumentos-y-metodos-de-observacion (OMM-N° 8)
    
    https://library.wmo.int/records/item/35809-international-meteorological-vocabulary (WMO-No. 182)
    
    #### Tabla resumen:
    
    | Variable | Definición Científica (Fuente OMM/AMS) | Unidad | Rol en la Predicción de Lluvia |
    | --- | --- | --- | --- |
    | **Temperatura** | Grado de agitación molecular del aire, medida por un termómetro al resguardo de la radiación solar. | °C / °F / K | Determina la capacidad del aire para contener vapor de agua. Su descenso es clave para la condensación. |
    | **Humedad Relativa** | Relación porcentual entre el vapor de agua real y el máximo posible a esa temperatura y presión. | % | Indica la cercanía a la saturación. Una HR alta es necesaria para la lluvia. |
    | **Presión Atmosférica** | Fuerza por unidad de área ejercida por el peso de la columna de aire. | hPa / mb | Su caída es un indicador de mal tiempo y tormentas. Es la base de la dinámica atmosférica. |
    | **Viento (Vel/Dir)** | Movimiento horizontal del aire. Dirección: de dónde viene. Velocidad: rapidez del desplazamiento. | m/s, km/h, kn / ° | Transporta humedad y sistemas frontales. Clave en tormentas severas. |
    | **Precipitación** | Producto líquido o sólido de la condensación del vapor de agua que cae de las nubes. | mm | Variable objetivo. Es el resultado del proceso que tu modelo busca predecir. |
- **¿De que forma se miden los datos? Metodos**
    
    Los datos se utilizaran convertidos a las variables correspondientes. No se utilizaran datos crudos (Ej: Resistencia eléctrica) para el analisis y utilizacion de los datos. Esto permite utilizar variables proporcionadas por estaciones confiables y universales de forma practica para la investigacion.
    
    - No se miden datos crudos extraidos de los sensores, se miden variables metorologicas traducidas por estos.
    
    **Temperatura del Aire:** 
    
    - **Método de medición estándar (OMM):** La OMM establece que la temperatura del aire debe medirse con un termómetro (de mercurio, resistencia o termistor) ubicado dentro de un abrigo meteorológico (garita) que lo proteja de la radiación solar directa y de la  precipitación, permitiendo al mismo tiempo la circulación del aire.
    - El sensor debe estar a una altura estándar de 1.25 a 2 metros sobre el suelo. La medición se realiza en grados Celsius (°C), que es la unidad que se utilizara.
    - **Método propuesto (bajo costo):** Se utilizara un sensor digital DHT22 (o similar como el AM2302). Este sensor integra un **termistor NTC** (Coeficiente de Temperatura Negativo) para medir la temperatura. Un termistor NTC es una resistencia cuya valor disminuye al aumentar la temperatura. El DHT22 convierte internamente esta resistencia a una señal digital 
    que el microcontrolador (Arduino, ESP32, etc.) puede leer fácilmente.
    
    **Humedad Relativa:**
    
    - **Método de medición estándar (OMM):** La OMM especifica que la humedad relativa (HR) se mide con un **higrómetro**, que puede ser de varios tipos: de cabello, de condensación (punto de rocío), o eléctricos (capacitivos o de resistencia).
    - El método más común en estaciones automáticas es el **sensor capacitivo**, que mide los cambios en la capacitancia de un polímero o material dieléctrico al absorber o liberar vapor de agua. La unidad de medida es el porcentaje (%).
    - **Método propuesto (bajo costo):** Se utilizara el mismo **sensor DHT22**, que incorpora un **sensor de humedad capacitivo**. Este sensor consiste en un condensador con un dieléctrico que absorbe humedad. Al cambiar la humedad, la constante dieléctrica del material cambia, lo que modifica la capacitancia del sensor. Este cambio se convierte en una señal digital que se transmite al microcontrolador.
    
    **Presion Atmosférica:**
    
    - **Método de medición estándar (OMM):** La presión atmosférica se mide con un barómetro. El estándar actual son los barómetros electrónicos (basados en sensores piezoresistivos o capacitivos).
    - Estos sensores contienen un diafragma de silicio que se deforma con la presión, generando un cambio en su resistencia eléctrica (efecto piezoresistivo) o en su capacitancia. La unidad de medida es el hectopascal (hPa), que es equivalente al milibar (mb) y que se utilizara en el proyecto.
    - **Método propuesto (bajo costo):** Se utilizara un sensor BMP180 o BMP280. Estos son sensores de presión barométrica MEMS (Micro-Electro-Mechanical Systems) que utilizan un diafragma piezoresistivo para medir la presión . El cambio en la resistencia del diafragma se convierte en un valor digital que se comunica al microcontrolador a través de protocolos I2C o SPI.
    
    **Viento (Velocidad y Dirección):**
    
    - **Método de medición estándar (OMM):** La OMM especifica que la velocidad del viento se mide con un anemómetro, y la dirección con una veleta.
    - El anemómetro de cazoletas (tres o cuatro cazoletas que giran con el viento) y la veleta son los instrumentos más comunes.
        - La velocidad se mide en m/s, km/h o nudos; Se utilizara km/h.
        - La dirección se mide en grados (°), donde 0° es el Norte, 90° el Este, etc. La altura estándar de medición es de 10 metros sobre el suelo.
    - **Método propuesto (bajo costo):** Se utilizara un anemómetro de cazoletas y una veleta, que suelen venir en kits como el SparkFun Weather Meter Kit. El anemómetro utiliza un interruptor de lengüeta (reed switch) que se cierra cada vez que las cazoletas completan una revolución, generando un pulso. La velocidad del viento es directamente proporcional a la frecuencia de estos pulsos. La veleta está acoplada a un potenciómetro que varía su resistencia según la orientación de la veleta. Esta resistencia se mide como un voltaje analógico, que se traduce en un ángulo de dirección.
    
    **Precipitación:**
    
    - **Método de medición estándar (OMM):** La OMM especifica que la precipitación se mide con un pluviómetro. El tipo más común en estaciones automáticas es el pluviómetro de cubeta basculante (tipping bucket).
    - Este instrumento consiste en un embudo que dirige el agua de lluvia a un pequeño balde o cucharón dividido en dos compartimentos. Cuando el balde se llena con una cantidad fija de agua (por ejemplo, 0.2 mm), se inclina y se vacía, generando un pulso eléctrico (a través de un interruptor de lengüeta) que es contado por el microcontrolador. La precipitación se mide en milímetros (mm), que es la unidad que se utilizara.
    - **Método propuesto (bajo costo):** Se utilizara el mismo pluviómetro de cubeta basculante que viene en kits como el de SparkFun. Este pluviómetro tiene una resolución típica de 0.2 mm por pulso. Cada vez que la cubeta se inclina, el interruptor de lengüeta se cierra y el microcontrolador registra un "pulso" de lluvia. El total de precipitación se calcula multiplicando el número de pulsos por la resolución del pluviómetro.
- **¿De donde se obtienen los datos? (Ubicacion y sistema de recoleccion datos)**
    
    **Obtencion:** La recoleccion de datos para el entrenamiento del modelo sera proporcionada por un ente externo, no datos propios.
    
    **Justificacion y abordaje:** Debido a los limitantes en los datos historicos necesarios para un entrenamiento eficaz, se utilizaran los datos extraidos de las estaciones validadas por el MWO/OMM, y con una coleccion de datos historicos completos de al menos 5 años continuos. 
    
    - Estas estaciones estan compuestas de dispositivos que recolectan los datos de cada variable de forma mucho mas precisa y confiable que un equipo de bajo costo.
    - El objetivo de esta fuente es **entrenar el modelo LIF de con datos historicos** proporcionados por una cierta estacion. Y posteriormente entrenar otra instancia del modelo pero con los datos inducidos a ruido y variaciones propias de los dispositivos de bajo costo para probar la flexibilidad del modelo independientemente de la calidad de los dispositivos.
    - **Se determinara el porcentaje de precision** que diferencia a ambos tipos de mediciones (profecional y bajo costo).
    - La recoleccion y posterior entrenamiento con datos propios en sensores de bajo costo se delega a una proxima apleacion de la investigacion actual (trabajo futuro).
        - Si utilizamos una estacion cercana: Si, sino queda la investigacion posterior limitada a la distancia factible de viaje.
    
    **Estacion elegida:** 
    
    - Se elegira una estacion que contanga un “WMO ID”, esto certifica que la estacion cumple con los estandares impuestos por la Organización Meteorológica Mundial.
    - Se consideraron 3 estaciones candidatas para la recoleccion de sus datos historicos debido a:
        - Su validacion como miembros de la MWO/OMM, validando un equipo de deteccion que cumpla con los estandares internacionales.
        - Datos completos y fiables ofrecidos por estas estaciones.
        - Cercania nacional y validacion extra por parte del SMN en el caso de las primeras 2 opciones. Y la tercera opcion como una estacion secundaria en el caso que las primeras 2 no sean viables.
    - Las estaciones son:
        - **SAEZ: EZEIZA** (Aeropuerto Internacional Ministro Pistarini), WMO ID: 87576
        - **SACO: CORDOBA** (Aeropuerto Internacional Ingeniero Aeronáutico Ambrosio Taravella), WMO ID: 87344.
        - **EDDF: Fráncfort del Meno, ALEMANIA:** Frankfurt Airport (Frankfurt am Main), ****WMO ID: 10637
    
    Aclaraciones sobre los datos extraidos de la estacion:
    
    - La estacion “Aeropuerto Internacional Ingeniero Aeronáutico Ambrosio Taravella” y “Ezeiza Aero” al ser miembros validados por el SMN, cumplen los estandares de la OMM/WMO para las mediciones con su precision correspondiente, sin embargo los dispositivos utilizados pueden variar de modelo especifico entre estaciones, normalmente estos dispositivos fueron proporcionados por:
        - **Lufft**
        - Vaisala
        - Campbell
        - OTT
        
        | Marca | ¿Hay evidencia pública? | Fuente |
        | --- | --- | --- |
        | **Lufft** | **Sí** | Documentación técnica del repositorio oficial del SMN |
        | **Vaisala** | Sí | Documentación de sistemas aeronáuticos (AWOS/MET) y licitaciones del Estado |
        | **Campbell Scientific** | Sí | Licitaciones y proyectos meteorológicos nacionales/provinciales |
        | **OTT** | Sí | Proyectos hidrometeorológicos argentinos y licitaciones |
        - El SMN utiliza diferentes fabricantes según la estación y la época. La única marca que se puede verificar directamente en documentación técnica oficial del SMN es LUFFT. Para Vaisala, Campbell y OTT existen evidencias de uso en sistemas meteorológicos argentinos o aeronáuticos, pero no una confirmación pública de que formen parte de la red general del SMN.
        - En los aeropuertos analizados puede coexistir 2 tipos de intrumentalizaciones diferentes.
            - Instrumentación del **SMN** (climatología y observaciones).
            - Instrumentación **AWOS** administrada en el entorno aeronáutico (EANA u otros organismos, según la configuración operacional).
    - Los datos extraidos de esta fuente, pudieron ser corregidos por el SMN debido a su normativa, provocando pequeñas discrepancias a los datos reales de sus sensores. Sin embargo esta correccion permite un analisis mas preciso de los datos (Documento creacion del SMN Artículo 3, inciso a)
    - **Otras opciones:**
        - “**Aeropuerto Regional Villa María** (Aeropuerto Regional Presidente Néstor Kirchner)” que permite facilidad logistica para probar este mismo modelo con datos extraidos de sensores a bajo costo en un futuro.
    
    **Fuentes:**
    
    - https://www.argentina.gob.ar/normativa/nacional/decreto-1432-2007-133371/texto
    - https://repositorio.smn.gob.ar/bitstream/handle/20.500.12160/448/Nota_Tecnica_SMN_2017-16.pdf?sequence=1&isAllowed=y
    - https://repositorio.smn.gob.ar/bitstream/handle/20.500.12160/469/Nota_Tecnica_SMN_2017-22.pdf?sequence=1&isAllowed=y
    - https://www.eana.com.ar/novedades-del-sector/eana-inauguro-el-primer-sistema-meteorologico-de-nivel-internacional-en-el
- **¿Quien provee los datos?**
    
    Al no extraer los datos manualmente, utilizaremos un proveedor que nos brinde los datos por un medio confiable y simple de utilizar.
    
    #### **Condiciones para la extraccion:**
    
    Los datos deben simular datos extraidos directamente de dispositivos fisicos, por lo que requieren una serie de condiciones:
    
    - **Datos crudos:** NO deben llevar ningun tipo de manipulacion mediante modelos matematicos.
    - **Frecuentes:** Deben cumplir con una frecuencia minima de 60 minutos entre cada dato obtenido.
    - **Verificacion:** Los datos extraidos del proveedor deben poder verificar su veracidad con los datos reales provistos por la estacion.
    - **Facilidadad:** Los datos deben poder extraerse y formatearse de una forma sencilla para el posterior entrenamiento.
    - **Datos historicos:** El proveedor debe poder ofrecer datos historicos con una antiguedad como minimo de 5 años usando los mismos dispositivos de deteccion para un correcto entrenamiento del modelo. Cantidad minima recomendada para una precision adecuada del modelo y debido a los cambios que surgieron los dispositivos en la estaciones principales.
    
    Se podran utilizar mas de una fuente para la comprobacion y correcta extraccion de los datos.
    
    - **Series de tiempo (argentina.gob.ar):** Medio oficial para la extraccion de datos, frecuencia diaria: Descartada
    - **Meteostat:** Plataforma open source diseñada para la extraccion y formateo de datos entregados por las estaciones o las instituciones meteorologicas. Incluye una recopilacion extensa de los datos publicados por el SMN a lo largo de los años. https://dev.meteostat.net/quality.html
        - La API de Meteostat proporciona metadatos de cada estación que incluyen su ID de WMO cuando está disponible.
        - La documentación oficial de Meteostat indica que todas las estaciones listadas en el directorio de Meteostat se adhieren a los estándares internacionales de la WMO cuando esos estándares aplican
        - La mayor parte de los datos de Meteostat proviene de servicios meteorológicos oficiales y puede considerarse fiable para un uso general. Es posible que existan pequeñas inconsistencias, aunque por lo general no afectan a las aplicaciones habituales. Para trabajos científicos de alta precisión, se recomienda realizar comprobaciones de calidad y validaciones adicionales sobre las observaciones en bruto.
        - Debido a esta razon, se utilizaran otras fuentes para respaldar los datos obtenidos por meteostat.
    - **Visual Crossing:** Plataforma privada que recopila y entrega de forma formateada los datos de instituciones meteorologicas oficiales aprobadas por la OMM/MWO: De pago, descartada
    - **NOAA GHCNh:** Cualquier estacion validada por la MWO, se extraen en crudo y procesan para tener una base de datos directa.
        - Se pueden utilizar librerias como “**meteora**” que permiten la obtencion de datos de una forma mucho mas sencilla.
    
    #### **Dificultades y resolucion:**
    
    - Para la extraccion de datos de las fuentes y estaciones oficiales se impone una gran dificultad. Los canales de comunicacion de estos datos provienen del sistema meteorologico nacional, los cuales no proveen los datos de forma directa para su extraccion historica en masa, sino que se proveen datos de forma resumida o simplemente visual y actual, sin un historial detallado y simple de recuperar.
    - Debido a esto, se utilizaran diferentes fuentes que recopilen los datos historicos provistos por el SMN o instituciones verificadas y junto a los datos generales y actuales provistos se podran corroborar y validar.
    
    #### **Eleccion:**
    
    - Se realizaran estracciones desde meteostat y meteora debido a la simplicidad de extraccion y formato adaptado para una facil manipulacion.
    - Se decidira posteriormente en la verificacion de datos faltantes el proveedor especifico a utilizar.
    
    #### **Fuentes:**
    
    - https://www.sciencedirect.com/science/article/pii/S0022169426001435?fr=RR-2&ref=pdf_download&rr=a16a87397c43acb8
    - https://ams.confex.com/ams/WAFNWPMS/webprogram/Paper425648.html
- **¿Que frecuencia de muestreo se utilizara, se promedian los datos?**
    
    #### **Frecuencia:**
    
    Los datos seran extraidos en rangos de una hora.
    
    #### **Justificacion:**
    
    Es la frecuencia minima que la estacion provee de forma abierta, y esta comprobado que resulta suficiente para una prediccion confiable con el sistema adecuado. No se agruparan los datos en tiempos mas extensos.
    
    #### **Investigacion de frecuencia para predecir eventos de lluvia:**
    
    **¿Una hora es una frecuencia suficiente para una prediccion optima del evento de lluvia?**
    
    Si pero con matices: Se puede identificar para la mayoria de lluvias los cambios de las variables precursoras del evento de lluvia.
    
    Sin embargo para eventos convectivos rapidos (<30m) estos cambios en las variables suelen ser mas sutiles y mas complejos de identificar con datos de 1h.
    
    - **Definicion evento de lluvia:**
        
        
        | Estudio | Definición de evento | Criterio de separación (MIET) |
        | --- | --- | --- |
        | Brasil et al. (2022) — Sustainability | Secuencia contigua de precipitación donde la profundidad mínima por tip ≥ 0.2 mm, separada por un período sin lluvia (MIET) | MIET = 6 h óptimo para regiones semiáridas |
        | Haas et al. (2025) — WCD/EGUsphere | Secuencia de épocas de 5 min donde la precipitación máxima en 5 min > 0.19 mm (≥ 2 tips) o media > 0.0039 mm (≈ 0.05 mm/h) | Períodos contiguos de precipitación |
    - **Clasificacion de lluvia segun duracion:**
    Tras analizar 530 eventos con MIET = 6h, se identificaron 3 clases:
        
        
        | Clase | % eventos | Duración media | Rango duración | Intensidad media | Descripción |
        | --- | --- | --- | --- | --- | --- |
        | I — Pequeños | 77% | 2.8 h | 0.08 – 11.58 h | 5.6 mm/h | Eventos ligeros a moderados |
        | II — Alta intensidad | 3% | 0.3 h (18 min) | 0.08 – 0.67 h | 45.9 mm/h | Tormentas convectivas cortas e intensas |
        | III — Largos / alta profundidad | 20% | 8.1 h | 1.0 – 25.58 h | 9.1 mm/h | Frentes, lluvias estratiformes |
        1. https://www.mdpi.com/2071-1050/14/3/1721
    
    - **Conclusion:**
        
        La frecuencia de 1h permite detectar tendencias sinópticas lejanas (2-8h antes).
        
        **NO es suficiente para:**
        
        1. Capturar la señal de activación (últimos 28-60 min antes del comienzo)
        2. Resolver eventos convectivos cortos (< 30 min de duración)
    
    **Fuentes extra:**
    
    https://wcd.copernicus.org/articles/6/949/2025/
    
    https://journals.ametsoc.org/view/journals/atsc/63/8/jas3735.1.xml
    
    ### ¿Se promedia la hora?
    
    DWD (estaciones alemanas, ej. EDDF)
    Según el CDC Newsletter Nr. 10 y los datasets descriptivos de DWD OpenData:
    
    | Variable | Tipo de medición | Detalle |
    | --- | --- | --- |
    | Temperatura 2m | Terminwert (instantánea) | Lectura en el horario sinóptico fijo |
    | Humedad relativa | Terminwert (instantánea) | Lectura en el horario sinóptico |
    | Velocidad del viento (synop) | Promedio 10 minutos | "10-minütigen Mittelwert, der im Intervall zwischen Minute 40 und 50 vor der vollen Stunde ermittelt wird" — promedio entre min 40 y 50 de cada hora |
    | Velocidad del viento (horas) | Media horaria | "Stundenmittelwert" — promedio de todos los datos de la hora |
    | Dirección del viento | Promedio 10 min | Misma ventana que velocidad |
    | Precipitación | Suma horaria | "Stundensumme" — total acumulado en la hora |
    | Presión | Terminwert (instantánea) | Lectura en el horario |
    
    > "Heute handelt es sich dabei um einen 10-minütigen Mittelwert, der im Intervall zwischen Minute 40 und 50 vor der vollen Stunde ermittelt wird und dem Stundentermin zugeordnet wird."
    (Hoy en día se trata de un valor medio de 10 minutos, que se determina en el intervalo entre el minuto 40 y 50 antes de la hora completa y se asigna al término horario.)
    > 
    
    En conclusion: Almacena observaciones sinópticas, que son exactamente estos valores puntuales en horarios fijos (0000, 0100, 0200 UTC, etc.).
    

#### Utilizacion y procesamiento de los datos:

- **¿Que cambios o transformacions sufren los datos originales?**
    
    El proveedor “Meteostat” extrae los datos desde una fuente global que estandariza los datos extraidos de cada institucion.
    
    **La ruta de estandarizacion es:**
    
    - SMN → WMO GTS → NOAA ISD → ISD Lite → Meteostat
    - Donde se describe cada parte como:
        - **Medición en la Estación (ej. SACO, SAEZ: ‘Codigo ICAO’):** Los sensores de la estación toman las mediciones de temperatura, presión, viento, etc.
        - **Transmisión al SMN:** Estos datos se envían al Servicio Meteorológico Nacional (SMN) de Argentina.
        - **Inserción en el Sistema Global (WMO GTS):** El SMN (como miembro de la Organización Meteorológica Mundial) envía estos datos al **Sistema Mundial de Telecomunicaciones (GTS)** de la OMM. Esta es la red global que permite a todos los países compartir información meteorológica en tiempo real.
        - **Captura por NOAA:** La **Administración Nacional Oceánica y Atmosférica de EE.UU. (NOAA)**, a través del **Centro Nacional de Información Ambiental (NCEI)**, recibe y archiva estos datos del GTS.
        - **Almacenamiento en el ISD:** La NOAA integra estos datos en su gran base de datos global: el **Integrated Surface Database (ISD)**. Este es el archivo principal que contiene observaciones horarias y subhorarias de más de 35,000 estaciones en todo el mundo.
        - **Creación del ISD-Lite:** Para hacer los datos más fáciles de usar, la NOAA crea un subconjunto llamado **ISD-Lite**. Este contiene solo 8 variables comunes (temperatura, punto de rocío, presión, viento, etc.) en un formato más simple.
        - **Agregación por Meteostat:** Meteostat toma el ISD-Lite (y otras fuentes) y lo procesa para ofrecerlo a través de su API y librería Python.
    - Cada país (Como por ejemplo Argentina con el SMN) usa sus propios formatos y protocolos. El WMO GTS es el estándar global de transmisión. El ISD de la NOAA es el estándar global de archivo. Meteostat es el agregador que te permite acceder a todo esto con una sola línea de código, evitándote tener que buscar con cada fuente por separado.
    - No se extraen los datos directamente desde el Sistema Global (WMO GTS) debido a que esta restringido a miembros de esa organizacion. Ni tampoco se extraen desde el ISD de NOAA debido a que requiere una extraccion y adaptacion compleja de los datos.
    - Utilizamos meteostat para obtener una fuente confiable y sencilla en la extraccion de datos historicos sin añadir complejidad en la extraccion de datos.
    - La confiabilidad de los datos es la misma, lo que cambia es la dificultad para acceder a ellos y procesarlos de manera consistente.
    
    **Actualizacion de ISD:**
    
    - El 24 de agosto de 2025 ****NOAA dejo de ofrecer datos actualizados por el servicio de “**ISD-Lite**”, migrando a su nuevo sistema mas complejo “GHCNh”.
    - Esto provoco que el principal proveedor de meteostat cambiara. Actualmente mantenien estos proveedores principales:
        - **DWD (Deutscher Wetterdienst):** hourly, daily, monthly, MOSMIX, POI
        - **ECCC (Environment and Climate Change Canada):** hourly, daily, monthly
        - **METAR:** reportes de aviación
        - **MET Norway:** pronósticos
        - **GHCN-Daily:** Nueva base de datos mantenida por la NOAA.
        - **ISD-Lite:** Base de datos por descontinuar de la NOAA.
    - Todos los datos anteriores a esa fecha son datos confiables recolectados por las estaciones, estandarizados y distribuidos por la WMO y NOAA.
    - La alternativa es extraer los datos directamente del **GHCNh,** o evaluar alternativas como “OGIMET” para extraer los datos directamente del METAR proporcionado por el SMN.
    
    Debido a esta ruta de estandarizacion, los datos pueden sufrir transformaciones o adaptaciones, desde la estandarizacion ISD-Lite su transformacion es:
    
    | Variable en ISD‑Lite | Formato en ISD‑Lite | Meteostat | Variable final en el script |
    | --- | --- | --- | --- |
    | Temperatura del aire | °C × 10 (ej. `234` = 23.4 °C) | Dividir por 10 para llevar a unidades reales | Temperatura (°C) |
    | Punto de rocío | °C × 10 | Se usa como insumo para calcular la humedad relativa | (No se entrega) |
    | Presión a nivel del mar | hPa | Sin cambio | Presión (hPa) |
    | Dirección del viento | Grados (°) | Sin cambio | Dirección del viento (°) |
    | Velocidad del viento | m/s × 10 (ej. `45` = 4.5 m/s) | Dividir por 10 → m/s, luego convertir a km/h (× 3.6) | Velocidad del viento (km/h) |
    | Precipitación | mm | Sin cambio | Precipitación (mm) |
    
    **Puntos clave de la transformacion:**
    
    **La Humedad Relativa NO es una medición directa:** El ISD-Lite no incluye la humedad relativa. Meteostat la **calcula** a partir de la temperatura y el punto de rocío utilizando la **fórmula de August-Roche-Magnus**.
    
    **Fuentes:**
    
    - https://library.wmo.int/records/item/35795-technical-regulations-volume-ii-meteorological-service-for-international-air-navigation https://community.wmo.int/site/knowledge-hub/programmes-and-initiatives/wmo-information-system-wis/about-manual-gts https://community.wmo.int/site/knowledge-hub/programmes-and-initiatives/global-observing-system-gos/wmo-no-544-manual-global-observing-system
    - https://www.ncei.noaa.gov/metadata/geoportal/rest/metadata/item/gov.noaa.ncdc:C00532/html  https://www.nesdis.noaa.gov/news/service-location-change-integrated-surface-data-global-hourly https://www.ncei.noaa.gov/products/global-historical-climatology-network-hourly https://www.ncei.noaa.gov/news/next-generation-climate-dataset-built-seamless-integration
    - https://www.ncei.noaa.gov/products/land-based-station/integrated-surface-database
    - https://www.ncei.noaa.gov/ http://ncei.noaa.gov/pub/data/noaa/isd-lite/isd-lite-format.pdf
    - https://www.ncei.noaa.gov/pub/data/noaa/isd-lite/
    - https://dev.meteostat.net/providers
- **¿Cuál es el porcentaje de datos faltantes en mi dataset y cuál es su patrón?**
    
    Se realizaron diferentes script capaces de comincarse a las API’s correspondientes de los proveedores para poder recuperar los datos de las estaciones seleccionadas en rango de fechas y frecuencias adecuados.
    
    El analisis concluyo que los datos seran extraidos de la estacion: **EDDF:** Frankfurt Airport (Frankfurt am Main)
    
    Debido a que en las estaciones argentinas analizadas validadas por el SMN y el MWO no proveen el dato clave precipitacion para utilizar como variable de exito.
    
    Debido a esto se busco una estacion capaz de contener un periodo de al menos 5 años continuos sin ningun dato faltante.
    
    **¿El EDDF interpola sus datos o utiliza metodos matematicos para rellenar datos de sensores o son todos datos propios de sus sensores?**
    
    Las variables fundamentales (temp, presión, viento, precipitación) son datos crudos de sensores. Solo la humedad relativa implica un cálculo matemático indirecto. La estación no interpola ni rellena datos artificialmente: los datos vienen completos del DWD vía WMO GTS → NOAA ISD.
    
    # **Scripts** para la recuperacion de datos.
    
    Estan realizados en Python 3.
    
    - **Parte 1: extraer datos**
        - Pide estación (Ezeiza o Córdoba), fechas (dd/mm/aaaa), y si usar modelo
        - Extrae 6 parámetros: temp, rhum, pres, wdir, wspd, prcp
        - Frecuencia: 1 hora (la más baja disponible)
        - Guarda .txt separado por espacios con header
            - Nombre: Estacion-ICAO-AAAAmmdd_AAAAmmdd-Modelo{Si|No}.txt
        - Valores faltantes se marcan con .
    - **Parte 2:** **analizar datos**
        - Analiza faltantes por variable y total.
        - Muestra porcentajes en terminal.
    - **Script ejemplo:** Extrae los datos directamente de los archivos ISD proporcionados por el NOAA.
        
        Procesa todos los archivos `.txt` de la carpeta, extrae las 6 variables horarias (temperatura, humedad relativa calculada, presión, dirección y velocidad del viento, y precipitación) y las guarda en un único archivo por estación con el formato solicitado.
        
        ### 📁 Script: `extractor_isd.py`
        
        ```python
        import os
        import re
        import math
        from collections import defaultdict
        
        # ----------------------------------------------------------------------
        # 1. Función para calcular la humedad relativa a partir de T y Td
        #    (Fórmula de Magnus)
        # ----------------------------------------------------------------------
        def calcular_rh(temp, dew):
            """
            temp: temperatura del aire en °C
            dew : punto de rocío en °C
            Retorna: humedad relativa en % (0-100) o None si falta algún dato
            """
            if temp is None or dew is None:
                return None
            try:
                t = float(temp)
                td = float(dew)
            except (ValueError, TypeError):
                return None
        
            a = 17.625
            b = 243.04
        
            es_t = 6.1094 * math.exp((a * t) / (b + t))
            es_td = 6.1094 * math.exp((a * td) / (b + td))
        
            rh = 100 * es_td / es_t
            # Acotar por posibles errores numéricos
            if rh > 100:
                rh = 100.0
            if rh < 0:
                rh = 0.0
            return rh
        
        # ----------------------------------------------------------------------
        # 2. Parseo de una línea del formato ISD crudo
        # ----------------------------------------------------------------------
        def parsear_linea(linea):
            """
            Extrae la información relevante de una línea ISD.
            Retorna un diccionario con:
              - date   : YYYYMMDD
              - time   : HHMM
              - temp   : temperatura (°C)
              - dew    : punto de rocío (°C)
              - slp    : presión a nivel del mar (hPa)
              - wdir   : dirección del viento (grados)
              - wspd   : velocidad del viento (m/s)
              - prcp   : precipitación (mm)
            """
            if len(linea) < 105:
                return None
        
            datos = {}
        
            # --- Fecha y hora (sección de control) ---
            datos['date'] = linea[15:23]   # YYYYMMDD
            datos['time'] = linea[23:27]   # HHMM
        
            # --- Viento (sección obligatoria) ---
            # Dirección: pos. 61-63 (0-index: 60-63)
            wdir_str = linea[60:63]
            datos['wdir'] = float(wdir_str) if wdir_str != '999' else None
        
            # Velocidad: pos. 66-69 (0-index: 65-69) escala 10
            wspd_str = linea[65:69]
            if wspd_str != '9999':
                datos['wspd'] = float(wspd_str) / 10.0
            else:
                datos['wspd'] = None
        
            # --- Temperatura del aire: pos. 88-92 (0-index: 87-92) escala 10 ---
            temp_str = linea[87:92]
            if temp_str[0] == '+':
                temp_str = temp_str[1:]
            if temp_str != '9999':
                datos['temp'] = float(temp_str) / 10.0
            else:
                datos['temp'] = None
        
            # --- Punto de rocío: pos. 94-98 (0-index: 93-98) escala 10 ---
            dew_str = linea[93:98]
            if dew_str[0] == '+':
                dew_str = dew_str[1:]
            if dew_str != '9999':
                datos['dew'] = float(dew_str) / 10.0
            else:
                datos['dew'] = None
        
            # --- Presión a nivel del mar: pos. 100-104 (0-index: 99-104) escala 10 ---
            slp_str = linea[99:104]
            if slp_str != '99999':
                datos['slp'] = float(slp_str) / 10.0
            else:
                datos['slp'] = None
        
            # --- Precipitación (sección adicional ADD) ---
            datos['prcp'] = None
            idx_add = linea.find('ADD')
            if idx_add != -1:
                # Extraer solo la parte ADD (hasta REM o EQD o final)
                resto = linea[idx_add + 3:]
                fin = len(resto)
                idx_rem = resto.find('REM')
                idx_eqd = resto.find('EQD')
                if idx_rem != -1:
                    fin = min(fin, idx_rem)
                if idx_eqd != -1:
                    fin = min(fin, idx_eqd)
                bloque_add = resto[:fin]
        
                # Buscar AA1, AA2, AA3, AA4 (precipitación líquida)
                precip_total = 0.0
                encontrado = False
                for i in range(1, 5):
                    patron = rf'AA{i}(\d{{2}})(\d{{4}})(\d)(\d)'
                    match = re.search(patron, bloque_add)
                    if match:
                        # periodo = int(match.group(1))  # no se usa para el valor horario
                        profundidad = float(match.group(2)) / 10.0  # mm
                        # cond = match.group(3)  # 2 = traza, normalmente se trata como 0.0
                        precip_total += profundidad
                        encontrado = True
                if encontrado:
                    datos['prcp'] = precip_total
        
            return datos
        
        # ----------------------------------------------------------------------
        # 3. Función principal
        # ----------------------------------------------------------------------
        def main():
            # Buscar todos los archivos .txt en la misma carpeta del script
            archivos = [f for f in os.listdir('.') if f.endswith('.txt')]
        
            if not archivos:
                print("No se encontraron archivos .txt en la carpeta actual.")
                return
        
            # Diccionario para acumular datos por estación (ICAO) y por hora (YYYYMMDDHH)
            # estructura: { ICAO: { YYYYMMDDHH: { 'temp': val, 'dew': val, ... } } }
            datos_estaciones = defaultdict(lambda: defaultdict(lambda: {
                'temp': None, 'dew': None, 'slp': None,
                'wdir': None, 'wspd': None, 'prcp': None
            }))
        
            for archivo in archivos:
                print(f"Procesando: {archivo}")
                with open(archivo, 'r', encoding='utf-8', errors='ignore') as f:
                    for linea in f:
                        linea = linea.strip()
                        if not linea:
                            continue
        
                        parsed = parsear_linea(linea)
                        if not parsed:
                            continue
        
                        # --- Obtener el ICAO desde la sección REM (METAR) ---
                        icao = None
                        idx_rem = linea.find('REM')
                        if idx_rem != -1:
                            bloque_rem = linea[idx_rem:]
                            # Busca METAR COR SAEZ o METAR SAEZ
                            match = re.search(r'METAR (?:COR )?([A-Z]{4})', bloque_rem)
                            if match:
                                icao = match.group(1)
        
                        if not icao:
                            # Si no se encuentra ICAO, se omite esta línea
                            continue
        
                        # Clave horaria: YYYYMMDDHH
                        clave_hora = f"{parsed['date']}{parsed['time'][:2]}"
        
                        # --- Mezclar datos de la misma hora (prioridad: no sobreescribir si ya existe) ---
                        datos_hora = datos_estaciones[icao][clave_hora]
                        for campo in ['temp', 'dew', 'slp', 'wdir', 'wspd', 'prcp']:
                            valor = parsed.get(campo)
                            if valor is not None and datos_hora[campo] is None:
                                datos_hora[campo] = valor
        
            # --- Escribir un archivo de salida por cada estación ---
            for icao, horas in datos_estaciones.items():
                if not horas:
                    continue
        
                # Ordenar cronológicamente
                horas_ordenadas = sorted(horas.keys())
                fecha_inicio = horas_ordenadas[0][:8]
                fecha_fin = horas_ordenadas[-1][:8]
        
                # Nombre del archivo: Estacion-ICAO-AAAAmmdd_AAAAmmdd-ModeloNo.txt
                # Usamos el ICAO como nombre de la estación (por no tener otro dato)
                nombre_archivo = f"{icao}-{icao}-{fecha_inicio}_{fecha_fin}-ModeloNo.txt"
        
                with open(nombre_archivo, 'w', encoding='utf-8') as salida:
                    # Escribir encabezado
                    salida.write("fecha hora temp rhum pres wdir wspd prcp\n")
        
                    for dt in horas_ordenadas:
                        vals = horas[dt]
        
                        # Calcular humedad relativa
                        rh = calcular_rh(vals['temp'], vals['dew'])
        
                        # Formatear fecha y hora
                        fecha_str = f"{dt[:4]}-{dt[4:6]}-{dt[6:8]}"
                        hora_str = f"{dt[8:10]}:00"
        
                        # Valores o '.' si faltan
                        temp_s = f"{vals['temp']:.1f}" if vals['temp'] is not None else "."
                        rh_s = f"{rh:.1f}" if rh is not None else "."
                        pres_s = f"{vals['slp']:.1f}" if vals['slp'] is not None else "."
                        wdir_s = f"{vals['wdir']:.0f}" if vals['wdir'] is not None else "."
                        wspd_s = f"{vals['wspd']:.1f}" if vals['wspd'] is not None else "."
                        prcp_s = f"{vals['prcp']:.1f}" if vals['prcp'] is not None else "."
        
                        salida.write(
                            f"{fecha_str} {hora_str} {temp_s} {rh_s} {pres_s} {wdir_s} {wspd_s} {prcp_s}\n"
                        )
        
                print(f"✅ Archivo generado: {nombre_archivo}")
        
        if __name__ == "__main__":
            main()
        ```
        
        ---
        
        ### ⚙️ ¿Cómo usarlo?
        
        1. Coloca el script (`extractor_isd.py`) en la misma carpeta donde están tus archivos `.txt` con datos ISD crudos (los que tienen formato como el que me compartiste).
        2. Ejecuta el script:
            
            ```bash
            python extractor_isd.py
            ```
            
        3. El script procesará **todos** los `.txt` de la carpeta, fusionará los datos por estación (código ICAO) y creará un archivo de salida por cada estación encontrada.
        
        ---
        
        ### 📄 Formato del archivo de salida
        
        - **Nombre**: `ICAO-ICAO-AAAAmmdd_AAAAmmdd-ModeloNo.txt`
            
            (ej. `SAEZ-SAEZ-20230101_20230101-ModeloNo.txt`)
            
        - **Contenido** (separado por espacios, con cabecera):
            
            ```
            fecha hora temp rhum pres wdir wspd prcp
            2023-01-01 00:00 22.7 52.2 1012.5 120 6.2 0.0
            2023-01-01 01:00 21.9 54.1 1013.1 110 6.3 0.0
            ...
            ```
            
        - **Valores faltantes**: se reemplazan por un punto (`.`).
        
        ---
        
        ### 🔍 Detalles del parseo y mezcla
        
        | Variable | ¿De dónde se extrae? |
        | --- | --- |
        | **temp** | Sección obligatoria, pos. 88–92 (escala 10). |
        | **rhum** | **No viene directamente**. Se calcula con la temperatura y el punto de rocío usando la fórmula de Magnus. |
        | **pres (SLP)** | Sección obligatoria, pos. 100–104 (escala 10) – disponible en informes `FM-12`. |
        | **wdir** | Sección obligatoria, pos. 61–63 (grados). |
        | **wspd** | Sección obligatoria, pos. 66–69 (escala 10, m/s). |
        | **prcp** | Sección adicional `ADD`, identificadores `AA1` a `AA4` (precipitación líquida acumulada en el período indicado). |
        
        **Nota sobre la frecuencia**:
        
        El script agrupa todos los registros de una misma hora (YYYYMMDDHH). Si hay varios informes en esa hora (ej. `FM-12` y `FM-15`), se fusionan tomando el primer valor no faltante de cada variable. Esto garantiza la mejor cobertura posible y una frecuencia horaria.
        
        ---
        
        ### ⚠️ Consideraciones
        
        - La humedad relativa se calcula a partir de la temperatura y el punto de rocío. Si alguno falta, se escribe `.`.
        - La precipitación se extrae como la **suma** de los campos `AA1`...`AA4`. Si el período indicado (ej. 6 horas) es mayor a 1 hora, el valor escrito corresponde al total de ese período en el momento del informe (no se distribuye horariamente). Esto es coherente con cómo se almacena originalmente.
        - El script solo procesa archivos con extensión `.txt`. Si tus archivos tienen otro nombre, solo cámbiales la extensión.
        
        Si tienes alguna duda o necesitas ajustar algo, ¡avísame!
        
    
    # Datos faltantes: Analisis y procedimiento.
    
    Se probaron diferentes proveedores para obtener el que brinde los datos mas completos para el posterior analisis y entrenamientos de los modelos.
    
    ## **Analisis de los diferentes proveedores:**
    
    Inicialmente se utilizo **metrostat,** resultando en esta cantidad de datos faltantes:
    
    - **Pedido realizado:**
        - **Rango de fechas:** 5 años (01/01/2020 a 01/01/2025).
        - **Estacion:** SAEZ.
        - **Proveedores:** metrostat (Sin algoritmos matematicos).
    - **Resumen datos faltantes:**
        
        Temperatura (°C)                         0/43303 (0.0%)
        Humedad relativa (%)                    21/43303 (0.0%)
        Presion atmosferica (hPa)              471/43303 (1.1%)
        Direccion del viento (grados)          335/43303 (0.8%)
        Velocidad del viento (km/h)              1/43303 (0.0%)
        Precipitacion (mm)                   43303/43303 (100.0%)
        **Total** 16.99%
        
    - **Analisis:**
        - Faltan todos los datos de la precipitacion (100% en frecuencia de una hora).
    - **Conclusion:**
        - Metrostat no expone datos confiables en la precipitacion.
            - Leve falta de datos en la presion, validos para aproximarlos.
        - Los datos dejan de tener el proveedor directo de NOAA apartir del año 2025, asi que limita el analisis a maximo 5 años completos partiendo desde el 2020.
        - Es necesario encontrar otros proveedores preferentemente mas directos para recolectar los datos directamente de la plataforma del NOAA.
    
    ---
    
    Posteriormente se utilizo el **ISD** proporcionado por el **NOAA**, descargado manualmente y creando un script capaz de extraer las variables y adaptarlas.
    
    Se realizo en un solo año para confirmar la falta de datos proveniente del ISD del NOAA, y descargar posibles problemas relacionados a meteostat.
    
    - **Pedido realizado:**
        - **Rango de fechas:** 1 año (2023), descarga manual.
        - **Estacion:** SAEZ.
        - **Proveedores:** ISD (NOAA)
    - **Resumen datos faltantes:**
    **Total de registros:** 8697
        
        
        | Variable | Presentes | Faltantes | % Faltante |
        | --- | --- | --- | --- |
        | temp | 8697 | 0 | 0.0% |
        | rhum | 8697 | 0 | 0.0% |
        | pres | 8556 | 141 | 1.6% |
        | wdir | 8512 | 185 | 2.1% |
        | wspd | 8697 | 0 | 0.0% |
        | prcp | 1195 | 7502 | 86.3% |
        | **TOTAL** | **44354** | **7828** | 15.0% |
    - **Analisis:**
        - Se incluyeron datos como la precipitacion acumulada cada 6 horas, permitiendo obtener un resultado mas completo de esta variable (aprox 13.7%).
        - Sin embargo el analisis queda limitado hasta mediados de 2025.
    - **Conclusion:**
        - Obtuvimos datos mas completos, pero sigue habiendo inconsistencias graves en la variable precipitacion.
        - De debe encontrar una alternativa para poder abordar la falta de la metrica de exito.
    
    ---
    
    Luego se utilizo la base de datos del **GHCNh**, para recolectar los datos actuales, completos (muchas variables) y con soporte longevo verificado por la **NOAA**.
    
    - Inicialmente se utilizo una **libreria de python llamada “meteora”**, permitiendo extraer los datos de las 6 variables necesarias directamente del GHCN.
    - **Pedido realizado:**
        - **Rango de fechas:** 5 años (01/01/2020 a 01/01/2025).
        - **Estacion:** SAEZ.
        - **Proveedores: meteora (Programa opensource que extrae los datos directamente del GHCN)**
    - **Resumen datos faltantes:**
    **Total registros:** 47,993
        
        
        | **Variable** | **% Datos faltantes** |
        | --- | --- |
        | Temperatura (°C) | 0.00% |
        | Humedad Relativa (%) | 0.01% |
        | Presión Estación (hPa) | 11.45% |
        | Precipitación (mm) | 100.00% |
        | Velocidad Viento (m/s) | 0.04% |
        | Dirección Viento (°) | 0.04% |
        | **TOTAL GENERAL** | **18.59%** |
    - **Analisis:**
        - Provee un dataset  completo en la mayoria de variables exeptuando la presion y precipitacion donde comienza a fallar notablemente.
    - **Conclusion:**
        - Si el dataset no contiene la variable precipitacion en la mayoria de los casos, se debera utilizar otra variable para suplantar la metrica de exito.
    
    **Por ultimo se utilizo el dataset directo GHCN de la NOAA.** Para esto se tuvo que crear un script que permitiera descargar, interpretar y organizar los datos para poder recolectar las varaibles necesarias en los periodos indicados.
    
    Se realizo para confirmar las metricas obtenidas por la libreria meteora y complementar con variables extras que provee el GHCNh.
    
    - **Pedido realizado:**
        - **Rango de fechas:** 5 años (01/01/2020 a 01/01/2025).
        - **Estacion:** SAEZ.
        - **Datos directamente del GHCNh, descargados manualmente.**
            - **URL (Variar año):** [https://www.ncei.noaa.gov/oa/global-historical-climatology-network/hourly/access/by-year/2020/psv/GHCNh_ARI0000SAEZ_2020.psv](https://www.ncei.noaa.gov/oa/global-historical-climatology-network/hourly/access/by-year/2020/psv/GHCNh_ARI0000SAEZ_2020.psv)
    - **Resumen de los datos:**
    - 
    - **Analisis:**
        - Sufre el mismo problema que meteora, sin embargo ofrece diferentes variables utiles que no se incluyen en meteora, al ofrecerlas en un porcentaje tan reducido, no permite un analisis adecuado.
    - **Conclusion: El problema esta en los datos que el SMN transmite al MWO, que a su ves es retransmitido por el NOAA.**
    
    - **Resumenes de los scripts e investigacion.**
        - **Investigacion**
            
            Extraer datos meteorológicos horarios del GHCNh (NOAA) para estaciones argentinas (SAEZ/Ezeiza y SACO/Córdoba) sin usar la librería meteora, accediendo directamente a los archivos PSV.
            
            1. **Estaciones identificadas en GHCNh:**
                - SAEZ (Ezeiza): ARI0000SAEZ (ICAO-based) o ARU00087576 (WMO-based)
                - SECO (Córdoba - Ambrosio Taravella): ARI0000SACO (ICAO-based) o ARU00087344 (WMO-based)
                - Coordenadas confirmadas desde el station list de GHCNh
            2. **Acceso directo a datos GHCNh (investigado):**
                - PSV files por estación/año: [https://www.ncei.noaa.gov/oa/global-historical-climatology-network/hourly/access/by-year/{year}/psv/GHCNh_{STATION_ID}_{year}.psv](https://www.ncei.noaa.gov/oa/global-historical-climatology-network/hourly/access/by-year/%7Byear%7D/psv/GHCNh_%7BSTATION_ID%7D_%7Byear%7D.psv)
                - PSV files por estación (periodo completo): [https://www.ncei.noaa.gov/oa/global-historical-climatology-network/hourly/access/by-station/GHCNh_{STATION_ID}_por.psv](https://www.ncei.noaa.gov/oa/global-historical-climatology-network/hourly/access/by-station/GHCNh_%7BSTATION_ID%7D_por.psv)
                - Formato: 38 variables, pipe-separated, columnas: STATION, DATE, variable1, variable2, ...
                Variables del GHCNh (38 variables)
                Las que existen en el dataset completo incluyen: temperature, dew_point_temperature, wet_bulb_temperature, relative_humidity, station_level_pressure, sea_level_pressure, altimeter, pressure3hr_change, wind_direction, wind_speed, wind_gust, precipitation, visibility, sky_cover1/2/3, sky_cov_baseht1/2/3, pres_wx_AU1/AU2/AU3, pres_wx_AW1/AW2/AW3, pres_wx_MW1/MW2/MW3, snow_depth, precipitation3_hour, Remarks
                
                **Reemplazo de precipitación:**
                Se estaba investigando qué variables pueden indicar si llovió o no cuando precipitation no está disponible:
                
                - pres_wx (present weather codes): Códigos WMO que describen el clima actual, incluyendo lluvia, nieve, etc. Los códigos 50-55 (drizzle), 60-65 (rain), 66-67 (freezing rain), 68-69 (rain/snow mix), 70-75 (snow), 80-90 (showers) indican precipitación.
                - precipitation_3_hour: Precipitación acumulada en 3 horas
                - snow_depth: Profundidad de nieve.
                
                **Investigación Precipitacion:**
                
                Para remplazar la medida del exito representada por la precipitacion se reviso alternativas:
                Documentación de NOAA (GHCNh), el ASOS User's Guide, y artículos técnicos sobre el sensor LEDWI (Light Emitting Diode Weather Identifier).
                
                1. **Cómo funciona el sensor de clima presente (LEDWI/ASOS)**
                    - NO es un modelo numérico ni probabilístico. Es un sensor óptico directo.
                    - Funciona así: emite un haz de luz infrarroja coherente a través de un path de 1 metro hacia un fotodiodo receptor.
                    - Cuando partículas de precipitación (gotas de lluvia, copos de nieve) atraviesan el haz, crean sombras que modulan la luz.
                    - El patrón de centelleo (scintillation) se analiza espectralmente:
                        - Altas frecuencias (1000-4000 Hz): indica lluvia (casi con certeza)
                        - Bajas frecuencias (75-250 Hz): indica nieve
                        - Espectro mezclado: se reporta como "Unknown Precipitation" (UP)
                    - La intensidad se determina por la potencia de la señal usando la distribución empírica Marshall-Palmer:
                        - Light: hasta 0.10 pulg/hora
                        - Moderate: 0.11-0.30 pulg/hora
                        - Heavy: >0.30 pulg/hora
                2. **Limitaciones conocidas**
                    - No diferencia bien drizzle (llovizna) de lluvia ligera
                    - Precipitación mixta (lluvia+nieve) → reporta "UP" (Unknown)
                    - Precipitación muy leve cerca del umbral de detección puede no detectarse
                    - No detecta bien ice pellets, snow grains, hail
                3. **Variables disponibles en GHCNh para precipitación**
                    - precipitation → Precipitación acumulada horaria (mm, medición directa con balde volcete calefaccionado)
                    - pres_wx_AU1/2/3 → Automated ASOS/AWOS sensors (cualitativo: tipo e intensidad)
                    - pres_wx_AW1/2/3 → Automated sensors worldwide
                    - pres_wx_MW1/2/3 → Manual reports (human observer - muy confiable)
                    - precipitation_3_hour a precipitation_24_hour → Acumulados multi-horarios
                    - snow_depth → Profundidad de nieve
                4. **Cómo funciona el sensor de clima presente (LEDWI/ASOS)**
                    - NO es un modelo numérico ni probabilístico. Es un sensor óptico directo.
                    - Funciona así: emite un haz de luz infrarroja coherente a través de un path de 1 metro hacia un fotodiodo receptor.
                    - Cuando partículas de precipitación (gotas de lluvia, copos de nieve) atraviesan el haz, crean sombras que modulan la luz.
                    - El patrón de centelleo (scintillation) se analiza espectralmente:
                        - Altas frecuencias (1000-4000 Hz): indica lluvia (casi con certeza)
                        - Bajas frecuencias (75-250 Hz): indica nieve
                        - Espectro mezclado: se reporta como "Unknown Precipitation" (UP)
                    - La intensidad se determina por la potencia de la señal usando la distribución empírica Marshall-Palmer:
                        - Light: hasta 0.10 pulg/hora
                        - Moderate: 0.11-0.30 pulg/hora
                        - Heavy: >0.30 pulg/hora
        - **Diseño Scripts y analisis**
            
            Extraer datos meteorológicos horarios del GHCNh (Global Historical Climatology Network hourly) de NOAA para estaciones argentinas (SAEZ/Ezeiza y SACO/Córdoba), sin usar la librería meteora, accediendo directamente a los archivos PSV de NOAA.
            
            1. **Variables para reemplazar precipitación**
            Dos opciones principales:
                - pres_wx (present weather codes): Variable tipo string que describe el clima actual. Los códigos indican explícitamente si llueve/nieva/graniza. Códigos como RA:02 (rain), SN:03 (snow), DZ:01 (drizzle), SH (showers), TS (thunderstorm), -/+ (light/heavy). Disponible como pres_wx_AU1 (automated ASOS/AWOS - primera opción), pres_wx_AW1 (automated sensors), pres_wx_MW1 (manual reports).
                - precipitation_3_hour: Precipitación acumulada en 3 horas, da valor numérico pero no es horario.
            - **Decisión:** Usar pres_wx_AU1 como variable de reemplazo, ya que indica directamente si hubo precipitación en cada hora.
            
            El script contiene:
            
            1. Menú para elegir SECO (SACO) o SAEZ.
            2. Pedir rango de fechas en formato DD/MM/YYYY.
            3. Descargar datos horarios vía HTTP directo a los PSV de NOAA.
            4. 5 variables core: temperature, relative_humidity, station_level_pressure, wind_speed, wind_direction.
            5. 6ta variable (reemplazo precipitación): pres_wx_AU1.
            6. Convertir datos de UTC a ART (America/Argentina/Buenos_Aires)
            7. Reemplazar NaN por "."
            8. Mostrar resumen: cantidad de registros, % faltantes por variable, % faltantes total.
            9. Guardar CSV con separador ; como {SACO|SAEZ}{YYYYMMDD}_{YYYYMMDD}.csv
            
            **Detalles tecnicos:**
            
            1. Usar librerías: requests, pandas, numpy
            2. Datos tecnicos:
                - IDs estación: ARI0000SAEZ y ARI0000SACO
                - URL PSV por año: [https://www.ncei.noaa.gov/oa/global-historical-climatology-network/hourly/access/by-year/{year}/psv/GHCNh_{station_id}_{year}.psv](https://www.ncei.noaa.gov/oa/global-historical-climatology-network/hourly/access/by-year/%7Byear%7D/psv/GHCNh_%7Bstation_id%7D_%7Byear%7D.psv)
                - Valores faltantes: -9999 en los datos numéricos indican missing
                - Zona horaria: UTC original, convertir a ART (UTC-3)
                - Formato fecha output: DD/MM/YYYY HH:MM
                - Separador CSV: ;
                - NaN → "." en el CSV final
            
            **Análisis de los datos disponibles**
            
            Se realizo un script capaz de identificar 19 variables criticas para determinar su porcentaje de disponibilidad en los registros extraidos del GHCNh (NOAA).
            ****6 archivos PSV de SAEZ (2020-2025), 329 columnas cada uno, ~9,500 registros/año = 57,406 registros totales.
            **Variables con datos completos (~100%)**
            
            | Variable | Disponibilidad | Descripción |
            | --- | --- | --- |
            | temperature | 100% | Temperatura |
            | relative_humidity | 100% | Humedad relativa |
            | wind_speed | 100% | Velocidad del viento |
            | wind_direction | 100% | Dirección del viento |
            | visibility | 100% | Visibilidad |
            | dew_point_temperature | 100% | Temperatura de rocío |
            
            **Variables con datos parciales**
            
            | **Variable** | **Disponibilidad** | **Descripción** |
            | --- | --- | --- |
            | station_level_pressure | 88.9% | Presión a nivel de estación |
            | sea_level_pressure | 90.2% | Presión a nivel del mar |
            | wet_bulb_temperature | 88.9% | Temperatura de bulbo húmedo |
            | sky_condition | 89.0% | Condición del cielo |
            | ceiling_height | 87.3% | Altura del techo de nubes |
            | pressure_3hr_change | 83.0% | Cambio de presión 3h |
            | altimeter | 98.2% | Altimetría |
            
            **Variables de precipitación (CRÍTICO)**
            
            | **Variable** | **Disponibilidad** | **Estado** |
            | --- | --- | --- |
            | precipitation | 0% | Vacía |
            | pres_wx_AU1 | 0% | Vacía |
            | pres_wx_AW1 | 0% | Vacía |
            | pres_wx_MW1 | 29.9% | ✓ Observador humano |
            | precipitation_6_hour | 7.4% | ✓ Acumulado 6h |
            | precipitation_24_hour | 1.1% | Muy poco |
    
    ## Conclusiones:
    
    Se analizo principalmente la estacion en ezeiza (SAEZ) y de forma secundaria (SACO) en cordoba. Ambas tienen gran falta de datos relacionados a la precipitacion y confirmacion de lluvia.
    
    Los demas datos de estas estaciones son completos.
    
    Esto no se debe directamente a la estacion, sino a los datos rentramistidos al MWO y posteriormente bolcados en las bases de datos del NOAA.
    
    Al NOAA no tener las variable de precipitacion o similar con los datos completos, nos quedan 2 principales alternativas.
    
    - Buscar un proveedor alternativo confiable que exponga los datos directos transmitidos desde EZEIZA, SACO (cordoba), o otra estacion meteorologica que permita complementar los datos ya recoelctados, tambien que permita validad y verificar los equipos que utilizan para la extraccion de datos. Y que los datos extraidos sean datos crudos para un analisis coherente, y no datos ajustados por algoritmos matematicos.
        - Otra estacion Argentina que cumpla con los estandares del MWO o se pueda determinar y validar con total certeza los dispositivos que utiliza, y que las mediciones transmitidas son realmente los datos crudos del sensor (sin alteraciones de algoritmos matematicos).
        - Obtener el o los datos faltantes (precipitacion/presion atmosferica) desde otro proveedor confiable en frecuencia horaria con un historial de al menos 5 años.
    - Buscar estacion meteorologica validada por el MWO que transmita una cantidad de datos completa para el correcto analisis del modelo. Independientemente del lugar de origen.
    
    ## Investigacion y definicion:
    
    Aqui se plasma la investigacion realizada para encontrar la alternativa ideal para cumplir con esta falta de datos.
    
    ### Resumen
    
    Se investigaron 3 opciones para resolver el problema de datos faltantes de precipitacion en la estacion SAEZ (Ezeiza, Argentina). La **Opcion 3** resulto ser la solucion optima: la estacion **Frankfurt Airport (WMO: 106370 / meteostat ID: 10637)** del Servicio Meteorologico Aleman (DWD) presenta **100% de completitud en todas las variables** (temperatura, humedad, presion, viento y precipitacion) para el periodo 2020-2024, accesible via meteostat.
    
    ---
    
    ### Opcion 1: Fuentes Alternativas de Precipitacion para SAEZ
    
    #### Hipotesis
    
    Encontrar una fuente alternativa que provea datos horarios de precipitacion (o variable equivalente que indique lluvia) para la estacion SAEZ (Ezeiza).
    
    #### Fuentes investigadas
    
    | Fuente | Acceso | Variables | Precipitacion | Estado |
    | --- | --- | --- | --- | --- |
    | **SMN Argentina** (Descarga OpenData) | `ssl.smn.gob.ar/dpd/descarga_opendata.php` | TEMP, HUM, PNM, DD, FF | NO disponible | ✅ Funciona |
    | **IEM METAR** (Iowa Env. Mesonet) | `mesonet.agron.iastate.edu` | tmpf, relh, drct, sknt, mslp, wxcodes | SOLO para EEUU | ⚠️ Sin prcp no-US |
    | **Meteostat** (Ezeiza 87576) | Libreria Python `meteostat` | temp, rhum, prcp, wdir, wspd, pres, coco | 51.5% prcp / 99.6% coco | ✅ Util como complemento |
    | **OGIMET** | [ogimet.com](http://ogimet.com/) | METAR historicos | Datos limitados | ❌ Conexion inestable |
    | **GHCNh RAW (NOAA)** | PSV directo | Todas las variables | **0% para SAEZ** | ❌ Sin datos |
    
    #### Resultado Opcion 1
    
    - SMN provee datos horarios de temperatura, humedad, presion y viento para toda Argentina, incluyendo Ezeiza ("EZEIZA AERO"). Sin embargo, **no incluye precipitacion** en los archivos horarios de descarga abierta.
    - Meteostat para Ezeiza (ID: 87576) ofrece **prcp al 51.5%** y **coco (codigo de clima) al 99.6%**. El codigo coco puede usarse como indicador de lluvia (>99% completo), pero su origen podria incluir datos modelados.
    - **Conclusion**: No es posible obtener una serie completa de precipitacion horaria para SAEZ de forma directa y 100% confiable desde estas fuentes.
    
    ---
    
    ### Opcion 2: Proveedor Alternativo Argentino al NOAA
    
    #### Hipotesis
    
    Encontrar un proveedor argentino (preferentemente SMN) que ofrezca las 6 variables con transparencia de equipos.
    
    #### Fuentes investigadas
    
    | Fuente | Acceso | Variables | Precip | Equipos | Estado |
    | --- | --- | --- | --- | --- | --- |
    | **SMN OpenData** | Descarga directa | TEMP, HUM, PNM, DD, FF | ❌ | Estaciones SMN oficiales | ✅ Libre |
    | **py-smn** (GitHub) | Libreria Python | temp, hum, pressure, wind | ❌ | Misma fuente SMN | ✅ Funciona |
    | **OpenSMN** (GitHub) | API proxy | Misma data SMN | ❌ | Misma fuente SMN | ✅ Alternativa |
    | **SMN API** | `ws.smn.gob.ar` | Variables actuales | ❌ | Requiere token | ⚠️ Limitado |
    | **INA** (Agua) | `alerta.ina.gob.ar` | Datos hidrologicos | ✅ parcial | Red hidrologica | ⚠️ No horario |
    
    #### Resultado Opcion 2
    
    - SMN ofrece datos horarios abiertos y gratuitos (TEMP, HUM, PNM, DD, FF) para toda su red de estaciones.
    - Las estaciones del SMN estan georreferenciadas y documentadas oficialmente (IGN/SMN).
    - **Limitacion**: No incluye precipitacion horaria en los archivos de descarga abierta.
    - **Limitacion**: Los datos disponibles cubren solo ~2017-presente, insuficiente para los 5 años requeridos de forma consistente para todas las estaciones.
    - **Conclusion**: SMN es un excelente complemento para variables core, pero no reemplaza completamente al NOAA para precipitacion.
    
    ---
    
    ### Opcion 3: Estacion WMO Ideal (SOLUCION SELECCIONADA)
    
    #### Hipotesis
    
    Encontrar una estacion WMO en cualquier parte del mundo con <1% de datos faltantes en las 6 variables, accesible via meteostat o meteora.
    
    #### Metodologia
    
    Se evaluaron estaciones de EEUU, Europa y Argentina mediante la libreria meteostat (v2.1.4) para el periodo 2020-2024 (5 años, 43848 registros esperados).
    
    #### Resultados de Estaciones Evaluadas
    
    | Estacion | ID Meteostat | Pais | temp | rhum | prcp | wdir | wspd | pres |
    | --- | --- | --- | --- | --- | --- | --- | --- | --- |
    | **Frankfurt Airport** | **10637** | **Alemania** | **100%** | **100%** | **100%** | **100%** | **100%** | **100%** |
    | London Heathrow | 03772 | Reino Unido | 100% | 100% | **52.0%** | 100% | 100% | 100% |
    | Amsterdam Schiphol | 06260 | Paises Bajos | 100% | 100% | 99.9% | 100% | 100% | 100% |
    | Madrid Barajas | 08495 | España | 100% | 100% | **100%** | 100% | 100% | 100% |
    | Paris CDG | 07145 | Francia | 100% | 100% | 94.1% | 100% | 100% | 100% |
    | Berlin | 10618 | Alemania | 100% | 100% | 97.1% | 100% | 100% | 100% |
    | Rome Fiumicino | 16245 | Italia | 100% | 100% | 97.1% | 100% | 100% | 100% |
    | Miami | 72202 | EEUU | 100% | 100% | 94.8% | 100% | 100% | 100% |
    | JFK New York | 74486 | EEUU | 100% | 100% | 93.9% | 100% | 100% | 100% |
    | San Diego | 72293 | EEUU | 100% | 100% | 95.5% | 99.7% | 100% | 99.9% |
    | Ezeiza (ref) | 87576 | Argentina | 100% | 100% | 51.5% | 100% | 100% | 100% |
    
    ### Estacion Seleccionada: Frankfurt Airport (ID: 10637)
    
    #### Informacion de la Estacion
    
    - **Nombre**: Frankfurt Airport (Frankfurt am Main)
    - **ID WMO**: 106370 / 103690 (10637)
    - **ID Meteostat**: 10637
    - **ID GHCNh**: GM0000010690
    - **Pais**: Alemania (DE)
    - **Coordenadas**: 50.05N, 8.60E
    - **Elevacion**: 100 m
    - **Operador**: Deutscher Wetterdienst (DWD) - Servicio Meteorologico Aleman
    - **Red**: DWD synoptic network, miembro de WMO
    
    #### Equipamiento (documentado por DWD)
    
    DWD utiliza en sus estaciones sinopticas de aeropuerto:
    
    - **Termometro**: PT100 de precision, proteccion contra radiacion
    - **Higrometro**: Capacitivo, en abrigo meteorologico
    - **Pluviometro**: Pluviometro de pesado (weighing rain gauge) o de balancin, calibrado, con calefaccion antihelada
    - **Barometro**: Barometro digital de precision
    - **Anemometro**: Anemometro ultrasonico 2D/3D
    - **Veleta**: Sensor de direccion de viento ultrasonico
    - **Calidad de datos**: DWD aplica control de calidad WMO, datos no ajustados por modelos matematicos
    
    #### Acceso a Datos
    
    - **meteostat** (libreria Python): `ms.Station(id='10637')`
    - **GHCNh (NOAA)**: ID `GM0000010690`
    - **DWD OpenData**: `opendata.dwd.de`
    
    #### Completitud (2020-2024)
    
    | Variable | Completitud | Registros |
    | --- | --- | --- |
    | Temperatura (temp) | **100.0%** | 43848/43848 |
    | Humedad (rhum) | **100.0%** | 43848/43848 |
    | Precipitacion (prcp) | **100.0%** | 43848/43848 |
    | Direccion Viento (wdir) | **100.0%** | 43848/43848 |
    | Velocidad Viento (wspd) | **100.0%** | 43848/43848 |
    | Presion (pres) | **100.0%** | 43848/43848 |
    
    #### Estadisticas de Precipitacion (2020-2024)
    
    - Total acumulado: 3246.9 mm
    - Horas con precipitacion > 0: 4028 (9.2%)
    - Maxima horaria: 29.60 mm
    - Promedio cuando llueve: ~0.81 mm/h
    
    ---
    
    ### Comparativa de Opciones y Decision Final
    
    | Criterio | Opcion 1 (SAEZ+MET) | Opcion 2 (SMN) | Opcion 3 (Frankfurt) |
    | --- | --- | --- | --- |
    | Completitud temp | 100% | 100% | **100%** |
    | Completitud hum | 100% | 100% | **100%** |
    | Completitud prcp | 51.5% / 99.6%coco | 0% | **100%** |
    | Completitud wind | 100% | 100% | **100%** |
    | Completitud pres | 100% | 100% | **100%** |
    | Datos reales (no modelo) | ⚠️ Dudoso coco | ✅ Confirmado | ✅ Confirmado |
    | Transparencia equipos | ⚠️ Parcial | ✅ SMN/IGN | ✅ DWD documentado |
    | WMO certified | ✅ SI | ✅ SI | ✅ SI |
    | Acceso meteostat | ✅ SI (51.5% prcp) | ❌ No | ✅ SI |
    | Periodo 5 años | ✅ 2020-2024 | ⚠️ Limitado | ✅ 2020-2024 |
    | Datos crudos | ⚠️ Parcial | ✅ | ✅ |
    
    ### **Solucion Final: Opcion 3 - Frankfurt Airport via meteostat**
    
    Se complementa con:
    
    1. **Script para Ezeiza (SAEZ)** via meteostat para quienes necesiten datos argentinos
    2. **Script para SMN** para obtener datos de estaciones argentinas (sin precipitacion)
    
- **¿Qué umbral de tolerancia a datos faltantes voy a aplicar y por qué?**
    
    En el contexto del preprocesamiento de datos, el **umbral de tolerancia a datos faltantes es el porcentaje máximo de valores ausentes que se permiten en un período de tiempo (por ejemplo, una hora, un día o un mes) para considerar que ese período es válido y puede ser utilizado en el análisis**.
    
    **El umbral de tolerancia cumple 2 funciones principales:**
    
    - **Asegurar la calidad de los datos:** Si faltan demasiados datos, cualquier valor que calcules a partir de
    ese período (por ejemplo, la media horaria de temperatura) será poco
    fiable y podría sesgar tu modelo.
    - **Equilibrar la integridad de la serie temporal:** Un umbral demasiado estricto (ej: 0% de tolerancia) haría que descartes muchos períodos, reduciendo drásticamente tu conjunto de datos de
    entrenamiento. Un umbral demasiado laxo (ej: 50%) permitiría la entrada
    de datos de baja calidad, comprometiendo la precisión de tu modelo
        
        El umbral busca el equilibrio entre calidad y cantidad de datos.
        
    
    **Umbral de tolerancia elegido:**
    
    Se decidio tomar como maximo porcentaje de datos faltantes un “20%” total, para lograr un balance que permita un analisis lo mas fiable a la realidad con un dataset incompleto.
    
    En el caso de datos faltantes continuos se plantea el siguiente cuadro de intervalos validos.
    
    | Variable | Umbral Máximo para Interpolación | Método Recomendado |
    | --- | --- | --- |
    | **Temperatura** | Hasta 3-4 horas | Interpolación Lineal o Spline |
    | **Presión** | Hasta 3-4 horas | Interpolación Lineal o Spline |
    | **Humedad** | 1-2 horas | Interpolación Lineal |
    | **Viento (Vel. y Dir.)** | 1-2 horas | Interpolación Lineal |
    | **Precipitación** | No interpolar - 1 hora | Marcar como dato faltante |
    
    Las variables clave son: precipitacion (datos consecutivos y muy variantes) que pueden generar datos erroneos facilmente al no seguir una tendencia bien marcada. Pudiendo ignorar lluvia en momento donde si sucedio o viseversa.
    
    La lluvia es un evento discreto y muy localizado que puede comenzar y terminar en cuestión de minutos.
    
    Se planteo el umbral maximo recomendado n base al metodo interpolacion lineal y Interpolación Spline (Cúbica), metodos muy simples de implementar y que permiten, en lagunas cortas de datos faltantes, predecir con alta fiabilidad los datos reales.
    
    **Fuentes:**
    
    https://repositorio.smn.gob.ar/bitstream/handle/20.500.12160/2724/Nota_Tecnica_SMN_2024-167.pdf?sequence=1&isAllowed=y 
    
    https://beta.iopscience.iop.org/article/10.1088/1742-6596/3191/1/012078/meta
    
    https://rmets.onlinelibrary.wiley.com/doi/abs/10.1002/joc.5836
    
    https://zgnyqx.ieda.org.cn/EN/Y2018/V39/I03/195
    
- **¿Qué método usaré para imputar o interpolar los datos faltantes?**
    
    Los datos faltantes son un gran problema para el correcto entrenamiento y diseño del modelo propuesto. Debido a ello se utilizara uno/varios metodos para la complementacion del dataset utilizado en caso de que falte informacion.
    
    #### Metodos para manejar datos faltantes
    
    1. **Interpolación lineal**: Si el período sin datos es corto (algunas horas), es el método estándar y aceptado, asumiendo una variación suave de las variables meteorológicas.
        1. En un caso extremo se pueden utilizar metodos mas complejos.
    2. **Eliminación de períodos**: Si la laguna es extensa, lo más riguroso es excluir ese período del análisis.
    3. **Múltiples estaciones**: Si tienes datos de una estación cercana, se pueden usar para estimar los valores faltantes mediante correlación.
    
    Los datos faltantes en periodos cortos y continuos (segun la variable) se abordaran con interpolacion lineal. Buscando tener un set de datos completo y confiable para el entrenamiento del modelo.
    
    **Interpolacion Lineal:** Traza una línea recta entre el valor anterior y el siguiente, y coloca los puntos faltantes en esa línea.
    
    Humedad, viento y precipitacion (solo en rangos muy cortos).
    
    **Interpolación Spline (Cúbica):** Ajusta una curva suave entre los puntos, en lugar de una línea recta.
    
    Presion y temperatura.
    
    En el caso de lagunas largas (+5h) se buscara rellenar los datos con proveedores alternativos o modelos mas complejos que permitan mantener la confiabilidad de los datos generados en relacion a los datos reales.
    
    En el caso de no poder rellenar la laguna de datos de forma confiable (porcentaje de error del ≥ 20%) los datos no se completaran. Quedando vacios ante el analisis.
    
- **¿Cómo identificaré y trataré los outliers (valores anómalos)?**
    
    Los outliners son valores anomalos dentro de los datos utilizados.
    
    Un valor anomalo es una medida que se diferencia de forma muy marcada del resto de datos, osea del promedio. 
    
    - Son datos que rompen el patron del resto de datos.
    
    ### Tipos
    
    Existen 2 tipos de outliners
    
    - Estadisticos: Son valores anomalos reales que salen de forma muy marcada del promedio comun de los datos.
    - Medicion: Son errores de medicion que resultan en valores fuera del promedio (anomalos).
    
    ### Como afectan al modelo
    
    **¿Existen errores de medicion en los datos?**: No en su mayoria, el DWD se encarga de abordar estos valores anomalos producidos por errores de medicion y corregirlos o en el peor de los casos no informalos, permite que los datos utilizados en el dataset sean coeherentes entre si.
    
    - Tabla de errores groseros/imposibles:
    - La WMO (1993) define límites explícitos de "suspect" y "erroneous" para cada variable, implementados en el test wmo_gross_errors de dataresqc:
    
    | Variable | Límite "suspect" (ej. lat 45±, invierno) | Límite "erroneous" | Fuente |
    | --- | --- | --- | --- |
    | Presión (estación) | 300-400 ó 1080-1100 hPa | <300 o >1100 hPa | WMO 1993, VI.7 |
    | Presión (nivel mar) | 910-940 ó 1080-1100 hPa | <910 o >1100 hPa | WMO 1993 |
    | Temperatura | −90 a −80°C ó +35 a +40°C | <−90 o >+40°C | WMO 1993 |
    | Punto de rocío | −99 a −85°C ó +30 a +35°C | <−99 o >+35°C | WMO 1993 |
    | Viento | 50-125 m/s | >125 m/s | WMO 1993 |
    | Humedad relativa | — (tiene su propio test de errores en dataresqc, variable acotada 0-100%) | — | dataresqc |
    - **Nota clave:** existe un test separado específico para Humedad Relativa y Cobertura Nubosa ("Gross Errors Test for Cloud Cover and Relative Humidity"), porque la humedad tiene su propio patrón de error (los sensores capacitivos se saturan/contaminan cerca del 100% — Bell 2015).
    
    **¿Que problemas pueden causar los outliners estadisticos?**: El principal problema que existe con este tipo de valores, es que minimizan los valores normales, provocando que los cambios precursores de una tormenta (pequeñas variaciones) pasen desapercibidas para el modelo.
    
    ### Como se abordaran
    
    **¿Como se deberan tratar los outliners estadisticos?:** Se deberan transformar antes de normalizarlos para su utilizacion en el entrenamiento, permitiendo que el modelo se pueda adaptar de forma adecuada a estos valores anomalos.
    
    **¿Que metodos se utilizaran?:**
    
    1. Se analizara primero que variable/s son las que provocan valores anomalos mas seguido.
        - No todas las variables producen valores anomalos con la misma intensidad, eso genera que se clasificen segun la intensidad con la que pueden cambiar.
        - Esto está directamente documentado en los valores por defecto del test de outliers del paquete dataresqc (herramienta oficial del Copernicus Data Rescue Service, C3S):
        
        | Variable | Distribución estadística | ¿Produce outliers (Tipo A)? | Fuente |
        | --- | --- | --- | --- |
        | Precipitación | Zero-inflated (muchos ceros) + cola pesada | SÍ, en abundancia — por eso necesita IQR=5 (el más amplio) | dataresqc (C3S); Marra, Amponsah & Papalexiou (2023) |
        | Velocidad del viento | Weibull, cola larga hacia velocidades altas | Sí, rachas extremas son la cola de la Weibull | Monahan (2006); Rehman et al. (2024); NIST "Peaks Over Threshold" |
        | Temperatura | ~Normal (gaussiana) | Pocos reales — por eso usa IQR=3 (el más estrecho) | dataresqc (C3S) |
        | Presión | ~Normal | Muy pocos — rango físico acotado | dataresqc (C3S) |
        | Humedad relativa | Acotada 0, 100% | Muy pocos reales — acotada físicamente | dataresqc (C3S) |
        | Direccion del viento | -No se aplican metodos lineales debido a sus datos circulares | - | Fisher, N.I. (1993) |
        - **Conclusión:** La precipitación es la variable que produce más valores anómalos con diferencia, seguida del viento. Temperatura, presión y humedad tienen distribuciones "bien portadas" y sus extremos reales son raros.
        - **Casos especiales:**
            - **Humedad relativa:**
            - **Direccion del viento:** No se normaliza en grados. Se descompone en componentes u/v (seno/coseno) y esas componentes sí se normalizan con z-score como las demás.
                - Consiste en descomponer la dirección en componentes cartesianas u/v, que vuelven a ser lineales:
                    
                    u = WS · sin(dir)     (componente Este-Oeste)
                    v = WS · cos(dir)     (componente Norte-Sur)
                    
                    Serpa-Usta et al. (2025), Atmosphere 16(11), 1292, DOI: 10.3390/atmos16111292 (https://www.mdpi.com/2073-4433/16/11/1292)
                    
    2. Se identificaran las estrategias para preprocesar los valores de esta variable, permitiendo abordar los valores anomalos.
        - El objetivo es comprimir los valores de gran escala para lograr una coherencia entre datos, y que no se minimicen entre ellos.
            - Al haber eliminado casi por completo los errores groseros de las variables, se utilizaran metodos para los outliners unicamente en las variables que lo necesiten. (fueron filtradas por QC institucional)
            - Transformaciones inapropiadas inducen artefactos estadísticos en series climáticas.
        - Se divide en 2 pasos: PASO 1 (transformación global) → PASO 2 (normalización).
        - Aqui se detalla el metodo que se utilizara para cada variable:
    
    | **Variable** | **Distribución** | **¿Transformar outliers?** | **Método** | **Justificación** |
    | --- | --- | --- | --- | --- |
    | **Precipitación** | Zero-inflated + cola pesada (gamma en positivos) | SÍ — prioridad máxima | log(1+x) luego z-score, o binaria 0/1 | Cola pesada documentada (Marra et al., 2023). dataresqc usa IQR=5 (el más amplio) y excluye ceros. Min-max sin transformar aplasta la lluvia normal |
    | **Velocidad del viento** | Weibull, sesgada a valores altos | SÍ — moderado | Z-score robusto (mediana/MAD) o Winsorización al percentil 99 | Distribución Weibull (Monahan, 2006). dataresqc IQR=4. Las ráfagas son físicamente reales (señal), no deben borrarse — solo evitar que distorsionen σ |
    | **Dirección del viento** | Circular [0°,360°) | Caso especial (no es outlier lineal) | Descomponer en u/v (seno/coseno) → normalizar esas componentes | No puede tratarse como lineal (Fisher, 1993). Outliers circulares se detectan con distancia circular robusta (Mahmood et al., 2017) |
    | **Temperatura** | ~Normal, acotada por clima | NO |  |  |
    | **Presión** | ~Normal, rango estrecho (950–1050 hPa) | NO |  |  |
    | **Humedad relativa** | Acotada 0,100% | NO |  |  |
    
    ---
    
    ### Fuentes
    
    El Hachem, A., Seidel, J., Imbery, F., Junghänel, T. & Bárdossy, A. (2022) — "Technical Note: Space–time statistical quality control of extreme precipitation observations". HESS, 26, 6137–6146. DOI: 10.5194/hess-26-6137-2022: https://hess.copernicus.org/articles/26/6137/2022/
    
    Furtado, Molina et al. (2026) — arXiv (Manejo de distribuciones no-normales y valores extremos en preprocesamiento climático.): https://arxiv.org/abs/2508.07062
    
    Brugnara, Y. et al., dataresqc: C3S Quality Control Tools for Historical Climate Data (R package v1.1.1, Apache 2.0). Funciones wmo_gross_errors (presión, temperatura, rocío, viento) y Gross Errors Test for Cloud Cover and Relative Humidity: https://ybrugnara.r-universe.dev/dataresqc/doc/manual.html#help-index
    
    OMM-N° 49. Reglamento Técnico, Volumen I — Normas meteorológicas de carácter general y prácticas recomendadas: ****https://library.wmo.int/es/records/item/32655-reglamento-tecnico-volumen-i-normas-meteorologicas-de-caracter-general-y-practicas-recomendadas
    
    Monahan, A. H. (2006). The Probability Distribution of Sea Surface Wind Speeds. Part II: Dataset Intercomparison and Seasonal Variability. *Journal of Climate*, *19*(4), 521-534. [https://doi.org/10.1175/JCLI3641.1](https://doi.org/10.1175/JCLI3641.1) https://journals.ametsoc.org/view/journals/clim/19/4/jcli3641.1.xml
    
    Fisher, N.I. (1993), Statistical Analysis of Circular Data (Cambridge University Press) — texto de referencia que establece que los datos circulares no pueden tratarse con métodos lineales, sino con distancia circular y estadísticos direccionales. ([https://www.cambridge.org/core/books/statistical-analysis-of-circular-data/324A46F3941A5CD641ED0B0910B2C33F](https://www.cambridge.org/core/books/statistical-analysis-of-circular-data/324A46F3941A5CD641ED0B0910B2C33F))
    
    Mahmood et al. (2017) — outliers circulares con distancia robusta. DOI: 10.22237/jmasm/1509495720: https://digitalcommons.wayne.edu/jmasm/vol16/iss2/22/
    
    Sippel, et al. (2015), *Quantifying changes in climate variability and extremes: Pitfalls and their overcoming*, *Geophys. Res. Lett.*,  42, doi:[10.1002/2015GL066307](https://doi.org/10.1002/2015GL066307). https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2015GL066307
    
    Bell, Simon (2015). Quantifying uncertainty in citizen weather data. PHD thesis, Aston University. https://publications.aston.ac.uk/id/eprint/26693/
    
- **¿Qué ventana temporal de entrada (lookback window) usaré?**
    
    **La ventana temporal se define como:** El número de puntos de datos actuales que deben utilizarse para predecir cada cantidad futura.
    
    - Referencia al “historial” de datos que el modelo utiliza como entrada para predecir datos futuros.
    - Es fundamental utilizar una ventana de tiempo suficiente para lograr una prediccion optima del evento climatico.
    - Las ventanas temporales permiten:
    
    ### Investigacion de ventanas temporales:
    
    Se busca identificar la ventana temporal de entrada optima para el modelo a desarrollar.
    
    - El dato fundamental para esta desicion, es la frecuencia en la que se entregan los datos, la cual es “1h”.
    
    #### Preguntas de la investigacion:
    
    **¿Porque se utilizan ventanas temporales?**
    
    1. **Capturar dependencias temporales**: Los fenómenos meteorológicos no son instantáneos; se forman a lo largo de horas. La ventana permite al modelo aprender la evolución de las variables (caída de presión, aumento de humedad, cambio de viento, etc…) que precede a la lluvia.
    2. **Proporcionar contexto**: Una sola medición horaria (ej. 1012 hPa) no dice nada sobre si la presión está cayendo o subiendo. Con una ventana de varias horas, el modelo puede identificar tendencias y tasas de cambio, que son mucho más informativas que los valores absolutos.
    3. **Reducir el ruido**: Las mediciones individuales pueden tener ruido o fluctuaciones aleatorias. Una ventana temporal permite al modelo promediar o integrar la información, haciendo la detección más robusta.
    
    **¿Que relacion tiene la ventana temporal con el modelo matematico LIF?**
    
    - El modelo LIF es una neurona que integra ****corriente de entrada a lo largo del tiempo hasta alcanzar un umbral, momento en el cual "dispara" un spike y reinicia su potencial de membrana. Su dinámica temporal está definida por la **constante de tiempo de membrana** (τ_mem), que determina qué tan rápido se acumula y "fuga" la información.
    - El rendimiento de una red LIF depende críticamente del tamaño de la ventana espacial (spiking window). Un estudio evaluó ventanas de 10 y 50 pasos de tiempo, encontrando que existe una compensacion entre rendimiento y consumo energético según el tamaño de ventana elegido.
    
    **¿Que rango de ventana temporal resulta optimo para idenitificar la tendencia de una lluvia?**
    
    - **La ventana óptima escala con el horizonte de predicción**: Para predicciones a corto plazo (1-6 horas), ventanas cortas (3-6 horas) son suficientes.
    - **Cuadro comparativo de fuentes: Señales precursoras**
        
        
        | Estudio | Señal precursora | ¿Con cuánta antelación? | Detectable a 1h? |
        | --- | --- | --- | --- |
        | [Wang & Hocke (2022) — 1199 eventos, Suiza](https://www.mdpi.com/2072-4292/14/12/2938) | IWV aumenta sostenidamente | 6-8 h antes | Sí |
        |  | Temperatura 2m → máximo | 30-60 min antes | Sí (Limite) |
        |  | Presión → mínimo | 30-60 min antes | Sí (Limite) |
        |  | Densidad del aire → disminuye | 2-6 h antes (60% eventos) | Sí |
        | [Haas et al. (2025) — 94 eventos, Austria](https://wcd.copernicus.org/articles/6/949/2025/) | IWV, CAPE, viento aumentan | 8 h antes | Sí |
        |  | LWP (agua líquida) → aumento brusco | 1 h antes | Sí |
        |  | Variabilidad espacial T2m → aumenta | 2 h antes | Sí |
        | [Li et al. (2023) — HK, 12 años](https://www.mdpi.com/2073-4433/14/3/571) | PWV/ZTD → lead time | ~8 h antes | Sí |
        |  | Temperatura bulbo húmedo → lead time | 5-8 h antes | Sí |
        | [Xue et al. (2024)— Tibet](https://www.mdpi.com/2073-4433/15/8/934) | PWV salto abrupto | 8 min antes | No |
    
- **¿Simulare sensores de bajo costo?**
    
    Debido a la necesidad de un historial verificable y ampleo se necesitaron extraer datos de una estacion meteorologica que contiene equipos de analisis profesionales.
    
    Esto provoca que el modelo no este adaptado al ruido y comportamiento natural de sensores de bajo costo. Quedando 2 opciones.
    
    #### 1. Simular comportamiento de sensores a bajo costo:
    
    Esto lleva a realizar las siguientes preguntas:
    
    - **¿Que lugares documentados utilizan sensores de bajo costo y umbrales fijos?**
    - **¿Qué características de los sensores de bajo costo necesito simular?**
    - **¿Cuáles son los errores documentados de los sensores que usaré?**
    - **¿Cómo y cual ruido modelaré?**
    - **¿Cómo validaré que la simulación es realista?**
    
    #### 2. Descartar el analisis dedicado a sensores de bajo costo.
    
    Se puede delegar el analisis con datos provenientes de sensores de bajo costo para investigaciones posteriores.
    
    “En esta primera parte de la investigacion buscara diseñar un modelo capaz de predecir lluvia de forma eficaz, y la adaptacion a sensores de bajo costo se realizara en estudios posteriores.”
    
    ### Conclusion:
    
    Para esta investigacion diseñare 2 instancias entrenadas con datos sin ruido y con ruido.
    
    Esto permitira identificar la diferencia de precision entre los datos reales y los expuestos al ruido (simulando la extraccion desde sensores de bajo costo). Y comprobara la flexibilidad del modelo para adaptarse a diferentes calidades de datos.
    
    Se realizo una investigacion propia de los sensores de bajo costo, sus estaciones, y metodos de prediccion.
    
    ### Investigacion: Simular datos de sensores de bajo costo.
    
    **Propósito:** Determinar cómo simular sensores de bajo costo, con sus errores y ruido para adaptar el modelo LIF a condiciones realistas de implementación.
    
    ---
    
    ## Índice
    
    1. Pregunta 1: ¿Es viable el uso de sistemas complejos externos (IA/satélites) ante la falta de sistemas en tierra?
    2. Pregunta 2: ¿Porque simular sensores de bajo costo? — Análisis de decisión
    3. Pregunta 2.1: ¿Qué lugares documentados utilizan sensores de bajo costo?
    4. Pregunta 2.2: ¿Que sistemas de prediccion utilizan las estaciones de bajo costo?
    5. Pregunta 2.3: ¿Qué características de sensores necesito simular?
    6. Pregunta 2.4: ¿Cuáles son los errores documentados de los sensores?
    7. Pregunta 2.5: ¿Cómo y qué ruido modelaré?
    8. Resumen
    
    ---
    
    ## Pregunta 1: ¿Es viable el uso de sistemas complejos externos (IA/satélites) ante la falta de sistemas en tierra?
    
    ### Respuesta: Cada sistema tiene un rol complementario, no sustitutivo
    
    #### 1.1 Satélites: No reemplazan estaciones en tierra
    
    Los satélites meteorológicos **no son sustitutos** de las estaciones en tierra (WMO, 2019 — *Visión del Sistema Mundial Integrado de Observación de la OMM para 2040*, WMO-No. 1243):
    
    | Limitación | Detalle |
    | --- | --- |
    | **Precisión inferior** | Radiosondeos tienen precisión de temperatura de 0.1 K y error de humedad ~2-3%, un orden de magnitud mejor que los mejores sensores satelitales |
    | **Resolución temporal insuficiente** | Satélites geoestacionarios muestrean cada 15-30 min; polares cada 6-12h. Un evento convectivo de 18 min puede ocurrir entre pasadas |
    | **Mediciones indirectas** | No miden temperatura superficial ni precipitación directamente; estimaciones derivadas de radianzas con incertidumbre significativa |
    | **Registros cortos** | ~40 años vs. 70+ años de estaciones en tierra (EDDF desde 1949) |
    
    **Cita textual WMO (edición en español de WMO-No. 1243):**
    
    > *"Ciertas variables son difíciles de medir desde el espacio... En ese caso, las mediciones en superficie seguirán desempeñando un papel fundamental.""Incluso en regiones en las que las capacidades espaciales son sólidas, las observaciones en superficie siguen siendo importantes para la calibración y la validación."*
    > 
    
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
    | Mao & Sorteberg (2026) — Noruega | Post-procesamiento ML de nowcasts NWP usando observaciones crowdsourced | Sí (ML) | Indirecto |
    | AMT (2026) — KNMI/HOASIS | Evaluación de estaciones compactas AiOWS. No hacen predicción — solo evalúan calidad de los sensores | No | No |
    
    > Las redes de estaciones de bajo costo existentes (Netatmo, CWOP, Sensor.Community, Weather Underground) no aplican IA ni fusión satelital para predicción. Usan mayoritariamente umbrales fijos (Zambretti, tendencias de presión) o modelos NWP estándar. Esto significa que tú no estarías en desventaja si tu modelo LIF tampoco usa satélites. De hecho, un enfoque con SNN/LIF para clasificación basada solo en datos de sensores en tierra sería más avanzado que lo que estas redes usan actualmente.
    > 
    
    ### Conclusión P1
    
    | Sistema | ¿Por qué no es fuente principal? | ¿Complemento? |
    | --- | --- | --- |
    | **Satélites** | Precisión inferior, medición indirecta, resolución temporal insuficiente | Sí |
    | **IA** | Requiere datos de estaciones para entrenar; no genera datos nuevos | Sí |
    | **Radar** | No mide superficie directamente, requiere calibración | Sí |
    
    ---
    
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
    
    ## Pregunta 2.1: ¿Qué lugares documentados utilizan sensores de bajo costo?
    
    ### 1. Red Netatmo / Estudio KNMI (global)
    
    - **Sensores:** Estación todo-en-uno compacta
    - **Estudio clave:** *Performance and longevity of compact all-in-one weather stations* (AMT, 2026)
    - **Hallazgo:** Temperatura útil si se gestiona; humedad, viento y precipitación fallan sin mantenimiento regular
    - **DOI:** [https://amt.copernicus.org/articles/19/3001/2026/](https://amt.copernicus.org/articles/19/3001/2026/)
    
    ### 2. CWOP — Citizen Weather Observer Program (NOAA, EEUU)
    
    - **Sensores:** Variados (Davis, estaciones caseras)
    - **Protocolo:** Datos cada 5-15 min, QC automatizado
    - **Estudio clave:** Bell, Simon (2015). Quantifying uncertainty in citizen weather data. PHD thesis, Aston University. — tesis doctoral sobre cuantificación de incertidumbre en datos ciudadanos, incluye estudio de deriva en servicio de sensores de humedad
    - **Hallazgo:** Sensores de humedad desarrollan bias positivo a humedades bajas/medias y bias negativo a >90% RH por contaminación del polímero capacitivo (confirmado por Brown et al., 2026)
    
    ### 3. Sensor.Community / [Luftdaten.info](http://luftdaten.info/) (global)
    
    - **Sensores:** DHT22, BME280, SDS011
    - **Enfoque:** Calidad del aire + temperatura/humedad
    - **Enlace:** [https://sensor.community/](https://sensor.community/)
    
    ### 4. Open Weather Map (global)
    
    - Integra estaciones ciudadanas de diversos fabricantes
    - **Enlace:** [https://openweathermap.org/](https://openweathermap.org/)
    
    ### Tabla resumen caracteristicas
    
    | Proyecto | Sensores | Resolución | Referencia |
    | --- | --- | --- | --- |
    | Netatmo/KNMI | AiOWS compactos | 5-15 min | AMT, 2026 |
    | CWOP (NOAA) | Davis, varios | 5-15 min | Bell, 2015 |
    | Sensor.Community | DHT22, BME280 | 2-5 min | Open Data |
    | Open Weather Map | Estaciones ciudadanas | Variable | OWM API |
    
    ### Ubicaciones exactas de las redes documentadas
    
    | Red | Cantidad | Ubicaciones principales | URL de mapas |
    | --- | --- | --- | --- |
    | CWOP | ~10,000+ | EE.UU. (mayoría), algunos en Canadá, Europa, Australia | [http://wxqa.com/memberlists.html](http://wxqa.com/memberlists.html) / [https://www.weather.gov/media/epz/mesonet/CWOP-OfficialGuide.pdf](https://www.weather.gov/media/epz/mesonet/CWOP-OfficialGuide.pdf) |
    | Netatmo | ~100,000+ | Global (170+ países) — mayor concentración en Europa (Francia, Alemania, UK), USA, Japón | [https://weathermap.netatmo.com](https://weathermap.netatmo.com/) |
    | Weather Underground | 250,000+ | Global — USA, Europa, Australia, Japón, Brasil | [https://www.wunderground.com/pws/overview](https://www.wunderground.com/pws/overview) |
    | Sensor.Community | ~15,000+ | Global — Alemania, Europa, USA, India, Australia, Brasil | [https://maps.sensor.community/](https://maps.sensor.community/) |
    | KNMI/AMT (2026) | 6 estaciones | Países Bajos (KNMI test field, De Bilt) | [https://amt.copernicus.org/articles/19/3001/2026/](https://amt.copernicus.org/articles/19/3001/2026/) |
    
    ---
    
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
    
    ## Pregunta 2.4: ¿Cuáles son los errores documentados de los sensores?
    
    ### 2.4.1 Error de Temperatura
    
    | Sensor | Bias medio | Error band | R² tras cal | Fuente |
    | --- | --- | --- | --- | --- |
    | BME280 (sin cal) | +0.14°C | ±0.61°C | — | Budiawan et al., 2026 |
    | BME280 (cal plano) | 0.03°C | ±0.33°C | 0.99-1.00 | Budiawan et al., 2026 |
    | DHT22/AM2302 (sin cal) | -0.13 a +0.44°C | RMSE 0.45-0.70°C | ≥0.99 | Araújo et al., 2020 |
    | DHT22/AM2302 (tras modelo lineal) | ~0 | ±0.41°C (DR) | ≥0.99 | Araújo et al., 2020 |
    
    **Chodorek et al. (2022):** *"It frequently happened that the error bound of the temperature measurements of the reference station (±1°C) was exceeded, which made the measurement non-satisfactory in terms of believability... so it cannot be used as the primary sensor and should not be used as the secondary one for temperature measurements for weather station purposes."*
    
    **Brown et al. (2026):** la deriva a largo plazo por envejecimiento está documentada en estaciones compactas sin mantenimiento (p.ej., el METER Atmos41 mostró deriva de humedad de +2.46% RH/año; la temperatura se mantuvo estable en ±0.3°C en cámara climática).
    
    ### 2.4.2 Error de Humedad Relativa
    
    | Sensor | Bias real | Error band | Deriva/año |
    | --- | --- | --- | --- |
    | BME280 (sin cal) | ±2.37% RH | ±10.02% RH | 0.5% RH/año |
    | BME280 (calibrado) | 1.65% RH | ±2.24% RH | 0.5% RH/año |
    | DHT22/AM2302 (sin cal) | -8 a +1% RH | ±5-8% RH | 0.5% RH/año |
    
    Fuentes: BME280 — Budiawan et al. (2026); DHT22/AM2302 — Araújo et al. (2020); deriva/año — Brown et al. (2026) reporta +0.56 a +2.46% RH/año en estaciones compactas sin mantenimiento.
    
    **CRITICO para tu modelo (Bell, 2015; Brown et al., 2026):**
    
    > *"Systematic humidity sensor drift... positive bias at low-to-mid range, negative bias at near-saturation conditions (>90% RH)."*
    > 
    
    **Implicación:** El error del sensor es MAYOR justo en el rango crítico para detección de lluvia. Un sensor de bajo costo podría reportar "100% RH" por contaminación cuando la humedad real ya descendió.
    
    ### 2.4.3 Error de Presión — BME280
    
    | Parámetro | Valor |
    | --- | --- |
    | Bias tras cal (Budiawan, 2026) | 0.06 hPa (tolerancia WMO: 0.1-0.15 hPa) |
    | Error band tras cal | ±0.8 hPa |
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
    > 
    
    ---
    
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
    
    **Fuente:** Budiawan et al. (2026) — tablas de bias antes/después de calibración.
    
    #### Componente 2: Ruido gaussiano (error aleatorio)
    
    ```python
    T_noise    = np.random.normal(0, 0.2)    # °C — σ ~0.2°C
    RH_noise   = np.random.normal(0, 1.5)    # % RH — σ ~1.5%
    P_noise    = np.random.normal(0, 0.2)    # hPa — σ ~0.2 hPa
    WS_noise   = np.random.normal(0, 0.3)    # m/s — σ ~0.3 m/s
    PRCP_noise = np.random.normal(0, 0.02)   # mm — cuantización domina
    ```
    
    **Fuente:** Araújo et al. (2020) — *Evaluation of Low-Cost Sensors for Weather and CO2 Monitoring* (MDPI IoT) — tablas de error y sigma para cada sensor.
    
    #### Componente 3: Deriva temporal (envejecimiento)
    
    ```python
    # Opcion A: Deriva lineal
    T_drift    = 0.5 * (t / 365.25)     # 0.5°C/año
    RH_drift   = 0.5 * (t / 365.25)     # 0.5% RH/año
    
    # Opcion B: Random walk (mas realista)
    T_drift[t]  = T_drift[t-1] + np.random.normal(0, 0.01)
    RH_drift[t] = RH_drift[t-1] + np.random.normal(0, 0.01)
    ```
    
    **Fuente:** Brown et al. (2026) — deriva a largo plazo en estaciones compactas sin mantenimiento (humedad: +0.56 a +2.46% RH/año; temperatura: ~-0.03 a +0.01°C/año). Bell (2015) documenta deriva de humedad en servicio. Nota: los valores 0.5°C/año y 0.5% RH/año del código son supuestos conservadores; ajustar según el sensor y la variable modelada.
    
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
    
    ### Propuesta implementación completa
    
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
    - No hay ningún paper documentado que aplique SNN/LIF a datos de sensores de bajo costo para predicción de lluvia
    
    ### Fuentes principales citadas
    
    1. **WMO (2019)**. *Visión del Sistema Mundial Integrado de Observación de la OMM para 2040* (WMO Vision for WIGOS). WMO-No. 1243, Edición de 2019.
        - [https://library.wmo.int/](https://library.wmo.int/)
    2. **Haas, S. J.; Kvas, A.; Fuchsberger, J. (2025)**. *Observation based precipitation life cycle analysis of heavy rainfall events in the southeastern Alpine forelands*. Weather and Climate Dynamics, 6, 949-963.
        - [https://wcd.copernicus.org/articles/6/949/2025/](https://wcd.copernicus.org/articles/6/949/2025/)
    3. **Brown, C. W.; Schadee, M.; de Haij, M.; Brandsma, T. (2026)**. *Performance and longevity of compact all-in-one weather stations – the good, the bad and the ugly*. Atmospheric Measurement Techniques, 19, 3001-3018.
        - [https://amt.copernicus.org/articles/19/3001/2026/](https://amt.copernicus.org/articles/19/3001/2026/)
    4. **Budiawan, I.; Ananda, N.; Wicaksana, H. S.; Burohman, A. M.; Mukhlish, F.; Ekawati, E.; Kurniadi, D. (2026)**. *A Study on Environmental Sensors for Low-Cost Weather Stations*. Engineering Innovations, 17, 57-74.
        - [https://www.scientific.net/EI.17.57](https://www.scientific.net/EI.17.57)
    5. **Araújo, T.; Silva, L.; Moreira, A. (2020)**. *Evaluation of Low-Cost Sensors for Weather and Carbon Dioxide Monitoring in Internet of Things Context*. MDPI IoT, 1(2), 286-308.
        - [https://www.mdpi.com/2624-831X/1/2/17](https://www.mdpi.com/2624-831X/1/2/17)
    6. **Chodorek, A.; Chodorek, R. R.; Sitek, P. (2022)**. *Response Time and Intrinsic Information Quality as Criteria for the Selection of Low-Cost Sensors for Use in Mobile Weather Stations*. *Electronics*, 11(15), 2448.
        - [https://doi.org/10.3390/electronics11152448](https://doi.org/10.3390/electronics11152448)
    7. **Bell, S. J. (2015)**. *Quantifying uncertainty in citizen weather data*. PhD thesis, Aston University.
        - [https://publications.aston.ac.uk/id/eprint/26693/](https://publications.aston.ac.uk/id/eprint/26693/)
    8. **Wang, W.; Hocke, K. (2022)**. *Atmospheric Effects and Precursors of Rainfall over the Swiss Plateau*. *Remote Sensing*, 14(12), 2938.
        - [https://www.mdpi.com/2072-4292/14/12/2938](https://www.mdpi.com/2072-4292/14/12/2938)
    9. **WMO (2025)**. *World Meteorological Congress endorses actions to promote AI for forecasts and warnings*.
        - [https://wmo.int/news/media-centre/world-meteorological-congress-endorses-actions-promote-ai-forecasts-and-warnings](https://wmo.int/news/media-centre/world-meteorological-congress-endorses-actions-promote-ai-forecasts-and-warnings)
    10. **Brasil, J. B.; Guerreiro, M. S.; Andrade, E. M. de; de Queiroz Palácio, H. A.; Medeiros, P. H. A.; Ribeiro Filho, J. C. (2022)**. *Minimum Rainfall Inter-Event Time to Separate Rainfall Events in a Low Latitude Semi-Arid Environment*. *Sustainability*, 14(3), 1721.
        - [https://www.mdpi.com/2071-1050/14/3/1721](https://www.mdpi.com/2071-1050/14/3/1721)
    11. **Sgoff, C.; Acevedo, W.; Paschalidi, Z.; Ulbrich, S.; Bauernschubert, E.; Kratzsch, T.; Potthast, R. (2022)**. *Assimilation of crowd-sourced surface observations over Germany in a regional weather prediction system*. Quarterly Journal of the Royal Meteorological Society, 148(745), 1752-1767.
        - [https://doi.org/10.1002/qj.4276](https://doi.org/10.1002/qj.4276)
    12. **Mao, Y.; Sorteberg, A. (2026)**. *Exploring the predictability of using crowdsourced observations in statistical postprocessing of NWP based precipitation nowcasts by machine learning*. Hydrological Research Letters, 20(1), 44-51.
        - [https://doi.org/10.3178/hrl.25-00020](https://doi.org/10.3178/hrl.25-00020)
    13. Bell, Simon (2015). Quantifying uncertainty in citizen weather data. PHD thesis, Aston University.
        - https://publications.aston.ac.uk/id/eprint/26693/

#### Modelo LIF:

Aqui se especifica el diseño del modelo LIF simplificado.
El modelo tecnico lo necesito diseñar y saber explicar yo, ES MI PROPIO DISEÑO.

### Normalizacion de los datos.

- **¿La normalizacion de variables es necesaria? ¿Que tecnica de normalizacion se utilizara?**
    - **Investigacion Normalizacion:**
        1. **¿Es la normalización estrictamente necesaria?**
            1. Respuesta corta: NO es matemáticamente obligatoria, pero SÍ es prácticamente necesaria (y mi caso específico, altamente recomendada).
                - El mecanismo del LIF que determina esta respuesta
                - El modelo LIF discretizado (Gerstner, Neuronal Dynamics, EPFL) es:
                    - V[t+1] = α·V[t] + (1-α)·I[t] donde α = e^(-Δt/τ_m); dispara si V ≥ θ; luego V ← V_reset
                    - La dinámica es lineal en la corriente de entrada It. Esto tiene dos consecuencias:
            2. Las escalas relativas se propagan directamente al potencial de membrana. Si la presión (~1000 hPa) entra como corriente 1000 veces mayor que la temperatura (15°C), el potencial de membrana V será dominado por presión y saturará el umbral θ casi siempre, produciendo disparos constantes que contienen poca información discriminativa sobre lluvia 
                - (Vasilache et al., 2025, arXiv:2504.11026; Guo et al., 2023, ICCV — Membrane Potential Batch Normalization for SNNs).
            3. Técnicamente, pesos aprendidos pueden compensar la escala (un w_presión ~0.001 vs w_temp ~0.1). Pero esto hace que el espacio de optimización sea mal condicionado (ill-conditioned), lo que degrada convergencia y estabilidad (Herranz-Celotti & Rouat, 2022, arXiv:2202.00282 — Stabilizing Spiking Neuron Training).
                - Evidencia empírica directa con tus mismas variables (Syaharuddin, Fatmawati & Suprajitno (2022), Int. J. Sustainable Development and Planning (DOI: 10.18280/ijsdp.170707), publicaron un estudio que probó 7 técnicas de normalización en datos de lluvia y humedad del aire (tus variables).
                - Textual:
                
                > "The use of original data (raw data) to train neural networks can lead to convergence problems... This will have implications for a high number of epochs and difficult networks to recognize data patterns. Therefore, the stage of normalization or standardization of data needs to be done before the data is trained."
                Resultados de su experimento: Z-score fue el mejor para datos de lluvia (MAE 0.051, MSE 0.004), y mean-MAD / Z-score para humedad. Con datos crudos, el modelo no convergía adecuadamente.
                > 
        2. **¿Cómo funciona el LIF en relación a la normalización? (el punto clave)**
            1. El modelo LIF simplificado recibe datos meteorológicos de una de dos formas. La respuesta a "¿necesito normalizar?" cambia según cuál uses:
            Camino A: Codificación por tasa (rate coding) — la más común para SNN
            En rate coding, el valor real se convierte en una tasa de disparo de un tren de spikes (típicamente Poisson). La encuesta de la revista Neural Processing Letters (2021, Springer) lo define así:
                
                > "Rate codes embed the information in the instantaneous or averaged rate of spike generation... signal amplitudes are directly mapped to spike frequencies."
                La fórmula típica: λ = v_normalizado × f_max (spikes/segundo).
                Aquí la normalización es prácticamente OBLIGATORIA, porque la tasa de disparo λ es proporcional al valor de entrada:
                > 
            - **Sin normalizar:** presión 1000 hPa → λ ~1000 spikes/s (saturación total), temperatura 15°C → λ ~15 spikes/s (prácticamente silenciosa)
            - **Normalizado a 0,1:** todas las variables generan λ en el mismo rango 0, f_max, comparables
            Conclusión: Si tu LIF usa rate coding (la opción estándar en la literatura de SNN aplicadas), la normalización min-max a 0,1 es la práctica necesaria para que el rango de tasas de disparo sea consistente entre variables.
            Camino B: Inyección directa de corriente (input analógico)
            Si el valor real entra directamente como corriente It = w·x (sin codificación Poisson), el modelo puede funcionar sin normalización porque los pesos aprendidos absorben la escala. Pero esto:
            - **Requiere inicialización cuidadosa (Herranz-Celotti & Rouat, 2022)**
            - **Sufre de convergencia lenta y riesgo de saturación**
            - **Es menos estándar en la literatura**
            
        3. **¿Cómo se realiza la normalización?**
        (Syaharuddin et al., 2022)
            
            
            | Técnica | Fórmula | Mejor para | Resultado en su estudio |
            | --- | --- | --- | --- |
            | Z-score (standardization) | x' = (x − μ)/σ | Lluvia, humedad | Mejor para lluvia (MAE 0.051) |
            | Min-Max | x' = (x − min)/(max − min) | Rate coding (acota a 0,1) | Bueno, depende del caso |
            | Mean-MAD | x' = (x − μ)/MAD | Humedad | Recomendado para humedad |
            | Decimal scaling | x' = x/10^k | Datos de magnitud uniforme | — |
            | Sigmoid / tanh | — | Datos acotados | — |
            - Furtado, Molina et al. (2026), arXiv:2508.07062 — "Setting the Standard: Recommended Practices for Data Preprocessing in Data-Driven Climate Prediction", publicado por un equipo que incluye a expertos del sector (el paper de referencia en preprocesamiento climático para ML).
            - Textual:
                
                > "Most climate datasets are inherently spatiotemporal, sparse, and possess spatial and temporal autocorrelations. The data are often nonstationary... Climate variables also have varying distributions, many of which are non-normal (e.g., gamma, bimodal, log-normal, and skew-normal), and exhibit non-linear interactions among themselves."
                > 
            
            **Propuesta:**
            
            1. **Crear anomalías estandarizadas** (restar la climatología mensual, luego estandarizar) en lugar de normalizar el valor absoluto. Esto es crítico para presión y temperatura, cuyas señales precursoras de lluvia son pequeñas variaciones (5-10 hPa, 2-3°C) sobre un valor de fondo grande y estacionario.
            2. **Tratar con cuidado valores extremos (outliers)** — fundamental en precipitación, cuya distribución es fuertemente no-normal (muchos ceros, cola pesada).
            3. **No** **mezclar datos de entrenamiento y validación** al calcular μ y σ (data leakage) — usar división temporal estricta.
            4. **Para presión específicamente:**
            La presión absoluta (950-1050 hPa) comprimida por min-max a 0,1 enterraría la señal informativa (los cambios de 5-10 hPa que preceden tormentas = solo 1% del rango). Para presión, la literatura sugiere 2 opciones:
                - Anomalía de presión (desviación de la media estacional)
                - Tendencia de presión (derivada temporal: ΔP/Δt en las últimas 3h — ya usada por el Zambretti Forecaster)
                    - Esto es más informativo que el valor absoluto y es directamente compatible con tu lookback window de 6-12h.
                    
        4. **Síntesis fundamentada**
            
            
            | **Pregunta** | **Respuesta** | **Fuente** |
            | --- | --- | --- |
            | ¿Normalización estrictamente necesaria? | No matemáticamente, pero sí prácticamente para convergencia, estabilidad y comparabilidad entre variables | Syaharuddin et al. (2022); Herranz-Celotti & Rouat (2022) |
            | ¿Necesaria para rate coding? | Sí, es esencial — la tasa de disparo λ es proporcional al valor normalizado | Vasilache et al. (2025); Neural Processing Letters (2021) |
            | ¿Cómo normalizar? | Z-score para lluvia/humedad (mejor empíricamente); anomalías estandarizadas para presión/temperatura; min-max 0,1 para rate coding | Syaharuddin et al. (2022); Furtado et al. (2026) |
            | ¿Por qué presión/temperatura con anomalía? | Su señal predictiva es la desviación (Δ), no el valor absoluto; min-max entierra la señal | Furtado et al. (2026) |
            | ¿Riesgo sin normalizar? | Convergencia lenta, saturación de tasa de disparo, dominio de variables de mayor magnitud, inestabilidad de gradientes | Syaharuddin et al. (2022); Herranz-Celotti & Rouat (2022) |
            - **Resumen de propuestas:**
                1. **Temperatura y humedad** → Z-score estacional (x − μ_mes)/σ_mes
                2. **Presión** → Anomalía o tendencia ΔP/Δt (3h)
                3. **Viento** → Z-score o min-max a 0,1 (magnitud comparable)
                4. **Precipitación** → Tratamiento especial por distribución no-normal: o bien log(1+x) antes de escalar, o umbral binario (0 = seco, 1 = lluvia) si el LIF solo detecta eventos
                5. **Antes de rate coding** → re-escalar a 0,1 para mapear a λ ∈ 0, f_max
            - **Esto está respaldado por:** Syaharuddin et al. (2022, IIETA), Furtado et al. (2026, arXiv:2508.07062), Vasilache et al. (2025, arXiv:2504.11026), Herranz-Celotti & Rouat (2022, arXiv:2202.00282), Guo et al. (2023, ICCV), y la encuesta de codificación en SNN (Neural Processing Letters, 2021).
    - **Conclusion:**
        
        Si, la normalizacion es esencial para que el modelo LIF simplificado pueda identificar los patrones correctamente.
        
        Con respecto a la normalizacion generalizada o individual: “el objetivo de la normalización no es que todas las variables tengan "la misma técnica", sino que todas terminen en la misma escala (0-1), cada una transformada según su propia distribución.”. 
        Esto permite identificar la tecnica mas adecuada para cada variable y normalizarla individualmente, permitiendo luego una sensibilidad adecuada para el modelo LIF.
        

---

### ¿Que tecnica de normalizacion se utilizara? (Lista por variable)

Las tecnicas de normalizacion utilizadas en cada variable, se determinan con un unico objetivo en comun: “Terminar con una escala final comun de 0 a 1”, permitiendo que ninguna variable domine el potencial de membrana.

#### **Contexto:** **Funcionamiento del modelo.**

En rate coding (la codificación estándar para SNN, snnTorch / Eshraghian et al. 2023, Proc. IEEE 111(9)):

> La información se codifica en la tasa de disparo λ, y λ **es proporcional al valor de entrada normalizado**. El rango final de TODAS las variables debe ser comparable (idealmente 0,1) para que ninguna domine el potencial de membrana del LIF.
Esto incentiva el uso de una técnica distinta por variable (según distribución), pero escala final común (0,1 o μ=0,σ=1).
> 

#### **Normalización óptima por variable:**

| **Variable** | **Técnica óptima** | **Por qué (evidencia)** | **Escala final** |
| --- | --- | --- | --- |
| **Precipitación** | Binaria (0/1) para la tarea de clasificación o
log(1+x) → min-max para intensidad | Cola pesada (Marra et al. 2023). dataresqc: IQR=5 (el más amplio), ceros excluidos. log comprime la cola sin borrar extremos reales | 0,1 |
| **Velocidad viento** | RobustScaler (mediana/MAD) o Winsorización p99 → z-score | Distribución Weibull sesgada (Monahan 2006). σ clásico se infla con ráfagas extremas; MAD es insensible (NIST/robust stats) | μ=0,σ=1 → re-escalar a 0,1 |
| **Dirección viento** | NO se normaliza en grados. Descomponer en u = WS·sin(θ), v = WS·cos(θ) → z-score de u y v | Variable circular (Fisher 1993). Sin descomposición, min-max/z-score producen saltos falsos en 0°/360° | μ=0,σ=1 |
| **Temperatura** | Anomalía estacional (opcional) → z-score | ~Normal (dataresqc IQR=3 = menos outliers). La señal precursora es la desviación (ΔT), no el absoluto (Furtado et al. 2026) | μ=0,σ=1 |
| **Presión** | Tendencia ΔP/Δt (3h) o anomalía (opcional) → z-score | ~Normal, rango estrecho. El min-max del valor absoluto (950-1050 hPa) aplasta la señal de ±5 hPa que precede tormentas | μ=0,σ=1 |
| **Humedad relativa** | Clip 0,100 (opcional) → z-score | Acotada físicamente, sin cola pesada. Riesgo real: saturación del sensor >90-100% (Bell 2015), se vigila no se transforma | μ=0,σ=1 |

**Aclaracion:** La precipitacion, velocidad viento y direccion viento son variables que se deben transformar y luego normalizar para un correcta interpretacion del modelo.

Sin embargo, las variables temperatura, presion y humedad realtiva no es necesaria la transformacion para la posterior normalizacion, sin embargo es recomendable para mayor precision.

- Se realizara una version del modelo con la normalizacion directa de estas ultimas 3 variables, y posteriormente se realizara en cuyo caso lo permita, una version con las variables transformadas y luego normalizadas.
- La transformacion inicial puede ser util para un entrenamiento del modelo que abarque el año completo y no solo epocas.

---

### ¿Como se adaptaran los valores para el entrenamiento? (Descripcion de tecnicas)

Para entregar los datos adecuados al modelo, se deberan transformar y normalizar segun corresponda cada variable segun un cierto metodo, permitiendo dejar un dataset listo para el entrenamiento del modelo.

#### **Procedimiento que experimentan los datos del dataset.**

Valor crudo → [PASO A: transformación] → [PASO B: normalización] → [PASO C: re-escalado a 0-1] → rate coding
Ej: 18.4°C      opcional según variable       z-score/min-max          valor ∈ [0,1]          λ = valor × f_max

#### Explicacion de Tecnicas:

- **Min-Max (re-escalado a 0-1)**
    - **Qué es:**
        - Re-escala linealmente al rango 0,1.
    - **Fórmula:**
        - x' = (x − min) / (max − min)
    - **Valores que se calculan:**
        - min y max observados en el set de entrenamiento.
    - **Ejemplo:**
        - (velocidad de viento, min=0, max=12 m/s):
        | Crudo (m/s) | Cálculo | x' |
        |-------------|---------|-----|
        | 0.0 | (0−0)/12 | 0.00 |
        | 3.0 | (3−0)/12 | 0.25 |
        | 9.0 | (9−0)/12 | 0.75 |
        | 12.0 | (12−0)/12 | 1.00 |
    - **Por qué se usa:**
        - Es el escalado final obligatorio para rate coding del LIF — la tasa de disparo λ = valor × f_max solo tiene sentido si el valor ∈ 0,1 (un valor 1 dispara a máxima frecuencia, un 0 no dispara).
        - Riesgo minimizado: Un outlier extremo infla max y aplasta todo lo demás. Por eso min-max se aplica DESPUÉS de las transformaciones que comprimen colas (log, robusto), no antes.
    - **Orden correcto:**
        - **transformar → z-score → min-max. El min-max es siempre el último paso de escalado.**
- **Binaria (umbral de lluvia)**
    - **Qué es:**
        - Convierte un valor continuo en 0 o 1 según supere un umbral.
    - **Fórmula:**
        - x' = 1  si x ≥ UMBRAL
        - x' = 0  si x < UMBRAL
    - **Cómo se define el umbral**: El criterio estándar en meteorología es:
        
        
        | **Referencia** | **Umbral de "evento de lluvia"** |
        | --- | --- |
        | **WMO (2017)** | Precipitación mensurable que alcanza el suelo: ≥ 0.1 mm en el periodo |
        | **Convención ISD-Lite/NOAA** | Precipitación horaria ≥ 0.1 mm (la resolución mínima reportada) |
        | **Criterio conservador** | ≥ 0.2 mm/h (evita falsos positivos por rocío/resolución del pluviómetro) |
        - Para este caso **se eligio utilizar: 0.2 mm/h.**
        - **Justificación:** El modelo debera estar adaptado a pluviómetros de cangilón (0.2 mm por vuelco) — un valor de 0.1 mm en ISD-Lite puede ser ruido de redondeo o rocío. Con 0.2 mm aseguras que al menos un vuelco real del cangilón ocurrió.
    - **Ejemplo (precipitación horaria):**
        
        
        | **Hora** | **Crudo (mm)** |
        | --- | --- |
        | 06:00 | 0.0 |
        | 07:00 | 0.1 |
        | 08:00 | 0.6 |
        | 09:00 | 2.3 |
        | 10:00 | 0.0 |
    - **Por qué se usa:** El objetivo del modelo es la clasificación binaria (¿lloverá en la próxima hora?).
        - La precipitación es la única variable con cero-inflación masiva y cola pesada — convertirla a binaria elimina TODO el problema de escala de golpe. El dato ya queda en {0,1}, que es exactamente el rango del rate coding.
- **Z-score (estandarización)**
    1. **Qué es:**
        - Convierte el dato en "cuántas desviaciones estándar se aleja de la media".
        - Utilizamos este metodo para convertir todas las unidades metorologias a una unica unidad universal: las desviaciones estandar con respecto a la media.
        - De esa forma un cambio de 5 hPa en la presion vale equivalente que un cambio en 1°C de temperatura.
            - Gracias a esto el LIF puede comparar y ponderar variables por su señal relativa, no por su magnitud bruta.
    2. **Fórmula:**
        - z = (x − μ) / σ
    3. **Valores que se calculan:**
        - μ = media aritmética de la variable (en el set de entrenamiento)
        - σ = desviación estándar de la variable
    4.  **Cómo se calculan:**
        - μ = (1/N) · Σ xᵢ
        - σ = √[ (1/N) · Σ (xᵢ − μ)² ]
        - Al ser una simple transformacion lineal para adaptar el valor, no aplicamos la convencion probabilistica de numeros continuos o discretos (integral o sumatoria).
            - No nos interesa convertir “z” en probabilidad, solo la utilizamos para compatibilizar las escalas.
    5. **Ejemplo concreto (temperatura horaria, un día de Frankfurt):**
        
        | Hora | Crudo (°C) | Cálculo | z |
        |------|-----------|---------|---|
        | 06:00 | 14.0 | (14.0 − 18.4)/3.1 | −1.42 |
        | 12:00 | 19.5 | (19.5 − 18.4)/3.1 | +0.35 |
        | 18:00 | 21.8 | (21.8 − 18.4)/3.1 | +1.10 |
        | 21:00 | 18.4 | (18.4 − 18.4)/3.1 | 0.00 |
        
        - Aquí μ=18.4°C, σ=3.1°C (calculados sobre todo el set de entrenamiento).
    6. **Por qué se usa:** 
        - Produce distribución con μ=0, σ=1, comparable entre variables. Mantiene los valores negativos y positivos (la media queda en 0). No acota — los z pueden exceder ±3 en extremos.
        - Resultado típico: z ∈ −3, +3 aproximadamente.
        - Permite obtener valores equivalentes entre variables, permitiendo posteriormente adaptarlos a una escala de (0,1) mediante min-max.
    7. **Problema que resuelve:** 
        - Que presión (~1000) no domine a temperatura (~18) en el potencial de membrana del LIF.

- **log(1+x) (Transformacion)**
    - **Qué es:**
        - Transformación logarítmica con desplazamiento +1 para comprimir la cola pesada sin perder los ceros.
    - **Fórmula:**
        - x' = log(1 + x)
    - **Por qué +1:**
        - log(0) = −∞. Con +1, un valor crudo de 0 queda log(1) = 0 (se conserva el "no llovió").
        - Es la transformación estándar para datos positivos sesgados (documentada en Best practice in statistics: The use of log transformation, PMC9036143).
    - **Ejemplo (precipitación horaria, log natural):**
        
        
        | Crudo (mm) | Cálculo | log(1+x) |
        | --- | --- | --- |
        | 0.0 | log(1+0) = log(1) | 0.00 |
        | 0.2 | log(1.2) | 0.18 |
        | 1.0 | log(2.0) | 0.69 |
        | 3.0 | log(4.0) | 1.39 |
        | 30.0 | log(31) | 3.43 |
    - **Cómo comprime:** El salto de 3→30 mm (×10 en crudo) se convierte en 1.39→3.43 (+2 en escala log). El salto de 0.2→1.0 (que te importa para detectar lluvia normal) pasa de 0.18→0.69 — proporcionalmente más visible que en la escala cruda.
        - Después del log se aplica min-max o z-score para llegar al rango final.
    - **Por qué se usa (alternativa a binaria):**
        - Si se quiere conservar la intensidad de lluvia (no solo presencia), log(1+x) permite que el LIF distinga "llovizna" de "Chubasco o torrencial" sin que esta ultima aplaste la escala.
        
- **Anomalía estacional (Transformacion)**
    - **Qué es:**
        - Resta el valor esperado para ese momento del año (climatología), dejando solo la desviación.
    - **Fórmula:**
        - x_anomalía = x − climatología(mes, hora)
    - **Valores que se calculan:**
        - La climatología = media histórica de la variable para cada combinación (mes, hora). Con 5+ años de datos EDDF se tiene ~12 meses × 24 horas = 288 promedios.
    - **Ejemplo (temperatura de Frankfurt, julio 14:00):**
        
        
        | **Dato** | **Valor** |
        | --- | --- |
        | Temperatura observada (14:00, 15-jul) | 24.5°C |
        | Climatología julio-14:00 (media 2000-2025) | 22.0°C |
        | Anomalía | +2.5°C |
    - **Por qué se usa:**
        - Elimina la estacionalidad (verano ≠ invierno, día ≠ noche). Así el LIF interpreta "+2.5°C" como "más caliente de lo normal para julio" en vez de "24.5°C = verano".
        - La señal precursora de tormenta (calor anómalo) queda aislada del ruido estacional.
        - Después de la anomalía se aplica z-score (normalizando la anomalía, no el absoluto)
        
- **Tendencia ΔP/Δt (Transformacion)**
    - **Qué es:**
        - La variación de presión en una ventana temporal (p. ej. 3 horas) — captura "la presión está cayendo".
    - **Fórmula:**
        - ΔP/Δt = (P[t] − P[t−3h]) / 3h (tendencia en hPa/h)
    - **Valores que se calculan:**
        - Ninguno estadístico — es una resta directa de la serie. Solo se define la ventana Δt (recomendada: 3h, coincidiendo con el Zambretti).
    - **Ejemplo:**
        
        
        | **Hora** | **P (hPa)** | **ΔP/Δt (vs 3h antes)** |
        | --- | --- | --- |
        | 09:00 | 1013.2 | — |
        | 10:00 | 1012.1 | — |
        | 11:00 | 1010.8 | — |
        | 12:00 | 1009.0 | (1009.0−1013.2)/3 = −1.40 hPa/h |
        | 13:00 | 1007.5 | (1007.5−1012.1)/3 = −1.53 hPa/h |
    - Una caída sostenida de −1.4 a −1.5 hPa/h es la firma típica de aproximación de un frente (base del Zambretti, que predice "lluvia" cuando ΔP < −1.6 hPa/h).
    - **Por qué se usa:** El valor absoluto de presión (1013 hPa) dice poco; la tendencia dice "se acerca algo". Es más informativo y elimina la estacionalidad y altitud de un golpe.
        - Después se aplica z-score sobre la tendencia.
        
- **u = WS·sin(θ), v = WS·cos(θ) (descomposición del viento) (Transformacion)**
    - **Qué es:**
        - Convierte la dirección (circular) en dos componentes cartesianas lineales.
    - **Fórmula (convención meteorológica):**
        - u = −WS · sin(θ)     → componente Este-Oeste
        - v = −WS · cos(θ)     → componente Norte-Sur
        - (El signo negativo es convención: u>0 = viento del Oeste, v>0 = del Sur.
        - Se puede usar la convención matemática sin signos.)
    - **Ejemplo concreto:**
        
        
        | **WS (m/s)** | **θ (°)** | **u = −WS·sin(θ)** | **v = −WS·cos(θ)** |
        | --- | --- | --- | --- |
        | 4.0 | 90 (del Este) | −4.0·1.0 = −4.0 | −4.0·0.0 = 0.0 |
        | 4.0 | 270 (del Oeste) | −4.0·(−1.0) = +4.0 | −4.0·0.0 = 0.0 |
        | 4.0 | 0 (del Norte) | −4.0·0 = 0.0 | −4.0·1.0 = −4.0 |
        | 4.0 | 350 | −4.0·(−0.174) = +0.69 | −4.0·0.985 = −3.94 |
        | 4.0 | 10 | −4.0·(0.174) = −0.69 | −4.0·0.985 = −3.94 |
    - **Punto clave:**
        - 350° y 10° (que en grados crudos están separados por 340°) producen u/v casi idénticos (+0.69/−3.94 vs −0.69/−3.94) — correcto, porque son casi la misma dirección (Norte). El wrap-around del círculo queda resuelto.
    - **Por qué se usa:**
        - La dirección es circular; el z-score/min-max en grados produciría saltos falsos en 0°/360°. Con u/v, la variable vuelve a ser lineal y normalizable. Además u y v incorporan la magnitud del viento (WS), así que si se usa u/v se puede incluso prescindir de WS como variable separada.
        - Esto genera 2 variables del viento, provocando que tengan sus propias estandarizaciones.
    - Se aplica z-score (o RobustScaler) a u y v independientemente.
        - **Consecuencia numerica:** El modelo contaba "6 neuronas" (5 sensores + alerta), con la descomposicion u/v el viento aporta 2 neuronas, quedando: T, P, HR, u, v, PRECIP (6 sensores) + alerta. Revisar la cuenta de neuronas en la metodologia final del paper.

- **RobustScaler (mediana/MAD)**
    - **Qué es:**
        - Igual que z-score pero usando estimadores robustos (insensibles a outliers).
        - Utiliza la mediana en vez de desviaciones, permitiendo mayor inmunidad a outliners.
    - **Fórmula:**
        - z_robusto = (x − mediana) / MAD; donde MAD = 1.4826 · mediana( |xᵢ − mediana(x)| )
    - **Valores que se calculan:**
        - mediana = valor central (el 50% está arriba, 50% abajo) — no se infla con extremos
        - MAD = mediana de las desviaciones absolutas respecto a la mediana
        - 1.4826 = factor de consistencia para que MAD estime σ en datos normales (si usaras z-score equivalente)
    - **Ejemplo (viento con una ráfaga extrema):**
        - Series = 2, 3, 2, 4, 3, 15, 2, 3
        
        | Parámetro | Valor |
        | --- | --- |
        | mediana | 3.0 |
        | |x−mediana| | 1,0,1,1,0,12,1,0 |
        | mediana de esos | 1.0 |
        | MAD | 1.4826 × 1.0 = 1.48 |
        | z_robusto de la ráfaga de 15 | (15−3)/1.48 = +8.1 |
        | z_robusto del 4 | (4−3)/1.48 = +0.67 |
    - **Comparación con z-score clásico:**
        - σ clásico = 4.4 (inflado por el 15) → el 4 daría z = 0.23 (aplastado).
        - Con MAD, el 4 da +0.67 — los valores normales quedan mejor separados porque la ráfaga extrema no infló la escala.
        - La dispersión de los datos normales se preserva fielmente.
    - **Por qué se usa (viento):**
        - La distribución Weibull del viento tiene rachas extremas reales. El RobustScaler las "tolera" sin dejar que distorsionen la separación de los valores normales.
        - Permite mantener una media y varianza adecuada a los valores, permitiendo evitar que un unico valor anomalo mueva estas variables hacia un extremo.
            - Ejemplo anexo con Z clasico:
            - μ = (2+3+2+4+3+15+2+3)/8 = 4.25 ← el 15 corrió la media hacia arriba
            - σ = √(Σ(x−μ)²/n) = √(135.5/8) = 4.12 ← el 15 infló la varianza
                
                
                | Dato | z CLÁSICO (σ=4.12) | z ROBUSTO (MAD=1.48) |
                | --- | --- | --- |
                | 2 | −0.55 | −0.67 |
                | 3 | −0.30 | 0.00 |
                | 3 | −0.30 | 0.00 |
                | 4 | −0.06 | +0.67 |
                | 15 | +2.61 | +8.09 |
    
- **Winsorización al percentil 99 (P99)**
    - **Qué es:**
        - Recorta los valores extremos al percentil 99 — los mayores quedan "clavados" en el valor del percentil 99 (no se eliminan, se acotan).
    - **Fórmula:**
        - x' = P99   si  x > P99
        - x' = P1    si  x < P1  (simétrico, opcional)
        - x' = x     en otro caso
        - Valores que se calculan: P99 = el valor bajo el cual está el 99% de los datos (y P1 si recortas también los bajos).
        - Osea el percentil 99 se refiere al valor que esta por encima del 99% de los datos.
        - Se ordenan los datos, se toma el valor en la posición 99%.
    - **Ejemplo (viento, si P99 = 14 m/s):**
        
        
        | **Crudo (m/s)** | **Tras Winsorizar** |
        | --- | --- |
        | 5.0 | 5.0 (no se toca) |
        | 13.0 | 13.0 (no se toca) |
        | 14.2 | 14.0 (clavado en P99) |
        | 22.0 | 14.0 (clavado en P99) |
- Diferencia con "eliminar" outliers: El valor 22 no se borra ni se modifica a un "valor inventado" — simplemente se limita al máximo razonable (P99). El LIF sigue viendo "ráfaga fuerte" (14), pero el σ/min-max no se distorsiona con el 22.
- **Por qué se usa:**
    - Es una alternativa a RobustScaler. A veces se aplica antes del RobustScaler para doble protección. En este caso, con datos ya QC'd por DWD, **es un refinamiento opcional.**
    - **Las ráfagas extremas reales rara vez superarán umbrales físicos.**

### ¿Se entrenara el modelo por temporadas o por todo el año?

#### B.1. Dos decisiones distintas que conviene separar

Hay dos preguntas que a menudo se mezclan y que conviene separar:

1. **Normalizacion**: ¿con que estadisticos (μ, σ) se estandariza cada variable?
    - Ya decidido en el doc principal (seccion 6.2): **por estacion**, usando anomalias estacionales. La señal predictiva de presion/temperatura es la **desviacion** respecto a la climatologia del mes, no el valor absoluto.
2. **Entrenamiento**: ¿se ajusta **un** modelo sobre los 12 meses, o **4 modelos** (uno por estacion)?

#### B.2. Literatura de nowcasting

**TA-SmaAt-UNet** (van Nieuwkoop & Mehrkanoon, 2026, arXiv:2606.09959):

> "TA-SmaAt-UNet improves upon the core SmaAt-UNet in every season, indicating that the benefit of temporal context is not restricted to a single part of the year. The improvement is particularly relevant in summer, which is also the most difficult season in terms of CSI. This is consistent with previous nowcasting evidence that models often struggle more with convective summer precipitation than with more persistent winter rainfall."
> 

Informacion clave:

- **El patron de la literatura** no es entrenar modelos separados por estacion, sino **entrenar un unico modelo** y darle **contexto estacional** (codificacion ciclica del momento del año: sin/cos del dia del año y de la hora).
- **El contexto estacional** es mas beneficioso cuanto mas **raro e intenso** es el evento (mejoras mayores en umbrales de 10 y 20 mm/h que en 0.5 mm/h). La estacionalidad importa especialmente para los eventos que mas importan en un sistema de alerta.
- **El verano es la estacion mas dificil** (conveccion), y el contexto estacional es justamente donde mas ayuda.

**Implicacion directa:** la estrategia respaldada es **un solo modelo + informacion estacional como entrada o como normalizacion**, NO fragmentar el entrenamiento en modelos por estacion.

#### B.3. Argumentos practicos para entrenar con el ano completo

| Criterio | Entrenar 1 modelo anual | Entrenar 4 modelos estacionales |
| --- | --- | --- |
| **Volumen de datos** | EDDF 2020-2024: ~43,800 h → ~43,800 muestras | ~10,950 h/estacion → 4x menos datos por modelo |
| **Eventos de lluvia** | Todos los regmenes (convectivo de verano, estratiforme de invierno) | Cada modelo ve solo su regimen; los eventos raros se fragmentan |
| **Robustez** | Umbrales y pesos estimados con mas evidencia | Mas varianza, mayor riesgo de overfitting |
| **Despliegue bajo costo** | 1 modelo, 1 umbral, 1 τ_m desplegable | 4 configuraciones + logica de seleccion de estacion |
| **Transferencia de patrones** | Los precursores comunes (caida de presion, alza de humedad) se aprenden una vez | Cada modelo los reaprende por separado |

Para un LIF simplificado de pocas neuronas y pocos parametros, el dato adicional del ano completo es directamente aprovechable: **mas datos = umbrales y pesos mas estables**.

#### B.4. Como evaluar la estacionalidad (sin sesgar)

La literatura de evaluacion de nowcasting da 3 reglas claras:

1. **El test set debe cubrir al menos un ciclo estacional completo.** En series temporales con estacionalidad, el periodo de prueba debe abarcar el ciclo completo para poder evaluar la captura de la estacionalidad (practica estandar en division temporal; los papers de nowcasting dividen por **años completos consecutivos**, p.ej. entrenar 2008-2020, validar 2006 o 2020, testear 2021).
2. **Reportar metricas por estacion.** Se reporta CSI/POD/FAR en los papers de nowcasting para desglosados por estacion buscando exponer la dificultad de cada una.
3. **Test sesgados.** Un año de prueba con eventos extremos concentrados en pocos meses infla o desinfla las metricas. El estudio del DGMR (AMS, AIES 2023) lo maneja explicitamente separando "Test—Heavy" (meses con eventos intensos) de "Test—Light" para no atribuir a la maquina lo que es sesgo del periodo de prueba.

#### B.5. ¿Como se implementa la informacion extra de la estacionalidad?

- La Estandarizacion (A), y la Contexto estacional (B) son dos mecanismos distintos.
    
    
    |  | **A. Estandarización estacional** | **B. Contexto estacional cíclico** |
    | --- | --- | --- |
    | **Qué es** | Un preprocesamiento de cada valor | Features de entrada adicionales |
    | **Qué hace** | Quita la climatología (el ciclo medio del año) → el dato queda como anomalía | Le dice al modelo "en qué época del año estamos" para que adapte su regla |
    | **Dónde vive** | Antes del rate coding, transformando T, P, HR, viento | En la neurona de alerta (como neuronas extra) |
    | **Pregunta que responde** | "¿Este valor es anómalo para esta época del año?" | "¿Como varian los patrones segun la epoca?" |
    
    Hacen cosas distintas y se combinan. La normalización (A) es la esencial; el contexto (B) es el refinamiento.
    
- **Mecanismo A: Estandarización estacional (anomalías)**
    - **El problema que resuelve**
        - **En Frankfurt**, la temperatura media pasa de ~1°C en enero a ~19°C en julio.
        - **Si estandarizas con μ, σ globales del año entero**, un día normal de enero (1°C) da z = (1 − 10)/7 ≈ −1.3 → parece una anomalía térmica enorme, cuando en realidad es simplemente invierno. Resultado: la neurona dispara por "estar en enero" en lugar de por "el clima está anómalo", que es la señal de lluvia.
        - **La estandarización estacional elimina el ciclo primero:**
            - z = (x − μ(t)) / σ(t)
            - donde μ(t) y σ(t) son la media y desviación de la variable en esa época del año.
            - Ahora z=0 significa "típico para esta época" y z=+2 significa "anómalamente alto para esta época"; Eso sí es señal predictiva.
    - **Tres formas de definir μ(t), σ(t)**
        1. **Por mes (12 grupos):** μ_m, σ_m por mes calendario, calculados solo sobre el train. Simple, pero tiene saltos artificiales el 31 de julio→1 de agosto.
        2. **Por estación (4 grupos):** Aún más simple, pero saltos aún más gruesos (marzo→abril, etc.).
            - Es conceptualmente simple pero introduce discontinuidades que el LIF (sensible a saltos) no necesita.
        3. **Climatología diaria suavizada (recomendada):** μ(doy) = media móvil centrada ±15 días sobre el day-of-year, con manejo circular del 31 dic↔1 ene. Continua, sin saltos, y es lo estándar en ciencias climáticas.
    
    Qué variable se adapta cómo al año entero
    
- **Mecanismo B: Contexto estacional cíclico (sin/cos)**
    - **Por qué el "momento del año" crudo no sirve:**
        - Si se diera al modelo day-of-year = 200 (julio) como número crudo:
        - **Es circular:** el día 365 y el día 1 son vecinos, pero numéricamente están a 364 de distancia. Es el mismo problema de discontinuidad que la dirección del viento.
        - **La neurona de alerta del LIF es lineal:**
            - Un input crudo con una frontera en 0°/365° obligaría al modelo a "saltar".
    - **La solución estándar: codificar el tiempo como par sin/cos**
    doy_sin = sin(2π·doy / 365.25)
    doy_cos = cos(2π·doy / 365.25)
    hod_sin = sin(2π·hora / 24)
    hod_cos = cos(2π·hora / 24)
        - Son continuas, acotadas en -1,1 y periódicas. Como la neurona de alerta es lineal, el modelo puede combinar doy_sin y doy_cos con pesos aprendidos para representar cualquier fase del año: un peso grande en doy_sin hace que la alerta responda más en verano (sin positivo) y menos en invierno.
    - **Implementación:**
    df['doy_sin'] = np.sin(2*np.pi*df['doy']/365.25)
    df['doy_cos'] = np.cos(2*np.pi*df['doy']/365.25)
    df['hod_sin'] = np.sin(2*np.pi*df['hour']/24)
    df['hod_cos'] = np.cos(2*np.pi*df['hour']/24)
    ****
    - Estos 4 valores entran como columnas extra en la neurona de alerta (la regresión logística / la búsqueda sobre w), con su propio peso aprendido. Como están acotados, no necesitan normalización (si pasaran por rate coding, re-escalarías a 0,1).
- **¿Por qué B es necesario si ya implemente A?**
La normalización (A) quita la media climatológica, pero no el hecho de que la relación anomalía→lluvia cambia con la estación:
    - Un mismo aumento de humedad predice lluvia más fiablemente en verano que en invierno. El contexto (B) le da al modelo la información para modular su regla según la época.
    - Es exactamente lo que demostró TA-SmaAt-UNet (mejora todas las estaciones, sobre todo la convección de verano).

#### B.6.

**Conclusion:** La estacionalidad fragmenta los datos y los patrones generales sin necesidad. Se necesita un modelo robusto que permita identificar los cambios producidos durante todo el año.

### Fuentes:

1. scikit-learn — StandardScaler (z-score) y su documentación sobre por qué se estandariza antes del modelado.
2. Herranz-Celotti & Rouat (2022) — arXiv:2202.00282 — estabilidad del entrenamiento de LIF y su relación con la escala de entradas.
3. Eshraghian et al. (2023) — Proc. IEEE 111(9) (snnTorch) — rate coding: λ proporcional al valor normalizado; el rango 0,1 como paso previo a la codificación.

---

### Codificacion y diseño del modelo LIF.

Aqui se planteara el modelo LIF simplificado a desarrollar.

El objetivo de esta seccion es poder especificar a nivel tecnico que componetes y que diseño tendra el modelo LIF, permitiendo ser de guia para su posterior codificacion.

Una vez planteada la base se exponen los conceptos fundamentales para definir la “estructura” del modelo LIF, y cada una de sus caracteristicas principales a revisar y decidir.

#### Conceptos fundamentales.

**Que es un LIF simplificado y que permite hacer:**

El modelo **Leaky Integrate-and-Fire** (LIF) es la neurona artificial mas simple con memoria temporal (Gerstner et al., 2014; Burkitt, 2006). Se comporta como un circuito RC: acumula corriente de entrada en el potencial de membrana V, lo deja **filtrarse** (leak) exponencialmente, y cuando v supera un umbral θ **dispara** un spike y se reinicia.

"Simplificado" significa aqui que se usara la version discreta y de un solo compartimiento: sin dendritas, sin canales ionicos, sin plasticidad biologica. Solo tres operaciones por paso: una multiplicacion (fuga), una suma (integracion) y una comparacion (umbral). Eso es lo que la hace desplegable en hardware de gama baja.

**Como se relaciona con este proyecto:**

| **Capacidad objetivo** | **Que aporta el modelo** |
| --- | --- |
| **Deteccion de anomalias por variable** | Cada neurona sensor integra su variable y dispara si esta "anomalamente alta/persistente" para la epoca del año |
| **Prediccion binaria de lluvia (proxima hora)** | La neurona de alerta combina las anomalias ponderadas y dispara si la combinacion supera su umbral |
| **Explicabilidad** | Los pesos de la alerta indican que variable contribuye y con que signo a cada prediccion |
| **Robustez al ruido de sensores baratos** | La integracion con fuga es un promedio exponencial: suaviza el ruido de BME280/DHT22/pluviometro |
| **Un solo modelo para todo el año** | Gracias a la normalizacion estacional (anomalias) + features de contexto temporal |
| **Hardware de bajo costo** | Solo sumas, productos y comparaciones: implementable en MicroPython/C |

**Analogia:** cada neurona sensor es un **filtro IIR de primer orden** (Utiliza el valor actual de la entrada y un valor de salida anterior para calcular la nueva salida) sobre la anomalia de su variable. El modelo completo es un **banco de filtros fijos + regresion logistica** en la alerta. Esta es la manera tecnica de explicar "como funciona" sin perderse en biologia.

#### **Ecuaciones y variables fundamentales.**

**La ecuacion diferencial del LIF es:**

- **τ_m · dV/dt = −(V − V_rest) + R_m · I(t)**
- **Basado en la forma continua (la definicion canonica)**

| **Simbolo** | **Significado** | **Unidad** | **Representa en el modelo** |
| --- | --- | --- | --- |
| `V(t)` | Potencial de membrana | mV (relativo) | actividad de la variable (adimensional) |
| `V_rest` | Potencial de reposo | mV | 0 (escala normalizada) |
| `τ_m` | Constante de tiempo de membrana | s (u horas) | 2-4 h por variable (escala de precursores) |
| `R_m` | Resistencia de membrana | Ω | se absorbe en los pesos aprendidos |
| `I(t)` | Corriente de entrada | mA | proporcional a la variable normalizada |

La solucion dice lo esencial: `V` **tiende** a `V_rest + R_m·I` con constante `τ_m`. Si la entrada se mantiene, `V` sube asintoticamente hacia ella; si la entrada se corta, `V` decae exponencialmente con `τ_m`.

**Disparo, reset y refractariedad**

- **Condicional:**
    
    if V(t) >= θ: #emitir spike (s=1)
       V(t) <- V_reset #(reset, tipicamente V_rest)
       #no recibir entrada durante t_ref (periodo refractario)
    

**Forma discreta (la que se codifica)**

Con paso temporal Δt y **Euler implicito/explicito** (equivalentes si Δt << τ_m):

- α = e^(−Δt/τ_m) (factor de fuga exacto)
V[t] = α·V[t-1] + (1−α)·(V_rest + R_m·I[t])

Con V_rest = 0 y absorbiendo la escala en la corriente:

- **V[t] = α·V[t-1] + (1−α)·I[t]**
- Esta es la ecuacion que se implementa. α juega el papel de "cuanta memoria conserva el paso anterior".

**Interpretacion clave: promedio movil exponencial (EMA)**

Reordenando la ecuacion se ve que el LIF subumbral **es** un promedio movil exponencial:

- **V[t] = (1−α)·I[t] + (1−α)·α·I[t-1] + (1−α)·α²·I[t-2] + …**

Es decir: la actividad de la neurona sensor en el instante t resume **toda la historia** de la variable, con pesos que decaen exponencialmente. La constante τ_m controla cuanta historia: con τ_m = 3 h, la contribucion de hace 3 h pesa e^(−1) ≈ 37%; hace 6 h, e^(−2) ≈ 14%. Esto es exactamente lo que se quiere para capturar la evolucion de precursores (caida de presion, subida de humedad) en ventanas de 6-12 h.

**Valores de α segun τ_m (paso horario)**

| **τ_m** | **1 h** | **2 h** | **3 h** | **4 h** | **6 h** | **12 h** |
| --- | --- | --- | --- | --- | --- | --- |
| α = e^(−1/τ_m) | 0.37 | 0.61 | 0.72 | 0.78 | 0.85 | 0.92 |

#### Componentes y parametros

**Neuronas y parametros del modelo se definen como:**

- 6 neuronas sensor (una por variable normalizada):
    - T, P (o ΔP), HR, u, v, PRECIPITACION
    - 4 features de contexto temporal (sin/cos de doy y hora) ← **NO son LIF, entran al readout**
    - 1 neurona de alerta (readout)
    - En total son: 7 Neuronas (6 sensores y 1 alerta) y 4 parametros (temporada y horario)

**Parametros: fijos vs aprendidos**

| **Parametro** | **Simbolo** | **Valor/regla** | **Quien lo decide** |
| --- | --- | --- | --- |
| **Constante de tiempo** | `τ_m,i` | 2-4 h por variable (T y HR mas lentas, P y PRECIP. mas rapidas) | Fijado (literatura de precursores) |
| **Umbral de disparo sensor** | `θ_i` | Percentil de la actividad (p.ej. disparar ~5-10% del tiempo) o libre | Fijado o aprendido |
| **Potencial de reposo** | `V_rest` | 0 | Fijado |
| **Reset** | `V_reset` | 0 (reset total) | Fijado |
| **Tasa maxima** | `f_max` | 200 spikes/s | Fijado |
| **Pesos sensor→alerta** | `w_i` | m + 4 valores | **Aprendido** |
| **Umbral de la alerta** | `θ_A` | 1 valor | **Aprendido** |

**Regla del diseno:** lo que tiene interpretacion fisica se fija; lo que solo se puede aprender de los datos se aprende. Esto mantiene el modelo con ~11-15 parametros libres (m + 1 + 4), entrenable con busqueda o regresion logistica sin GPU.

#### Arquitectura: Sensores hacia la neurona de alerta

**Flujo de datos**

- **Variable cruda**
- **→ transformacion** (z-score estacional / ΔP / u/v / binaria)
- → x̂ ∈ [0,1]  **(tras clip y min-max)**
- → I[t] = x̂[t] · f_max        **(rate coding)**   O   I[t] = x̂[t]   **(directo)**
- **→ neurona sensor i:** V_i[t] = α_i·V_i[t-1] + (1−α_i)·I_i[t]
- **→ actividad** a_i[t] = V_i[t]  (+ spike si V_i >= θ_i)
- **→ sinapsis:** I_A[t] = Σ_i w_i · a_i[t]  (+ Σ_j v_j · tiempo_j[t])
- **→ alerta:**   V_A[t] = α_A·V_A[t-1] + (1−α_A)·I_A[t]
- **→ decision:** si V_A[t_final] >= θ_A → lluvia la proxima hora.

**Explicacion: La conexion sensor → alerta (las sinapsis)**

- Cada neurona sensor i se conecta a la alerta a traves de **una sinapsis con peso w_i** (excitatoria si w_i > 0, inhibitoria si w_i < 0). La alerta recibe la **suma ponderada** de las actividades:
- I_A[t] = w_1·a_1[t] + w_2·a_2[t] + ... + w_6·a_6[t] + v_1·doy_sin + v_2·doy_cos + v_3·hod_sin + v_4·hod_cos
- En forma matricial: I_A[t] = W^T · x[t], donde W = [w_1..w_6, v_1..v_4] y x[t] es el vector de caracteristicas (features) en t.
- **Interpretacion meteorologica (Signo y magnitud):** un w_HR grande y positivo significa "humedad anomala empuja a llover"; un w_P negativo (sobre la anomalia de presion) significa "presion subiendo empuja a no llover" (la lluvia suele venir con presion en caida, que es anomalia negativa). **El signo y magnitud de cada peso es interpretable.**

**La neurona de alerta como LIF**

Para ser coherentes con "6 neuronas LIF", la alerta tambien integra (con su propio `τ_A`, corto, 1-2 h) y dispara al superar `θ_A`. Pero como las features ya llevan memoria, la alerta puede **decidir al final de la ventana**:

- **Version binaria (hardware):** predice lluvia si `V_A[t_final] >= θ_A`.
- **Version probabilistico (calibracion):** `P(lluvia) = σ(V_A[t_final] − θ_A)` con la sigmoide `σ(x) = 1/(1+e^(−x))`. La sigmoide es la version suave del umbral: el umbral es `P ≥ 0.5`. Esto permite calibrar el umbral en validacion (seccion 6.3).

**Rate coding (Poisson) vs inyeccion directa: puente teorico**

Hay dos formas de alimentar las neuronas:

- **Camino A (rate coding):** cada paso genera un tren de spikes de Poisson con tasa `λ = x̂·f_max`.
- **Camino B (inyeccion directa):** se inyecta directamente `I = x̂·f_max`.

La **equivalencia teorica**: como el LIF es lineal (subumbral), el valor esperado de la membrana bajo Poisson **es** la membrana con inyeccion directa (la media del Poisson es `λ`). Es decir:

- E[ V_A con rate coding ] = V_A con inyeccion directa

Por eso en la implementacion de referencia se usa la forma directa (determinista, reproducible, entrenable con regresion logistica), y el rate coding de Poisson queda como la **version de hardware** del mismo modelo.

- Esto se puede citar con Herranz-Celotti & Rouat (2022) y la equivalencia promedio/EMD.

**Consecuencia practica importante:** las constantes de escala (`f_max`, `R_m`) son factores constantes de un modelo lineal → **se absorben en los pesos aprendidos `w`**. No hay que "sintonizarlas" a mano para que las tasas sean comparables; la regresion logistica las acomoda sola. (Si se mantiene la version Poisson, si hay que fijar `f_max` igual en todas las variables, como ya esta decidido.)

#### Definicion de codificacion.

En un SNN, la informacion externa (los valores normalizados de las variables) debe convertirse en **trenes de spikes**. A esa conversion se la llama **codificacion neuronal**. La referencia se resume asi:

> "Rate codes embed the information in the instantaneous or averaged rate of spike generation... signal amplitudes are directly mapped to spike frequencies." (Neural Processing Letters, 2021)
> 

La clasificacion central divide la codificacion en **rate coding** (codificacion por tasa) y **temporal coding** (codificacion temporal), dependiendo de si la informacion vive en el *numero* de spikes o en el *momento exacto* en que ocurren (Neural Processing Letters, 2021).

#### **Formas de codificacion:**

**1. Rate coding (codificacion por tasa) — Adrian & Zotterman (1926)**

- **Como funciona:** el valor de la variable se mapea a la **frecuencia de disparo**. Con codificacion de Poisson: `λ = x̂ · f_max`, donde `λ` es la tasa (spikes/segundo), `x̂` el valor normalizado y `f_max` la tasa maxima.
- **Formula del codificador del modelo:** `f = ((x_norm - min)/(max - min)) · f_max` (doc principal, seccion 7.3), con `f_max = 200` spikes/s.
- **Ventajas:** simple de implementar, robusto al ruido (promedia informacion sobre muchos spikes; spikes individuales perdidos o desplazados no cambian la tasa), equivalente a la activacion de una neurona artificial ordinaria, entrenable con los metodos estandar (BPTT / gradiente sustituto).
- **Desventajas:** requiere ventanas largas para estimar la tasa con precision (lento), baja densidad de informacion, mayor numero de spikes y mayor consumo energetico.

**2. Temporal coding (codificacion temporal)**

La informacion vive en el **momento exacto** de los spikes. Subcategorias:

| Tecnica | Que codifica | Referencia clave |
| --- | --- | --- |
| **TTFS / latency** | El tiempo hasta el primer spike (Δt ∝ 1/amplitud; mayor amplitud → spike mas temprano). Un spike por ventana. | Gollisch & Meister (2008), *Science* 319 |
| **Rank-order (ROC)** | El **orden** de los primeros spikes de una poblacion de neuronas, no los tiempos exactos. | Thorpe & Gautrais (1998) |
| **ISI** | Los intervalos entre spikes consecutivos (mayor capacidad de datos; 2+ spikes/ventana). | Pyramidal cells (biologia) |
| **Phase** | La fase de los spikes respecto a una oscilacion interna de fondo. | Hipocampo, sistema olfativo (O'Keefe & Recce, 1993) |
| **Burst** | Racha de spikes (bursts); alta confiabilidad y eficiencia energetica. | Talamo, corteza auditiva |
| **Temporal contrast** | La **derivada** de la senal (sensores event-driven tipo DVS). | Event-based vision |

**Comparativa de las formas de codificacion**

Guo et al. (2021, *Frontiers in Neuroscience* 15:638474) compararon rate, TTFS, phase y burst en MNIST/Fashion-MNIST con SNN entrenado con STDP, evaluando exactitud, latencia, operaciones sinapticas (SOPs), robustez y tolerancia a fallos:

| Esquema | Exactitud | Latencia de inferencia | SOPs (Operaciones sinapticas) | Robustez |
| --- | --- | --- | --- | --- |
| **TTFS** | Mejor | 4x / 7.5x menor que rate (entrenamiento/inferencia) | 3.5x / 6.5x menos que rate | Sensible a variaciones en el tiempo (jitter temporal) |
| **Rate** | Menor | Lenta (larga latencia para converger) | Alta | Mas robusto y simple |
| **Phase** | Intermedia | Rapida | Muy alta | La mas resiliente al ruido de entrada |
| **Burst** | Buena | Rapida | Alta | Mejor compression y tolerancia a fallos |

La encuesta de Springer (2021) agrega una advertencia clave para la decision de arquitectura:

> "Rate-based schemes... convince through their robustness against fluctuations and noise as well as their simplicity... Temporal encoding schemes on the other hand rely on the precise timing of every single spike and can thus achieve higher information densities and efficiencies. However they involve more complex architectures and lacking training methods."
> 

**Esquema elegido para el modelo LIF: rate coding**

| **Criterio del proyecto** | **Como lo satisface rate coding** |
| --- | --- |
| **Filosofia bajo costo / hardware simple** | El codificador por tasa es el circuito mas simple (un integrador con capacitor); TTFS/ISI requieren circuitos mas complejos (Liu et al., *Neural Encoding Strategies for Neuromorphic Computing*). |
| **Sensores de bajo costo = ruidosos** | Rate coding es uno de los esquemas **mas robustos al ruido** (promedia informacion sobre muchos spikes). Es exactamente la tolerancia que necesitan datos de BME280/DHT22/pluviometro de cangilon. |
| **Entrenamiento maduro** | Rate coding se entrena con BPTT/gradiente sustituto; las tecnicas temporales "lacking training methods" (Springer 2021). |
| **Escala temporal horaria** | La desventaja de rate coding (lentitud) es irrelevante: el modelo decide en escala de horas (τ_m 2-4 h, lookback 6-12 h), no de milisegundos. |
| **Consistencia entre variables** | Todas las variables usan la misma f_max=200 y el mismo mapeo λ = x̂·f_max, garantizando tasas comparables. |
| **Simplicidad de interpretacion** | La tasa de disparo de una neurona sensor equivale a "cuanto de anomala esta esa variable", que es exactamente el rol de detector de anomalias del modelo. |

**Limitacion a reconocer:** rate coding tiene menor densidad de informacion y mayor gasto energetico por spike que TTFS (Codificacion temporal). Para un LIF de 11 neuronas esto es aceptable, La comparativa de Guo et al. (2021) da los numeros de referencia para esa discusion.

### Desiciones a tomar.

1. **Feature de la alerta:** ¿actividad continua (membrana, recomendada) o spike binario del sensor (alarma por variable)? O ambas (actividad + tasa de spikes).
2. **La alerta integra o decide:** ¿`V_A` se evalúa al final de la ventana (recomendado) o se requiere un disparo en cualquier paso dentro de la ventana?
3. **τ_m por variable:** ¿se fijan individualmente (recomendado) o uno global con sensibilidad?
4. **Reset:** ¿`V_reset = 0` (recomendado) o `V_reset = θ − Δ` (reset parcial, mas biológico)?
5. **Umbrales θ_i:** ¿percentiles fijos (90-95) o libres en la busqueda?
6. **Feature de la ventana:** ¿actividad del ultimo paso, promedio de los ultimos k pasos, o maximo de la ventana?
7. **Version del codigo:** ¿forma directa determinista (base) + Poisson como ablation/hardware, o solo Poisson?
8. **f_max y micro-pasos:** si se usa Poisson, definir `dt_sim` y cuantos micro-pasos por hora (τ_m >> dt_sim).

### Fuentes

#### Definicion baseline y variable objetivo:

**PASOS A SEGUIR:**

- ACLARAR CONCEPTOS TECNICOS DEL MODELO LIF.
- DEFINIR VARIABLE OBJETIVO.
- DEFINIR TEORICAMENTE Y TECNICAMENTE EL BASELINE A DISEÑAR.

#### Protocolo de entrenamiento y evaluacion:

Si los calculas con todo el dataset, inflas artificialmente el rendimiento reportado

### GUIA de la Metodologia:

- GUIA METODOLOGIA:
    
    ### Metodología de Preprocesamiento de Datos para el Modelo LIF de Predicción de Lluvia
    
    El preprocesamiento es la etapa más crítica de tu investigación, ya que determina la calidad de los datos que alimentarán tu modelo LIF. Una metodología deficiente en esta fase puede invalidar todo el trabajo posterior, incluso si el modelo es excelente. Por eso, es fundamental abordarla con el máximo rigor.
    
    A continuación, te presento una guía completa y detallada, estructurada en dos partes:
    
    1. **Preguntas Fundamentales:** Las preguntas que debes responder para cada sub-paso, que te guiarán en la toma de decisiones metodológicas.
    2. **Metodología Paso a Paso:** Un procedimiento concreto, reproducible y justificado, adaptado a tu contexto de sensores de bajo costo y datos de estaciones profesionales.
    
    ---
    
    ### Parte 1: Preguntas Fundamentales para el Preprocesamiento
    
    Estas preguntas son el esqueleto de tu metodología. Responderlas te obligará a definir cada aspecto con claridad y a justificar tus elecciones.
    
    ### 1. Adquisición y Calidad de los Datos (Datos Faltantes y Outliers)
    
    | # | Pregunta | ¿Qué implica? |
    | --- | --- | --- |
    | 1.1 | **¿Cuál es el porcentaje de datos faltantes en mi dataset y cuál es su patrón?** | Determinar si los faltantes son aleatorios o sistemáticos (ej. fallas del sensor en horas de lluvia intensa). |
    | 1.2 | **¿Qué umbral de tolerancia a datos faltantes voy a aplicar y por qué?** | Decidir si elimino la hora/día si falta más del X% de los datos. El SMN usa 20% para datos cada 10 minutos. |
    | 1.3 | **¿Qué método usaré para imputar o interpolar los datos faltantes?** | ¿Interpolación lineal, interpolación por vecinos, o simplemente eliminar la observación? |
    | 1.4 | **¿Cómo identificaré y trataré los outliers (valores anómalos)?** | ¿Por desviación estándar (ej. > 3σ), por rango intercuartil (IQR), o por un criterio físico (ej. temperatura > 60°C)? |
    | 1.5 | **¿Qué hago con los outliers?: ¿los elimino, los corrijo o los trato como eventos especiales?** | Para tu proyecto, un outlier podría ser una señal de tormenta, no un error. Esto es clave. |
    
    ### 2. Frecuencia Temporal y Resolución
    
    | # | Pregunta | ¿Qué implica? |
    | --- | --- | --- |
    | 2.1 | **¿Cuál es la frecuencia de muestreo original de los datos (ej. 10 min, 1 hora)?** | Definir la resolución temporal base del dataset. |
    | 2.2 | **¿A qué frecuencia debo remuestrear (upsampling o downsampling) los datos para mi modelo LIF?** | Decidir si usaré los datos tal cual (ej. 10 min) o los agruparé (ej. 15 min). |
    | 2.3 | **¿Cuál es el horizonte de predicción (lead time) que busco?** | ¿Quiero predecir la lluvia en 30 minutos? ¿1 hora? Esto define la etiqueta de entrenamiento. |
    | 2.4 | **¿Qué ventana temporal de entrada (lookback window) usaré?** | ¿Cuántos pasos de tiempo atrás usaré para predecir el futuro? (ej. 60 minutos de historia para predecir los próximos 30). |
    | 2.5 | **¿Cómo manejaré la estacionalidad diaria y mensual?** | ¿Agrupo por hora del día? ¿Por estación del año? |
    
    ### 3. Simulación del Comportamiento de Sensores de Bajo Costo
    
    | # | Pregunta | ¿Qué implica? |
    | --- | --- | --- |
    | 3.1 | **¿Qué características de los sensores de bajo costo necesito simular?** | Ruido, sesgo sistemático, deriva, menor resolución. |
    | 3.2 | **¿Cuáles son los errores documentados de los sensores que usaré (ej. DHT22, BMP280)?** | Investigar en hojas de datos y en la literatura (ej. el estudio del KNMI). |
    | 3.3 | **¿Cómo modelaré el ruido: ruido gaussiano, ruido de cuantificación, o ambos?** | Definir la distribución y la magnitud del ruido. |
    | 3.4 | **¿Qué sesgos sistemáticos debo introducir?** | Ej. el DHT22 tiende a sobreestimar la humedad en ambientes secos y subestimar en ambientes muy húmedos. |
    | 3.5 | **¿Cómo afectará la menor resolución (ej. temperatura con 0.5°C vs 0.1°C) a los datos?** | Redondear los valores o cuantificarlos. |
    | 3.6 | **¿Cómo validaré que la simulación es realista?** | ¿Compararé con datos reales de bajo costo si llegara a tenerlos? |
    
    ### 4. Normalización y Escalado
    
    | # | Pregunta | ¿Qué implica? |
    | --- | --- | --- |
    | 4.1 | **¿Qué método de normalización usaré?** | Min-Max (escalar entre 0 y 1), Z-score (media 0, desviación 1), o robusto (basado en cuartiles). |
    | 4.2 | **¿Normalizaré todas las variables con el mismo método?** | ¿O cada variable requiere un tratamiento diferente? |
    | 4.3 | **¿Los parámetros de normalización (media, desviación) los calcularé sobre todo el dataset o por estación del año?** | Esto afecta la generalización del modelo. |
    | 4.4 | **¿La normalización se hará antes o después de la simulación de bajo costo?** | El orden es importante. |
    
    ### 5. Codificación para el Modelo LIF (Variables a Spikes)
    
    | # | Pregunta | ¿Qué implica? |
    | --- | --- | --- |
    | 5.1 | **¿Qué método de codificación usaré para convertir las variables continuas a spikes?** | Codificación por tasa (frecuencia de spikes), codificación por tiempo (latencia), o por umbral (delta modulation). |
    | 5.2 | **¿Qué tasa de spikes máxima (máx. frecuencia) utilizaré?** | Define la resolución temporal del código de spikes. |
    | 5.3 | **¿Normalizaré las variables antes de la codificación para que los rangos sean comparables?** | Sí, es fundamental. |
    | 5.4 | **¿Cómo manejaré las variables con diferentes rangos y unidades?** | Asegurar que todas contribuyan equitativamente a la membrana de la neurona LIF. |
    
    ### 6. Creación de la Variable Objetivo (Etiqueta) y baseline
    
    | # | Pregunta | ¿Qué implica? |
    | --- | --- | --- |
    | 6.1 | **¿Cómo definiré el evento de "lluvia" que quiero predecir?** | ¿Precipitación > 0.2 mm en 10 min? ¿> 1 mm en 1 hora? Definir el umbral. |
    | 6.2 | **¿Con qué horizonte temporal definiré el evento?** | ¿Predecir si lloverá en los próximos 30 minutos? ¿1 hora? |
    | 6.3 | **¿Crearé una etiqueta binaria (llueve/no llueve) o continua (intensidad esperada)?** | Para una alerta temprana, lo más útil es la etiqueta binaria. |
    | 6.4 | **¿Cómo manejaré los eventos de lluvia de baja intensidad (trazas)?** | ¿Los consideraré como lluvia o los ignoraré? Definir un umbral mínimo. |
    | 6.5 | ¿Como definire y diseñare el baseline para la comparacion? | Definir teoricamente el baseline y posteriormente describir su funcionamiento tecnico. (Umbrales fijos). |
    
    ### 7. Separación de Datos para Entrenamiento y Prueba
    
    | # | Pregunta | ¿Qué implica? |
    | --- | --- | --- |
    | 7.1 | **¿Qué proporción de datos usaré para entrenamiento, validación y prueba?** | Ej. 70% entrenamiento, 15% validación, 15% prueba. |
    | 7.2 | **¿Mantendré el orden temporal o haré una división aleatoria?** | Para series temporales, **nunca** se usa división aleatoria. Se respeta el orden cronológico. |
    | 7.3 | **¿Dejaré un "período de calentamiento" (warm-up) antes de la prueba?** | Para que el modelo LIF pueda estabilizar su estado de membrana. |
    | 7.4 | **¿Cómo aseguraré que los eventos de lluvia estén representados en todas las particiones?** | Usar validación cruzada con bloques temporales o asegurar una distribución balanceada. |
    | 7.5 | ¿Que tipo de entrenamiento utilizare? ¿Porque? ¿Como definire las variables fijas y aprendidas? | Definir una buena estructura para el entrenamiento y evaluacion del modelo. |
    
    ### 8: REVISIONES
    
    - Revisar investigacion y escribir todo en neutro.
    - Revisar fuentes correctas con respecto a la informacion.
    - Realizar resumen consiso (conclusion) del modelo a crear, como, porque y para que.
    
    Por ultimo empezar a redactar el paper sobre el diseño del modelo y la investigacion realizada.
    
    ---
    
    ### Parte 2: Metodología de Preprocesamiento Paso a Paso
    
    A continuación, presento el procedimiento concreto que deberías seguir. Lo he estructurado en pasos lógicos y justificados, basados en la literatura científica y en los estándares de la OMM.
    
    ### Metodología de Preprocesamiento para el Modelo LIF de Predicción de Lluvia con Sensores de Bajo Costo
    
    #### 1. **Adquisición de Datos**
    
    1.1. **Seleccionar la fuente de datos:** Se obtendrán datos históricos de la estación meteorológica de la UNVM (Villa María) o de la estación SACO (Córdoba) a través de sus respectivos portales públicos. Se priorizará la estación de Villa María por su cercanía geográfica.
    
    1.2. **Definir el período de estudio:** Se seleccionará un período de al menos **5 años** de datos, que es el mínimo recomendado por la OMM para análisis estacionales y para asegurar una muestra representativa de eventos de lluvia.
    
    1.3. **Identificar las variables a utilizar:** Se extraerán las siguientes variables, con su frecuencia original (idealmente cada 10-15 minutos):
    - Temperatura del aire (°C)
    - Humedad relativa (%)
    - Presión atmosférica (hPa)
    - Velocidad del viento (km/h)
    - Dirección del viento (°)
    - Precipitación acumulada (mm)
    
    #### 2. **Control de Calidad y Datos Faltantes**
    
    2.1. **Cálculo de datos faltantes:** Para cada variable, se calculará el porcentaje de datos faltantes por hora y por día.
    
    2.2. **Aplicación de umbral de tolerancia:** Siguiendo el criterio del SMN (Nota Técnica 2024-167), se eliminarán las horas que tengan **≥20% de datos faltantes** (es decir, si la estación mide cada 10 minutos, se elimina la hora si faltan 2 o más de los 6 valores). Para los días, se eliminarán si tienen **≥20% de horas faltantes**.
    
    2.3. **Imputación de datos faltantes:** Para los períodos con menos del 20% de faltantes, se aplicará una **interpolación lineal** entre los valores válidos anteriores y posteriores. Esta elección se basa en que las variables meteorológicas tienden a tener una variación suave en escalas de minutos (OMM, 2018).
    
    2.4. **Detección de outliers:** Se identificarán outliers utilizando el **método del rango intercuartil (IQR)** , donde un valor se considera outlier si está fuera del rango `[Q1 - 1.5*IQR, Q3 + 1.5*IQR]`. Este método es robusto y no asume normalidad (Hastie et al., 2009).
    
    2.5. **Tratamiento de outliers:** Un outlier podría ser una señal de tormenta (ej. una caída brusca de presión), por lo que **no se eliminarán automáticamente**. Se etiquetarán y se analizará su contexto temporal; si corresponden a un cambio climático real, se mantendrán.
    
    #### 3. **Simulación de Sensores de Bajo Costo**
    
    Dado que el proyecto se enmarca en un sistema de bajo costo, los datos originales (de sensores profesionales) serán transformados para simular el comportamiento de sensores económicos, siguiendo la metodología propuesta por el **estudio del KNMI (2024)** y validada por investigaciones de la Universidad de Reading (2022).
    
    3.1. **Inyección de ruido:** A cada variable se le añadirá un ruido gaussiano con media cero y desviación estándar igual al error típico del sensor simulado:
    
    - **Temperatura:** σ = 0.5°C (basado en especificaciones del DHT22)
    - **Humedad:** σ = 3% (basado en especificaciones del DHT22 para HR media)
    - **Presión:** σ = 1 hPa (basado en especificaciones del BMP280)
    - **Viento:** σ = 0.5 m/s (basado en especificaciones de anemómetros de bajo costo)
    
    3.2. **Introducción de sesgos sistemáticos:** Siguiendo los hallazgos del KNMI (2024) y de la literatura sobre sensores de bajo costo (ej. DHT22), se aplicarán los siguientes sesgos:
    
    - **Humedad:** Se añadirá un sesgo positivo de +2% para valores de HR < 30%, y un sesgo negativo de -3% para valores de HR > 90%.
    - **Velocidad del viento:** Se aplicará un factor de subestimación del 10% para vientos inferiores a 2 m/s (debido al desgaste mecánico del anemómetro de cazoletas).
    
    3.3. **Reducción de resolución:** Los valores se redondearán a la resolución típica de los sensores de bajo costo:
    
    - **Temperatura:** 0.5°C
    - **Humedad:** 1%
    - **Presión:** 1 hPa
    - **Viento:** 0.5 m/s
    - **Precipitación:** 0.2 mm (resolución del pluviómetro de cubeta basculante)
    
    3.4. **Validación de la simulación:** Se comparará la distribución de los datos simulados con las hojas de datos de los sensores reales y con estudios previos de caracterización de sensores de bajo costo (ej. el estudio de la Universidad de Reading, 2022).
    
    #### 4. **Selección de Ventanas Temporales (Lookback y Lead Time)**
    
    4.1. **Definición del horizonte de predicción (lead time):** El modelo LIF predecirá si lloverá en los próximos **30 minutos**, basado en la literatura que indica que este es un horizonte de nowcasting útil para sistemas de alerta temprana local.
    
    4.2. **Definición de la ventana de entrada (lookback window):** Se utilizará una ventana de **60 minutos (6 pasos de 10 minutos)** como entrada, basado en los hallazgos del **paper de Ischia (2025)** que identificó retardos óptimos de 0, -10 y -20 minutos. La ventana de 60 minutos captura la evolución de las variables que anteceden a la lluvia.
    
    4.3. **Creación de secuencias temporales:** Para cada instante `t`, se creará un vector de entrada `X_t` que contiene los valores de las cinco variables en los tiempos `t-60`, `t-50`, `t-40`, ..., `t` (6 pasos de 10 minutos). La etiqueta `y_t` será 1 si la precipitación en el intervalo `[t, t+30]` supera el umbral definido, y 0 en caso contrario.
    
    #### 5. **Creación de la Variable Objetivo (Etiqueta)**
    
    5.1. **Definición del umbral de lluvia:** Se definirá un evento de lluvia como aquel en el que la precipitación acumulada en **10 minutos** supera los **0.2 mm** (que es la resolución mínima del pluviómetro de bajo costo y el umbral de detección mínimo recomendado por la OMM). Este umbral permite detectar incluso lluvias ligeras o trazas.
    
    5.2. **Etiquetado:** Para cada instante `t`, se calculará la precipitación acumulada en los próximos 30 minutos a partir de los datos originales de precipitación (no simulados). Si esta cantidad supera el umbral de 0.2 mm, se etiqueta `y_t = 1` (lluvia), de lo contrario `y_t = 0`.
    
    #### 6. **Normalización y Escalado**
    
    6.1. **Método:** Se aplicará una **normalización Z-score** (media 0, desviación estándar 1) a cada variable por separado, utilizando los parámetros calculados sobre el conjunto de entrenamiento. Esta técnica es estándar en el preprocesamiento para redes neuronales y es especialmente adecuada para el modelo LIF, ya que los spikes se codifican a partir de estos valores normalizados.
    
    6.2. **Cálculo por estación del año:** Dado que los patrones climáticos varían estacionalmente, se calcularán medias y desviaciones estándar **separadas para cada estación** (verano, otoño, invierno, primavera). Esto permite que la normalización capture las diferencias estacionales y mejore la detección de anomalías dentro de cada estación.
    
    #### 7. **Codificación de Variables a Spikes para el Modelo LIF**
    
    7.1. **Método de codificación:** Se utilizará una **codificación por tasa de spikes (rate coding)** . Para cada paso de tiempo, el valor normalizado de cada variable se convertirá en una frecuencia de spikes (número de spikes por unidad de tiempo) proporcional al valor de la variable. Este es el método más común para datos de series temporales en SNN (Diehl & Cook, 2015).
    
    7.2. **Tasa máxima de disparo:** Se establecerá una tasa máxima de 200 spikes por segundo para el valor máximo de la variable normalizada (es decir, para valores de Z-score = +3). Esto asegura que las neuronas tengan una resolución temporal suficiente para capturar los cambios rápidos de presión y viento.
    
    7.3. **Implementación:** Se implementará un codificador en Python que, para cada valor normalizado `x_norm`, genere un tren de spikes de Poisson con una frecuencia `f = (x_norm - min)/(max - min) * f_max`. El codificador se ejecutará para cada paso de tiempo de la ventana de entrada.
    
    #### 8. **Separación de Datos en Entrenamiento, Validación y Prueba**
    
    8.1. **División temporal:** Se utilizará una división temporal, **manteniendo el orden cronológico**, para evitar el *data leakage* (que información del futuro contamine el entrenamiento).
    
    8.2. **Proporciones:** Se asignará el **70% de los datos** a entrenamiento, **15%** a validación (para ajuste de hiperparámetros) y **15%** a prueba (para evaluación final). Los datos de prueba serán los más recientes, para evaluar el modelo en condiciones futuras.
    
    8.3. **Período de calentamiento (warm-up):** Para el modelo LIF, se descartarán los primeros 10 pasos de cada secuencia de validación y prueba para permitir que la membrana de la neurona se estabilice. Esto sigue la práctica común en SNN (Diehl & Cook, 2015).
    
    #### 9. **Documentación de la Metodología**
    
    9.1. **Registro de todos los pasos:** Se documentará cada paso del preprocesamiento, incluyendo los parámetros utilizados, las decisiones tomadas y las justificaciones, en un cuaderno de Jupyter o en un script de Python bien comentado.
    
    9.2. **Reproducibilidad:** El código completo del preprocesamiento se subirá a un repositorio público (ej. GitHub) junto con el código del modelo, para garantizar la reproducibilidad de los resultados, tal como exigen las buenas prácticas de la investigación científica.
    
    ---
    
    ### 📊 Esquema Resumen de la Metodología
    
    ```
    DATOS CRUDOS (Estación UNVM o SACO - frecuencia 10 min)
        │
        ├─ 1. CONTROL DE CALIDAD
        │   └─ Eliminar horas con >20% faltantes
        │   └─ Interpolar linealmente faltantes <20%
        │   └─ Detectar outliers con IQR
        │
        ├─ 2. SIMULACIÓN DE BAJO COSTO
        │   ├─ Inyectar ruido gaussiano
        │   ├─ Aplicar sesgos sistemáticos (humedad, viento)
        │   └─ Reducir resolución
        │
        ├─ 3. CREACIÓN DE ETIQUETAS
        │   └─ Definir umbral de lluvia (0.2 mm/10 min)
        │   └─ Etiquetar para horizonte de 30 min
        │
        ├─ 4. NORMALIZACIÓN Z-SCORE
        │   └─ Por variable y por estación del año
        │
        ├─ 5. CODIFICACIÓN A SPIKES
        │   └─ Rate coding (Poisson) con f_max = 200 Hz
        │
        ├─ 6. CREACIÓN DE SECUENCIAS
        │   └─ Lookback de 60 min (6 pasos de 10 min)
        │   └─ Lead time de 30 min
        │
        └─ 7. DIVISIÓN TEMPORAL
            └─ 70% entrenamiento (con estacionalidad)
            └─ 15% validación
            └─ 15% prueba
    ```
    
    ---
    
    ### Conclusión
    
    Esta metodología de preprocesamiento aborda de manera completa y rigurosa cada uno de los aspectos críticos para tu investigación. Al implementarla, aseguras que tu modelo LIF:
    
    1. **Entrena con datos de calidad**, habiendo tratado correctamente los faltantes y outliers.
    2. **Es representativo de un sistema de bajo costo**, gracias a la simulación realista de los sensores.
    3. **Aprende patrones temporales relevantes**, gracias a la selección de ventanas basada en la literatura científica.
    4. **Es reproducible y justificable**, gracias a la documentación y al uso de estándares reconocidos.
    
    Esta base te permitirá enfocarte en el desarrollo y la evaluación del modelo LIF, sabiendo que tus datos han sido procesados con el máximo rigor científico y alineados con los objetivos de tu proyecto para el CNEISI.
    
- **Limitaciones de la adquisicion de datos:**
    - Analisis open-meteo:
        
        ### 🔍 Open-Meteo: Análisis de su Procesamiento y Limitaciones
        
        Open-Meteo es técnicamente impresionante, pero su naturaleza como agregador de datos implica procesos que debes conocer.
        
        - **Datos y Cobertura**: Agrega modelos de más de 15 servicios meteorológicos nacionales
        
        , usando
        
        **reanálisis**
        
        como ERA5, que combinan observaciones con modelos matemáticos
        
        . Ofrece datos desde 1940 con resolución horaria
        
        , pero la resolución de 15 minutos
        
        **no proviene de observaciones directas**
        
        ; son datos interpolados a partir de modelos horarios en la mayoría de las regiones
        
        - .
        - **Métodos de Interpolación**: Open-Meteo no aplica una única técnica. Cada variable (temperatura, radiación solar, precipitación) usa métodos diferentes
        
        . Por ejemplo, la precipitación se divide en función del intervalo de interpolación. Para la radiación solar, usan un algoritmo basado en el índice de claridad
        
        - . **Esto significa que los datos de precipitación en frecuencia de 15 minutos
        son, en parte, una construcción matemática, no una medición directa.**
        - **Selección de Estación por Coordenadas**: Open-Meteo utiliza el modelo numérico de mayor resolución para tus coordenadas, no una estación física específica
        
        . Por defecto, selecciona la celda de la cuadrícula, pero puede elegir otra si el ajuste de elevación es mejor
        
        - . **Esto implica que tus datos no provienen de una estación concreta como SACO o la UNVM, sino de un modelo que combina múltiples fuentes de datos para
        esa ubicación.**
        - **Validación**: Aunque usa datos de estaciones, son datos **reanalizados** y no pueden ser validados contra los sensores crudos de una estación específica, ya que no existen como tal en su salida.
    1. ¿El script recopila datos de múltiples estaciones o solo datos crudos de una estación?
    Descarga una estación por ejecución. Los datos son crudos (el valor directo de la observación), con estas salvedades:
    | Fuente | ¿Dato crudo de estación real? |
    |--------|-------------------------------|
    | SMN WIS2 | ✅ Sí — observación SYNOP directa del aeropuerto |
    | INA Alerta5 | ✅ Sí — medición de estación meteorológica |
    | INTA SIGA | ✅ Sí — sensor de estación agropecuaria |
    | Open-Meteo | ❌ No — es grilla interpolada (modelo reanálisis ERA5 + datos satelitales) |
    Para corroborar: comparar con el API directamente. Por ejemplo, el script SMN consulta [http://w2b.smn.gob.ar/oapi/collections/urn:wmo:md:ar-smn:slt0ci/items?wigos_station_identifier=0-20000-0-87576](http://w2b.smn.gob.ar/oapi/collections/urn:wmo:md:ar-smn:slt0ci/items?wigos_station_identifier=0-20000-0-87576). Puede pegar esa URL en un navegador y ver el GeoJSON idéntico.
    2. Método para descargar las 5 variables fundamentales
    Para cada fuente, el comando específico:
    SMN WIS2 (Ezeiza, SYNOP crudo):
    python descargar_datos_unificado.py descarga --fuente smn --estacion "EZEIZA AERO" --inicio 2026-02-25 --fin 2026-07-12
    Variables: air_temperature, dewpoint_temperature, wind_speed, wind_direction, pressure_reduced_to_mean_sea_level, horizontal_visibility, cloud_cover_total
    Open-Meteo (coordenadas, 5 vars completas):
    python descargar_datos_unificado.py descarga --fuente openmeteo --lat -34.56 --lon -58.42 --inicio 1940-01-01 --fin 2026-07-12 --frecuencia 60
    Variables: temperature_2m, relative_humidity_2m, pressure_msl, wind_speed_10m, wind_direction_10m, precipitation
    INTA (solo temp + humedad + precip, sin viento ni presión):
    
    # Tiempo real (10 min, solo hoy):
    
    python descargar_datos_unificado.py descarga --fuente inta --estacion "Anguil" --frecuencia 10
    
    # Diario histórico:
    
    python descargar_datos_unificado.py descarga --fuente inta --estacion "Anguil" --frecuencia 1440
    3. Frecuencias disponibles por fuente
    
    | Fuente | < 60 min | Histórico < 60 min | Histórico >= 60 min |
    | --- | --- | --- | --- |
    | Open-Meteo | ✅ 15 min (interpolado) | ✅ 1940-presente | ✅ |
    | SMN WIS2 | ❌ 1-6 h | ❌ solo desde feb 2026 | ✅ solo feb-jul 2026 |
    | INA Alerta5 | ❌ horaria | ❌ solo ~3 años | ✅ horaria (~3 años) |
    | INTA SIGA | ✅ 10 min | ❌ solo hoy | ✅ diaria (1999-presente, 226 estaciones) |
    | Ninguna fuente argentina de datos CRUDOS de estación real ofrece < 60 min histórico. Solo Open-Meteo lo hace, pero es interpolado. |  |  |  |
    1. Fuente más abierta y verificable → SMN WIS2
    Gana claramente porque:
    - Estándar abierto: OGC API - Features (estándar internacional geoespacial)
    - WIS2 de WMO: Implementación del marco de la Organización Meteorológica Mundial
    - WIGOS IDs: Cada estación tiene un identificador WMO (0-20000-0-87576) que se puede buscar en OSCAR ([https://oscar.wmo.int](https://oscar.wmo.int/)) para ver:
        - Instrumentos exactos instalados
        - Altura del barómetro, tipo de anemómetro, etc.
        - Prácticas de observación
        - Historia de la estación
    - GeoJSON estándar: Los datos se pueden validar con cualquier visor GeoJSON
    - MQTT público: Transmisión en vivo vía mqtt://everyone:everyone@w2b.smn.gob.ar:1883
    Ejemplo: Ezeiza en OSCAR → [https://oscar.wmo.int/surface/#/search/station/stationReportDetails/0-20000-0-87576](https://oscar.wmo.int/surface/#/search/station/stationReportDetails/0-20000-0-87576)
    1. Fuente + estación que cumpla: cruda, 10+ años, <60 min, todas las variables, verificable
    No existe en Argentina. Este es el hallazgo clave de la investigación:
    | Requisito | ¿Quién lo cumple? |
    |-----------|------------------|
    | Dato crudo de estación real | SMN, INTA, INA |
    | 10+ años de historia | INTA (diario), SMN WIS2 (NO, solo 5 meses) |
    | < 60 minutos de frecuencia histórico | Ninguno (INTA 10 min solo hoy, SMN 1-6h solo 5 meses, INA horaria solo 3 años) |
    | 5 variables fundamentales | SMN (sí), INTA (NO tiene viento ni presión) |
    | Verificable por estándar abierto | SMN WIS2 |
    La mejor aproximación es dual:
    2. Open-Meteo a 15 min para el período largo + frecuencia sub-horaria (aceptando que es interpolado)
    3. SMN WIS2 para datos crudos reales, verificables, aunque solo desde feb 2026 y 1-6 h de frecuencia
    Si se necesita estrictamente dato crudo + histórico largo + sub-horario, habría que buscar datos de estaciones meteorológicas privadas (Red Meteorológica RMET, Davis WeatherLink, etc.) o gestionar el acceso a la API interna del SMN (no pública vía WIS2).

---

### Sintesis del modelo y los datos:

- **propuesta sobre la estructura del modelo LIF.**
    - **Estructuralmente.**
        
        Se utilizara un modelo deterministico basado en el modelo matematico LIF. Este modelo dependera de variables esenciales para la prediccion climatica de los eventos de lluvia.
        
        Se plantean 3 variables fisicas: Presion, Temperatura y la humedad. Esenciales para la prediccion de tormentas.
        
        - Si bien para una prediccion mas exacta se necesitan 3 variables extras: Altitud, Viento en altura y choques de aire.
        - Al ser un modelo simplificado utilizaremos las variables esenciales para una prediccion a muy corto plazo (0-3 horas), añadiremos una variable mas ademas de las 3 variables fisicas presentadas anteriormente, siendo esta el “viento“ en sus compoententes de “velocidad” y “direccion”.
        
        El modelo LIF funciona mediante una carga, acumulacion, y descarga, donde si la acumulacion supera cierto umbral, pasa ocurrir un spike.
        Se plantea una estructura de 5 neuronas LIF, donde cada sensor tenga una neurona asociada a el, y estas 5 neuronas se asocien a una unica neurona que provoque la alerta. En total utilizariamos 6 neuronas para la prediccion del evento.
        
        [Sensor V.Direccion] --> (Neurona Vd) -
        [Sensor Presión]     --> (Neurona P)  --
        [Sensor Temperatura] --> (Neurona T)  ---> (Neurona Salida: ALERTA TORMENTA)
        [Sensor Humedad]     --> (Neurona H)  --/
        [Sensor V.Velocidad] --> (Neurona Vv) -/
        
        **¿Utilizamos un pluviometro (precipitacion) como neurona?**
        
    - **Matematicamente.**
        
        La **ecuacion del modelo LIF** consiste en una **EDO de primer grado:**  
        
        - EDO propuesta:
        
        $$
        \tau_m \frac{dV(t)}{dt} = -(V(t) - V_{rest}) + R \cdot I(t)
        $$
        
        - Para el programa, se simplifica en:
        
        $$
        V(t + \Delta t) = V(t) + \frac{\Delta t}{\tau_m} \left[ -(V(t) - V_{rest}) + R \cdot I(t) \right]
        $$
        
        Los datos que se le ingresen a cada neurona deben ser normalizados, para no romper la escala. Se convierten en un numero adimensional.
        
        - Se calcula como una funcion por partes, donde se define el rango minimo (cero) y el rango maximo (Imax) esperable, se define el dominio para que no superen ese rango establecido, y se normalice el valor. Si el sensor detecta valores aun mas altos, el valor adimensional entregado sigue siendo el limite (Imax).
        
        Esto funcionara como un bucle, que acumulara los spikes generados por las neuronas conectadas a los sensores, cuando supere el umbral dado, la cuarta neurona genera un spike que sirve de “Alerta” para la tormenta.
        
        **Asignacion de parametros:**
        
        - Parametros arbitrarios pero logicos para plantear la base del modelo.
        • **V_rest (Voltaje de reposo) = 0:** Si no hay tormenta ni cambios en los sensores, la neurona tiende a quedarse en cero.
        • **V_reset (Voltaje de reinicio) = 0:** Cuando la neurona tira un *spike* (alerta), se vacía por completo y vuelve a empezar desde cero.
        • **V_th (Voltaje umbral) = 1.0:** El 100% del potencial de la neurona es el límite. Si el voltaje llega a 1.0, se dispara la alerta.
        • **R (Resistencia de membrana) = 1:** Se fija en 1 para que desaparezca de la multiplicación ($R \cdot I = 1 \cdot I = I$). Así, la “corriente“ entra directo al modelo sin escalar el voltaje.
        - La ecuacion queda:
        
        $$
        V(t + \Delta t) = V(t) + \frac{\Delta t}{\tau_m} \left[ -V(t) + I(t) \right]
        $$
        
        - Estos valores se asigan segun el sistema utilizado: Todos los valores deben respetar la misma unidad de tiempo.
            - $\Delta t$: Simboliza el paso del tiempo, el valor se asigna en base a cada cuanto tiempo se obtienen los datos: 1 min, 60 seg, segun convenga.
            - $\tau_m$: Hace referencia a la “memoria” de la neurona, por cuanto tiempo preserva el dato entregado, esto va acorde al fenomeno analizado y su variacion en el tiempo. Se deben poder cruzar los datos nuevos con los viejos.
            - $k$: Constante de ganancia, se regula para que ante una variacion anormal, permita generar pulsos relevantes para el spike. Se calcula mediante: $k = \frac{I_{max}}{\Delta W_{max}}$. Donde $\Delta W_{max}$ es el valor maximo esperado para ese fenomeno (presion, temperatura, etc).
        - Se utilizara un metodo basado en datos, donde se deja al modelo en un bucle automatizado leyendo los datos de los registros historios de los sensores, donde se ajustara de forma automatica los valores internos de las variables del sistema, permitiendo tener un modelo con los valores precisos para la correcta predicion.

- **Determinar variables y servicio meteorologico a utilizar para extraerlas.**
    - **Determinar viabilidad de tiempos necesarios para predecir la tormenta.**
        - Se determino que una frecuencia de “1h” es suficiente para la prediccion de eventos de lluvia con una tasa de exitos y fallos razonable segun investigaciones y pruebas externas previas.
        - Se definen las variables a recolectar como: Humedad, Presion, Temperatura, Viento (Velocidad, direccion)
    - **Determinar lugar de la recoleccion de datos.**
        - Debido a la cercania y transparencia local, se utilizaran estaciones meteorologicas nacionales (Argentina).
        - Entre ellas se pueden identificar a estas estaciones principales: Aeroparque (CABA); Córdoba (SACO); Ezeiza (SAEZ).
    - **Determinar entidad de la recoleccion.**
        - Se utilizara la pagina “open meteo” para la recoleccion de datos, debido a su accesibilidad, extensa base de datos y facilidad de recoleccion por API. https://open-meteo.com/
        - Se puede utilizar como alternativa la pagina OGIMET, ****para chequear datos especificos como la clasificacion del fenomeno. https://www.ogimet.com/
        - Como anexo se pueden incluir datos brindados por el Servicio Meteorológico Nacional: https://www.smn.gob.ar/descarga-de-datos

---

## 4) REDACCION DEL PAPER

En esta seccion se desarrolla el planteamiento, analisis, ejecucion de la investigacion y proyecto, narrado para la adaptacion al PAPER.

### 3.1 Resumen (Abstract)

Redacta un párrafo inicial de prueba. Debe incluir: contexto/problema, enfoque propuesto, método, resultados esperados, contribución.

**Plantilla:**

> "La detección temprana de tormentas locales sigue siendo un desafío en zonas con recursos limitados, donde los sistemas comerciales son costosos y los métodos de umbral simple producen altas tasas de falsas alarmas. Este trabajo propone un sistema de alerta temprana de bajo costo basado en un modelo de neurona LIF (Leaky Integrate-and-Fire) simplificado, aplicado como detector de anomalías en series temporales de variables atmosféricas (presión, temperatura, humedad). A diferencia de las redes neuronales tradicionales, el modelo LIF procesa datos de forma event-driven, lo que permite un cómputo eficiente en hardware de gama baja. Se simulará el modelo utilizando datos del SMN [o dataset específico] y se comparará su tasa de detección y falsos positivos contra un baseline de umbrales fijos. Se espera demostrar que el enfoque LIF reduce significativamente las falsas alarmas manteniendo una sensibilidad competitiva, validando su viabilidad como base para sistemas de alerta descentralizados y de bajo costo."
> 

### Resumen (Abstract): (Inicial)

La deteccion temprana de lluvia local sigue siendo un desafio actual en zonas con recursos limitados, requiere sistemas de deteccion costosos para una precision decente, utilizando alternativas simples como los metodos de umbral fijo produciendo altas tasas de falsas alarmas. Este trabajo propone la ultilizacion del modelo matematico de neurona LIF (Leaky Integrate-and-Fire) simplificado para un sistema de alerta temprana de bajo costo, utilizado como detector de anomalías en series temporales de variables atmosfericas (presión, temperatura, humedad, precipitacion y viento). El modelo LIF acumula pulsos (potencial de membrana), genera decaimiento (fuga de potencial) y emite un disparo al superar el umbral (Spike) permitiendo simularlo con operaciones basicas que producen un computo eficiente en hardware de gama baja. Se utilizaran datos proporcionados por el dataset “GHCNh” del NOAA y se comparara la tasa de deteccion y falsos positivos contra un modelo baseline de umbrales fijos. Se espera demostrar que el modelo LIF reduce significativamente las falsas alarmas manteniendo una sensibilidad competitiva y validar la viabilidad del sistema propuesto como una herramienta alternativa al modelo de umbrales fijos para la deteccion de lluvia en entornos locales a bajo costo.

- **Desarrollo parte por parte:**
    
    **contexto/problema:** 
    
    La deteccion temprana de lluvia local sigue siendo un desafio que requiere sistemas comerciales costosos para una precision decente, donde las alternativas baratas como los metodos de umbral simple producen altas tasas de falsas alarmas. 
    
    **enfoque propuesto:** 
    
    Este trabajo propone la ultilizacion del modelo matematico de neurona LIF (Leaky Integrate-and-Fire) simplificado para un sistema de alerta temprana de bajo costo, implementado como detector de anomalías en series temporales de variables atmosfericas (presión, temperatura, humedad, precipitacion y viento).
    
    **método:**
    
    El modelo LIF acumula pulsos (potencial de membrana), genera decaimiento (fuga de potencial) y emite un disparo al superar el umbral (Spike) permitiendo simularlo con operaciones simples que producen un computo eficiente en hardware de gama baja. Se utilizaran datos proporcionados por el dataset “open-meteo” y se comparara la tasa de deteccion y falsos positivos contra un modelo baseline de umbrales fijos.
    
    **resultados esperados:**
    
    Se espera demostrar que el modelo LIF reduce significativamente las falsas alarmas manteniendo una sensibilidad competitiva.
    
    **contribución:**
    
    Se busca validar la viabilidad del sistema propuesto como herramienta para la deteccion de lluvia en entornos locales a bajo costo.
    

## 5) Inquietudes/Problemas.

**Estos problemas se deben resolver ANTES de programar el modelo.**

1. **Multiples analisis diferentes para la justificacion.**
    1. El paper consiste en una premisa clara de comparar un modelo LIF con un modelo de umbrales fijos.
    2. A medida que se avanzo en la especificacion del modelo, surgieron diferentes ambiguedades que se decidio limitar para centrar el caracter comparativo del paper junto al desarrollo del modelo, y no derivar en multiples comparaciones varias.
    3. Luego se propuso para abordar estas ambiguedades la comparativa de multiples variables, lo que lleva a una extension del paper y un posible trabajo demaciado abarcativo por “miedo” de no ser lo suficientemente riguroso o detallado.
    4. Las “comparaciones extras” que surgieron en esta especificacion fueron:
        1. **Estacionalidades:** Al tener alta variabilidad para la prediccion de lluvia en diferentes epocas del año, se decidio realizar 5 instancias del modelo diferente, las cuales seran entrenadas cada una en una estacion del año diferente y la quinta sera entrenada con los datos de todos los años en general (sin excluir estaciones).
        2. **Precision de los sensores:** Al no tener la disponibilidad de datos historicos para entrenar el modelo con datos de sensores de bajo costo, y existiendo la imposibilidad logistica y de tiempo de viajar a una estacion con los dispositivos pertinentes para adaptar los datos historicos de la estacion meteorologia a las variaciones pertinentes de los dispositivos de bajo costo.
            1. Se utilizaran los datos de la estacion de alta precision local, como la de villa maria en el Presidente Néstor Kirchner Regional Airport, sin embargo se piensa añadir ruido a las mediciones precisas para entrenar 2 instancias del modelo y comparar su precision:
                1. La intancia que se entrena con los datos precisos y la intancia que se entrenara con los datos alterados. Luego se comparara su precision para determinar el la medida porcentual de aciertos de cada modelo bajo el mismo periodo de tiempo.
2. **Datos inconsisos:**
    1. Se plantea la obtencion de datos de la estacion “Aeropuerto Regional Villa María”, sin embargo los datos se extran no de su pagina web oficial sino de un proveedor externo que permite un como uso de la API, el cual es openmeteo.
        1. ¿Esa API realmente muestra los datos oroginales? ¿Que tan seguro y fiable es? ¿Existen alternativas?
        2. ¿La estacion elegida es realmente la ideal, no existen otras estaciones con mayor sustento para la investigacion? ¿Es realmente fiable los datos recolectados de esta esatcion? ¿Se conoce sus dispositivos?
        3. Si es fiable a nivel de datos, precision y dispositivos para esta investigacion, ¿Es justificacion suficiente la eleccion de esta estacion para una proxima ampleacion del paper con datos historicos de la estacion adaptados a dispositivos de bajo costo?. ¿Que beneficios a nivel investigativo me dá elegir esa estación? 
        4. Verificar si a lo largo del periodo seleccionado cambiaron su dispositivos de medición. Tomar un periodo donde esos dispositivos no hayan cambiado.
    
    **RESOLUCION:** Se utilizara la plataforma meteostat junto a analisis del SMN para la estacion particular de SECO en cordoba o Ezeiza en Buenos Aires.
    
    - Esto se debe a que se necesitan datos precisos y confiables, que permitan ser verificados y comprobados por informacion extraida de entes oficiales como el SMN y la MWO.
    - Debido a esto se decidio utilizar de referencia a estaciones que cumplan los estandares del SMN y el MWO, recibiendo un WMO ID particular. Esto verifica tanto su autenticidad, transparencia y metodos/dispositivos utilizados.
        - Junto a ello se debe poder extraer sus datos de manera practica y fiable, por lo que se utilizara meteostat para la extraccion de datos, y la plataforma del SMN para la verificacion y validacion de estos, junto a ello se puede implementar el uso de la plataforma “Visual Crossing” para respaldar las observaciones de las diferentes variables. De esa forma nos aseguramos de obtener mediciones lo mas fiables posibles a la realidad.
3. **Estudio de teoria y referencias:**
    1. Se deben confirmar 2 cuestiones fundamentales:
        1. ¿Me debo saber la teoria de pies a cabeza sobre como funcionan las neuronas LIF, o el concepto general me basta para explicar el modelo? Eso cambia si debo estudiar los papers completos o solo los conceptos fundamentales de este.
        2. ¿Hay demaciadas referencias? Actualmente exiten multiples citas a trabajos, papers y documentos tecnicos que aportan veracidad a los temas tratados, pero ¿son necesarias tantas referencias distintas? ¿Se puede acortar el numero de referencias o se necesita todo para mayor rigurosidad? Algunas referencias dan la impresion de ser redundantes o aportar conceptos/justificaciones minimas.