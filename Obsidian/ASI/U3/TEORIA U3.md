Conceptos de: Ingeniería de Software – Proyecto – Proceso – Producto - Método – Técnicas – Herramientas.

El Proceso de Desarrollo – Modelos de Proceso: Concepto. Importancia. Actividades genéricas - Distintos modelos de proceso.

Presentación del Proceso Unificado de Desarrollo (PUD) y el Lenguaje Unificado de Modelado ([UML](https://cvirtual.frvm.utn.edu.ar/mod/resource/view.php?id=137373 "UML")), su utilidad y contribución a la ingeniería de software.

Pensamiento ágil. Surgimiento. El manifiesto ágil. Marcos ágiles de trabajo: SCRUM.

---
## Modelos de procesos de desarrollo de software: Presentacion

Es un marco estructurado que define etapas para el desarrollo de software.
- Se plantea la crisis del software:
	- Demanda creciente (en aumento) de aplicaciones para harware. (Software)
	- Amplicaciones cada vez mas exigentes.
		- Mas complejidad.
		- Tiempo menor de desarrollo.
	- Significado de **"desarrollar software":**
		- Atender requisitos y satisfacer grupos de interes (stakeholders).
		- Respetar costos y cronogramas.
	- El resultado son productos de baja calidad y procesos con bajo grado de satisfaccion y productividad.
		- Osea al hacer rapido el software complejo da como resultado un producto mediocre que no cumple las espectativas de la organizacion.

- Problemas en la construccion del software:
	- No cumplen las especativas de los usuarios.
	- Hay fallas recurrentes em el programa.
	- Dificil prevision de costos.
	- Modificar el software es dificil y costoso.
	- Menor calidad y sobrepaso de la fecha limite.
	- Dificultad al modificar el hardware con el mismo software.
	- No se aprovecha de forma optima los recursos.

- Posibles causas del mal desarrollo de software.
	- Escasa/tardia validacion del cliente.
	- Inadecuada gestion de requisitos.
	- Sin medicion del procesos/datos historicos.
	- Estimaciones inprevistas de plazos de desarrollo y costos de este.
	- Irracional presion en cumplir plazos.
	- Sin gestion de riesgos formales.
	- SIn proceso formal de pruebas.
		- Ni inspecciones del software/codigo.

#### ONG IEEE:
- Define la aplicacion de la ingenieria en el software.
- la ingeniería de software es la aplicación de un enfoque **sistemático, disciplinado y cuantificable** al desarrollo, operación y mantenimiento de software. En esencia, busca aplicar principios de ingeniería para producir software fiable, eficiente y de alta calidad dentro del ciclo de vida

El objetivo de la ingenieria de software es lograr un producto de calidad, mediante un proceso apoyado en metodos y herramientas.

#### El proceso de desarrollo de software:
- Para la correcta construccion un producto o sistema se deben seguir pasos predecibles.
- Definicion procesos:
	- Una serie de pasos realizados para un proposito determinado.
	- Es lo que la gente hace, usando procedimientos, métodos, herramientas y equipos, para transformar materia prima (entrada) en un producto (salida) que tienen valor para un cliente.
	- Una serie de procedimientos, metodos, herramientas y equipos trabajando conjuntamente para transformar la materia prima (entrada) en un producto (salida), resultando en mayor satisfaccion para el cliente.
- En la ingenieria de software la entrada correpsonde  a los requerimentos, y la salida al software desarrollado.
- La calidad del producto esta atada a la calidad del proceso que lo realizo.

**Definicion de calidad en software:**
- **Calidad es cumplir con los requerimientos de alguien.**
- **Calidad es el valor para una persona** 🡪 Valor es aquello que se está dispuesto a pagar para obtener sus requerimientos.
- **Calidad es satisfacción de las necesidades y expectativas de los clientes y usuarios** – consumidores “a menor costo”.
- **Modelos de calidad:**
	◻ ISO (Organización Internacional de Normalización) – ISO
9001:2008
	◻ CMMI (Capability Maturity Model Integration)
Suponer las necesidades del cliente provoca que creemos un producto en base a nuestra pespectiva, sin ser lo que realmente el cliente quiere, y por lo tanto, de una calidad baja para ellos.

#### Importancia desarrollo de software:
Debe ofrecer estabilidad, control, organizacion a una actividad que si no se lo da, puede volverse caotica.
Ademas de esa premisa, el desarrollo de software debe ser agil, permitiendo documentar y pulir aquellas actividad esenciales para el sistema.
Se prioriza la entrega de valor antes de la burocracia.
Se necesitan procesos para dar previsibilidad a los proyectos y permitir escalarlos, de esto nace un debate entre 2 idiologias:
- Se plantea la discrepancia entre:
- **Estabilidad y organizacion (proceso rigido)** donde todo se documenta y avanza con planificacion previa. Volviendolo lento y caro.
- **Desarrollo agil (organizado pero flexible),** que no se centra en hacer las cosas rapido simplemente, sino en poder adaptar el proyecto si en un momento se lo requiere, eso significa poder. Cumple el mismo objetivo pero de manera eficiente.
	adaptarse a los tiempos modernos sin tener que cambiar todo el software.
	Se propone una documentacion inteligente, que el proceso contenga lo indispensable de informacion para poder orientar al equipo y que el producto tenga calidad sin 
	informacion innesesaria en el proceso.

#### Actividades del proceso
Actividades genéricas del proceso:
	■ Definición: el Qué. Incluye: planificación del proyecto y
	análisis de requisitos.
	■ Desarrollo: el Cómo. Incluye : diseño del sw, generación del
	código y prueba del sistema.
	■ Mantenimiento: el Cambio.
		◻ Corrección de errores.
		◻ Adaptaciones por evolución del entorno.
		◻ Mejoras en el negocio. Aumento de la capacidad del producto.
	Actividades de Soporte (actividades protectoras):
	■ Seguimiento y control de proyectos
	■ Gestión de riesgos
	■ Aseguramiento de la calidad del software
	■ Revisiones técnicas formales
	■ Medición
	■ Gestión de la configuración del software
	■ Gestión de la reutilización
	■ Preparación y producción del producto de trabajo

#### Proyecto de desarrollo de software: Son instanciaciones del proceso
Los proyectos de desarrollo de software son instanciaciones del proceso definido organizacionalmente.
![[Pasted image 20260501202103.png|569]]


#### Modelos de proceso de desarrollo de software:
Modelo para basarse a la hora de desarrollar software.
- Define la estructura del proceso, basado en un desarrollo racional y controlable.
- Todos inicialmente conocen los requisitos.
- Aumentan la calidad de resultados parciales y finales.
- Se documenta todo el proyecto.
- Los modelos no son rigidos.
- Se determina el orden de las fases. Guia extra del orden de actividades.
- Criterios de transicion entre fases.
- Cada face tiene paremtros de control.
- Planifican en base a que el software tiene un ciclo de vida.
	- Se propone, se contruye, se mantiene y finalmente muere.
	- Este es el ciclo de software debido a que son dinamicos, siento al fase de mantenimiento la mas longeba.
	- Los software se hacen flexibles debido a que tienen que evolucionar, osea adaptarse a los diferentes cambios, y eso es parte del ciclo de vida.
- #### Tipos de modelo:
	- Lineal/cascada:** Modelizado a partir del ciclo convencional de la ingenieria.
		- Se divide en etapas, la documentacion de las etapas son entradas para otra etapa, se desarrolla una por una.
		**Ventajas:** Sencillo de plantear.
		◻ Planificación sencilla.
		◻ Una plantilla estructurada para ingeniería de software.
		**Desventajas:** Costoso, tardado, errores ignorados, sin poder evolucionar.
		◻ Las iteraciones son costosas y aunque son pocas es normal congelar parte del
		desarrollo y continuar con las siguientes fases.
		◻ Los problemas se dejan para su posterior resolución, lo que lleva a que estos
		sean ignorados o corregidos de una forma poco elegante.
		◻ Existe una alta probabilidad de que el software no cumpla con los requisitos del
		usuario por el largo tiempo de entrega del producto.
		◻ Es inflexible a la hora de evolucionar para incorporar nuevos requisitos. Es difícil
		responder a cambios en los requisitos.
		**Útil en proyectos:**
		◻ Con todas las especificaciones claras inicialmente.
		◻ Productos no novedosos.
	- **Contruccion de prototipos:** Consiste en contruir prototipos del producto final antes de desarrollarlo, para que el cliente lo apruebe.
		- No es el producto final, sino un modelo a escala para verificar ciertas funcionalidades.
		- **Tipos del modelo:**
			- Prototipo en papel o un modelo basado en PC que describa la interacción hombre-máquina.
			- Prototipo que implemente algunos subconjuntos de la función requerida del programa deseado.
			- Programa existente que ejecute parte o toda la función deseada pero que tenga otras características que deban ser mejoradas en el nuevo trabajo de desarrollo.
		- Sirve cuando el cliente no sabe lo que quiere o los requisitos son inentendibles.
	- **Proceso evolutivo:** Permiten desarrollar versiones cada vez mas complejas del software
		- **Tipos:**
			- ![[Pasted image 20260501205240.png|509]]
		- **Modelo Incremental:**
			- Cada etapa consiste en expandir incrementos de un producto de software operacional.
			-  Los incrementos pueden ser entregados al cliente.
			-  Cada incremento es diseñado, codificado, probado, integrado y entregado por separado.
			-  Los incrementos se desarrollan uno después de otro
			**Ventajas:**
			-  La especificación puede desarrollarse de forma creciente.
			-  Los usuarios y desarrolladores logran un mejor entendimiento del sistema.
			- Ideal cuando es difícil establecer todos los requerimientos por anticipado.
			- Se obtiene una rápida retroalimentación del usuario, ya que las actividades de especificación, desarrollo y pruebas se ejecutan en cada iteración.
			**Desventajas:**
			-  Este modelo sólo es efectivo en proyectos pequeños o medianos con poco tiempo para su desarrollo y sin generar documentación para cada versión.
			-  Si los requerimientos crecen, la arquitectura y el diseño puede cambiar drásticamente.
	- **Modelo en Espiral**
		-  Propuesto por Barry Boehm en 1988
		-  Desarrollo en ciclos.
		-  En cada ciclo:
			-  se define el objetivo,
			-  se analizan los riesgos, desarrollo y verificación de la solución obtenida,
			-  revisión de resultados y planificación del siguiente ciclo.
		![[Pasted image 20260501205733.png|254]]
		- Ventajas:
			-  Resolución temprana de riesgos.
			-  Definición de arquitectura en sus fases iniciales.
			-  Basado en un proceso continuo de verificación de la calidad.
			-  Ideal para productos con un nivel alto de inestabilidad de los requerimientos.
		-  Desventajas:
			-  No aplicable a proyectos bajo contrato.
			-  No recomendable en proyectos simples por su alto costo.

## UML:
