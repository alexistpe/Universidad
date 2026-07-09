### **Teoria inicial en papel.**
### **Tipos de sistemas operativos:**
- Mainframe: Sistemas operativos diseñados para manejar volumenes de datos masivos. Su fuerte no es la velocidad.
- Servidores: Diseñados para maquinas que ofrecen servicios a otras.
- Multiprocesadores: Se conectan varias CPU a la vez.
- Desktop: Sirven para maximizar la experiencia del usuario comun al utilizar la pc.
- Movil: SO portable, la gran limitacion es la bateria, la cual requiere que el sistema sea muy eficiente.
- Embebido: Es el internet de las cosas (IoT), tienen una unica funcion y la maximizan.
- Tiempo real: Dispositivos diminutos que requieren alto nivel de optimizacion para funcionar de forma independiente por largos periodos.
- Tarjetas Inteligentes: Corren en un chip y maximizan en la seguridad

### **Conceptos de SO:**
#### Proceso: Consiste en un programa en ejecucion.
- Contiene informacion relevante para funcionar.
- Se asocia a un espacio en memoria y un conjunto de recursos.
- Jerarquia de procesos: Relacion jerarquica entre padre hijo que determina el orden de ejecucion.
- Creacion: Existe diferentes comandos en cada SO para iniciar un proceso. `fork/exec` en Linux vs. `CreateProcess` en Windows
- Tabla de procesos: Se encarga de verificar ele stado de cada proceso.
- Interpretes de comandos: Es un proceso mas que lanza procesos mediante la interpretacion de comandos (shell/GNU).
- Comunicacion entre procesos: Las diferentes formas en las que se comunican los datos entre procesos.
- Identificadores: Definen mediante numeros quien es el dueño de ese proceso y que permisos tiene.
**Espacio de Direcciones:**
- Administración de memoria: Se aftrae la memoria de los procesos, permitiendo administrarla de forma inteligente y evitando sobre escritura.
- Espacio de direcciones: Cada proceso ve una cierta capacidad de direccionamiento (de 0 - n), donde lo utiliza como su memoria individual.
- Cada proceso cree tener su propia memoria (memoria virtual): Esto permite tener varios procesos funcionando al mismo tiempo y distribuyéndose de formas eficientes.
- El SO mapea direcciones virtuales: Esto sucede en tiempo real, permitiendo traducir la dirección relativa que dio el proceso en una dirección real en la RAM.
**Archivos:**
- Jerarquía de directorios: Raiz del arbol (root/; C:/)
- Ruta absoluta: (home/alexis/universidad)
- Ruta relativa: (../config)
- Directorio de trabajo: Es un punto de referencia para interpretar la dirección absoluta del archivo.
- Descriptor de archivos: Al momento de ejecutar archivos mediante syscall (llamada al sistema), no devuelve el archivo entero, sino q devuelve un "Numero" (**entero pequeño**) que equivale al archivo a llamar.
- Tipos particulares: Todo se representa como un archivo.
	- Archivos de bloque: Disco rígido o SSD (lectura en bloques) y permite utilizar el principio de cercanía para el cache.
	- Archivos de carácter: El mouse o el teclado, se lee en ráfagas, esto imposibilita el uso del principio de cercanía, ya que depende de que este haciendo el usuario en ese momento.
	- Tuberías (pipes): Consiste en la comunicación entre procesos, esto se realiza mediante una tubería (|), permitiendo que la salida (envio) de un proceso sea la entrada de otro.
- Sistema de archivo raíz: en windows se utiliza un unico identificador raiz para llamar a las diferentes particiones o discos. En unix se identifica mediante un unico simbolo: /
	- Mount/Umount: Obtiene particiones del disco y las almacena en "home"

#### Entrada / Salida:
**Subsistema independiente de entrada y salidas:** 
	Sirve para comunicar las aplicaciones con los componentes fisicos mediante el SO. Este subsistema se encargar de recibir una instruccion generica y utilizar el hardware para ejecutar la instruccion de forma especifica. Este sistema es independiente del dispositivo, osea que puede adaptarse a cualquier dispositivo.
**Driver:**
	SI depende del dispositivo, y es necesario para que las instrucciones se puedan ejecutar correctamente en el hardware especifico.
El subsistema y el driver se comunican para poder manejar los datos dentro de archivos.

**Tecnicas E/S: Informar a la cpu que el proceso de lectura/escritura termino.**
	Existen 3 metodos principales.
	- **Polling (busy wait):** Pregunta iterativamente si termino, esto consume recursos constantes debido a que la cpu queda ocupada esperando un proceso tardado.
	- **Interrupciones:** Una vez enviada la instruccion, la cpu queda libre, cuando termina el proceso, se envia una señal electrica hacia la cpu para interrumpir el proceso que estaba haciendo y avisarle.
	- DMA (DIRECT MEMORY ACCESS): Es un dispositivo aparte (controlador) y sirve para mover un gran volumen de datos. La cpu envia la tarea y sigue con las demas, el dispositivo se encarga de mover los datos a la ram. Interrumpe a la cpu cuando termina.
**Organizacion de pila en E/S: Como los organiza el SO para que funcione.**
- **Manejadores de interrupciones (handles):** Capa externa que recibe la instruccion de la cpu y comunica al driver.
- **Driver:** Se comunica directamente con el controlador del hardware.
- **Capa independiente:** Maneja el cache y buffering para agilizar la busqueda que pide el procesador.

#### Protección:
La proteccion en un SO viene a raiz de multiples inconvenientes entre multiples programas activos al mismo tiempo. Y no es mas que un mecanismo para preservar los recursos, limitando su acceso.
1) **Permisos de archivo (rwx) y Formas de acceso:**
- **Lectura (r):** Ver el contenido.
- Escritura (w): Modificar contenido.
- Ejecucion (x): Correr archivo o entrar a directorio.
- append y delete: Agregar y eliminar contenido.
	Esto se mide en niveles: 
	**Dueño (7):** 4(r)+2(w)+1(x)=7 (hace lo que quiere).
	**Grupo (5) y Otros (5):** 4(r)+1(x)=5 (solo leen y ejecutan)
2) **Integridad y Confiabilidad:**
	Consiste en la proteccion de los archivos ante sobreescritura y la certificacion de los usuarios.
	**Integridad:** Para mantener un orden entre los diferentes programas, el SO se encarga de que los programas solo puedan modificar su espacio asignado, evitando invadir los de otras aplicaciones.
	**Confiabilidad:** Los recursos solo son utilizados por los que verifican ser administradores/tener el rango necesario.
3) Autenticación y Autenticidad:
	En este apartado se encuentran las diferentes verificaciones que realiza el sistema para permitir el acceso a los recursos.
	**Contraseñas:** Es parte del proceso de login y te asigna los permisos correspondientes.
	**Autenticidad:** Se verifica de donde viene, no solo de quien es: Los diferentes softwares se firman para verificar realmente que ese software es el original y no una posible alteracion perjudicial.
4) Antivirus e IDS
	Capas de seguridad extra al SO.
	Antivirus: Software que registra los diferentes archivos y procesos buscando patrones de software perjudicial (codigo malicioso).
	IDS (Sistema de deteccion de intrusos): Monitorea la red y el comportamiento del sistema constantemente, buscando actividades sospechosas.

#### Shell:
La shell o consola es un programa visual que interpreta comandos del usuario y los comunica al kernel.
- **El Intérprete de Comandos (CLI):**
	Es el proceso que se queda esperando recibir algo (reactivo), cuando recibe el comando, lo separa por parametros y le pide al kernel para que lo ejecute.
	**Ejemplos POSIX:** `bash` (el estándar), `zsh` (el que solemos tunear), `fish` o `dash`.
- **Redirección y Tuberías (Pipes):**
	Permite que los procesos colaboren entre si.
	**Redirección (`>`, `>>`, `<`):** Podés mandar la salida de un comando a un archivo en lugar de a la pantalla.
	**Tuberías (`|`):** Conectás la salida de un proceso con la entrada de otro. Es la base de la filosofía: "hacer programas que hagan una sola cosa y la hagan bien".
- **Variables de Entorno y Scripts:**
	Consiste en metodos para indicar donde se encuentran los comandos.
	**Variables:** Datos como el `PATH` le dicen a la Shell dónde buscar los programas que querés ejecutar para que no tengas que escribir la ruta completa cada vez.
	**Scripts:** Se puede crear un script tipo .sh que contenga los diferentes comandos a ejecutar, y se llame a ese archivo para ejecutar los diferentes comandos. Para automatizar tareas repetitivas.
- **Diferencia entre GUI y CLI:** Ambas son una shell, solo que la GUI tiene una interfaz grafica y la CLI es puramente de texto (comandos).

#### Reflexiones:
**Cada nueva especie de computadora pasa por el desarrollo de sus ancestros**
	Los SO embebidos de hoy repiten conceptos de los mainframes de los 60.
**La tecnología «va y viene»**
	Mainframes → PCs → servidores → cloud → edge. Los conceptos reaparecen.
**Conceptos obsoletos se traen a la actualidad frecuentemente**
	Tiempo compartido (60s) → containers modernos. Batch jobs → serverless.
**Los cambios en la tecnología hacen que vuelvan esos conceptos**
	El procesamiento en la nube recuerda al modelo cliente/servidor centralizado.
**Esto ocurre tanto para hardware como para software**
	ARM resurge en laptops y servidores. Terminales tontos → thin clients → web apps.

#### Llamadas al Sistema — Definición:
Mecanismo en el cual un usuario pide acceso para utilizar recursos del kernel.
Metodo para acceder al kernel en modo usuario. Las syscalls son las "ventanillas" donde los programas piden esos recursos. 
Los programas deben hablar con el administrador de recursos (SO) para utilizarlos. 
Unica forma legal para acceder a los recursos del kernel siendo un usuario.
Grupos principales:
▸ Gestión de procesos: fork, exec, exit, waitpid
	Se encarga de todo el ambito de ejecucion de codigo (Manipulacion de procesos en terminal).
	-  **`fork()`**: Crea un clon exacto del proceso padre.
	- **`exec()`**: Reemplaza el código del clon por un programa nuevo (ej. cuando lanzás el `ls`).
	- **`exit()`**: El proceso dice "terminé mi laburo" y devuelve un estado al padre.
	- **`waitpid()`**: El padre se queda esperando a que el hijo termine para no dejar "procesos zombis".

▸ Gestión de archivos: open, read, write, close, seek, stat
	Se encarga de manejar la informacion en almacenamientos (archivos).
	- **`open()`**: Abre o crea un archivo y te da un **File Descriptor** (el numerito que vimos antes).
	- **`read()` / `write()`**: Pasan datos entre el archivo y un buffer en la memoria del proceso.
	- **`stat()`**: Te da la "ficha técnica" del archivo (tamaño, fecha de creación, dueño).

▸ Gestión de directorios: mkdir, rmdir, link, unlink, mount
	Administrar el arbol de archivos con su jerarquia (modificar rutas/direcciones).
	- **`mkdir()` / `rmdir()`**: Crean o borran carpetas.
	- **`mount()`**: Pega un sistema de archivos (como un pendrive) en una carpeta de tu árbol `/`.
	- **`link()` / `unlink()`**: Crean o borran nombres que apuntan a un mismo archivo físico (inodo).

▸ Misceláneas: chmod, kill, time, chdir
	Conjunto variado de instrucciones para interactuar con diferentes procesos (cateogira de "Extras").
	- **`chmod()`**: Cambia los bits de protección (rwx).
	- **`kill()`**: Envía señales a otros procesos (no solo para matarlos, también para pausarlos o avisarles algo).
	- **`time()`**: Pide al SO la hora exacta del reloj de hardware.
	- **`chdir()`**: Cambia el directorio de trabajo actual (**cwd**) del proceso.
![[Pasted image 20260408110805.png|818]]

### Estructura del SO
#### **Sistema Monolítico:**
El sistema monolitico, propone que el SO sea un unico programa grande con privilegios totales del hardware (modo kernel). No hay divisiones como tal, es un unico binario cargado en memoria.
Este modelo es extremadamente potente (todos los procesos se comunican de inmediato entre si), pero a costa de que cualquier vulnerabilidad puede 
	provocar un colapso de todo el sistema al lanzar un error.
Internamente suele estar organizado de forma lógica para que los programadores no se vuelvan locos (modelo Tanenbaum):
1. **Programa Principal:** Recibe las Syscall, cuando llega busca el servicio o procedimiento que se pidio para invocar o atender.
2. **Procedimientos de Servicio:** Realizar el trabajo asignado por las syscall, ponen en funcionamiento la logica para completar la tarea.
3. **Procedimientos Utilitarios:** Funciones de apoyo comunmente frecuentadas.Ej: mover datos en memoria o utilizar el reloj.
**Rendimiento vs estabilidad:**
Los SO monoliticos son los mas utilizados por su alta velocidad, permiten llamar a procesos casi instantaneamente (unico programa), evitando el retraso de un sistema "distribuido" en diferentes partes individuales, No hay "gastos extra" (**overhead**).
Al no haber seguridad entre modulos, un error en un modulo especifico se lleva a todo el sistema por delante (kernel panic o pantalla azul). Todo el sistema vive y muere como una unica unidad.

#### **Sistemas de Capas:**
Es una forma de organizar la estructura interna del SO.
**Regla:** Una capa solo puede pedirle servicios a la capa que tiene inmediatamente abajo.
**Modularidad:** Permite desarrollar y depurar cada parte del SO por separado.
**Costo de Rendimiento:** Cada petición debe atravesar varias capas, lo que genera "indirección" y hace que el sistema sea más lento que uno monolítico.

**Capa 1 - Gestión de memoria y drum:** Es la base. Se encarga de decidir qué partes del programa van a la RAM y cuáles al almacenamiento (en esa época se usaban tambores magnéticos o "drums").
**Capa 2 - Comunicación operador-proceso:** Administra cómo el sistema le avisa cosas al encargado de la máquina (el operador) y viceversa.
**Capa 3 - Gestión de Entrada / Salida:** Maneja los buffers y el flujo de datos hacia los periféricos (teclado, cinta, discos).
**Capa 4 - Programas de usuario:** Aquí es donde corren tus aplicaciones. Ellas no ven el hardware, solo ven los servicios que les dan las capas de abajo.
**Capa 5 - El operador:** Es el nivel más alto, donde el humano interactúa con todo el sistema ya abstraído.

#### Microkernel:
El microkernel divide las funcionalidad del kernel en diferentes modulos. Estos modulos se comunican mediante el IPC que sirve para comunicar procesos.
Se divide de esta forma: Es un ecosistema de **pequeños programas** que colaboran entre sí.
- **El Núcleo (Kernel):** Solo se encarga de lo básico: **IPC** (comunicación), **planificación** y **gestión de memoria** elemental.
- **Servidores (Modo Usuario):** Todo lo demás (drivers, archivos, red) corre como si fuera una app común.
Esto aporta una ventaja y desventaja clara.
	Es resiliente: Si falla un modulo, se puede reiniciar individualmente sin perjuiar al resto del equipo, permitiendo que siga funcionano.
	Es lento: La comunicacion entre modulos es mas lenta que en el kernel monolitico.
Ademas de ello, permite añadir moulos e forma muy fexible, pudiendo añadir y eliminar servidores, cosa que en un kernel monolitico es mas complejo (se debe recompilar).

#### Cliente/Servidor y Máquinas Virtuales:
Similar a la propuesta del microkernel pero llevada al extremo.
Los procesos (modulos) externos pueden estar en maquinas distintas conectadas por red que realicen ese proceso particular.
Se plantea la propuesta del uso de Maquinas Virtuales para ejecutar modulos individuales en la misma pc pero en diferentes instancias.
- **Abstracción de ubicación:** Al cliente (el proceso que pide algo) no le importa si el servidor de archivos está en su propia memoria o en un servidor en China. La comunicación se hace por mensajes a través de la red.
- **Flexibilidad:** Podés actualizar el servidor de archivos sin tocar el resto del sistema.
- **El punto débil (Latencia):** En un núcleo monolítico, llamar a una función toma nanosegundos. Acá, mandar un mensaje por red toma milisegundos. Es muchísimo más lento, por eso se usa para servicios que no requieren velocidad crítica instantánea.
Hypervisor (VMM): Es el proceso intermediado entre el SO real y el SO emulado, recibe las instrucciones del SO simulado (se piensa que es el SO principal), y se las traduce al SO real.
	Se simula un disco virtual donde el SO lo utiliza como sistema real.
	Permite Aislamiento Total, pudiendo ser infectado y no afectar al SO principal.
Lo que se busca con esta distribucion es la estabilidad, que un error en un servidor no afecte al resto.

## Comandos utiles SHELL:
### Comandos Guia
****
**Ubicacion:**
- **ls:** Lista todo lo que hay dentro de la carpeta donde estas.
- **cd:** Permite moverte entre directorios. ".." = dir padre, "." = dir actual. Combinacion: /../../ para retroceder mas carpetas.
- **pwd:** Te indica el directorio donde estas parado.

**Manipular archivos/directorios:**
- **cat**: imprime por pantalla el contenido del archivo en cuestion
- **cp:** copia el contenido de un archivo en otro, tambien puede crear el archivo.
- **touch:** Crea un archivo con x extension. Se pueden crear multiples archivos con la misma intruccion:
- **nano:** Permite editar un archivo, requiere un programa.
- **mkdir:** Crear directorio
- **rm:** Borrar archivos.
- rmdir: borrar directorios vacios.
- **mv:** Mueve un archivo a otro, corta y pega. Renombra el archivo (lo corta completo y lo pega en otro lado).

**Utilidades generales:**
- **man:** manual de comandos.
- **echo:** escribe por consola.
- **mount:** montar discos externos. Se puede usar como otro directorio.
	- Se necesita: mount + disco + direccion.
- **unmount:** desmonta discos externos.
### Combinacion de comandos
**Manipular archivos:**
- **Crear multiples archivos:** touch f1 f2 f3, 3 archivos diferentes.
- **Escribir archivos:** echo (texto) > (archivo) = Escribe en un archivo.
	- echo (texto) >> (archivo) = Escribe añadiendo una nueva linea.
		- Si el archivo no existe lo crea.
- **Borrar recursivamente:** rm -r (direccion): borra todo.

**Informacion sobre:**
- ls -la: Detalle de archivos y direcctorios, con los diferentes datos y permisos.

**Señales:**
- Para matar un proceso se envian señales: se utiliza kill -9 -id-, sale directamente
- Para detenerlo, se cambia el estado no lo mata directamente: kill 19 -id-
- Para cambiarle el estado a activo: kill 18 -id-

**Usos de artilugios:**
- Usar "/" es para indicar una **carpeta que existe**, no usar la barra sirve para crear direcciones:
	- /c1: busca de la raiz al c1.
	- c1: crea la carpeta c1.
- **Comodines:** Se pueden usar junto a las instrucciones para wmanipular gran variedad de archivos y filtrar por caracteres.
	- " * " sirve para mostrar todo lo que contenga los caracteres que indique, ej: ls file* => trae cualquier archivo que tenga file al primero.
		- Otros ejemplos: 
	- " ? ": trae un archivo que contenga exactamente 1 caracter mas, ejemplo: ls file? => el archivo file77 no lo traeria por ejemplo.
		- Se pueden agregar mas "?" para permitir mas caracteres: ls file?? => ahora si trae el file77
- **Rutas:**
	- Absolutas: Empiezan por "/", comienzan de la raiz.
	- Relativas: Depende donde estemos parados comienza.
- **Permisos:**
	Permite darle posibilidad a un archivo que ejecute comandos y llamadas al SO.
	El SO se divide en 3 partes: Propietario, Grupo y Usuario. Respectivamente
	Existen 3 tipos de permisos provenientes del binario, con sus respectivas combinaciones, si se agrega un '1' esta habilitado, se agrega un '0' esta deshabilitado: 
	- 0 (Lectura), 0 (Escritura), 0 (Ejecucion), el primero lectura, segundo escritura y el tercero ejecucion.
	- Si tenemos 100, solo habilitamos lectura, si tenemos 011: solo escritura y ejecucion etc...
	Para que un archivo pueda recibir esta combinacion particular de servicios segun las 3 tipos de personas se especifica:
	- comando base para permisos: chmod (combinacion) (archivo)
		- Combinacion: 
			- Se debe indicar la combinacion de permisos con un numero decimal que representa 3 numeros en binario (Ej: 7 = 111)
			- Se deben agregar estos numeros en secuencia segun los permisos del propietario, grupo y usuario respectivamente.
			- Ejemplo: chmod 745 arch.txt, Aqui indique para el archivo: Propietario: 111 (todos los permisos), grupos: 100 (lectura), Usuario: 101 (lectura y ejecucion).
### Directorios
Se organiza mediante un estandar: **FHS** (Filesystem Hierarchy Standard).
- /home: usuarios.
- /etc: archivos de procesos internos del sistema.
- /tmp: temporales.
- /bin: archivos ejecutables del sistema.
- /var2: almacena datos de variables.
- /boot: sirve para bootear el sistema.
- **Extras:**
	- **dev y proc: son directorios dinamicos, sus datos cambian constantemente.**
	- lib64: librerias externas para binarios.
	- mnt: puntos de montaje temporales.
	- run: Info volatil del ultimo arranque.
	- srv: Datos particulares del servicio servidor.
	- root: Directorio personal root.
	- sys: Interfaz visual para ver el estado del kernel y configurar.
	- usr: Utilidades para la aplicaciones de usuario.
