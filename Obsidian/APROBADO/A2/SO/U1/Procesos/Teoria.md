## Diapositiva 1 - Procesos (sintesis general):
#### Agenda:
•Conceptos generales
• Definición
• Creación
• Terminación
• Jerarquías
• Estados de Proceso

#### Conceptos a repasar:
**Concurrencia:**
- Es la forma que utiliza el sistema operativo para tener varios procesos activos compitiendo por los recursos, no se ejecutan todos en simultaneo, sino que se va dando prioridad a procesos individuales de forma limitada para simular esa sensacion de concurrencia.
**Multiprogramacion:**
- Busca que la pc este procesando todo el tiempo posible, aprovechando los espacios de "espera" para poder ejecutar otros procesos pendientes. Ej: Mientras que el proceso A busca en el disco, ejecuto el proceso B.
**Pseudoparalelismo:**
- Consiste en simular la "multitarea" osea la ejecucion de diferentes procesos en simultaneo mediante la asignacion de CPU limitada a los procesos. El SO aprovecha la gran velocidad de la CPU, para ir intercambiando los procesos que la utilizan a una velocidad que se vuelve inperseptible para el humano, permitiendo generar esa sensacion de paralelimo.
**Multinucleo:**
- Al tener mas de un nucleo de procesamiento, permite ejecutar procesos individuales en cada nucleo, esto genera un verdadero procesamiento simultaneo, permitiendo ejecutar 2 o mas tareas en el mismo tiempo fisico, segun la cantidad de nucleos.

**Proceso:**
Es un programa en ejecucion: Es un contenedor que contiene todo lo que el programa en ese momento necesita.
Cada proceso contiene los siguientes elementos para que el SO sepa que esta haciendo:
- Codigo (segmento de texto): Instrucciones que el procesador tiene que leer.
- Datos y Heap: Se guarda la memoria dinamica y datos que el programa debe leer. Son areas logicas en la memoria virtual.
- Stack: Maneja las llamadas de funciones y variables locales.
- Contexto: Contiene el estado de registros de la CPU y un listado de los archivos que tiene abiertos.

**Diferencia entre proceso y programa:**
La diferencia fundamental esta en su comportamiento:
**Proceso:** Es una entidad activa, se ejecuta y comienza a consumir memoria y CPU mediante diferentes instrucciones.
**Programa:** Es una entidad pasiva, un archivo ejecutable que no consume recursos activamente de la computadora, solo el espacio en memoria del programa en si (ocupa su lugar en el almacenamiento, sin cambios repentinos).

**Planificacion (scheduling):** Consiste en el mecanismo utilizado por el SO para organizar la ejecucion de procesos en la CPU, en busca de maximizar: Eficiencia (Que no se pierda tiempo de uso en la CPU esperando) y equidad (Que todos los procesos puedan usar su correspondiente tiempo en la CPU).
El SO manipula el orden y tiempo de la ejecucion de cada proceso.

**Entrada/salida redireccion:**
Para que los procesos puedan comunicarse, se utilizan metodos de entrada (por defecto toma los datos por teclado) (Stdin), salida (Salida por consola) (Stdout), y redireccion es la capacidad de la terminal de cambiar la direccion (destino) de estas entradas/salidas.
- **Salida (`>` o `>>`):** En lugar de mandar el texto a la pantalla, lo guarda en un archivo.
- **Entrada (`<`):** En lugar de esperar que vos escribas algo, el proceso lee los datos directamente de un archivo.
- **Tuberías (Pipes `|`):** Conectás la salida de un proceso directamente a la entrada de otro. Es la base de la filosofía Unix: "hacer programas simples que colaboren entre sí".


#### Diferencias entre Fork y Exec:
**Fork:** Duplica el proceso actual, llamando a folk, esto permite crear un segundo proceso identico, heredando sus variables, datos, archivos abiertos, y diferentes identificadores, esto permite luego, crear un proceso nuevo, modificando los datos internos de este proceso duplicado.
**Exec (execve()):** Esta instruccion borra el contenido del hijo y lo remplaza por el nuevo programa.
**Diferencia con windows:** Aqui se usa CreateProcess(), que crea un proceso nuevo directamente, sin clonar nada.
#### BCP:
El BCP es el identificador del proceso, este contiene:
- Estado: Indica el tiempo de vida que lleva el proceso: **Nuevo** (creándose), **Listo** (esperando CPU), **Ejecutando**, **Bloqueado** (esperando E/S) o **Terminado**.
- Registros de cpu: Guarda los "pasos" que estaba siguiendo en el cpu, para que cuando regresa sepa por donde estaba.
- Identificador numerico: PID: Process ID, con los IDs de usuarios y grupos. Se asigna un unico entero pequeño que identifica a ese proceso de los demas.
- Prioridad: Se usa para determinar si ese proceso debe utilizar la CPU o le toca a otro.
- Punteros a memoria: Referencias a diferentes secciones del proceso.
- Información de estado de E/S: Indica que elementos de hardware y descritores de archivos abiertos (Se te da un numero que identifica al archivo que pediste en la syscall) que esta utilizando el proceso en este momento. Osea que los tiene a su poder.
	- El descriptor de archivos abiertos que utiliza el SO usa unas llamadas estandar:
	  - **0 (stdin - Entrada estándar):** Por donde el proceso "escucha" (generalmente el teclado).
	  - **1 (stdout - Salida estándar):** Por donde el proceso "habla" (la terminal).
	  - **2 (stderr - Error estándar):** Un canal aparte para avisar si algo salió mal, así no se mezcla con los datos normales.
	  Cuando se usa ">" o "|", se esta cambiando la direccion de esa salida (el numero estandar).
- Información de auditoría: Estadisticas del proceso que el SO utiliza para optimizar el rendimiento (tiempo de CPU, uso, tiempo de reloj transcurrido, limites de recursos, etc...)

#### Jerarquia e identificadores:
Los procesos se organizan de forma jerarquica, como un arbol genialogico:
El primer proceso es el **init (PID 1):** Es el "adan" de los demas procesos, se encarga de lanzar los procesos basicos para el arranque del sistema (login, red, etc...)
**UID y GID:** Determina que proceso es el dueño. Al estar por jerarquia, si tu proceso es el UID 0, tenes la capacidad de matar cualquier proceso, leer cualquier archivo o interactuar con cualquier otro proceso.

#### IPC:
Es la forma que tienen los procesos de hablarse entre si.
- Cada proceso se encuentra encapsulado en su propia memoria virtual, para que no rompa otros procesos.
- Se comunican mediante señales, como por ejemplo:
	- "Kill -9": Cerrar inmediatamente el programa.
	- "|": sirve para comunicar la salida de un proceso con la entrada de otro.
	- Etc...

#### Tipos de procesos: 
Existen 3 tipos de procesos diferentes:
- Primer plano: (Foreground): Son reactivos, esperan ser activados por el usuario, son procesos con los que interactuamos, toman una entrada mediante stdin y no devuelven la salida hasta que terminan de procesarlo.
- Segundo plano (Background): Se ejecuta un proceso sin bloquear la terminal, permiten seguir utilizando el sistema para otras tareas mientras ellos estan funcionando de fondo (en la terminal).
	- Tipo especial: Demonio (Daemons): Se inician con el sistema, y permanecen en segundo plano hasta que el sistema se apaga. Varios dependen del init y algunos son fundamentales para brindar servicios esenciales sin necesidad de vivir en la terminal, como el servicio de red sshd.


### Flujo de pedido para lectura en programa modo usuario:
- Un programa modo usuario necesita leer un archivo o elementod el hardware, asi que realiza una llamada mediante read(), para poder solicitarselo al Sistema operativo. Hace una llamada al sistema. (Aplicación llama `read()`)
- Esta llamada cae en la libreria estandar de C, "libc" que traduce los parametros indicados por el programa en organizarlos en los registros de la cpu (en lenguaje ensamblador), Se ocupa un registro especifico con el numero unico de esa llamda en ese momento, osea el numero unico que identifica la syscall. (Wrapper (codigo) en libc)
- Este codigo de la libreria ejecuta una intrucccion en la cpu, esto lanza una interrupcion de software interrumpiendo tu programa de golpe, y cambia la pc de modo usuario a kernel. Salta a una direccion fija de mempria donde el SO tiene su tabla de interrupciones. (INT 0x80 / SYSCALL)
- El kernel ve el registro para encontrar el numero de tramite pedido y ejecuta el trabajo a la correspondiente intruccion que contiene los privilegios para leer, hablar con controladores, mirar cache y obtener datos del hardware. mediante syscall_read. (Kernel: `sys_read()`)
- Una vez guardados los datos en la misma memoria del programa, se pone a la CPU en modo usuario, y se lanza una instruccion tipo sysret o iret para desperatar al programa y lea justo la linea posterior al read con todos los datos cargados. (Retorno a user space)

### Diagramas de cambio de estados:
Trata de como se va modificando el estado del proceso a lo largo de su vida.
- Listo (ready): Esta cargado y preparado en la ram pero esperando que el planificador (shceduling) le de el turno para comenzar a procesar sus intrucciones (Turno en la cpu).
- Ejecutando (running): Esta ejecutando en ese instante las intrucciones en el hardware.
- Bloqueado (Blocked / waiting): No puede seguir operando porque esta esperando un evento externo, una lectura o input, en ese momento la cpu lo deja de atender.

**TRANSICIONES:**
- ready -> running: El planificador (sheduler) le da un turno para el uso de la cpu, y el proceso comienza a ejecutar instrucciones.
- running -> ready: El proceso puede no haber terminado de ejecutar todas las intrucciones, pero se termino su turno designado por el scheduler, volviendolo al estado de listo.
- running -> blocked: El proceso ejecuta una llamada a un dispositivo de E/S, como esta llamada es extremadamente lenta comparada a la velocidad del CPU, este proceso pasa a estar bloqueado hasta que la llamada se ejecute, liberando a la cpu.
- blocked -> ready: El proceso termina la llamada a el dispositivo de E/S, este interrumpe a la cpu, para poner al proceso en fila de espera del scheduler otra vez.

### Diagramas de colas: 
Consiste en como se organiza la memoria para guardar estos procesos con sus respectivos estados.
Se estructuran los procesos como colas (FIFO).
Se divide en 2 areas:
- **Cola de listos:** Aqui se guardan los bloques de control (BCP: identificador del proceso) de los procesos en estado listo. El planificador lee el cabezal de estos procesos para determinar cual sigue.
	Al salir del estado running -> ready, se posiciona al final de la cola.
- **Cola de dispositivos:** Es la lista de los procesos bloqueados, aqui el SO organiza una cola de espera diferente para cada dispositivo de E/S: (Uno para la impresora, otro la placa de red, etc...).
	Se posiciona en la cola de espera para el dispositivo de E/S que realizo la peticion, cuando se ejecuta su orden, sale de la cola y se posiciona a la lista de listos (ready).

### Modelo de 5 estados:
Suma el nacimiento y muerte del proceso (Planificando toda la vida del proceso), es la estructura clasica.
Los nuevos estados son:
- Nuevo (new): El SO esta creando el proceso, se le asigno un BCP, pero aun no esta disponible en la ram.
- Terminado (terminated): Se mata o termina el proceso, liberando memoria y recursos, el SO se encarga de liberarlos.

### Imagen del proceso:
Se crea al sacar el proceso del disco y llevarlo a la ram.
Es un bloque donde se contiene toda la informacion del proceso en la ram: El codigo, datos dinamicos, pila, bloque de control, etc...
Contiene 4 componentes:
- **Programa de usuario (text segment):** Se especifican las instrucciones en binario que debe leer el procesador de forma secuencial, suelen ser solo de lectura para el proceso no se modifique a si mismo.
- **Datos de usuario (Data segment & Heap):** Consiste en las variables globales del programa, las constantes y el heap, este ultimo consiste en el espacio dinamico que el proceso va requiriendo a lo largo de su ejecucion.
- **Pila del sistema (stack):** Es una estructura LIFO, utilizada para almacenar parametros, variables locales, funciones llamadas, direcciones de retorno, etc... para orientar a la CPU cuando la funcion termina.
- **Bloque de control del proceso:** Es la porcion de memoria pertenenciente al SO para poder identificar y maniobrar el proceso, aqui se ubica el BCP. Contiene la metadata que el kernel necesita.
### BCP ATRIBUTOS:
Es la estructura fundamental que usa el SO para identificar los procesos, si el BCP de un proceso se elimina, este proceso deja de existir para el SO.
Sus atributos se clasifican como:
- **Identificacion del proceso:**
	Valores numericos para identificar a los procesos.
	- PID: Entero pequeño que identifica de forma unica al proceso (DNI).
	- PPID: El identificador del padre que lo creo al proceso mediante una llamada al sistema tipo "fork". Mantiene la estructa de arbol genealogico.
	- UID: Identifica al usuario que lanzo el proceso, si este usuario es el root, este proceso tiene acceso a todo el hardware.
- **Identificador de estado del procesador:**
	Cuando se quiere hacer pseudoparalelismo (sacar un proceso de la cpu para meter otro).
	- Se realiza una instantanea del proceso en ese momento para retomarlo mas tarde:
		- Contador de programa (PC): Indica la direccion de la proxima instruccion a ejecutar.
		- Puntero de pila (SP): Apunta al tope actual del stack del proceso, permite identificar las llamadas pendientes que quedaron por hacer.
		- Registros generales: Contenido temporal de los datos que se estaban calculando en los registros internos de la CPU en ese momento antes de que se retirara.
- Informacion de control: 
	Es la informacion que usa el kernel para poder coordinar el trabajo realizado.
	- Estado del proceso: El estado de como se encuentra el proceso: Ready, running, blocked, etc...
	- Informacion de la planificacion: Indican la prioridad del proceso y las estadisticas de cuanto uso la cpu, cuanto le toca, etc...
	- Descriptores de archivos: Es una lista de los archivos o dispositivos de E/S que el proceso uso o esta usando.


### Eventos que provocan la creacion de un proceso:
Consiste en una serie de eventos clasicos que obligan al SO a crear un evento.
- Inicio de sesion interactivo: Consiste en un proceso que maneje la interfaz para comunicarse entre vos y el.Ya sea grafica, una shell, etc...
- Servicios de SO: Se crean automaticamente al encender la computadora para manejar diferentes complementos necesarios apra el funcionamiento del sistema. El SO los inicia como demonios, siendo ejecutados aveces sin el conocimiento del usuario, ejemplo: conexion a red.
- Trabajo por lote: Para sistemas industriales o servidores, se manda una lista de tareas secuencialmente ordenadas, el SO lee una por una y asigna un proceso designado para cumplirla.
- Engendrado por un proceso existente (spawn): Sucede cuando un proceso activo en el SO, le pide crear otro proceso hijo para delegar cierta tarea.
### Creacion de procesos:
Son los pasos que sigue el SO para crear un proceso valido dentro del sistema.
- **Asignar un PID:** El SO tiene en su pool de identificadores los diferentes PID's (Process ID) para identificar cada proceso individual vivo en la maquina, cualquier espacio libre que haya se lo asigna a este proceso, es un entero pequeño.
- **Reserva de espacio:** El SO le pide al administrador de memoria que seleccione y bloque una parte de la memoria ram para la creacion del proceso, esta seccion debe ser lo suficientemente grande para que entre la imagen del proceso alli.
- **Iniciar BCP:** En el espacio protegido del kernel se crea el BCP para el proceso especifico, se rellenan por el SO los campos de identificacion: PID, PPID, UI, PC etc...
- **Establecer enlaces:** El proceso al nacer, es enlazado al sistema, añadiendolo como una rama del arbol genealogico de procesos, enganchado al padre que lo engrendro, ademas su BCP se asigna en la cola de listos (ready queue) para el uso del CPU para que el planificador lo tenga en cuenta para comenzar a usar la CPU.
- **Expansion de estructuras de datos:** El proceso no tiene acceso a todas las funcionalidades del sistema, sino que vive en su propia burbuja, el SO crea los "bloques de accesorios" para que el proceso pueda interactuar con el entorno, se le asigna el descriptor de archivos, registros de autoria, contabilidad de tiempo, etc... 

### Hilos:
Es una entidad de ejecucion mas pequeña del proceso, un "proceso liviano", es un proceso mas pequeño de un proceso.
Este concepto propone utilizar al proceso original como un "contenedor" de los datos, donde los diferentes "procesos livianos" interacturan con los elementos de ese contenedor (viven dentro de ese contenedor, utilizado su memoria y variables), permitiendo ahorrarse reservar un espacio en memoria para la creacion de otro proceso, y permitiendo una mayor rapidez de creado y borrado que el fork.
- Un proceso puede tener uno o multiples hilos, que inducen paralelismo o pseudoparalelismo ejecutandose en la CPU segun la cantidad de nucleos que tenga.
- Al compartir memoria induce ventajas en:
	- Rapidez de comunicacion: A los procesos ver la misma variables locales y cambios (porque viven en el mismo espacio de memoria), estos se comunican instantaneamente (sin necesidad de una tuberia que gaste memoria extra).
	- La creacion de un hilo de un proceso es muy economica en terminos de procesamiento y almacenamiento para el SO, debido a que unicamente se le añade un indetificador (PC, registros, stack), sin necesitar un BCP, espacio en memoria, etc...

Existen hilos del kernel y de usuario.
Tienen diferentes permisos.
## Diapositivas IPC:
IPC (_Inter-Process Communication_) Es un concepto, una serie de mecanismos para solucionar el problema particular de los recursos compartidos. Es la insfrestructura, no un proceso activo.
El IPC consiste en resolver el problema de comunicacion entre procesos, debido a que estos quieren colaborar.
Consiste en resolver 3 puntos fundamentales:
- **Paso de informacion:** Cada proceso tiene su propio espacio de memoria aislada, para poder comunicar esta memoria entre 2 procesos, se utilizan mecanismos que permitan transferirla desde un proceso hacia otro mediante mecanismos logicos.
- **Interposicion (Condiciones de carrera):** Que 2 procesos lean el recurso al mismo tiempo y lo modifiquen en simultaneo causando una corrupcion en los datos guardados.
	- El SO, se encarga de que eso no suceda mediante el IPC, obligando a los procesos a excluirse mutuamente si el otro esta interactuando con el recurso, y esperando que este termine antes de interactuar.
- **Dependencias:** Un proceso puede necesitar el resultado de otro proceso, esto significa que los procesos se tienen que coordinar para que el primero duerma hasta que el segundo termine y obtenga el resultado necesario para desperar al primer proceso.
En el caso de los hilos de un mismo programa, se resuelve y complican 2 problemas diferentes: Primero el compartir memoria se vuelve instantaneo, debido a que se encuentran en el mismo contenedor, pero se incrementa muchas veces el peligro de que 2 procesos modifiquen la varible al mismo tiempo, como por ejemplo en un procesador multinucleo. Esto requiere obligatoriamente procedimentos estrictos de sincronizacion.

#### Condiciones de carrera:
Expandimos el segundo punto de interes, las condiciones de carrera, que determina cuando 2 procesos quieren modificar el mismo recurso.
¿Como nace el problema y como funciona?
- Una sola "linea" o indicacion, el procesador la desarma en varias intrucciones minusculas, osea anatomicas.
- El proceso de c = c + 1 se divide en: leer el valor, modificarlo, y guardarlo. Cada una se ejecuta de forma completa.
- El problema nace cuando el planificador del SO comete errores al desalojar al proceso a mitad del procedimiento porque se termina su turno de uso de CPU por ejemplo.
Ejemplo:
- Imaginá que la variable compartida vale **10**.
- El **Proceso A** arranca y hace el paso 1: lee el 10 y se lo guarda en su registro.
- Justo en ese microsegundo, se le acaba el tiempo al Proceso A. **El planificador lo saca de la CPU y mete al Proceso B** (Desalojo). El Proceso A se va a la cola de listos acordándose de que para él la variable vale 10.
- El **Proceso B** corre completo: lee el 10, le suma 1 (11) y lo escribe en la RAM. Ahora en la RAM dice 11.
- El planificador revive al **Proceso A**. El Proceso A retoma desde el paso 2 con el valor que él ya tenía guardado en su registro (el 10 viejo). Le suma 1 (11) y ejecuta el paso 3: escribe un 11 en la RAM.

#### Exclusion mutua y region critica:
Para solucionar las condiciones de carrera, se requirio definir la zona critica que se busca modificar y aplicar restricciones servera para evitar los problemas de las condiciones de carrera.
- **Region critica:** Es la parte del codigo del programa que interactua con el recurso compartido, si se evita esta parte del programa, los datos nunca se van a corromper.
- **La exclusion mutua:** Es la consecuencia de este analisis, si un proceso entra en su region critica, osea esta ejecutando instrucciones que interactuan con un recurso compartido, para los demas procesos queda terminalmente prohibido ejecutar su region critica mientras otro proceso lo este haciendo, quedando en la lista de espera hasta que el proceso termine de ejecutar su region critica.
	- Si un proceso esta ejecutando la region critica, el resto de procesos se guarda en la cola de espera.
Para lograr la exclusion mutua, tenembaun planteoe stas 4 condiciones generales, sirve tanto para software como hardware.
1) No pueden haber 2 procesos o mas modificando la misma region critica de manera simultanea: 
	- La definicion base de exclusion mutua, si el proceso A esta ejecutanod su region critica, el proceso B debe esperar en la cola de espera.
2) No se pueden hacer suposiciones sobre la velocidad y procesamiento:
	- El codigo de sincronizacion debe ser universal para cualquier tipo de sistema independientemente de su rendimiento, debe funcionar tanto en una maquina vieja mononucleo a una supercomputadora de 64 nucleos.
3) Ningun proceso que no este en su region critica puede bloquear a otro proceso.
	- Impone que solo los procesos que esten en su region critica tienen derecho a bloquear otros procesos que no lo esten, debido a que el estar modificando una region critica presenta riesgos de corrupcion en los datossi otro proceso externo interviene.
4) Ningun proceso debe esperar eternamente para entrar a su region critica.
	- El SO debe garantizar de que todo proceso que espere en la cola de la region critica pueda ejecutarse, y no espere eternamente debido a procesos con mayor prioridad que entran y salen constantemente.

### Exclusión mutua con espera ocupada
Consiste en la explicacion de diferentes metodos antiguos que se utilizaban para solucionar el problema de los recursos compartidos dados por la condiciones de carrera.
Consiste en 4 metodos principales:
- **Deshabilitar interrupciones:** Consiste en que cuando el proceso empieza a ejecutar su region critica, desactiva el reloj del SO, esto permite que el proceso se ejecute de forma completa sin interrupciones y cuando salga vuelva a activar el reloj, permitiendo que el SO vuelva a funcionar. Desactiva las interrupciones por hardware, que le avisan al SO que el tiempo del proceso termino.
	Esta solucion tiene multiples vulnerabilidades al asignarle tanta responsabilidad a un solo proceso: 
	- Si el proceso se cae o entra en un bucle, el sistema operativo queda sin posibilidad de retirarlo porque esta "pausado", provocando que se tenga que resetear todo el sistema.
	- En el caso de tener mas de un nucleo, este metodo queda inutilizable, debido a que otro nucleo en simultaneo puede entrar a la zona critica, aun estando el SO "desactivado" para ese proceso.
- **Variable candado:** Se implemento un metodo que consistia puramente en software, se usaba una variable global "candado", que se ponia en 0 = no hay nadie, y 1 = ocupado, si un proceso queria entrar y la variable estaba en "1", se quedaba en un bucle esperando a que esa variable se ponga 0 para cambiarla a 1 de vuelta y entrar a ejecutar.
	Los problemas de este metodo son los mismos de la condicion de carrera, al no ser una operacion atomica, 2 procesos que esten esperando o quieran ingresar, pueden leer al mismo tiempo la variable, modificarla y porsteriormente ejecutar a la vez la region critica.
- **Alternancia estricta:** Consiste en una variable turno, que va tomando valores segun el turno del proceso, ejemplo: Tenemos proceso 0, y 1.
	- El "proceso 0" entra a ejecutar la zona critica cuando "turno = 0"
	- El "proceso 1" entra a ejecutar la zona critica cuando "turno = 1"
	- Ambos procesos al salir, cambian el numero de turno, si esta en 1 pasa a 0, y viseversa.
	Problema: Si el "proceso 0" tiene una region critica muchas veces mas pequeña que la del otro "proceso 1":
	- Cuando el "proceso 0" se ejecute: primera vez (ejecuta toda la region critica), segunda vez (ejecuta su propio codigo no critico, que puede ser extenso)
	- Cuando el "proceso 1" se ejecute: primera vez (ejecuta una parte de la region critica), y tiene que esperar al "proceso 0" QUE VIOLA LA REGLA 3 para seguir ejecutandose.
	- Un proceso no critico esta bloqueando a uno que si es critico. Ese es el problema.
- ==Solucion de peterson: Es la solucion definitiva del problema de exclusion mutua.==
	Consiste en utilizar el algoritmo de alternancia estricta (variable turno), pero incluir la intencion de cada proceso, si un proceso quiere entrar a la region critica, se setea como "interesado", si no quiere entrar a la region critica, se setea como "no interesado". Al final, termina siendo una exclusion mutua perfecta, abordando las 4 reglas de tanembaun.
	Se usan 2 estructuras de datos:
	- Una variable turno.
	- Un array de 2 booleandos (Los interesados).
	Cada proceso empieza en no interesado (false) y sede su turno al otro proceso.
	**Ejemplo situacion:** 
	- El proceso 0 (no interesado), el proceso 1 (interesado).
	- El proceso 1 esta interesado, entonces pone su bandera true y CEDE su lugar al proceso 0.
	- Si el proceso 0 no esta interesado (false), y el proceso 1 se ejecuta.
	- Cuando terminas de ejecutar tu region critica, entonces cambias tu estado a (no interesado).
	**Caso simultaneo:**
	Si ambos procesos quieren ejecutarse al mismo instante (ambos interesados) pasaria:
	- Alguno de los 2 llegara primero fisicamente:
	- Proceso 0 (interesado) cede su puesto al proceso 1.
	- Proceso 1 (interesado) cede su puesto al proceso 0.
	- El proceso 0 esta interesado y le cedieron el puesto, asi que entra a la zona critica mientras que el proceso 1 queda esperando.
	**Algoritmo:**
		`void entrar_region(int proceso) {`
		    `int otro = 1 - proceso;             // Identifica al competidor`
		    `interesado[proceso] = TRUE;         // Paso 1: Levanto la mano ("Quiero entrar")`
		    `turno = proceso;                    // Paso 2: Soy cortés ("Te cedo el turno, pasá vos primero")`
		    
		    `// Espera ocupada: me quedo acá si el otro quiere entrar Y tiene el turno`
		    `while (turno == proceso && interesado[otro] == TRUE);` 
			`}`
	
		void salir_region(int proceso) {
		    interesado[proceso] = FALSE;        // Al salir, bajo la mano ("Ya no me interesa")
			}

#### Dormir y desperar (sleep and wakeup)
El problema que ocurre usualmente en los SO, es que hay procesos que "malgastan" tiempo de la CPU, en procesos poco productivos (como no hacer nada). Para solucionar esto se crearon diferentes llamadas al sistema para controlar estas situaciones:
- **Sleep():** El proceso se manda a dormir (Listo -> bloqueado), retirandose de la CPU.
- **wakeup():** El proceso vuelve a la cola de espera para poder ejecutarse. (bloqueado -> Listo)
Permite que procesos de baja prioridad que deban realizar ciertas tareas, desplacen a los procesos de alta prioridad que no tienen tareas relevantes y estos sean despertados una vez que los procesos de baja prioridad terminaron.

**Problema productor-consumidor:**
Aqui nace un problema con estas llamadas al sistema, en la situacion donde:
- Haya un productor (agrega elementos) y un consumidor (elimina elementos) de un mismo espacio en memoria.
- Y existe una variable cuenta que evalua cuantos elementos hay en el espacio de memoria:
	- El consumidor se va a dormir (sleep) si la cuenta = 0.
	- El productor se va a dormir (sleep) si la cuenta = max.
	- Ambos se avisan mutuamente para despertarse, suponiendo que se durmieron:
		- Si cuenta = max, y el consumidor entra a procesar, despierta al productor (wakeup(productor)).
		- Si la cuenta = 0, y el productor entra a procesar, despierta al consumidor (wakeup(consumidor)).
- Puede ocurrir que por ejemplo: El consumidor entre a procesar, lea cuenta = 0 y programe la instruccion sleep(), pero justo antes de ejecutarla el Planificador del SO lo saca por exceso de tiempo. Quedando sleep() pendiente.
- Luego entra el productor a procesar, detecta que cuenta = 0 y levanta al consumidor (que ya esta despierto) (wakeup), esta señal se pierde.
- Cuando el consumidor vuelve a habilitarse, ejecuta sleep() y se va a dormir.
- El productor continua hasta que cuenta = max y tambien se va a dormir.
Una solucion fue poner un "bit de confirmacion", que guardaba la señal de "wakeup()", evitando que el proceso se vaya a dormir erroneamente, pero en sistemas donde tenes mas de un productor/consumidor, vas a necesitar mas de un bit de confirmacion, y la estructura se vuelve inviable.

#### SEMAFOROS
Viene de edsger dijkstra, plantea un algoritmo de señales con memoria: 
- Se plantea una variable S con la cantidad de recursos disponibles.
- Y 2 operaciones atomicas (Sola instruccion indivisible: que se ejecutan de forma directa en la CPU y donde el planificador del SO no puede cortar esa actividad (generando una condicion de carrera), o se hace la operacion o no se hace).
	- Down (P, wait): 
		- Resta 1 al valor del semaforo s = s - 1
		- Si el resultado es < 0, entonces no habian recursos libres, frenando al proceso inmediatamente: sleep(), lo mete en la cola de espera del semaforo.
	- Up (V, signal): 
		- Suma 1 al valor del semaforo s = s + 1
		- SI el resultado es <= 0, entonces hay procesos anteriores que estaban durmiendo, asi que, el SO mira la lista de procesos pendientes y levanta al primero: wakeup()
El semaforo (la variable) se puede adaptar a diferentes entornos, permitiendo poder generalizar este metodo para cualquier situacion.

### Mutex, Monitores y pasaje de mensajes:
Son variantes del semaforo, que a medida que fue evolucionando los SO y tecnologia, el semaforo comun quedo corto para ciertas situaciones, y surgieron variantes para esos casos.
**Mutex:** Un semaforo que no sabe contar, sirve de "candado", para prohibir una region critica de forma binaria.
- Mutex_lock(): si esta en cero, lo pasa a 1 y entra, si esta en 1, este proceso se bloque y espera a que se libere.
- Mutex_unlock(): Pone el mutex en 0 y despierta al siguiente en la lista.
	Los hilos de software lo utilizan mucho debido a la eficiencia que propone comparado a la cantidad de veces que se utiliza.
	Al manejarse en instrucciones atomicas, no sufre de condicion de carrera.
**Monitores:**
Es la construccion de un lengauje de programacion (un bloque especial de codigo).
Dentro del monitor metes las variables compartidas y funciones que la modifican.
El compilador se encarga de inyectar los candados por dentras rigiendose por la principal regla de: Es TERMINANTEMENTE prohibido que mas de 1 proceso esten ejecutando el mismo procedimiento detro del monitor. En caso de querer ejecutar el mismo proceso, la llamada queda en la lista de espera hasta que termine.

**Pasaje de mensajes:**
En caso de que los procesos no compartan la misma memoria ram (cosa que se asume en todos los anteriores metodos), se usa el pasaje de mensajes como una forma de solucionar esa falencia.
El modelo deja de usar variables compartidas y usa syscalls puras de kernel.
- send(destino $mensaje): Envia un bloque de bytes.
- receive(origen $mensaje): Se bloquea esperando el bloque de bytes.
Aqui no hay regiones criticas en memoria como tal, sino que el SO se encarga de recibir los datos, estructurarlos, manejar los buffer, sincronizar, etc...


### Barreras:
Es un metodo utilizado cuando multiples procesos tienen que completar una tarea juntos (computacion paralela o pseudoparalelismo), sirve para frenar el avance de los procesos a la siguiente etapa hasta que todos lleguen al mismo punto (la barrera).
Sirve debido a que los procesos pueden avanzar a diferentes velocidades, provocando desincronizacion.
Se maneja en metas, cada meta debe tener a todos los procesos listos (osea que hayan terminado sus tareas anteriormente propuestas) para continuar, si no terminaron todos, los procesos que terminaron quedan bloqueados esperando a los que no.
Una vez que llegan todos los procesos a la barrera, esta lanza una señal al SO que desbloquea a todos los procesos en simultaneo, comenzando la nueva etapa.

## SO - Planificacion:
Permite inducir el pseudoparalelismo, organizando y decidiendo que procesos utilizan la CPU o los dispositivos durante cierto tiempo, para luego intercambiarlos por otros.
Problema: Se tienen multiples procesos listos con un solo procesador activo, en este momento el SO pasa de convertirse en un administrador de archivos a un repartidor de tiempo de cpu altamente efectivo y preciso.
#### **Planificador de procesos (Scheduler)**:
- Es una parte del kernel encargada de decidir que proceso utiliza la cpu y por cuanto tiempo.
- Existen diferentes tipos de planificador segun la situacion a abordar, no existe un unico planificador perfecto:
	- DOS: Sistema mono-proceso, sin planificador:
		- Solo se ejecutaba un programa a la vez, esto llevo a que el programa se adueñara de la CPU al 100%, y que esto sea hacia hasta que el proceso termiara o vos lo cerraras.
	- Rendering: (Procesamiento por lotes):
		- Cuado no hay un usuario interviniendo por atras, simplemente se tiene un conjunto de tareas a realizar, y el objetivo es que se realicen de la forma mas efectiva posible, conviene que se le de el 100% de CPU a una tarea pesada y no se gaste en otra cosa hasta que termine, para evitar microgastos innecesarios.
	- Servidor red, sistemas interactivos (Multiprogramacion):
		- El objetivo aqui es minimizar el tiempo de respuesta, necesita atender multiples procesos diferentes de peticiones de usuarios o de una propia computadora personal al mismo tiempo, y necesita repartir el potencial de computo entre todos los diferentes procesos activos, de forma que pueda simular esa sensacion de "fluides" y "pseudoparalelismo".
- **Costo de cambio de contexto:** Es un acto fisico que realiza el planificador del SO para sacar un proceso que se esta ejecutando en el procesador para poner otro, ese procedimiento lleva un costo donde la cpu no esta realizando ninguna tarea util, simplemente esta realizando una accion tecnica.
	- Proceso:
		- Se detiene el proceso A.
		- Se guardan los diferentes registros y datos de estado en su BCP
		- Se limpian la memoria cache del procesador y el MMU para que el segundo proceso traiga su contexto.
		- Se carga el proceso B.
#### El planificador necesita saber el tipo de proceso que tiene en frente para poder determinar como actuar ante el, que tiempo darle,  que hacer con su estado etc... El desafio es intercambiar estos procesos de forma inteligente para optimizar el uso y potencia de la CPU al maximo.
- Se determina que los programas tienen un ciclo de vida turbulento: intercambian entre 2 estados: E/S y CALCULO, el Calculo exige mucho a la CPU y la E/S lo deja de brazos cruzados (no lo utiliza)
- Segun que estado predomine en el programa se determinan 2 categorias:
	- **Limitados a calculo (CPU-BOUND):** Especializados en utilizar la cpu en extensos calculos, con exporadicos momentos de E/S. Tiene rafagas de CPU muy extensas.
		- Software de renderizado.
	- **Limitados a E/S (I/O BOUND):** Normalmente son procesos interactivos o de comunicacion, sus rafagas de calculo son minusculas, y las rafagas de E/S microscopicas.
		- Navegador web, reproductor de musica.
El objetivo del Planificador del SO, es utilizar el componente CPU lo mas posible, evitando a toda costa que se quede al 0% de uso esperando un resultado. Ante un evento de E/S, el planificador debe reaccionar de inmediato e intercambiar el proceso por otro que use el CPU para una tarea relevante (CPU bound)
- El problema principal es que, a medida que pasa el tiempo la CPU paso a ser miles de veces mas rapida que los dispositivos fisicos, y llevo a que esta pase casi el 99% de su tiempo esperando a los dispositivos fisicos en vez de calcular.
- Tanenbaum hace una advertencia clave para el futuro: **a medida que las CPUs se vuelven más rápidas, los procesos se vuelven más I/O-bound**.

#### Algoritmos del planificador:
El planificador tiene diferentes algoritmos para llevar a cabo su proposito
- **No Apropiativos:**
	El planificador pasa a un estado "pasivo", donde elige a un proceso de la cola de listos, este se adueña del procesador y el planificador deja de intervenir, y el proceso puede salir por 2 motivos:
	- Haga una llamada E/S, sale voluntariamente.
	- Termino de procesar, termino su tarea y ejecuta exit() o return.
	Este metodo era super util en la epoca del procesamiento por lotes, gastaba lo minimo y necesario en retirar y añadir un proceso, pero para sistemas interactivos modernos esto es un peligro, si el programa en cuestion entra en un bucle infinito, el planificador no lo podria sacar (estaba durmiendo), y el proceso nunca le iba a avisar, congelando toda la computadora.
- **Apropiativos:**
	El algoritmo en cuestion le asigna a cada proceso una "rodaja" un espacio de tiempo para poder usar la CPU (cuantum), aprox unos 10-100 milisegundos.
	Se utiliza en todos los sistemas interactivos modernos: Linux, windows, etc...
	Funcionamiento:
		- Utiliza un chip de hardware: EL reloj del sistema.
		- Cada cierto microsegundos este reloj del sistema manda una interrupcion por hardware al procesador.
		- Cuando esta interrupcion llega al CPU, el kernel toma el control con su manejador de interrupciones. Descontando tiempo del cuantum del proceso actual.
		- Cuando este tiempo llega a 0 o menos que 0, se saca el proceso de CPU, guarda su contexto (BCP) y se llama a otro proceso de la cola de listos para que use la CPU.
	Este cambio constante lleva un costo acumulado de context swich.
#### Metricas de exito:
Cada entorno tiene sus propias metricas de exito (Medidas de progreso).

**3 metricas de tanenbaum:**
- **Rendimiento (_Throughput_):** Procesos que la CPU logra terminar por hora.
- **Tiempo de retorno (_Turnaround Time_):** TIempo total de un proceso que se lanza hasta que termina por completo (tiempo de espera + tiempo de ejecucion).
- **Tiempo de respuesta (_Response Time_):** El tiempo que el sistema tarda en responder cuando el usuario realizo una interaccion. En empezar a mostrar algo.

**Algoritmos:**
- **Procesamiento por lotes:** Para casos donde hay montones de datos por procesar sin la necesidad de atender a un usuaro que esta interactuando con el sistema activamente.
	- No apropiativos.
	- Busca maximizar el tiempo de procesamiento, el uso de la CPU, minimizando el cambio entre procesos (**minimizar el Turnaround Time**).
		- **Algoritmos:**
			- **Primero en entrar primero en ser atendido (FCFS):** Simple, se arma una fila con los diferentes procesos, y si sos el siguiente en la fila, vas a usar la CPU. Usa el metodo FIFO.
				- El problema es que procesos mas pequeños pueden quedar atras de procesos enormes: Efecto Convoy.
				- Para el caso de procesos de E/S muy pequeños en calculo, deben esperar mucho tiempo al proceso CPU bound gigante para usar la CPU, esto provoca que se desperdice tiempo en los dispositivos E/S que se pueden aprovechar si la CPU y los dispositivos E/S trabajaran de forma conjunta en vez de forma separada. (Cuando los procesos pequeños entran a CPU, calculan rapidamente y mandan una señal para los dispositivos E/S, alli el proceso gigante empieza a usar la CPU mientras que los dispositivos E/S estan buscando la informacion, ese seria el ecenario optimo que este algoritmo no asegura).
			- **El trabajo mas corto primero: (SJF)** Se deben conocer los tiempos de antemano, para hacer pasar a los procesos que sean mas cortos, esto permite que el rendimiento general sea mucho mas optimo y la cola de procesos se libere mucho mas rapido.
				- Todos los procesos valen lo mismo a nivel jerarquico, el orden es unicamente medido por el tiempo que pasa entre ellos.}
				- Hoy en dia para sistemas interactivos este metodo no sirve, debido a que no se puede preveer el tiempo que pueda llevar los diferentes procesos que se ejecutan, antes se especificaba cuanto tiempo tardaba cada uno y en base a eso se organizaba, si mentian en el tiempo estimado, el SO los mataba.
- **Interactivo:** 
	- Apropiativos.
	- Aqui se **maximiza el tiempo de respuesta**, busca que la experiencia del usuario que esta interactuando activamente con el sistema sea fluida. Se busca cumplir con la proporcionalidad, que cada tarea avance un poco en cada segundo permitiendo que tareas simples se ejecuten mucho mas rapido que tareas complejas.
		- **Algoritmos:**
			- **Round robin:** El algoritmo mas noble, propone una cola circular, donde se le asigne un cuantum a cada proceso, garantizando el tiempo del proceso en la cpu usando el metodo FIFO donde el proceso que agoto su cuantum se va al fondo de la fila con su contexto (BCP) guardado.
				- SI el proceso sin terminar su cuantum, pide una instruccion de E/S, sale voluntariamente del CPU y se dirigue al final de la cola. Permitiendo que el planificador busque al siguiente y lo ponga a disposicion de la CPU.
				- El exito o fracaso del round robin depende del tamaño del cuantum: Uno largo: Puede dar la sensacion de rechazo, Uno corto: Da la sensacion de bajo rendimiento (el CPU pasa una buena porcion del tiempo solo intercambiando procesos), el rango estandar es entre 10 milisegundos y 100 milisegundos, un rango que resulta imperceptible para el cerebro humano.
			- **Jerarquia:** Los procesos se dividen en niveles de jerarquia, donde se van turnando uno por uno hasta completarse, normalñmente usando round robin, sin salir de su nivel de jerarquia, cuando en el nivel de jerarquia actual no hay mas procesos listos, se pasa al siguiente.
				- **Riesgo:** inanicion, si siguen llegando procesos de alta jerarquia, los procesos de baja jerarquia nunca se ejecutaran.
				- Solucion: Se le va aumentando la prioridad al proceso a medida que este envegese, para que tenga oportunidad de competir con los de arriba.
			- **Planificacion garantizada matematicamente:** Se usa un algoritmo matematico para metir la tasa de tiempo que merece cada proceso con respecto a el tiempo real que paso en procesamiento en CPU, si esta tasa de lo que paso/merece es muy baja, el SO lo mete de urgencia para compensar la falta de procesamiento.
				- Calculo: Tasa de tiempo merecido: Tiempo total del proceso / total de procesos activos, TIempo real consumido: milisegundos reales que estubo en la CPU, y el ratio = tiempoEnCPU/TiempoMerecido.
			- **Planificacion por partes equitativas (Fair-Share):** El tiempo de computo se divive por usuarios, no por procesos, si los usuarios tienen la misma prioridad, entonces se divide el tiempo de computo entre ellos independientemente de los procesos que tenga cada uno.
			- **Planificacion por sorteo:** Busca optimizar los tiempos de calculo realizando una asignacion del cuantum por sorteo
				- Se le asigna a cada proceso una cierta cantidad de boletos (0 - 100) segun su prioridad
				- Los de mayor prioridad tienen mas boletos (0-50) y los de menor prioridad tienen menor cantidad de boletos (50-60). 
				- El kernel genera un numero aleatorio en un ciclo de reloj super economico, el proceso que tenga ese valor en su rango obtiene el beneficio de usar ese cuantium.
				- **Ventajas:**
					- **Reactivo:** Si un proceso necesita atencion urgente, el planificador le provee de multiples boletos, aumentando ampleamente sus chances de ser elegido.
					- **Incentiva la cooperacion:** Prioriza procesos criticos, si hay procesos que trabajan en conjunto (A y B), y el proceso A debe esperar el resultado del proceso B, le puede transferir por esa vez todos sus boletos para que el proceso B tenga mas chances de salir elegido.
					- Provee de flexibilidad probabilistica.
- **Tiempo real:** 
	- No apropiativos en tiempos cortos.
	- Son para sistemas criticos, donde se necesita previsibilidad y correcto funcionamiento, donde un retraso de un milisegundo puede ser fatal o desastrozo.
	- Aqui cada proceso se estudia a fondo, permitiendo que se sepa exactamente cuando va a tardar, y estos apropien la CPU por cierto tiempo y luego la dejen voluntariamente. En rafagas cortas de tiempo, divide la tarea en pequeños pasos para dejar lugar a los demas procesos.
	- Se busca cumplir los plazos de entrega y predicibilidad (que el sistema siga funcionando correctamente bajo diverso espectro de situaciones).
#### Metas universales:
Cada sistema operativo debe cumplir con ciertas reglas para que el planificador pueda usar los recursos eficientemente:
**Equidad:** Cada proceso debe tener la garantia de tener un turno en la CPU, no debe sufrir inanicion por procesos nuevos que no le permiten procesar.
**Politica:** El SO puede romper las politicas si hay una regla jerarquica explicita que le de una prioridad a otros procesos sobre los basicos (root).
**Balance:** Planificacion del SO debe encargarse de que todos los procesos (ya sean de CPU o E/S) trabajen en paralelo para una eficiencia general.

### Interbloqueos:
Sos diferentes metodos de repartir recursos y tiempo de CPU para evitar que los procesos no queden completamente congelados.
Es una situacion donde dos o mas procesos estan bloqueados de por vida debido a que uno requiere un recurso que esta utilizando otro.
Los interbloqueos son muy peligrosos para el SO, debido a que dejan procesos bloqueados que pueden llevar a un uno minimo de la CPU mientras que los procesos que la quieren utilizar simplemente estan "esperando" algo que nunca llevara, solucionandose unicamente con un reinicio manual.
	Esta interbloqueado si cada proceso del conjunto esta esperando un evento que solo otro proceso del conjunto puede causar.
	Todos esperan a alguien que tambien esta esperando.
Ejemplo: 
	Se tiene al proceso 1 y 2:
	- P1: Obtiene acceso a la camara.
	- P2: Obtiene acceso al microfono.
	- Luego el P1 quiere obtener acceso al microfono, debido quiza a una videollamada.
	- Y el P2 quiere obtener acceso a la camara por cierta razon.
	Como ambos recursos estan siendo ocupados por un proceso, ambos se bloquean ocupando:
	- Espacio en la ram, en la tabla de procesos.
	- Y sin poder ejecutarse.
Un interbloque ocurre cuando hay un recurso en juego, ocurre una competencia por el recurso.
	Es un elemento del hardware o software que puede ser utilizado por un numero limitado de elementos a la vez, normalmente 1.
	Se dividen en 2 categorias segun como reacciona el sistema operativo:
	**Apropiables:**
		El sistema operativo se lo puede quitar a un proceso a la fuerza sin causar ningun fallo en el programa ni ningun daño.
	**No apropiables:**
		No se le pueden quitar al sistema operativo sin que un programa falle o dañe el equipo/datos.
**CONDICIONES DEL PROCESO:** Un proceso debe estar programado de cierta forma, cumpliendo una serie de condiciones para que utilice un recurso de forma legal dentro del estandar POSIX del sistema operativo.
	**Se realizan diferentes syscall:**
	**Solicitar (Request):** Solicita usar el recurso en cuestion, si otro proceso lo esta usando, entonces queda en pausa (bloqueado) hasta que ese proceso termine. Open()
	**Usar (Use):** Una vez que el recurso se libero, el proceso tiene total poder sobre el y puede utilizarlo como desee.
	**Liberar (Release):** Una vez que ese proceso termino de hacer su trabajo, libera el recurso para su proximo uso. Close()
	Si se programan de mala forma estas instrucciones, provocan que los recursos nunca se liberen y los procesos duerman.

#### Metodos para evitar esta competencia de los recursos:
Se utilizan diferentes metodos para que el recurso en cuestion no sea corrompido por el acceso de 2 procesos a la vez.
**Mutex o semaforo logico:** Se asocia el archivo o variable (recurso no apropiable) a un mutex (candado logico): Se modifica una variable booleana, que permite saber si alguiene sta utilizado el proceso (0) o si esta libre (1), esto permite solicitarlo, verificar y entregarselo o mandar el proceso a la cola de bloqueados. El semaforo logico utiliza una metodologia con el mismo objetivo.

#### Abrazo mortal (consecuencia):
Ocurre cuando hay una adquisicion de recursos de una manera secuencial, y un proceso/programa en particular necesita 2 o mas recursos en simultaneo.
Aqui la culpa la tiene el planificador del SO, al dar un cuantium de tiempo, el proceso no llega a adquirir todos los recursos que necesita, y otro proceso puede entrar apropiarselos, esto provoca que el proceso se bloquee hasta que el proceso apropiador debloquee el recurso, llevando a un posible abrazo mortal:
- Secuencia:
- P1: Pide el recurso 1 y cuando quiere pedir el recurso 2 el planificador lo saca porque finalizo su cuantium.
- P2: Pide el recurso 2 y el planificador lo saca tambien.
- P1: Vuelve a la cpu y al pedir el recurso 2, ve que se esta usando por el P2 y se bloquea.
- P2: Vuelve y al pedir el recurso 1, ve que esta ocupado y tambien se bloquea.
- Ninguno va a terminar de usar el recurso porque ambos estan bloqueados.
El SO arregla esto obligando a los procesos a pedir los recursos de manera organizada y prohibe que se pidan de manera cruzada: Primero se pide el recurso 1 y luego el recurso 2.
	De esa forma el proceso 2 no bloquea al 1 y este ultimo logra adquirir sus recursos y finalizar la terea.

#### Condiciones para los interbloqueos: Condiciones coffman
Existen 4 condiciones fundamentales para que se considere que ocurre un interbloqueo, si se llega a romper al menos 1 de estas 4, el interbloqueo se vuelve imposible.
- **Exclusion mutua:** El recurso se le pertenece a un solo proceso, no puede ser compartido.
- **Contencion y espera (Hold and wait):** Un proceso que tiene un recurso, puede darse el lujo de pedir otro y esperarlo (cambiar a bloqueado) teniendo en su propiedad el recurso anterior (sin liberar el anterior).
- **No apropiativa:** Los recursos que tenga ese proceso no pueden ser arrebatados por el SO. Deben ser liberados voluntariamente.
- **Cadena circular:** Consiste en debe existir una relacion entre los diferentes procesos, donde algunos necesiten recursos que tienen otros. Un proceso espera el recurso que tiene otro proceso de la cadena circular. (Grafo de asignacion de recursos).
Para solucionar el problema debes atacar una de estas condiciones, si logras resolver alguna de estas, los interbloqueos se vuelven casi imposibles de suceder. Busca preveenir interbloqueos.

#### Ejemplos: Modelado de interbloqueos:
![[Pasted image 20260519152631.png|513]]
![[Pasted image 20260519152646.png|529]]
![[Pasted image 20260519152700.png|498]]
![[Pasted image 20260519152713.png|487]]

#### Algoritmo avestruz:
Consiste en ignorar la existencia de los interbloqueos, al considerarlos "poco comunes", asume que no existen y no aplica metodos para solucionarlos.

#### Deteccion interbloqueos:
Formas de detectar diferentes tipos de interbloqueos.
**Un solo recurso de cada tipo:** 
	Consiste en tener, un solo archivo compartido, o una sola impresora, etc... Al simplificar la cantidad de recursos, se vuelve un problema del area de la teoria de grafos: Se busca un ciclo cerrado en el "diagrama" de las flechas.
	Al haber un recurso de cada tipo, la condicion de un ciclo cerrado es condicion necesaria y suficiente para la existencia de un interbloqueo.
	Se utiliza un grafo dirigido: procesos y recursos son nodos de diferentes formas.
	La disposicion de las flechas tiene un significado especifico.
		- **Recurso $\rightarrow$ Proceso (Flecha saliendo del cuadrado):** Significa **Asignación**. El proceso ya tiene retenido el recurso (Hold).
		- **Proceso $\rightarrow$ Recurso (Flecha saliendo del círculo):** Significa **Solicitud**. El proceso está bloqueado esperando que le den ese recurso (Wait).
	Se usan algoritmos para la detencion de ciclos en un grafo.
	Cada nodo se toma como raiz. Si empiezo a bajar en profundidad (seguir las aristas) y vuelvo a pasar por el mismo, entonces estoy en un ciclo.

#### Recuperacion de interbloqueos:
Una vez que se detecta un interbloqueo, el SO utiliza diferentes metodos para poder solucionarlo, estos no tienen una formula magica, alguien va a salir perjudicado, debido a que todos los procesos estan trabados compitiendo por lo mismo.
Vias de escape:
- **Por apropiacion:** Consiste en quitarle el recurso a la fuerza sin que el proceso sepa, esto es altamente complejo, y peligroso en recursos no apropiables: ej impresora. Requiere normalmente una intervencion manual.
- **Retroceso (Rollback):** Se busca que el proceso "viaje en el tiempo", usando puntos de control grabados en el disco, para liberar el recurso que ocupo.
- **Matar proceso (kill):** La solucion mas "bruta" y barata, consiste en matar a un proceso del ciclo o a un "tercero inocente" que contenga la pieza que destraba todo.
	- Aqui hay que tener sutil cuidado con que proceso se mata: 
		- **Matar a un inocente:** La solucion mas limpia es matar a un tercero inocente que no es parte del interbloqueo, pero contiene un recurso necesario para alguno de los que si estan en el interbloqueo, esto permite que al liberar el recurso del tercero inocente, uno de los procesos del ciclo termine su trabajo y destrabe a los demas.
		- **Matar a un proceso del ciclo:** Si no hay un tercero inocente disponible, se elige el proceso del ciclo con menores consecuencias ante la muerte:
			- **Se elige a procesos nuevos:** Buscan a procesos que no procesaron casi nada, para permitir terminar a los que si lo hicieron, consiste en economizar tiempo de computo.
			- **El menor riesgo de corrupcion:** Si la eliminacion de un proceso puede provocar algo irreversible como una corrupcion de guardado, entonces el kernel prefiere mantener la integridad de los datos matando a proceso que puedan empezar de cero sin causar corrupcion de datos: Ej un navegador, reproductor, etc...

#### Evitar interbloqueos metodos:
Evitar un interbloqueo es la mejor forma de resolverlos, permite al SO no llegar a un callegon sin salida, se define al SO como un "ajedrezista" al momento de asignarle un recurso a un proceso, permitiendo preveer todas las posibles combinaciones que puedan ocacionar un bloqueo.
**Se otorga el recurso SOLO cuando el interbloqueo es seguro que no sucedera.**
Existen 2 metodos graficos que utiliza el SO para detectar estos interbloqueos antes de que sucedan:
	**Trayectoria de recursos:** Consiste en "graficar" 2 procesos con exactamente 2 recrusos en un plano 2D, si fueran 3 recursos es en el plano 3D, y 4 no se puede graficar.
		Consiste en detectar cuando estos procesos entran en una zona donde las necesidades de ambos se cruzan, mapeando sus avances en el tiempo:
		![[Pasted image 20260519161700.png|405]]
		La zona rayada son los momentos donde se utilizan los recursos y la zona central (doblemente rayada) es donde ocurre el interbloqueo.
		La linea es el como avanzan ambos procesos.
		- Si el proceso quiere avanzar hasta la zona del interbloqueo, el SO se niega a darle el recurso y lo bloquea temporalmente hasta que se deje de avanzar hacia esa zona.
	**Algoritmo del banquero:** Es un metodo que se utiliza para multiples procesos a la vez.
		Obtiene el nombre de la similitud con un banquero que administra la linea de credito para diferentes usuarios.
		- Se tiene: La cantidad de recursos disponibles del SO y la cantidad maxima que puede pedir cada uno. (Free y Max)
		- Se tienen recursos que necesitan todos los procesos, esto permite determinar cuantos recursos se le pueden entregar a cada proceso para que termine su tarea y libere los que tenia: Ejemplo
			- **Estado SEGURO:**
			- Se tienen los procesos que tienen una cierta cantidad de recursos y pueden pedir hasta una cierta cantidad:
				- A tiene 3 y puede pedir hasta 9 (Le faltan 6).
				- B tiene 2 y puede pedir hasta 4 (Le faltan 2).
				- C tiene 2 y puede pedir hasta 7 (Le faltan 5).
			- En caja (el SO) tiene 3 recursos para entregar (libres).
				- ¿**Es seguro entregarles los recursos?: Si**
				Al proceso B se le entregan 2 recursos llevandolo a (4), realiza su proceso y libera los 4 recursos que ocupaba, llevando el contador del SO a 5.
		- El objetivo es entregar todos los recursos necesarios para un proceso, que este termine y libere los recursos que anteriormente estaba ocupando, de esa forma se evita el interbloqueo.
		**¿Cuando es INSEGURO?:** cuando luego de ir entregando recursos y liberando, quedan procesos que no llegan a obtener todos los recursos necesarios.
			Al verificar un estado no seguro, los procesos NO estan en un interbloqueo todavia, solo entra en un estado donde ya no puede asegurar que todos los procesos tengan sus recursos suficientes, esto lleva a interntar preveenir que se llegue a un estado inseguro.
			La solucion del SO consiste en prevenir el estado inseguro, asignandole recursos a los procesos SOLO mientras mantengan un estado se seguridad.
	![[Pasted image 20260519164415.png|689]]
