Debo plantear la metodologia para llevar a cabo la practica, consiste en 3 pasos: Mapa de procesos, plantilla, bpmn, derivacion requisitos.
Tambien debo tener en cuenta las diferentes condiciones que me impone la materia para definir cada uno de estos puntos.
Y tambien estudiar la terminologia del bpmn, debido a que es mas compleja.

Tengo 3 dias, asi que me tengo que poner desde ya a hacer las cosas de forma organizada y eficiente.
## Metodologia:
- Revisar notas, casos de estudio y teoria para determinar las restricciones al momento de hacer cada una de las etapas.
	- Dividir por estamas, primero condiciones del mapa, de la plantilla, luego del bpmn, luego de la derivacion a requisitos.
- Comenzar a practicar, una vez obtenido las condiciones, con casos de estudio ya resueltos para corregirnos luego.
	- Inicialmente buscar casos de estudio ya corregidos, intentar hacerlos por mi cuenta, ver en que me equivoque y anotarlo para no volver a repetir eso.
- Una vez practicado con los casos resueltos, practicar con preparciales o con casos pidiendo correcciones a la IA. Y comparando con los otros.
Los primeros pueden ser parte hechos en pc, sobretodo el bpmn para agilizar, pero del 3ro para delante, todo debe ser papel, para poder identificar estrategias.
HOJA A3
- Una vez estudiado y practicado, realizar parciales con tiempo para prepararse para el verdadero parcial.

## Estudio y recopilacion de errores/restricciones:
### Mapa de procesos:
Es una estructura que permite representar los diferentes tipos de procesos de una organizacion, organizarlos jerarquicamente, y enmarcar la fuerza impulsora y el producto obtenido.
**Tipos de procesos:**
- **Estrategico:** Son procesos definidores, buscan potenciar la organizacion analizandola a futuro, Toman desiciones que afectan la estructura de la organizacion.
	- ¿Que se necesita para que funcionen los proceos clave y apoyo?
- **Central:** El proceso central de la organizacion, el principal, le aporta valor al cliente. Son los procesos que materializan el producto o servicio.
	- ¿Cual es la razon de ser de la empresa?
- **Soporte:** Son procesos de rutina, que sirven para sustentar a la organizacion en su actividades. Brindan apoyo a los demas procesos.
	- ¿Que hace la empresa para cumplir sus objetivos?

#### Lista de condicionales:
**Estructura:**
- Un proceso puede abarcar varias areas (son transversales.)
- Comienza con la persona/empresa o entidad interesada.
- La salida del proceso central es la satisfaccion de las partes interesadas desde un principio, si el proceso central (core) no le aporta un valor real, entonces no es un proceso central.
- Insumos abarca la materia prima de la empresa.
- Pueden haber multiples procesos centrales.
- Los procesos pueden abarcar varias areas.
- Se define el objetivo de cada proceso.
- Los interesados no se les pone una palabra generica tipo cliente, se le pone una palabra adaptada al contexto.
	- Cliente -> Inversor.

**Practica:**
- Si la actividad de "venta" abarca multiples actividades, entonces es llamda "comercializacion" (toma de pedido,producción,cobro,entrega).
- Los alquileres no son venta, el producto se "presta" por un determinado periodo, luego se devuelve, **es necesario modelizar la devolucion.**
- Los estrategicos normalmente definen.
- **Proceso central:** puede dividirse en 2 procesos si es muy grande de modelar, mientras ambos les den valor al cliente.
	- Uno se para en lugar del cliente para encontrar el proceso central.
- Si el enunciado nombra un proceso, eso debe estar si o si.
- EL PROCESO DEBE APORTAR VALOR AL CLIENTE.
	- Inscripciones NO APORTA VALOR, solo es parte del proceso que aporta valor.
- 

### Plantilla:
¿Que es? ¿Como funciona y para que sirve?
Es un recuadro que sirve para especificar las diferentes partes de un proceso especifico.
Aqui se suelen tomar a los procesos centrales para expandirlos.
- La plantilla tiene correlacion con le mapa de procesos y sirve de molde para el BPMN.
#### Lista de condicionales:
**Estructura:**
- Se modela unicamente el proceso/s centrales.
- **Reglas de negocio:** Deben tener el orden: Condicion - Accion.
	- Definen a la empresa.
- **Objetivo:** Solo debe estar relacionado con el proceso, es el principal.
- **Proveedores:** Son los que aportan al proceso central.
	- Tambien se detectan sus insumos, osea QUE aportan.
- **Recursos:** Solo se identifican recursos humanos (personas/responsables), no tecnologicos.
- **Formularios/registrar/datos:** Es todo lo que consista en adquirir informacion. Se debe detectar la informacion, no perder tanto tiempo en otras cosas.
	- Formularios: Salidas o entradas al sistema en una sola instancia. Es un plantilla preparada. (Ej: Listado de participantes). Obtencion de datos estandarizada.
		- No sirve para la toma de desiciones debido a su baja cantidad de datos. Comprobante vs Listado de comprobantes con estadisticas.
	- Registros: Registros de muchas instancias de informacion. Datos que se especifican de forma generica: "Datos del cliente"
	- Informacion: Nace de los registros. Es algo efimero, transaccional, que se usa en el proceso. Deben servir para tomar desiciones. Es un conjunto de datos, se escribe en plural.
- **Restricciones:** Solo de entes externos a la organizacion.
- 

**Practica:**
- **Objetivo:** Evitar gestionar/administrar (Viene del SI), evitar ingresos/ganancias (Viene de la orgaizaicon).
- **Proveedores:** Unicamente lo que aportan, no significa que todos los procesos aporten si o si, pueden haber procesos que aporten.
	- Es valido mientras su insumo se consuma en el proceso realizado.
	- No necesariamente debe ser un proceso dentro de la organizacion.
- Si no especifica con que se cobra, entonces definimos efectivo.
- Se debe limitar el analisis al cliente verdadero, descartar exepciones.
- Si no tiene un cierto item como: restricciones, que puede no tener, entonces se escribe "no aplica".
	- Si el enunciado no lo especifica.
- **El objetivo:**
	- Comienza con la palabra en infinitivo.
	- Describe el proceso y lo que abarca.
- **El producto** siempre es positivo, nunca es negativo.
	- DEPENDE DE LA SALIDA DEL MAPA DE PROCESOS, DEBE HABER RELACION.
### BPMN:
¿Que es? ¿Como funciona y para que sirve?
Es una notacion grafica que describe los pasas de los procesos de negocio.
Se realiza el modelaje del proceso con mayor informacion. Puede NO ser central.
- El BPMN tiene correlacion con la plantilla, y sirve de molde para los requisitos.
#### Lista de condicionales:
**Estructura:**
- El producto de la plantilla es el evento final del bpmn.
- Si el flujo se detiene por una actividad, se le añade un evento de espera.
	- Debe ser algo muy especifico, si no se aclara, se considera continua.
- Conviene hacer actividades especificas para cada situacion, en vez de realizar un loop sobre las mismas actividades.
- Se sigue el flujo de la plantilla.
- Se modelan los procesos con mayor informacion.
- Se modela una unica instancia del proceso, que servira para todas las demas veces que se use.
- El hoja se puede crear un glosario con las diferentes especificaciones de tipos de actividades, eso sirve para poder poner "s" = script, en vez de dibujar el simbolo.
- No vamos a tener que graficar los subprocesos.
	- Si el proceso a modelar tiene subprocesos para funcionar, entonces se pueden dejar como una caja negra.

**Practica:**
- Pueden existir multiples eventos de cancelacion, pero uno solo de finalizacion.
- El bpmn debe tener correlacion con la plantilla, se corrige a partir de ahí.
- Las tareas se escriben en infinitivo.
- Las bases de datos se escriben en singular.
- Se pueden modelar tanto el proceso central como otros, dependiendo cual tenga mas informacion.
- DERIVACION de la plantilla:
	- Formularios: artefactos.
	- Registros: Almacenamientos de escritura.
	- Informacion: Almacenamientos de lectura.
- Los recursos humanos se derivan como lanes.
- Las reglas de negocio estan correlacionadas con las condiciones en el bpmn (divisiones de flujo).
- Las compuerta paralela sirve para continuar el proceso en 2 flujos simultaneos, y se puede volver a unir con otra compuerta paralela.
	- Tambien sirve para esperar que ambos procesos terminen.
### Requisitios:
¿Que es? ¿Como funciona y para que sirve?

#### Lista de condicionales:
**Estructura:**
- Se deriva del bpmn.
- Comienza con una actividad automatica del bpmn (tarea de usuario).
- Diseñas el software que apoyara al proceso.
- Se comienza a pensar en datos con respecto a la Base de datos.
- Se deriva con una terminologia de alcances (Consultar, registrar, emitir).
**Practica:**
- Se utilizan alcances, consultar, etc...
- Todas las tasks automaticas de usuario / script son alcances (se derivan del bpmn).
	- Si es manual la task, entonces NO se deriva.
- Una vez realizado los alcances se crean los emitir.
	- Estos dependen de los datos que ya tenga disponible de los alcances anteriores.
- Si la tarea es tipos script, deriva directamente en software.
- Si es transaccion, entra como valido.
- Los datos dispuestos en el bpmn, se deben encontrar en el SI, debe haber trazabilidad de datos entre ambos.

### ITEMS CLASE CONSULTA:
- Identificar proceso: ¿Cual es el proceso y cuanto abarca.?
- Regla de necio imperativa: Condicion - Accion.
- BPMN: NO SE DEBE ESCRIBIR SOBRE LA COMPUERTA, SINO QUE SE ESPECIFICA EN LA ACTIVIDAD ANTERIOR.
	- Si el tiempo esta especificado y alguiene externo que rompe ese tiempo, entonces va un evento de espera: Ej: 15 dias hasta que el cliente se dealta.
	- El temporal es si sabes el tiempo exacto que va a suceder.
	- El evento intermedio si depende de una persona.
	- LAS ESPERAS NO SE MARCAN COMO TAREAS.
	- No se utilizan tareas de relgas de negocio especificamente.
	- SE DEBE PONER SOBRE LA FLECHA DE LA COMPUERTA EXCLUSIVA LA DESCRIPCION DE PORQUE SE TOMO ESE CAMINO. (ROTULADO, CADA CAMINO DEBE ESTAR DESCRITO PARA QUE ES).
	- UNA TAREA PUEDE TENER UN ARTEFACTO Y UN ALMACENAMIENTO A LA VEZ.
	- CADA DOCUMENTO APARECE UNA SOLA VEZ ENE L BPMN DE LA TAREA CORRESPONDIENTE.
	- EL CLIENTE NO ES UN CARRIL VALIDO. FIJATE EN LA ORGANIZACION.
	- REGISTRAR UN CIERTA INFORMACION EN UN ESTADO NO ES LO MISMO QUE REGISTRAR UNA NUEVA INFORMACION; REGISTRAR LA ENTREGA DE UN PEDIDO NO ES LO MISMO QUE REGISTRAR UN NUEVO PEDIDO.
	- EVITAR LA PALABRA REGISTRAR EN EL BPMN.
	- Las tareas fisicas se especifican en el bpmn, y aunque sea manual, se registra la informacion que le este dando, ej dar documento, el documento se registro.
	
	**ACLARACIONES PARA EL PARCIAL:**
	SE TIENEN 2 HORAS PARA REALIZAR EL PARCIAL.
	La parte teorica solo si desaprobaste el teorico 1 y 2, o menos de 3 en el 3.
- Preguntas:
	- ¿Cuando aplica arca en las restricciones? ¿Las restricciones se grafican en el bpmn?
		- Las restricciones especiales se aclaran en el caso de estudio, y se dan por implicitas al momento de realizar la actividad en el bpmn. No hace falta aclararlas como tal.

## Analisis de la practica con casos de estudio:
Aca se analizaran los errores o ambiguedades sobre las diferentes resoluciones de los casos de estudio.
### Metodologia:
- Avanzar hasta el caso de estudio nro 4.
	- Si se llega antes de la hora de comer, seguir con los demas hasta la hora de comer.
	- Si no se llega a realizar antes de la hora de comer, se tiene tiempo maximo hasta las 3pm.
- Realizar preparciales hasta terminarlos y verificarlos, contando el tiempo (temporizador).
- Aprender todos los simbolitos del bpmn, los que podemos requerir, no avanzar con los que no vimos en la catedra.
### Comidas Rápidas:
Resolucion carpeta.
Correcciones:
**Mapa de procesos:**
- Si hay 2 procesos que definen el mismo objeto van juntos.
- Verificar verdadero valor que aporta, no solo el titulo del caso de estudio.
**Plantilla:**
- No olvidarse el cliente (persona/entidad interesada en).
- En los proveedores tambien entran los procesos definidores de, todo proceso que tenga relacion directa con el proceso central y lo que usa.
	- Ya sea precios, tipos, recursos humanos, o mismos insumos materiales.
- Registros:  Todo lo que tenga que ver on transacciones entra bien especificado en datos.
- Reglas de negocio: Solo se toma el camino bueno, si no hay una condicion bien clara que divida el flujo con informacion incluida, no va. En el bpmn se transforma en division de flujo, si en el bpmn no se puede dividir el flujo, entonces no es una regla de negocio.
![[comidarapida.png]]

### Caso de estudio 2:
**CORREGUIR CASO DE ESTUDIO.**

