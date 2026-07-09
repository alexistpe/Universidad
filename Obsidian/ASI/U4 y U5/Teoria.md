## Temario:
Requerimientos: Concepto - Categorías - Tipos: Requerimientos funcionales y no funcionales.  
Ingeniería de Requerimientos. Dificultades con los requisitos.  
Procesos de la Ingeniería de Requerimientos: Estudio de Factibilidad - [Elicitación](https://cvirtual.frvm.utn.edu.ar/mod/resource/view.php?id=137394 "Elicitación") – Especificación – Validación.
**SINTESIS:** Ingenieria de requerimentos, elicitacion de r. funcionales y no funcionales.

## Requerimetos:
### Requerimentos de software:
Un requerimento es una funcion o condicion que se debe implementar en el nuevo sistema que se esta realizado (Incluir una caracteristica).
	Puede ser una forma de obtener datos, procesarlos o generarlos (producirlos), como tambien para dar apoyo.
Una condicion necesaria par alcancar el objetivo del usuario.
Una condicion o capacidad impuesta en el sistema que permitasatisfacer un documento formalmente impuesto.

### Ingenieria en requerimentos
Se trata de la definicion de requerimentos de forma colaborativa e iterativa mediante:
- Analizar el problema.
- Documentar los resultados obtenidos.
- Chequear la presicion de los modelos.

### Tipos de requerimentos:
Se divide en 2 categorias: Funcional y no funcional:
#### Funcional:
Se refiere a la integracion de un requerimento sin tener encuenta su implementacion real.

#### No funcional:
Se refiere a la integraciond e un requerimento teniendo en cuenta aspectos de su implementacion real en el sistema.

**Sinstesis:** En el funcional se plantea la propuesta sin implementarla, y en el No funcional se plantea implementandola en el sistema, conllevando a multiples analisis sobre la forma y capacidad de esa implementacion.

### Proceso de la ING en requerimentos:
Esto abarca 5 fases muy diferenciadas entre si, como resultado se obtiene el documento de especificacion de requerimentos de software apodado (ERS).
#### Analisis de factibilidad:
Analiza para decidir si vale la pena continuar con el desarrollo del sistema.
Tiene en cuenta 3 aspectos fundamentales:
- **Factibilidad tecnica:** Se trata de si la organizacion tiene los recursos tecnicos necesarios para implementar el sistema. (Ej: SI las computadoras del negocio son lo suficientemente potentes y compatibles)
- **Factibilidad economica:** Son los recursos economicos necesarios para que el sistema pueda: Terminar de desarrollarse, ponerse en funcionamiento y brindar el mantenimiento necesario. Si los recursos disponibles no alcanzan, se debe replantear el desarrollo y ajustarse a esos margenes o cancelarlo directamente.
- **Factibilidad operativa:** Plantea la diyuntiva de que **condiciones** debe cumplir las **personas que utilizaran el sistema****, analizar si estan capacitados, si hay que capacitarlos, etc...

#### Elicitacion:
Proceso por el cual se analiza el trabajo del cliente/usuario para determinar sus necesidades y por consecuencia los requerimentos para el sistema.
	Esto tambien incluye a las restricciones medioambientales.
	Como resultado se obtienen los requerimentos de todas las partes involucradas.
**Herramientas:**
	Entrevistas
	Cuestionarios
	Observaciones
	Otras
El analista cuenta con fuentes de informacion para la correcta elicitacion y produccion de los requerimentos:
- Expertos en el dominio
- Literatura sobre el dominio
- Software existene
- Software similar en otros dominios.
- Standares (Nacionales e internacionales)
- Consiste en los diferentes stakeholders.
#### Especificacion:
Consiste en la elaboracion del documento legal "ERS": En el cual se detallan los requerimentos propuestos para el desarrollo del software junto a diferentes medidas a implementar.
Este documento sera utilizado por gran parte del equipo, junto a ser un respaldo legal para el proximo desarrollo.
De aqui parten una serie de puntos para enmarcar un "estandar" de la ERS:
- La especificacion debe ser: Correcta, no ambigua, completa y verificable.
- Ademas de su caracter tecnico, puede ser utilizada y vista como un "contrato" para los diferentes usuarios y desarrolladores que participaran del proyecto.
- Es la declaracion oficial y detallada de los requerimentos. (Un documento completo donde se especifican a fondo los requerimentos)
- Es el punto de partida para el desarrollo del sistema.
- ![[Pasted image 20260524115631.png|269]]

#### Validacion:
Es un proceso donde se corrige el modelo de requerimentos en contraposicion de las intenciones del usuario para que juntos se pueda certifican un correcto artefacto para el desarrrollo.
Es el proceso donde se evalua lo analizado con la vision del usuario que lo necesita.
De aqui nacen varios metodos para la verificacion:
	- Prototipos: Un modelo rapido de construccion para la evaluacion y aprendizaje del sistema requerido.
	- Animacion: Es una vision grafica del proceso en accion: Se representan los objetos graficamente y se permite interactuar con ellos en tiempo real.
	- Lenguaje natural: Propone una vision amistosa atactando tanto las necesidades del analista como las del usuario.
	- Sistemas expertos: Son herramientas CASE, sirven para relevar requerimentos teniendo una base de buenas practicas junto al dominio en el que se va a trabajar. Es un ayudante que contiene la informacion necesaria para relevar los requerimentos.

### Documentos de especificacion de requerimentos de software (ERS):
Es un documento legal que especifica que se debe hacer en el sistema para satisfaccer los requerimentos detectados tanto en el usuario como del sistema.
La ERS abarca desde el usuario que pago para el desarrollo y adquisicion del software hasta los ingenieros responsables de este mismo.
- Es una declaracion oficial de lo que el sistema va a hacer para satisfacer los requerimentos indicados.
![[Pasted image 20260524122259.png]]

![[Pasted image 20260524111923.png|772]]

#### Participantes del proceso:
Aqui se incluyen a todas las personas que pueden participar del proceso de requerimentos:
- **Supervisores de control:** Quienes marcan los "puntos de control" (hitos) y cronogramas para el control de desarrollo, llevando a restringirlo.
- **Clientes y usuarios:** Deben identificar los requerimentos propuestos y verificar que satisfacen sus necesidades.
- **Gerertes de negocio:** Analizan las consecuencias que puede producir la construccion y uso del software.
- **Analista de negocio y funcionales:** Se encargan de comprender y extraer los requerimentos de la organizacion para luego implementarlas en el desarrollo del software.
- **Diseñadores:** Utilizan los requerimentos para aplicarla en una solucion aceptable que se implementara con un sistema basado en software.
- **Verificadores:** Son personas que se encargand e verificar que el software funcione correctamente en base a diferentes pruebas y sesiones.


## Extension de partes individuales:
### Elicitacion:
Obtencion y analisis de los requerimentos, incluyen a diferentes tipos de personas de la organizacion.
- Se utilizan diferentes fuentes de informacion, como: Usuario, formularios, informes, manuales, programas, etc...
**Metodos para la obtencion de informacion para identificar los requerimentos y analizarlos.**
- Entrevista: Conversacion dirigida en formato preguntas y respuestas.
	- Se busca tanto las opiniones como el sentimiento del entrevistado.
	- Permite identificar las reacciones y sentimientos del entrevistado.
	- Surgimiento de preguntas espontaneas y utiles.
	- Permite que el entrevistado se explaye.
- **Cuestionario:** Es una tecnica basada en preguntas, que permite obtener respuestas concretas ante las diferentes diyuntivas.
	- Permite obtener opiniones, posturas, conductas y caracteristicas de las diferentes personas de la organizacion.
	- Abarca gran numero de personas, el analisis posterior de las respuestas es mucho mas facil de procesar.
- **Oservacion:** Permite al analista observar que camino y como es manipulada la informacion dentro de la organizacion (obtenida, procesada, compartida, etc...)
	- Permite determinar como se trabaja (realizar actividades) en la organizacion y como se manipula la informacion entre personas.
- **Herramientas varias:** Foro, Panel, lluvia de ideas, Técnica Phillips 66.

**Tareas fundamentales de la elicitacion:**
	**Planeacion:**
	- Cuando y a quien le dirige la recoleccion de datos.
	- Conocimiento del dominio. Para una posterior consulta informada en los puntos clave.
	- Diseño de la herramienta propuesta.
	**Desarrollo:** 
	- Para la correcta obtencion de informacion se utilizan los metodos:
	- Toma nota.
	- Graba.
	- Filma.
	- Usan formularios.
	**Organizacion:**
	- Resumenes.
	- Informes.
	- Minutas.
	- Cuadros.
	- Listado de requerimentos
	- Especificacion de requerimentos.

## Requerimentos:
Se expandiran el material individual de los requerimentos funcionales y no funcionales.
Los requerimentos son caracteristicas que el programa tendran que nacen para solucionar una cierta necesidad del cliente, de forma directa o indirecta.
### Funcionales:
Estos requerimentos consisten en el analisis previo y teorico del problema, no tanto con la implementacion real, sino mas con la solucion propuesta.
Para poder identificar los requerimentos funcionales correctamente, se dividira la explicacion en diferentes puntos secuenciales (pasos).
#### 1) Dominio del problema.
De deben identificar el contexto y los objetivos del sistema a construir, esto lleva a cubrir los siguientes puntos.
- Identificar el TIPO de sistema a desarrollar, osea que es lo que vamos a desarrollar, que hace, como funciona, para que sirve.
- Identificar y analizar los procesos de negocio que seran soportados por el sistema.
- Conocer actores involucrados, y las responsabilidades de cada uno.

#### 2) Actores.
Para un buen desarrollo del sistema, se deben identificar los actores de este.
Un actor es una entidad que interactua con el sistema.
Un actor puede ser tanto un ser humano con un cierto rol (Encargado, administrador, chofer), como tambien otro sistema que intercambie informacion con nuestro sistema a desarrollar.

Tip practico: Realizar una tabla con el nombre del actor y su descripcion de que funcion cumple en este sistema.

#### 3) Recolectar informacion.
Se debe recolectar informacion para determinar los requerimentos, por lo que se utilizan diferentes tecnicas como:
- Entrevistas.
- Analisis de documentos.
- Observaciones.

#### 4) Redactar Requerimientos Funcionales.
Los requerimentos funcionales consisten en lo que el programa debe hacer.
Funcionalidad especificas que permitiran satisfacer las necesidades del usuario.
**Estructura esperada:**
- Debe comenzar con un verbo en infinitivo: Registrar, consultar, emitir.
- Indicar que accion realiza el sistema y en que entidad se aplica. Se debe explicar claramente.
- Determinar si corresponde a un cierto actor.
Ej: Registrar los datos personales de un nuevo chofer.

**Buenas practicas:**
- Ser concisos pero específicos.
- Evitar ambigüedades (“el sistema debe ser fácil de usar” no es funcional y además es
ambiguo).
- Enfocar cada requerimiento en una única funcionalidad.

#### 5. Agrupar por actor/modulo funcional
Una vez redactado lo anterior, para una mayor organizacion, cada requerimento debe estar agrupado segun una cierta categoria, que pueden ser los autores o los modulos del sistema a los que pertenencen.
Va desde uno solo a muchos.

#### Puntos fundamentales:
Se detallan en forma de items los puntos fundamentales a cubrir.
- Cubrir los procesos clave del sistema.
- Estar redactado con claridad, usando verbos activos.
- Estar agrupado por actor o módulo.
- Reflejar necesidades reales y específicas.
- Ser una base sólida para el modelado posterior (casos de uso, historias de usuario, etc


### No funcionales:
Se dividen en diferentes categorias, pero el concepto fundamental son la descripcion de como eso se implementara en el mundo real.
##### Categorias principales:
- **Producto:** Se asocia al funcionamiento del producto.
	A su vez, esta categoria tiene sub categorias relacionadas:
	- **Usabilidad:** Consiste en sintesis en todas aquellas cosas que afectan directamente la experiencia del usuario en tiempo real.
		Consiste en especificar diferentes cuestiones relacionadas a: El tiempo, conformidad, documentacion.
	- **Performance:** Indica como rinde el sistema bajo diversas pruebas de uso.
		Ademas del concepto, existen subcategorias de la performance.
		- **Concurrencia:** Se prueban diferentes procesos en un mismo intervalo de tiempo todos juntos.
		- **Tiempo de respuesta:** Se mide las operaciones realizadas en un rango de tiempo determinados, y se obtiene la medida operaciones/tiempo: Transacciones por segundo T/S. Tambien se determinan promedios y demas. Se encarga de estadisticas con respecto al tiempo relacionado a las funcionalidades del sistema.
			- Se identifican 2 sub estadisticas: Cantidad, y rendimiento.
		- **Utilizacion de los recursos:** La eficiencia para utilizar los recursos del sistema, como el disco: Espacio utilizado en disco. Se refiere a la eficiencia en estos dispositivos.
	- **Confiabilidad:** Abarca diferentes puntos, y se relaciona con la seguridad que le da el software al cliente en algun aspecto, como:
		- **Disponibilidad:** En un porcentaje de tiempo, cuanto se encuentra disponible el software.
		- **Tiempo minimo entre fallas:** Cual es la cantidad minima posible de tiempo transcurrido entre fallas.
		- **Tiempo** **reparacion minima:** Cual es el tiempo minimo posible para que se repare ante cierto incidente.
		- **Errores:** Categorizar a los errores encontrados o posibles segun una categoria con descripcion especifica.
		- **Certeza:** Se refiere a la precision especifica y la certeza segun un estandar que es requerida para la salida del sistema.
	- **Portabilidad:** Se refiere a la capacidad del sistema (producto) para adaptarse a diferentes tipos de tegnologias actuales o futuras segun convenga.
	- **Seguridad:** Se divide en 2 sub categorias.
		- **Logica:** Se refiere a requerimentos referidos a la seguridad de acceso al software por medios logicos (digitales), y la proteccion de estos datos sensibles.
		- **Fisica:** Se refiere a la capacidad de proteger los dispositivos fisicos que mantienen al sistema, con medidas de control fisicas para evitar la falsificacion de los datos, interrupciones del servicio, integridad, etc...
	- **Interfaz:** Se divide en 4 subcategorias.
		- **Usuario:** Consideraciones generales que el cliente requiere para su aplicacion de forma visual.
		- **Hardware:** La interfaz de hardware (como este se comporta y comunica) debe poder ser soportada por el software a construir.
		- **Software:** Permiten que diferentes componentes se comuniquen entre si, esencial para el producto a desarrollar y donde su interaccion con el producto es esencial.
		- **Comunicaciones:** Se refiere a dispositivos externos donde el software a desarrollar debe comunicarse. Como puede ser la red de internet, un servidor, o dispositivo remoto.
- **Organizacionales:** Restricciones de la organizacion las cuales se utilizan para generar el producto adaptado a ella.
	- Existen 2 subcategorias, que a su vez tienen subcategorias, son: Restricciones de negocio y tecnicas.
	- **Restricciones de negocio:** Todo trata sobre la organizacion y sus restricciones burocraticas.
		- **Entrega:** Si la organizacion plantea plazos de entrega especificos, con fecha, hora, etc...
		- **Eticos:** Requerimentos que deben considerar algun valor moral o pautas de conducta.
		- **Legales:** Requerimentos legales que protegen el derecho, seguridad y confidenciabilidad del producto a desarrollar con su documentacion. Se identifica segun la legislacion que aplique.
		- **Estandares:** Si se especifican estandares minimos que el desarrollo o aplicacion deben cumplir.
	- **Restricciones tecnicas:** Se divide en 2 subcategorias
		- **Implementacion:** Cualquier consideracion que impacte de forma directa en el desarrollo del producto, como puede ser la preferencia por algun software de desarrollo o herramienta especifica.
		- **Interoperabilidad:** Necesidad en forma de requisitos donde el producto de software a desarrollar se debe poder comunicar con otros productos de software del exterior. Para determinado proposito, normalmente intercambiar informacion.
- **Externos:** La relacion entre entidades externas al sistema y el sistema.


## Especificación de Requerimientos
Consiste en el metodo para poder especificar estos requerimentos fundamentales para el sistema de forma adecuada.

