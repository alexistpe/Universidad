Aqui se va a extender toda la teoria de MEMORIA, para su posterior estudio para el parcial cuestionario.
Se enlistan los temas de esta unidad:
- Introducción y sistemas sin abstracción de memoria
- Abstracción de memoria y espacio de direcciones
- Administración de memoria libre e intercambio (Swapping)
- Memoria virtual y paginación
- Algoritmos de reemplazo de páginas
- Cuestiones de diseño y segmentación

### Metodologia:
La metodologia que utilizaremos para estudiar esta unidad es: Expandir todos los temas teoricos y realizar un resumen del practico, debido a que tuvimos 3 practicos principales.
- Expandir teoria.
- Revisar practicos realizados, y relacionar los temas.
- Realizar cuestionarios y preguntas practicas sobre lo visto en esta unidad.

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
			En esta situacion, la MMU genera una interrupcion al procesador (Interrupcion de hardware: Page fault) antes de que ejecute esa instruccion.
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
			- Y junto a eso el bit de presencia (1 presente, 0 ausente: buscar en memoria).
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
	**Local:** Permite aislar el espacio entre procesos, mejorando la resilencia total, evitando que un programa se expanda ocupando a otros en la memoria. Pero a costa de perder memoria con procesos que pueden estar inactivos, y tener procesos activos utilizando una cantidad de memoria infima (20 paginas inactivasvs 3 paginas intercambiandose constantemente).

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


# Administracion de Sistema de archivos
### PRIMERA PARTE: QUE ES UN SISTEMA DE ARCHIVOS
Se divide en 2 fases fundamentales: Como funcionan tecnicamente y como los utiliza el SO, inicialmente extenderemos la primera, luego la segunda.
Archivo como una unidad de aftraccion de la memoria, funciona como una aftraccion que utiliza el SO para guardar datos en la unidad de almacenamiento segundario. Quitando la logica tecnica de como funciona fisicamente el dispositivo. (Como se mueven los discos o como se exitan las celdas).
El archivo viene a solucionar el problema donde se necesita almacenar mucha memoria y que sea persistente (Sobrevivir al corte de energia).
	Muchos procesos a su vez deben ser capaz de acceder a esta informacion concurrentemente.
Los archivos son unidades logicas creadas por los procesos.
La parte del sistema operativo que trata archivos se le llama "sistema de archivos".

**VISTAS:**
- Usuario: Ve la interfaz grafica, carpetas, directorios, con su nomenclatura y atributos visualmente adaptado. Puede ver los permisos y realizar diferentes operaciones basicas.
- SO: Ve un conjunto de bytes seccionados por sectores fisicos y en conjunto de bloques. El SO utiliza mapa de bits y listas enlazadas para determinar los espacios ocupados y disponibles. 
	- Para determinar que bloque le pertenece a cada archivo, el SO utiliza i-nodos y FAT (tabla de asignacion de archivos). Permite mantener en orden la indexacion.
	- El SO se encarga de manejar la fragmentacion en la memoria, al borrar espacios determinados de un archivo, quedando "sueltos" en medio de los demas.

**Nomenclatura:** Es como se lo llaman a estos archivos, se divide en 3 fases historicas:
- **MS-DOS:** Se utilizaba la regla de 8.3, 8 caracteres para el nombre, un punto y 3 caracteres para la extension.
- **Unix/Linux:** Son Case-sensitive, distinguen entre mayusculas y minusculas, permitiendo tener archivos con el mismo nombre fonetico pero diferenciacion logica: Parcial.txt, PARCIAL.txt son archivos diferentes. Permiten nombres de hasta 255 caracteres.
- **Windows:** Case-sensitive pero no permite tener 2 archivos con el mismo nombre: "Hola.txt" y "HOLA.txt" se pisan entre si.
La extension es solo una convencion, realmente solo aporta una guia para el usuario y ciertos programas, a nivel de SO, la extension solo es parte del nombre. Lo importante es el codigo de dentro.

**Estructura:** Exitieron 3 formatos principales para organizar los archivos por dentro, estos son:
- **Secuencia de bytes (Moderno):** Consiste en una secuencia continua de bytes, donde cada programa se encarga de interpretarlo. Es la forma moderna en que se identifican los archivos y permite amplea flexibilidad.
- **Secuencia de registros:** Se divide un archivo en bloques de tamaño fijo llamado registros, donde se leia cada uno secuencialmente, era muy comun antes por las tarjetas perforadas.
- **Arbol de registros:** Consiste en un arbol de registros de tamaño variable, donde cada registro tiene una "clave", o posicion fija donde el SO busca de forma directa el registro necesario.
- ![[Pasted image 20260614161558.png|470]]
**TIPOS DE ARCHIVOS:** Existen 4 tipos de archivos principales, mediante el comando ls -l se pueden identificar.
- **Regulares (-):** Estos contienen datos de los usuarios. Pueden ser de texto ASCII, o ejecutables imagen, binario, etc...
- **Directorios (d):** Son archivos del sistema, contienen nombres y direcciones de otros archivos. Permiten dar estructura a las carpetas.
- **Archivos especiales de caracteres (c):** Manejan flujos de datos provenientes del hardware: Mouse, teclado, etc... (Byte a Byte)
- **Archivos especiales de bloque (b):** Permiten identificar componentes del hardware como archivos, que permiten acceder mediante diferentes operaciones. No ocupan espacio en el disco, son un "acceso" a los drivers del componente fisico.

**Acceso/atributos/operaciones:**
- **Acceso:** Como accedemos a los archivos
	- Secuencial: Leer los datos uno por uno.
	- Directo/aleatorio: Leer los datos de forma directa. Se mueve un puntero interno denominado "Seek".
- **Atributos:** Metadatos, son variables de control que utiliza el SO para identificar datos fundamentales del archivo, son todo lo **externo al archivo**.
	Consisten en diferentes datos externos al contenido del archivo:
	- Tamaño: Cantidad acual de bytes
	- NUMERO MAGICO: Permitia identificar que tipo de archivo es. No solo por la extension, es una serie de bytes fundamentales en ese tipo de archivo.
	- Fecha: Creacion utlimo acceso.
	- Permisos de proteccion: Quien puede y no puede acceder. Bits de lectura RWX.
	- Propietario: UID del usuario o GID del grupo.
	- Flags: Banderas del sistema: Oculto, solo lectura, comprimido, etc...
	- ![[Pasted image 20260614162217.png|369]]
- **Operaciones basicas (Syscalls file system):**
	- **Create/delete:** Crea un archivo vacio o borra uno.
	- **Open/Close:** Antes de usar un archivo, se debe cargar en el sistema, eso se refiere a buscarlo, cargar sus atributos, direcciones, devolviendo un descriptos de archivo (numero entero). CUnado finaliza, lo elimina, para liberar memoria.
	- **Read/write:** Obtiene los bytes de la posicion del puntero actual y los lleva hacia el area de trabajo del proceso, o va y graba los datos de la RAM en disco.
	- **Seek:** Mueve el puntero del lugar actual hacia el lugar indicado para obtener los datos correspondientes.
- **Directorios: Jerarquia, rutas y operaciones:** Para organizar miles de archivos diferentes, los SO utilizan directorios para encapsular la informacion.
	- **Jerarquia (Sistemas de archivos arbol):** Es como se organizan los archivos hoy en dia, se utiliza un formato de arbol, donde parte de un directorio raiz y se va extendiendo infinitamente en cada rama del arbol.
		- **Rutas (path):** Se utilizan para organizar un archivo dentro de un arbol.
			- **Ruta absoluta:** Incluye desde la raiz, pasando por todos los directorios hasta el destino. No importa donde estes parado.
				- /home/ale/files/uni/SO.txt
			- **Ruta relativa:** Utiliza la posicion actual para dirigirse mas profundo o mas arriba.
				- pwd. (ver ubicacion)
				- ./uni/SO.txt (actual)
				- ../godot/p1.gd (padre)
	- DIrectorios jerarquicos de un solo nivel: Todos los archivos se ven en el mismo nivel, no hay "subcarpetas". Es inviable a gran escala.
	**Operaciones:**
	- **mkdir / Rmdir:**  Crear o eliminar un directorio (carpetas), rmdir solo borra si esta vacia, evita un desastre.
	- **Opendir / Closedir / Readdir:** Permite abrir a una carpeta como si fuera un archivo de texto para ver que estructura de archivos tienen dentro.
	- **Link:** Crea un enlace a un archivo (acceso directo o ruta solida (softlink or hardlink)). Conecta el nombre a un nuevo nodo de archivo fisico en la ram/disco.
	- **Unlink:** SIrve para borrar la relacion creada entre un nombre y un nodo archivo. Cuando un archivo se queda sin enlaces (nadie lo puede llamar, porque nadie lo relaciona), el archivo es "borrado" por el SO al etiquetarlo como "disponible", no borra sus datos, solo lo pasa a la lista de espacio liberado.

### SEGUNDA PARTE: COMO EL SO ADMINISTRA LOS ARCHIVOS
Como el SO convierte la aftraccion de un archivo, a un sistema de bloques numericos organizados en diferentes partes del disco.
Se busca el equilibro entre hacer que el disco sea lo mas rapido posible y a la vez confiable.
#### Distribucion sistema de archivos:
Consiste en como el SO organiza un disco para agrupar las diferentes partes de los archivos (se expandira mas adelante como particiona el SO los archivos en pequeños bloques):
Las partes de este disco son:
- MBR: Donde el SO arranca, normalmente aqui se encuentra el GRUB. Primeros 512 bytes
- Partition table: Tabla de particiones, indica como se divide el disco en particiones, donde comeinza y termina cada una. Aqui se indica cual es la particion activa.
- Cada particion contiene segun el formateo que se le realice:
	- **Bloque de arranque (boot block):** Primeros bloques de cada particion, se dejan "libres" por convencion. Sirve por si es la particion activa donde se carga el SO.
	- **Superbloque (Superblock):** Es uno de los bloques mas importantes, este contiene todos los metadatos necesarios para identificar las caracteristicas del bloque, es lo primero que se sube a la RAM.
		- Metadatos globales del File system: Tamaño de bloques, cantidad de bloques, inodos disponibles, tipo del Sis. archivos y el numeor magico para determinar que no este corrupto
	- **Gestion de espacio libre (free space mgmt):** Aqui se guardan estructuras que permiten determinar el espacio disponible, como el mapa de bits.
	- **Inodos (I-nodes):** Un area del disco que esta reservada para un arreglo ginante de indexacion. Cada archivo tiene un Inodo asignado que guarda sus atributos y punteros que indican en que bloque del disco quedaron almacenadas sus datos reales.
		- Osea es una estructura que permite indexar archivos y determinar que parte le pertenecen a el.
	- **Directorio raiz (root dir):** Contiene la carpeta raiz (/) de la particion, permite crear el arbol jerarquico de las carpetas de esa particion.
	- **Archivos y directorios (files and directories):** El sector mas grande de toda la particion, aqui se graban todos los bytes de informacion correspondientes a los archivos.

#### Implementación del sistema de archivos:
Consiste en que metodos utiliza el SO para identificar las partes de los archivos, ya que estos se dividen en bloques al ser muy grandes.
Por esta razon de escases de espacio individual para cada archivo, el SO necesita un metodo de asignacion, para poder identificar y relacionar diferentes bloques sueltos por el disco a un mismo archivo.
**Metodos:**
- **Asignacion contigua:**
	- Plantea la solucion mas sencilla, que se mapee todo el archivo de corrido: Si el archivo que empieza en la dir 100, tiene 5 bloques, estos ocuparan respectivamente las direcciones: 100, 101, 102, 103, 104.
	- **Ventajas:** Facil implementacion y rastreo, solo se anotan donde el archivo comienza y cuantos bloques tiene. Ademas de una rapida velocidad, al buscar solo en un lugar todos los datos (cabezal del disco).
	- **Desventajas:** Fragmentacion alarmante al borrar ciertos archivos, dejando huecos que no son posibles de aprovechar. Ademas de la falta de previsiblidad de espacio, al crear un nuevo archivo, el sistema a priori no sabe cuanto espacio va a ocupar, asi que entra el dilema de darle poco o darle mucho.
	- Este tipo de asignacion funciona exelente para discos de solo lectura (se escribe una sola vez), debido a que se organiza para que no suceda la fragmentacion, y deja de haber falta de previsiblidad. Como por ejemplo: CD y DVD.
- **Lista ligada:**
	- Este metodo busca eliminar la fragmentacion aplicando la logica de una lista ligada continua, permitiendo un aprovechamiento completo (guardando donde se pueda cada bloque), pero siendo lento de iterar y buscar, debido a que funciona con la logica de un puntero que apunta a la bloque siguiente.
		- Se guarda en los primeros bytes del punero la direccion al bloque siguiente.
	- La desventaja principal es el acceso super lento, al tener que pasar por todos los nodos anteriores para la busqueda.
		- Ademas de reduce el tamaño total del bloque dejando se ser potencia de 2, complicado la eficiencia a nivel de software.
- **Tabla de memoria (FAT):** 
	- Se realizo para solucionar el problema de la eficiencia al buscar datos.
	- Todos los bytes punteros dentro de los bloques pasan a una tabla centralizada, la tabla de memoria cargada en la memoria ram.
	- El SO identifica mediante la tabla cargada en memoria el bloque especifico al que tiene que ir, y manda esa unica instruccion a la unidad de almacenamiento secundario.
	- La desventaja principal es que para discos grandes deja de ser eficiente, al tener discos de 1TB, el SO debe crear una tabla de un tamaño proporcional (gigabytes) en la ram, siendo ineficiente en la memoria.
- **Inodos:**
	- Soluciona los problemas de escalabilidad en FAT.
	- Se crea un mini indice individual para cada archivo, acumulando los datos siguientes en una estructura fija y eliminando la necesidad de una tabla gigante:
		- Atributos (permisos, dueño, tamaño (metadatos)).
		- Numero fijo de direcciones directas (Ej: primeros 8 bloques).
	- La eficiencia sucede debido a que solo se cargan los Inodos que ESTEN ABIERTOS en ese preciso momento, dejando los demas en el disco sin ocupar memoria ram, y permitiendo recuperarlos o llevar Inodos a disco si corresponde.
	- Al tener un numero fijo de direcciones para utilizar (8 bloques de 4kb = 32kb), si el archivo necesita referenciar mas direcciones, entonces el ultimo casillero del Inodo referencia a un bloque de punteros indirectos (_Address of block of pointers_) que contiene mas direcciones del archivo, permitiendo redireccionar de forma efectiva cientos de GB.
		- Si es necesario, se pueden redireccionar a bloques indirectos dobles o triples, maximizando la capacidad de redireccionar a bloques, pudiendo un Inodo de tamaño fijo abordar terabytes de informacion.

#### Directorios:
El directorio es un archivo que contiene las direcciones de los demas archivos.
- Un directorio tiene el mapeo logico y relaciones entre archivos y sus nombres.
**Estructura:**
- Es una tabla con 2 columnas: NombreLegibleArchivo | ReferenciaLocalizacion.
- Cuando se abre un archivo, el SO utiliza la "Resolucion de rutas", donde: Ejemplo: /usr/me/so
	- Viaja al sector raiz del disco. Mediante un Inodo de valor fijo. (/)
	- Lee la raiz del arbol hasta encontrar la primera parte de la direccion. (/usr)
	- Al encontrarla, extrae su Inodo y busca en ese nodo la siguiente parte de la direccion. (/usr/me)
	- Repite hasta encontrar el final de la direccion. Recolecando su Inodo para leer los datos de ese archivo especificado. (/usr/me/so)
**Diseños para armar los directorios de una carpeta:**
- Directorio simple de tamaño fijo (FAT):
	- Cada entrada media un tamaño fijo, ejemplo 32 bytes.
	- Se guarda los atributos completos (tamaño, permisos, fechas, etc...)
	- El problema principal viene cuando queres añadir mas atributos, se debe restructurar todo el directorio provocando errores de corrupcion.
- Referenciado a Inodos:
	- Es como se realiza en Unix y linux, el archivo que maneja los directorios es super fino, teniendo 2 columnas:
		- Nombre y Referencia (Nro inodo).
		- Al manejar todo por inodos, los atributos viven dentro de esta estructura de inodos, sin ocupar espacio en este archivo de directorios.
	- La principal ventaja es el bajo consumo de almacenamiento y la posibilidad de crear enlaces duros (nuevos archivos que referencian a los mismos datos).
		- Los hardlinks permiten tener 2 nombres distintos que referencian al mismo inodo: los mismos datos.
Problemas con los nombres largos: En los sistemas antiguos se utilizaban 8 caracteres fijos, cuando se empezo a habilitar los 255 caracteres, comenzaron a haber ciertos problemas con las estructuras de tamaño fijo (Directorio simple de tamaño fijo), que se intentaron abordar de 2 formas:
- En linea (In Line):
	- Las entradas pasan a tener longitud variable.
		- Cada registro comienza con un numero obligatorio que indica la cantidad de caracteres a utilizar. (_File entry length_)
		- Atras de eso estan los atributos y el nombre real, terminando en un caracter nulo.
	- Se crea fragmentacion al borrar un archivo de nombre grande y remplazarlo por otro de nombre corto. Quedando un hueco dificil de aprovechar para el kernel.
- Monticulo (Heap):
	- La entrada de la carpeta se vuelve de tamaño fijo, guardando sus atributos, y el nombre se referencia mediante un puntero directo hacia el montiuclo de texto llamado Heap, que se posiciona al final de la estructura del directorio.
	- Ventaja: Aqui los nombres de los archivos se van acomodando uno atras del otro. Permitiendo modificar el nombre solo editando el puntero de la tabla fija, evitando gastar mucho procesamiento de CPU.
#### Archivos y directorios compartidos:
Aqui se plantea la forma moderna por la cual se permite interactuar con un mismo archivo, un mismo directorio entre varios usuarios a la vez, sin tener que duplicar ese archivo ocacionando perdida de espacio e incompatibilidad:
- La solucion tecnica es el uso de Inodos y enlaces duros. El kernel resuelve mediante:
	- a: El usuario C tiene un archivo en su carpeta. El inodo del archivo dice que C es el dueño y sus enlaces son 1.
	- b: El usuario B crea un link hacia el archivo del usuario C, no duplica los datos, sino que crea un nuevo enlace a esos datos, una nueva ruta.
		- Incrementa el contador de referencias.
	- c: C quiere borrar su archivo, realiza un rm, el SO al ver que hay mas de 1 enlace, borra el nombre de la carpeta de C y reduce en 1 unidad el contador de links al archivo. Los datos persisten, sin embargo C ahora ya no puede acceder a esos datos, ya que lo borro de sus directorios.
	Cada usuario tiene sus propias carpetas y directorios, y los datos fisicos reales solo identifican en cuantos de estos directorios, carpetas estan referenciados.

#### Bitacora y eliminacion fisica:
Cuando el contador de links de un archivo llega a cero, entonces este es eliminado por el SO definitivamente, esto se realiza en un proceso de 3 pasos atomicos:
- Quita al archivo con su directorio.
- Libera el numero del Inodo. Cambia el estado del inodo para identificarlo como "libre".
- Devuelve los bloques al disco. Identifica los lugares que ocupaba en el disco y los marca como "libres".
Si se llegara a cortar la enegia en medio de estas operaciones corromperia la computadora:
- Al borrar el nombre de la carpeta pero no sus datos ni inodo generando un proceso zombie ocupando espacio pero si haber forma de referenciarlo. 
- O al dejar disponible el Inodo, pero los bloques de datos siguen estando ocupados, generando un problema de punteros cruzados al apuntar al asignar ese mismo inodo a otro archivo que apunta a informacion vieja.

**SOLUCION DE BITACORA:**
- Para solucionar este problema, el SO tiene un sistema de bitacora, que permite anotar los pasos proximos a realizar para saber exactamente en que punto estaba antes de la desconexion de energia.
- Se reserva una forma circular y oculta dentro del disco, donde anota toda operacion a realizar, antes de que la realice verdaderamente.
- Una vez realizada, vuelve a esa bitacora y anota que fue completada.
- Cuando la cantidad de tareas supera al limite de espacio designado, al ser circular, se van pisado las nuevas tareas con las viejas.
Se utilizan en sistemas ext3/4 (Linux) y NFTS (Windows).
El kernel antes de montar el Sistema de archivos (File system), busca la bitacora e identifica que tareas quedaron pendientes de realizar.
- Antes de cargar todo, fuerza la realizacion de esos pasos o vuelve para atras para continuar con un sistema limpio.

#### Administracion de espacio:
Explican metodos para administrar el espacio en el disco, existen 2 metodos principales:
- Asignacion contigua: Los bytes de un archivo se guardan uno detras de otro. EN sectores fisicos pegados.
- Asignacion NO contigua: El archivo se divide en partes que se pueden ubicar en cualquier parte de la particion.
El metodo utilizado importa muchisimo debido a que al organizarse en la memoria secundaria, lleva mucho tiempo para acceder a la informacion, provocando que el metodo elegido afectara en gran medida el rendimiento.

**Tamaño del bloque:**
- Consiste en la cantidad de almacenamiento que ocupara un bloque perteneciente a un archivo, este suele ser equivalente a una "pagina", vista anteriormente, debido a que comparten el mismo concepto, hoy en dia suele ser una medida fija por bloque de unos 4kb.
- El dilema de la cantidad de bytes por pagina fue muy ampleo, teniendo problematicas de un bloque con muchos bytes o con pocos bytes, llevando a que estadisticamente se calculara que el bloque de 4kb sea el mas efectivo en efectividad entre: Espacio, velocidad.

#### Funciones esenciales del Sistema de archivos:
- **Registros de bloques libres:** 
	- Indica los espacios disponibles para utilizar, los espacios "vacios" dentro del disco.
	- **Bitmap:** Una matriz donde se representas proporcionalmente todos los lugares (cada bit es un bloque en el disco).
	- **Lista enlazada:** Los bloques vacios se apuntan entre si. Lenta para buscar pero permitiendo una representacion limpia y barata en terminos de espacio.
- **Cuota de disco:** 
	- Permite poner un limite en megabytes a cada usuario en el sistema, que puede ser fijo o flexible. 
	- En archivos compartidos: Evita que un usuario o un grupo acapare todo el espacio disponible.
- **Estrategias de respaldo (Backup):**
	- El file system debe soportar herramientas de clonacion de seguridad para los archivos. Existen 3 tipos principales.
		- Full: Se copia el 100% de los archivos en el disco. SIendo lento y pesado pero muy confiable.
		- Incremental: Solo respalda los archivos que cambiaron en el ultimo respaldo incremental, permitiendo guardar solo lo que cambio en el incremento. Siendo liviano y rapido
		- Diferencial: Se repaldan los archivos que cambiaron desde el ultimo Fulll. Brindando seguridad y eficiencia.
- **Consistencia de archivos:**
	- Son sistemas de seguridad que se activan cuando ocurren ciertas corrupciones relacionadas con los archivos en el momento de un apagado repentino.
	- Al reiniciar la computadora esta activa estos sistemas de seguridad que analizan la estructura de los archivos y buscan contradicciones binarias para permitir rescatar los datos huerfanos antes de montar el sistema, permitiendo arrancar el sistema de forma correcta.
	- Siendo: `fsck` (File System Consistency Check) en linux; `scandisk` en windows.


## Practica:
Aqui se extendera la practica realizada para la U2 de Sistemas operativos, esto incluye:
- Paginacion.
- Enlaces duros y blandos.
- Asignacion de permisos.

### Metodologia:
- Leer teoria con respecto a ese aspecto practico. Extraer ideas y ejercicios fundamentales.
- Realizar practica sobre lo leido segun los documentos de la catedra.
- Expandir con el siguiente tema.

#### Paginacion:
**Resumiendo teoria:** La paginacion es un metodo que surgio de la necesidad de dividir la memoria del sistema en memorias mas especializadas, provocando que se dividiera en la memoria principal (RAM) y memoria secundaria (Disco, etc...).
Cuando un programa es mas grande que la memoria ram, o lo suficiente para acaparar el espacio util, llega el concepto de paginacion que no es mas que un metodo para permitir que una computadora logre usar programar mucho mas grande que sus propias memorias, eso tiene que ver con el disco, donde se almacena el verdadero programa, que al momento de ejecutarlo se particiona en bloques (paginas) que se dirigen a la memoria principal si se necesitan utilizar en ese instante.
El sistema de archivos que hay detras maneja toda la logica de division en bloques.
- La paginacion resuelve el problema de: Fragmentacion, multiprogramacion y velocidad.
- La paginacion requiere un metodo para remplazar las paginas una vez que la memoria ram esta llena de estas. de ahí nacen varios metodos eficientes cada uno en su caso.

Antes existia la monoprogramacion. 
	Esta forma de programacion consistia en un solo programa que ocupaba toda la memoria ram al utilizarse.
	En este punto al haber un unico programa en ejecucion, este utilizaba la memoria ram disponible a su gusto, esto llevo a que se plantearan 3 modelos fundamentales:
	- SO direcciones bajas, programa en direcciones altas.
	- SO solo usa direcciones de solo lectura.
	- Los devices y parte del SO se almacenan en memoria ROM y el resto se almacena en la ram con el programa.

A medida que se fue expandiendo la capacidad, se intento realizar un intento de multiprogramacion organizando a 2 programas que utilizaran diferentes direcciones de ram, llevando a un malgasto de eficiencia al tener que calcular direcciones relativas antes que hacer algo.

Luego nacio el intercambio, este metodo permitia quitar los programas que esten esperando una E/S y mandarlos al swap.
Este metodo flaqueaba en la fragmentacion, al tener que dejar un espacio extra a los programas para que se expandieran.

Posteriormente llego la memoria virtual. Este metodo proponia que el programa no se debia cargar completo en la memoria RAM, esto debido a que solo se debia cargar en la memoria ram la parte que se este utilizando.
Esto llevo a utilizar un dispositivo de hardware especializado en la division e intercambio de estos "bloques" llamado "MMU".
- Cada programa se le dice que tiene una memoria infinita segun la arquitectura, y eso permite que el programa la ocupe y utilice como mejor le parezca.
- En realidad el programa se divide en partes iguales y se van subiendo a la ram las partes que el programa necesita ejecutar.
- Cada trozo del programa se le llama "pagina".
- Solo se cargan las paginas que se van a utilizar en ese momento en la RAM, las demas quedan en el disco.
- La ram se divide en espacios iguales llamados marcos de pagina.
- Los programas al querer utilizar una pagina que no se encuentra cargada, la MMU interviene tirando un "error de pagina", despertando al kernel.
Para identificar los espacios libres en la ram y el disco se utilizan:
- Mapas de bits.
- Listas enlazadas que apuntan a espacios vacios. (Se intenta que los nodos no queden fragmentados, se agrupan).
Estos metodos tienen ciertos problemas como la fragmentacion, indexado lento, y tiempo desperdiciado.

Existen 5 algoritmos de ajuste:
**Fist fit:** Asigna el primer hueco que encuetre. Empieza desde el inicio.
**next fit:** arranca la busqueda desde donde quedo anteriormente.
**best fit:** Busca el hueco perfecto (que entre justo).
**Worst fit:** elije el hueco mas grande.
**dos listas:** Separa los nodos de los procesos y los huecos en busca de acelerar la busqueda.

Modelos de memoria virtual:
- Overlays: Se utilizo primitivamente, lo que se hacia era dividir el programa en varios pedazos antes de compilar, eso permitia ejecutar cada parte de forma individual en la memoria ram, permitiendo que un programa mas grande que la memoria pudiera correr.
	- Al ser manual y complejo, la idea se remplazo.
- Paginacion: la paginacion llego para resolver los problemas de los overlays, delegando la responsabilidad a la MMU y el SO, que se encargaran de adminisitrar el programa individualmente en trozos fijos y especificos.
	- Esto permitio una fluides y compatibilidad completa, al trozar el programa en partes de igual tamaño.
	- Y permitirle brindar una memoria virtual completa y propia.
	- La ram se dividia en partes del mismo tamaño llamados marcos de pagina.
	- Las direcciones virtuales asignadas a cada programa se manejan por la MMU, que permite mover e organizar la memoria virtual de cada programa con respecto a la memoria real (RAM).
	- El fallo de pagina ocurre cuando la parte que pide el programa no esta guardada en la memoria principal. En ese momento la MMU crea una interrupcion por hardware que activa al kernel.
	Las situaciones que se pueden dar son la Hiperpaginacion: Eesto sucede cuando el SO tarda mas tiempo intercambiando paginas que ejecutando codigo util, provocando un congelamiento en la pc.
	Proceso para convertir una direccion de pagina en memoria virtual a una dir en memoria principal:
	- Se obtiene la dir virtual.
	- Se extrae los 4 primeros bits (MAS SIGNIFICATIVOS).
	- Se busca la posicion (numero) que forman esos 4 bits en la tabla, se obtiene un numero en esa posicion. Se encuentra el valor del marco fisico de la ram.
		- Se identifica el bit de presencia en 0 = ausente; 1 = presente.
	- Ese numero se remplaza en los bits mas significativos de la direccion, manteniendo los demas.
	**Tabla de pagina:** Se encarga de identificar los espacios ocupados en la ram y en el disco.
		Esta contiene 6 banderas de referencia.
	- Cache desactivada: 1 para que esa pagina no se guarde en la memoria cache.
	- Referencia: Cuando se lee o modifica una pagina, se pone 1.
	- Modificado: Se pone en 1 cuando se escribe en la pagina.
	- **Proteccion:** se determina por 3 bits.
	- Presente/ausente: 1 para indicar que esta cargada en la ram (Presente).
	- Nro marco de pagina: Guarda el nro real del marco de pagina.
	
	**Algoritmos de remplazo:** Algoritmos para remplazar paginas.
	- NRU (NO USADA RECIENTEMENTE): Permite identificar a cada pagina segun 2 estados: Referenciada y Escrita.
		- Cada caso es una combinacion de todas las posibilidades entre estos 2 estados, teniendo 4 casos:
		- 1) 0, 0
		- 2) 0, 1
		- 3) 1, 0
		- 4) 1, 1
	- FIFO (fist in, first out), pemite realizar una especie de lista donde se van remplazando los primeros que llegan.
	- Reloj: Se basa en la segunda oportunidad, el reloj pasa una vez y marca a todo como "libre", si encuentra algun libre lo remplaza, sino, solo le cambia el estado.
		- Al ser circular, si todos estan ocupados, al primero que le cambio el estado es el primero que eliminara.
	- LRU: El mejor, que seria identifica cual es la pagina mas longeva y la elimina, no se usa debido a su cara implementacion de hardware.
	- Envegecimiento: Aging, consiste en simular el LRU por software, eso significa gastar almacenamiento para indicar cual pagina es la que lleva mas tiempo sin utilizarse.
	Filosofia de asignacion global vs local:
	- Global permite que cualquier proceso se pueda extender como quiera, causando una posible acaparacion de recursos.
	- Local, aisla el programa con su memoria particular, provocando que se evite la acaparacion de memoria, pero a costa que de existan programas que esten ocupando memoria sin estar activos, provocando que programas que si estan activos intercambien las paginas constantemente.
	Segmentacion:
	- Consiste en dividir un programa en diferentes tamaños.
	- Cada segmento representa una parte esencial del programa.
	- Cuando un segmento intenta leer algo fuera de el, se le llama a segmentation Fault.
	


- #### Archivo practico:
	- Graficar paso a paso como los programas se dividen en diferentes paginas que se van cargando en la ram y llevandolas a disco cuando corresponde.


## Sistema de archivos: Enlaces duros y blandos.


## Permisos logica:
Aqui se describe toda la logica de los permisos y su aplicacion practica.
Permisos: Son lo que permite a una cierta entidad poder acceder a un archivo en el sistema.

- Estas entidades son: Usuario (u), Grupo (G), Otros (Una persona que no pertenece al sistema)(O).
	- El root es un ser omnipotente que tiene permisos totales sobre todos los archivos.

- Los permisos se especifican en ternas: Numeros en octal que reseprentan el permiso particular para esa entidad.
	- Eso significa que se determina mediante:
		- Lectura (r) = 100 (4)
		- Escritura (w) = 010 (2)
		- Ejecutar (x) = 001 (1)
		Para el caso de 5 por ejemplo: Tiene acceso de lectura y ejecucion.
		El 7: tiene aceso a los 3 permisos.
	- El numero final se determina como una sumatoria de cada permiso individual: 3 = Read (2) + Execute (1).

Para asignar permisos simbolicos se detalla con estos atributos:
- Categoria (A quien): u (user); g (grupo); o (others); a (all).
- Operadores (Accion): + (Agregar permiso); - (Quitar permiso); = (Pisa lo anterior y establece algo nuevo).
- Permisos (Letras): r (lectura); w (Escritura); x (Ejecutar).

Se escribe en el orden "rwx" para poder asignar los permisos correctamente.

- Comandos de ejemplos:
	- [Comando] + [Persona] + [Operador] + [Permiso]
	- Octal: chmod 666 archivo (SE PISAN LOS PERMISOS ANTERIORES).
	- Simbolico: chmod a+rw archivo (PERMITE AGREGAR O DESCARTAR PERMISOS DE UNA FORMA SIMBOLICA).
		- Multiples cambios: chmod u=rwx,o=r archivo (EL DE LA IZQUIERDA RECIBE EL VALOR DE LA DERECHA).

#### Demas comandos de la familia de CHMOD:
- **umask:** Establece las reglas de los permisos para todos los archivos proximos a crearse en la terminal.
- **setfacl y getfacl:** Permite asignar permisos a un usuario determinado.
- **chattr:** Exclusivo de linux, permite poner el atributo inmutable a un archivo, chattr +i archivo; eso provoca que el archivo sea inmutable y que no se pueda renombrar o modificar hasta que no se le saque el atributo inmutable.
**EJEMPLOS DE USO PRACTICO:**
