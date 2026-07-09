# Modelo LIF simplificado de detección de eventos climáticos

Debilidad: Tenés que ser muy preciso en llamarlo "modelo LIF simplificado inspirado en neurociencia computacional" y no "red neuronal de picos" ni "SNN”

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

- **Presicion:** Solo alerta cuando las condiciones realmente se confirmaron, evitando falsos positivos. (Caracteristica modelo LIF)
- **Bajo costo:** Permite utilizar el modelo y sensores con poco capital.
- **Solucion de un problema real:** Una necesidad real resuelta a bajo costo con alta presicion.

Para su aplicacion utilizaremos la tegnologia bioinspirada llamada LIF. Esta tegnologica consiste en Integracion y disparo con fugas, consiste en un modelo matematico para simular neuronas biologicas en su fucionamiento basico, sin embargo utilizaremos una version simplificada del mismo, donde simularemos una unica neurona con parametros simples para el experimento en cuestion.

---

## Propuesta:

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

## Desarrollo:

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
        
        ![image.png](Modelo%20LIF%20simplificado%20de%20detecci%C3%B3n%20de%20eventos%20cl/image.png)
        
    
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

# Base sobre la que construir

- **GUIA**
    
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
    

Se habla de un trabajo o investigacion.

Para plantear la base debemos responder 3 preguntas fundamentales, que van a ir dando forma al trabajo a realizar:

1. **Formalización de la idea de investigación** (¿qué vas a investigar realmente?)
2. **Delimitación del proyecto** (¿dónde empieza y dónde termina tu trabajo?)
3. **Preparación de la propuesta para CNEISI** (lo mínimo que necesitas tener definido antes de escribir una línea de código)

# Entrega del PAPER: 28/08/26

[Pendiente](Modelo%20LIF%20simplificado%20de%20detecci%C3%B3n%20de%20eventos%20cl/Pendiente%2038b3a6e010e380cd92c1f7b943230814.csv)

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
    
    ![image.png](Modelo%20LIF%20simplificado%20de%20detecci%C3%B3n%20de%20eventos%20cl/image%201.png)
    
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
        
        ![image.png](Modelo%20LIF%20simplificado%20de%20detecci%C3%B3n%20de%20eventos%20cl/image%202.png)
        
- Existen otros modelos aparte de LIF, sin embargo este es el que permite representar de forma solida y eficiente las señales necesarias, sin agregar complejidad extra innecesaria al modelo.
    
    ![image.png](Modelo%20LIF%20simplificado%20de%20detecci%C3%B3n%20de%20eventos%20cl/image%203.png)
    
- **No necesita entrenamiento exaustivo.**
    - Si bien se necesita una serie de pruebas para determinar el valor ideal para las variables del modelo, no se realizara un entrenamiento exaustivo como el “Surrogate Gradient Learning”, los valores de las variables utilizadas se ajustaran manualmente o por “grid search”, debido a la simplicidad del modelo. El paper de Maass (1997) permite explicar el potencial computacional y capacidad subyacente de este modelo sin necesitar entrenamiento previo.

#### Definicion del modelo a utilizar

- El modelo es un LIF de una sola neurona con parámetros fijos (deterministico), sin aprendizaje, implementado en Python, usando rate coding (frecuencia de disparo) implícito. Esto es exactamente lo que EONS y Vacuum Spiker usan como arquitectura mínima para detección binaria en series temporales. 
La diferencia original del trabajo es el dominio de aplicación (variables climáticas argentinas del SMN) y la comparación directa contra un detector de umbral estático como punto de partida para la evaluacion.
- **Tabla comparativa:**

![image.png](Modelo%20LIF%20simplificado%20de%20detecci%C3%B3n%20de%20eventos%20cl/image%204.png)

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

**¿Con que presicion se predice tormentas segun la interpretacion de estas variables?**

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

**Datos satelitales:** Gran cobertura geografica brindando alta presicion a costa de un gran gasto en la infrestructura, y delegando la localizacion y prediccion a corto plazo.

**Infrestructura terrestre:** Brinda alta presicion y confiabilidad local pero produciendo un costo elevado al construir y mantener la infrestructura.

**Metodos de umbrales fijos:** Simples y baratos de implementar, pero generando una baja presicion aumentando apleamente la tasa de falsas alarmas.

#### Propuesta y puntos clave

El modelo LIF adaptado a las tormentas plantea equilibrar alta presicion con el bajo costo de la infrestructura necesaria.

Permite en base a sensores de bajo costo (comparado a la infrestructura terrestre u orbital de las estaciones meteorologicas) y un modelo matematico adaptado, poder brindar un modelo simple y barato de implementar con una presicion mayor al umbral fijo.

### Delimitación del Proyecto:

#### Que se va a hacer

Se quiere desarrollar un modelo predictor de eventos de lluvia basado en el modelo matematico LIF (Que son redes neuronales pico en su version simplificada).

**Se plantean los siguientes requisitos:**

- Origen de los datos.
- Ubicaciones a predecir por el modelo.
- Rango de prediccion.
- Epoca del año.
- Lenguaje y programa de implementacion.
- Tipos de lluvia.
- Modelo comparativo.
- Datos a utilizar.
- Modelo a desarrollar.

**Puntos principales:**

| **Dimension** | **Atributo** | **Dato** |
| --- | --- | --- |
| Geografia | Ubicacion fija. | Aeropuerto Internacional Ingeniero Aeronáutico Ambrosio Taravella, Cordoba, Argentina. |
| Rango | Horizonte a muy corto plazo. | 2h a 5Min. |
| Estaciones | Determinada (Analisis) | Se entrenara en cada estacion en particular y luego se entrenara en base a todas las estaciones, se comparara cada modelo para determinar que estacion tiene mayor tasa de acierto y si el entrenamiento en base a estaciones particulares es superior al entrenamiento en general con todas las estaciones. |
| Proveedor | Externo | Se utilizara un proveedor que permita acceder a los datos de forma directa y eficaz para el entrenamiento. No seran datos extraidos de forma individual, sino que se utilizaran datos provistos por la institucion dueña de la infrestructura. https://open-meteo.com/ |
| Evento | Evento de Lluvia | Se buscara predecir unicamente eventos de lluvia que provoquen precipitaciones. |
| Implementaciontecnica | Accesible y simple | Se eligira un lenguaje y IDE que permita extraer los datos de forma sencilla y eficaz, entrenar el modelo LIF a desarrollar y brindar correctamente los resultados extraidos del modelo. 
Se buscara algo eficaz y sencillo de trabajar que sea util para la investigacion debido al interes centrado en la comparativa y no en la implementacion eficiente u optimizacion del programa final. |
| Modelo comparativo | Umbrales fijos | Se utilizara un modelo tradicional basado en umbrales fijos especificado en metodologia para comparar la presicion del modelo LIF simplificado. |
| Datos | 6 datos principales | Se extraeran 6 datos fundamentales de los sensores brindados por el proveedor, que permitan entrenar el modelo, estos son: Temperatura, presion, humedad, precipitacion, viento (velocidad|direccion).
Se utilizara la precipitacion como confirmacion de que ocurrio la lluvia, con el objetivo de utilizarlo como feedback en el entrenamiento del modelo (Metrica de exito). |
| Modelo a desarrollar | Basico y determinista | El modelo matematico LIF a utilizar representara una red minima de apenas 6 neuronas que representaran individualmente cada sensor especificado (Temperatura, presion, humedad, viento (velocidad|direccion), evento de lluvia (Neurona de alerta)). Se utilizara la ecuacion diferencial ordinaria que representa al comportamiento de una neurona, y se ajustaran los valores de cada una de las 6 neuronas individualmente en el “entrenamiento”.
Se ajustaran los valores con el entrenamiento que permita maximizar la presicion y simplicidad de ejecucion. |

#### Que NO se va a hacer

Se detallan las caracteristicas y areas que NO va a abordar esta investigacion:

- NO se entrenara un mismo modelo para multiples ubicaciones diferentes.
- NO se desarrollara para rangos de predicion de mas de dos horas. Aunque pueda lograr una prediccion de ese rango.
- NO se predeciran tormentas. Solo se predeciran eventos de lluvia especificados en la metodologia.
- NO se utilizaran datos mas complejos a los especificados, como imagenes satelitales. Solo se utilizaran 5 sensores terrestres determinados como:  Temperatura, presion, humedad, precipitacion, viento (velocidad|direccion).
- NO incorporara un sistema de alerta temprana que se comunique con organismos, autoridades, ciudadanos o cualquier infrestructura de alerta compleja . Solo se alertara de forma simbolica en el software desarrollado.
- NO se utilizaran sensores personales para el entrenamiento, analisis u desarrollo. Se utilizaran datos de un proveedor externo.
- NO se implementara en hardware embebido real. Solo se simulara por software.
- NO se desarrollara un modelo probabilistico. Se utilizara el modelo matematico LIF deterministico que representara una red neuronal de tercera generacion simplificada.
- NO se centrara optimizar la latencia de los dispositivos u otro atributo tecnico relacionado. Se centrara en desarrollar un modelo teorico predictivo util.
- NO se comparara el modelo LIF simplificado a desarrollar con modelos mas complejos y avanzados que sean diferentes al modelo tradicional de umbrales fijos especificado en la metodologia.
- NO medira intensidad de la lluvia. Solo mide el evento de lluvia determinado en la metodologia.

---

### Investigacion redes SNN (redes neuronales de pico)

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

### Metodologia inicial (provisoria):

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

### Metodología (diseño experimental)

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
- ¿De que forma se miden los datos?
    
    Determinar el formato de medicion de estos datos necesarios, para que no haya ambiguedades en la forma de medirlos.
    
- ¿De donde se obtienen los datos?
    
    determinar pagina donde se obtienen, y resaltar porque no utilizar otras paginas mas rigurosas como la de OMM, o capaz el SMN, o algo asi, y justificar hasta la muerte el uso de open meteo y no la utilizacion de otra fuente o de datos propios.
    
    Justificar que los datos recolectados efectivamente cumplan los metodos explicados en la seccion anterior.
    
- ¿Que ubicacion se utilizaran para el analisis?
- ¿Que frecuencia de muestreo se utilizara?

#### Preprosesamiento de los datos:

#### Modelo LIF:

#### Definicion baseline:

#### Protocolo de evaluacion:

Define paso a paso cómo ejecutarás tu experimento:

| Paso | Qué debes definir |
| --- | --- |
| **1. Adquisición de datos** | ¿De dónde obtienes los datos? ¿Qué variables usas? ¿Frecuencia de muestreo? |
| **2. Preprocesamiento** | Normalización, detección de outliers, ventanas temporales |
| **3. Definición del modelo LIF** | Ecuación de membrana, parámetros, cómo se codifica la entrada a spikes |
| **4. Definición del baseline** | ¿Qué regla de umbral usarás para comparar? |
| **5. Protocolo de evaluación** | ¿Cómo medirás éxito? ¿Qué métricas? (precisión, recall, F1, tasa de falsos positivos) |

**Tu tarea:** Escribe un borrador de los 5 pasos anteriores, con el nivel de detalle que te permita empezar a programar.

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
        
        [Sensor V.Direccion] --> (Neurona Vd) -\
        [Sensor Presión]     --> (Neurona P)  --\
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

La deteccion temprana de lluvia local sigue siendo un desafio actual en zonas con recursos limitados, requiere sistemas comerciales costosos para una presicion decente, donde las alternativas baratas como los metodos de umbral fijo producen altas tasas de falsas alarmas. Este trabajo propone la ultilizacion del modelo matematico de neurona LIF (Leaky Integrate-and-Fire) simplificado para un sistema de alerta temprana de bajo costo, utilizado como detector de anomalías en series temporales de variables atmosfericas (presión, temperatura, humedad, precipitacion y viento). El modelo LIF acumula pulsos (potencial de membrana), genera decaimiento (fuga de potencial) y emite un disparo al superar el umbral (Spike) permitiendo simularlo con operaciones basicas que producen un computo eficiente en hardware de gama baja. Se utilizaran datos proporcionados por el dataset “open-meteo” y se comparara la tasa de deteccion y falsos positivos contra un modelo baseline de umbrales fijos. Se espera demostrar que el modelo LIF reduce significativamente las falsas alarmas manteniendo una sensibilidad competitiva y validar la viabilidad del sistema propuesto como una herramienta alternativa al modelo de umbrales fijos para la deteccion de lluvia en entornos locales a bajo costo.

- **Desarrollo parte por parte:**
    
    **contexto/problema:** 
    
    La deteccion temprana de lluvia local sigue siendo un desafio que requiere sistemas comerciales costosos para una presicion decente, donde las alternativas baratas como los metodos de umbral simple producen altas tasas de falsas alarmas. 
    
    **enfoque propuesto:** 
    
    Este trabajo propone la ultilizacion del modelo matematico de neurona LIF (Leaky Integrate-and-Fire) simplificado para un sistema de alerta temprana de bajo costo, implementado como detector de anomalías en series temporales de variables atmosfericas (presión, temperatura, humedad, precipitacion y viento).
    
    **método:**
    
    El modelo LIF acumula pulsos (potencial de membrana), genera decaimiento (fuga de potencial) y emite un disparo al superar el umbral (Spike) permitiendo simularlo con operaciones simples que producen un computo eficiente en hardware de gama baja. Se utilizaran datos proporcionados por el dataset “open-meteo” y se comparara la tasa de deteccion y falsos positivos contra un modelo baseline de umbrales fijos.
    
    **resultados esperados:**
    
    Se espera demostrar que el modelo LIF reduce significativamente las falsas alarmas manteniendo una sensibilidad competitiva.
    
    **contribución:**
    
    Se busca validar la viabilidad del sistema propuesto como herramienta para la deteccion de lluvia en entornos locales a bajo costo.