Aqui se va a extender toda la teoria de MEMORIA, para su posterior estudio para el parcial cuestionario.
Se enlistan los temas de esta unidad:
- Introducción y sistemas sin abstracción de memoria
- Abstracción de memoria y espacio de direcciones
- Administración de memoria libre e intercambio (Swapping)
- Memoria virtual y paginación
- Algoritmos de reemplazo de páginas
- Cuestiones de diseño y segmentación

## Apunte:
**Introduccion/inicio:** 
Se plantea la situacion donde los programas crecen mas que la memoria disponible, encontrando e implementando funciones nuevas que devoran la ram disponible.
Aunque se busque la ram perfecta (Velocidad, magnitud, barata y perpetua), eso no existe en la vida real, llevando a utilizar metodos de division de memoria.
- Cache.
- Ram.
- Discos (Almacenamiento secundario).
El trabajo del planificador es hacer que esta memoria que ve el proceso cumpla con estas condiciones manejando estas 3 diferentes memorias.

**Monoprogramacion:**
Al programa correr de forma unica, acaparando la mayoria de recursos, no era necesario ni existia la aftraccion a memoria. Se usaba un sistema MS-DOS, donde la direccion fisica era la que el programa veia y utilizaba. Se dividia de la siguiente manera:
- Modelo (a): El SO se aloja en las direcciones bajas y el programa en las altas.
- Modelo (b): SO solo usaba la memoria de solo lectura.
- Modelo (c): Los device (controladores de dispositivos) se escriben en la ROM, y el resto del SO junto a los datos del programa se almacenan en la ram juntos.
Bajo esta logica y induce vulnerabilidades criticas de sobreescritura y no permite la multiprogramacion.
**INTENTO DE MULTIPROGRAMACION:** Resubicacion estatica
- Se intento abordar la multiprogramacion, osea programas funcionando en simultaneo en la memoria ram, y sin un chip potente de MMU, en ese momento se planteo una resolucion mediante la separacion en secciones:
	- Al tener programas en memoria, cada uno ocupaba una cierta parte de la ram, llevando a que sus diferentes direcciones de referencia se sobreescribieran sobre la marcha.
	- Esto tiene 2 claros problemas:
		- Tardar al cargar el programa: Llevando a tardar mucho en sumas arimeticas antes de siquiera iniciar el programa.
		- Esto provoca que la ram siga estando vulnerable ante diferentes fallas en la escritura y redireccion de programas.

### Intercambio:
La limitacion de la reubicacion estatica es que si los programas eran mayores a la ram disponibles, entonces no se podia ejecutar el siguiente programa (otro mas), estaba limitado por la memoria disponible.

Por esa razon llego el metodo de "intercambio", este metodo lo que hacia es escanear la memoria, en busca de procesos cancelados o en pausa, a estos procesos se los sacaba de la ram, debido a que estaban esperando ocupando espacio al vicio.
	Se copiaba todo en el disco SWAP.
Este metodo producia fragmentacion en la ram, provocada porque los procesos en cuestion ocupaban mayor cantidad de memoria a medida que se ejecutaban, van haciendo calculos, llamadas, variables, etc...
	Esto produce que se le deba dejar una cierta cantidad de memoria previa disponible, y al tener que pasarlo a disco y volverlo a la ram, pueda provoca que el programa sea mas grande que lo asignado para el en la ram, provocando que se deban buscar nuevos espacios, y otros queden vacios (sin uso), pero reservados.

### Memoria virtual
Nacio este concepto para solucionar las diferentes problematicas que generaba el swap.
La filosofia o concepto consiste en que un programa no debe estar cargado completo en la ram, solo lo necesario (no hace falta que todo este cargado simultaneamente en la ram).
El SO y una unidad MMU, permiten realizar el metodo: Cada proceso se le dice que tiene su propia memoria, que es continua y gigante. Esta ilucion representa el espacio de direcciones virtuales. Yendo desde el 0 hasta el maximo teorico de la arquitectura.
**Funcionamiento:**
- El SO divide al programa en diferentes trozos llamados **paginas**, de un tamaño igual cada una.
- La ram fisica se divide en pedazos iguales, llamados **marcos de pagina**.
- Al cargar un programa de gran tamaño para la memoria, el SO carga solo las paginas necesarias para las intrucciones que ejecutara en ese momento.
	- El resto de paginas queda en el disco sin siquiera tocar la ram.
- Si el programa quiere usar una pagina que esta en disco, lanza un **error de pagina**, que despierta al kernel para que mueva esa pagina a la ram.

#### Metodos para la administracion de memoria libre:
**MAPA DE BITS:** Divide la memoria en unidades de asignacion fijas. Esto permite identificar bloques que estan ocupados por procesos (1), o estan libres (0), se detallan en una matriz donde cada bloque tiene subloques. Se le asigna un 1 o cero si el bloque esta ocupado por un proceso o vacio.
Cada bloque abarca multiples direcciones de memoria.
- Siempre ocupa el mismo espacio en memoria. Independientemente de los procesos, se fijan estos bloques antes.
- Al ser un conjunto de vectores, resulta mas simple al momento de evaluar operaciones logicas mediante hardware.
- Los huecos pueden tardar mucho en encontrarse (Ej: 4 huecos contiguos)
- La unidad de asginacion puede provocar que se desperdice memoria: Fijando un tamaño proporcional al tamaño de la memoria real, provocando que un proceso robe memoria inutilmente al ser mucho mas pequeño que el bloque entregado: bloque minimo: 32k, lo que ocupa el proceso: 4k.

**Listas enlazadas:** Propone un enfoque dinamico, donde el espacio disponible esta representado por nodos conectados entre si. Se representa como una lista encadenada de nodos, un nodo contiene:
- **Bandera: P** (Proceso), H (Hueco).
- **Direccion de inicio** (de la RAM).
- **Longitud** (cuantas unidades mide ese bloque).
**Casos de adaptacion:**
	Al morir un nodo, ese nodo queda libre (H), sin embargo el SO identifica las diferentes situaciones que pueden suceder para adaptar el nodo a su situacion y ahorrar espacio.
	Si un nodo muere pueden pasar estos 4 casos:
	* **Caso (a) - Entre dos procesos:** X estaba entre A y B. Al morir, el nodo de X simplemente muta su bandera de "P" a "H". 
	* **Caso (b) - Vecino derecho es hueco:** X tenía un hueco a la derecha. Al liberarse X, el kernel los fusiona en un único nodo "H" más largo. 
	* **Caso (c) - Vecino izquierdo es hueco:** X tenía un hueco a la izquierda. Se fusionan hacia atrás en un solo nodo "H".
	* **Caso (d) - Rodeado de vacíos:** X estaba entre dos huecos. Al morir X, los tres bloques se fusionan eliminando dos nodos de la lista y consolidando un único hueco gigante en la RAM.
	En sintesis el SO intenta de todas las formas posibles que los nodos queden fragmentados en pequeños lugares, busca organizar los nodos para maximizar la longitud del nodo Hueco.
El beneficio de este metodo es la eficiencia algoritmica, teniendo nodos declarados por su estado y longitud, aplicando algoritmos rapidos o perfectos (el primer Hueco disponible o el Hueco ideal).
Junto a la facilidad en la unificacion de nodos, al solo cambiar el puntero de la lista.
Sin embargo hay casos no deseables:
	Fragmentacion: Si hay multiples procesos pequeños ocupando un unico nodo, se crean microhuecos que no sirven para los demas procesos, y el numero de nodos con sus conexiones aumenta en gran medida, pudiendo consumir gran parte de la memoria ram.
	Acceso indexado lento: El SO debe leer todos los nodos anteriores hasta llegar al nodo que desea modificar, por lo que se vuelve lento para tareas rutinarias, ocupando tiempo de CPU que no se ve impactado en tareas reales.
![[Pasted image 20260530112443.png]]
![[Pasted image 20260530112419.png]]
**Algoritmos:**
- **Primer Ajuste (_First Fit_):** El más rápido. Escanea desde el inicio y asigna el primer hueco donde entre el proceso.
    
- **Siguiente Ajuste (_Next Fit_):** Variante del anterior. Arranca a buscar desde donde se quedó la última vez para distribuir mejor la ocupación.
    
- **Mejor Ajuste (_Best Fit_):** El más "tacaño". Recorre toda la lista buscando el hueco que calce más justo para no desperdiciar nada, aunque genera micro-huecos inútiles.
    
- **Peor Ajuste (_Worst Fit_):** El más "derrochador". Elige a propósito el hueco más grande para que el sobrante sea utilizable por otro proceso.
    
- **Alternativa de Dos Listas:** Separar los nodos de procesos de los nodos de huecos para acelerar la búsqueda, pagando el costo de una desasignación más compleja.

### Memeoria virtual metodos:
Para poder resolver el problema que los programas no cabieran en la memoria ram debido a su baja capacidad para lo que el programa necesitaba.
Se utilizaron diferentes metodos a lo largo de la historia que abordaron el problema de diferentes formas.
**Overlays (sobrepuestos) antes de la memoria virtual:** 
	Fue una solucion primitiva que dividia el programa en partes decididas por el programador (pedazos logicos: overlays) al momento de compilacion.
	La mecanica era simple: Se cargaba el gestor de overlays abajo de la ram, quedando fija ahí. El resto de la ram quedaba como "memoria comun de intercambio"
		Cuando el programa arrancaba, se cargaba su primer overlay (overlay 1) en la zona comun de la RAM. Cuando el programa debia ejecutar otra funcion que no estaba en ese overlay, se cargaba el segundo overlay pisando al primero por completo.
	Fue un dolor de cabeza para los desarrolladores, debido a que debian calcular cada byte milimetricamente para que cabiera en el espacio disponible de la ram, y si el programa ejecutaba o llamaba alguna funcion que no se encontraba en el overlay actual, el programa tiraba error critico.
**Paginacion y memoria virtual:** 
	La memoria virtual llego con una premisa clara para resolver las dificultades de los overlays, el hardware y el SO se encargaban de administrar la division y intercambio.
	La division y propuesta se realizo de esta forma:
		El programa se dividia en bloques pequeños de igual tamaño llamados **paginas** (de aprox. 4k cada uno).
		La ram fisica tambien se corta en trozos del mismo tamaño, llamados **marcos de pagina.**
		Solo se suben a la RAM fisica las paginas que el programa esta utilizando activamente en ese preciso instante, el resto de paginas se encuentran en el disco.
			Si el programa ejecuta una linea de una pagina que no se encuentra en la ram en ese momento, la busca en el disco y la trae a la ram para que el programa la pueda ejecutar, en ese proceso de busqueda, el proceso queda en bloqueado.
	**Conceptos:**
		**Aftraccion del espacio logico:** El SO aftrae las direcciones fisicas (reales) de la memoria y les brinda una unica memoria virtual a cada programa, su direccion virtual es manipulada por la MMU (Unidad de administracion de memoria), que sirve para traducir esa direccion virtual en una direccion fisica valida.
		La MMU se encarga de la mudanza de paginas, sin que el programa se de cuenta, pudiendo tener pequeñas partes del programa dispersadas por toda la memoria.
		Al conjunto de memoria que se encuentra realmente en la ram se la denomina conjunto residente (residente set). Este conjunto debe estar bien calibrado para no estar constantemente leyendo el disco en busca de paginas faltantes.
		**Fallo de pagina:** Consiste en la situacion donde el programa le pide al procesador ejecutar una parte que no se encuentra cargada en memoria principal (El bit de presencia es "0", la direccion que fue a buscar el procesador no esta cargada).
			En esta situacion, la MMU genera una interrupcion al procesador (INterrupcion de hardware: Page fault) antes de que ejecute esa instruccion.
			Luego entra el SO en accion bloqueando el proceso y ejecuta una peticion de E/S para ir a buscar esta pagina faltante.
			Cuando la termina de buscar y cargar en la ram, se envia una interrupcion de E/S, el kernel despierta, identifica que la pagina esta disponible en la ram y cambia su bit de presencia a "1". Habilitando al proceso a continuar con la instruccion.
		**- Puntos a evaluar:**
			Tamaño de las paginas: Uno pequeño reduce la fragmentacion, pero aumenta el tamaño de las tablas de paginas, y saturan el TLB.
				Las paginas grandes son muy optimas ante llamadas al disco, manteniendo un tamaño reducido de la tabla de paginas, pero desperdician mucho espacio si los procesos solo ocupan una porcion de esa pagina total.
	**Ventajas:**
		Se pueden mantener mas procesos en la memoria principal.
		Se cargan solo los fragmentos necesarios en ese momento.
		El tamaño del programa no es determinante para poder cargarse en la ram. (Se divide en partes iguales y pequeñas).
	**Hiperpaginacion:**
		Situacion donde el SO remplaza una pagina que se necesitaba usar.
		El SO pasa mas tiempo intercambiando paginas que ejecutando codigo real. (Congelamiento).
	**Paginacion:**
		Es la tecnica utilizada para la gestion de memoria virtual, osea lo explicado anteriormente:
			Se divide el espacio logico de un programa en "paginas" (bloques) y la memoria principal tambien se divide en marcos (bloques) de igual tamaño.
			Permite darle la ilusion al programa de que tiene mucha mas memoria disponible de la real, y esta memoria virtual que utiliza el programa puede ser significativamente mas grande que la memoria real. Ese diferencia se puede amplear segundo la arquitectura del procesador, Ej: 32 bits = 2³² bytes.
			El problema es que si es demasiado grande, puede esa tabla para la paginacion, ser mas grande que la misma ram real.
			Osea, si las direcciones virtuales (Memoria virtual) son grandes, entonces la tabla de paginas tambien sera grande.
	**Mecanica fisica:**
		El procedimiento para convertir una direccion fisica en una direccion real de la ram es el siguiente:
		- Se recibe el valor de la pagina a buscar 8196
		- Se obtienen los primeros 4 bits del numero.
			- El numero formado se utiliza como indice de un array de la tabla de paginas.
			- Dentro de la fila en cuestion se encuentra el numero del marco fisico (el bloque en la ram).
			- Y junto a eso el bit de presencia (1 presente, 2 ausente: buscar en memoria).
		- Esos 3 bits del marco obtenido, se utilizan para crear una nueva direccion con el formato: 3 bits del marco + resto de la direccion anterior (direccion inicial sin los 4 bits mas significativos). 8196 -> 24580
		![[Pasted image 20260530161707.png|354]]
	**Tabla de paginas:**
		Aqui se ubican la organizacion de las diferentes paginas tanto de la ram como del disco. Esta tabla puede ser plana (ocupa espacio linealmente, en casos de programas grandes es inviable), o tambien puede tener una estructura multinivel (como por ejemplo para arquitecturas de 64 bits).
		Esta memoria virtual se almacena en la RAM, permitiendo un rapido acceso a la informacion.
		Cada columna de esta tabla, tiene un cierto bit que indica cierta cosa: La MMU se encarga de modificiarle los diferentes "estados".
		- **Cache desactivada:** Se le pone 1 para evitar que la CPU guarde en la memoria cache interna una copia de la pagina, obligandola a leer del dato en la ram.
		- **Referencia:** Cada vez que me lee o modifica la pagina, la MMU le pone un "1"
		- **Modificado:** Se pone en 1 solo cuando un proceso escribe en la pagina.
		- **Proteccion:** 3 bits que determinan los permisos de acceso a la pagina.
		- **Presente/Ausente:** Se pone en "1" si esta cargada fisicamente en la RAM.
		- **Nro marco de pagina:** Guarda la direccion base real (fisica). (El resultado del calculo de la MMU).
### Algoritmos de reemplazo de páginas:
Es necesario para cuando la memoria ram tiene mas procesos de lo normal y es necesario sacar una pagina de la memoria ram para añadir otra.
El algoritmo "ideal" debe: Eliminar la pagina que no se referencio hace mucho tiempo y no va a volver a usarse en mucho tiempo. (Paguina que tomara mas tiempo ser requerida)
Ese algoritmo ideal es inalcanzable ya que no se sabe cuando esa pagina se debe extraer.
Existen 5 algoritmos principales que intentan abordar este problema:
- **NRU (No usada recientemente):** Clasifica en 4 categorias a las paginas segun el estado de los bits.
	- Busca ser la opcion mas barata y optima mediante software.
	- La categoria mas baja es la que se remplaza, se guia por la actividad de la pagina, representada por 2 bits R(Referenciada), e M(Escrita (sucia o limpia)):
		- Clase a (Ideal): (0,0) 
		- Clase b: (0,1)
		- Clase c: (1,0)
		- Clase d: (1,1)
	- Una vez identificada a las paginas con la clase mas baja, se elige aleatoriamente y elimina. Es eficiente, facil de implementar.
- **FIFO:** 
	- Utiliza el metodo FIFO para poder realizar espacio para nuevas paginas.
	- Se organizan a todas las paginas en una lista organizadas por el algoritmo FIFO (First in, First Out).
	- Es lento de procesar comparado a los demas (mover los elementos dentro de la fila).
	- Cuando ocurre un fallo de pagina y la debe ingresar a la cola, se descarta la pagina mas vieja (la primera), y remplaza por la nueva.
	- Es un algoritmo conflictivo ya que elimina de forma "ciega": Si la primera pagina es una variable utilizada constantemente, el echarla provocara que se vuelva a producir un fallo de pagina, ademas del fallo (_Anomalía de Belady_) donde el algoritmo FIFO provoca mas fallos de pagina al agregarle mas RAM (mas marcos).
- **Reloj:** Basa su concepto en la segunda oportunidad:
	- Visualiza a los marcos de pagina como elementos dentro de una lista circular.
	- Utiliza un puntero que va modificando su elemento como la aguja de un reloj.
	- Si se encuentra a un marco con la bandera R = 1, la cambia a cero y continua.
	- Al encontrar un elemento con R = 0, lo saca y remplaza por la pagina nueva.
	- Es rapido y facil de implementar.
- **LRU:** Least recently used.
	- Identifica la pagina que lleva mas tiempo sin usarse y la libera, remplazandola por la otra.
	- Para un correcto funcionamiento del LRU, se necesita hardware aparte que asigne un valor de 64 bits a cada pagina, siendo bastante caro.
	- En la practica, la LRU casi nunca se usa por los altos costos asociados.
- **Envejecimiento: Aging**
	- Es una simulacion por software del LRU.
	- Cada pagina tiene una variable entera interna del kernel.
	- Se va actualizando con cada pulso reloj.
		- En cada pulso al bit de control de cada pagina y lo desplaza un bit hacia la derecha.
		- Luego obtiene el bit de R (referencia) y lo incerta en la primera posicion (Mas significativa).
	- Este algoritmo verifica el valor de esta variable y la pagina con variable mas pequeña (se accedio muy pocas veces, muchos R = 0) se descarta.
		- Busca a la pagina con la variable de valor numerico mas bajo.

### Asignacion Local vs Global
Es la mirada que tiene el SO sobre la ram ocupada entre paginas y procesos. Sirve al momento de remplazar paginas.
**Local:** Ve unicamente a las paginas del mismo proceso. Busca mantener la misma cantidad de paginas por proceso. Remplaza tomando en cuenta a las paginas de ese proceso que genero el fallo de pagina.
**Global:** Ve todos los procesos por igual, y remplaza tomando en cuenta a todos.
**PROS Y CONTRAS:**
	**Global:** Permite maximizar el uso de ram activa AL MAXIMO, aprovechando memoria sin utilizar de procesos inactivos. Pero pudiendo provocar Hiperpaginacion por procesos malintencionados o mal programados que acaparten gran parte de la ram.
	Local: Permite aislar el espacio entre procesos, mejorando la resilencia total, evitando que un programa se expanda ocupando a otros en la memoria. Pero a costa de perder memoria con procesos que pueden estar inactivos, y tener procesos activos utilizando una cantidad de memoria infima (20 paginas inactivasvs 3 paginas intercambiandose constantemente).

### Sobrepaginacion (Thrashing):
Sucede cuando hay demaciados procesos en la memoria, provocando que su conjunto recidente sea menor al minimo necesario para trabajar, provocando que ni bien entren a CPU largen un fallo de pagina, perdiendo tiempo en buscar muchas paginas en vez de procesar algo real.
Si hay varios procesos en la RAM, permite que la CPU este constantemente laburando, pero si hay demaciados, termina ocurriendo un colapso.
**Intercambio:** Utilizando metricas de hardware, cuando el SO detecta que se esta produciendo una sobrepaginacion, automaticamente bloquea a un par de procesos y los saca de memoria mediante swapping, reduciendo la multiprogramacion.

### Extras:
**Paginas compartidas:** Utilizadas cuando se abren varias instancias del mismo programa.
**Bibliotecas compartidas (Shared Libraries):** Se ubican en un lugar de la ram especifico, donde todos los procesos que la requieran acceden a ella.
**Demonio de paginacion:** Busca liberar espacio en la ram para permitir que esta no colapse. Vive dormido pero se despierta periodicamente para revisar la ram. Si la cantidad de marcos libres cae debajo del umbral minimo, osea que no queda espacio disponible en la ram, el demonio se despierta y empieza a ejecutar algoritmos de remplazo de pagina.
	Corre en segundo plano como un proceso de maxima prioridad.
	Tambien mira paginas que tengan el "Dirty bit" en "1", osea que fueron escritas o modificadas, para guardarlas asincronicamente en el disco. Cambiando el valor del bit a cero.
**SEGMENTACION:**
	Consiste en dividir un programa en segmentos de diferente tamaño (no de forma condicional), permitiendo tener las partes individuales de cada programa, de un tamaño dinamico, NO fijo como las paginas.
	Un segmento es una parte estrategicamente seleccionada del programa, sus diferentes modulos: Variables globales, codigo principal, pila de funciones (Stack), etc...
	La tabla de segmentos administrada por la MMU debe actuar diferente: Debe registrar 2 datos en vez de uno (osea el identificador del marco de pagina):
		Base: La direccion fisica de la ram donde el proceso comienza.
		Limite: La cantidad de bytes que utiliza (Debe ser exacto).
	Ademas la direccion logica deja de ser un numero plano y pasa a ser un par: Numero del segmento, desplazamiento.
	Si el proceso intenta leer un byte que se sale de su segmento, entonces se lo bloquea automaticamente dando el error (**`Segmentation Fault`**).
	Este metodo permite asignar una memoria independiente a cada segmento, permitiendo un mejor aislamiento de cada parte del programa.
	Permite compartir modulos enteros entre otros programas, asignando el permiso correspondiente guiandose por la funcion a realizar. 