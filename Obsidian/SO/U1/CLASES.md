#### PARCIAL LA PRIMERA SEMANA DE MARZO.
### U1)
Introduccion.
	Condiciones de aprobacion.
	3 instancias de evalulacion teorica y 1 practica
	preguntar SAE investigacion con musseta
	Se basa en la fundamentacion tecnica, no tanto en la practica. Explicar como y porque funciona de esa forma un sistema operativo.
	Los sistemas operativos no solo de pc, sino q para cualquier dispositivo (concepto general)
	La U1 consiste en abarcar superficialmente todos los temas para evaluarlos individualmente.
	7 unidades en total.
- Componentes.
- Definicion y tipos de vista
- Modos de ejecucion.
	- Kernel como SO, externo a las manager de ventanas y/o aplicaciones complementarias
- Jerarquia usuario/kernel
- Objetivo de SO
- Servicios
- SO maquina extendida
	- Concepto de memoria virtual (aftraer memoria fisica por SO, no aplear con disco).
- SO como administrador de recursos
**Clase 2: Practica.**
- Repaso Arquitectura computadora.
- Instalar MV debian (ya hecho)
	- Tabla de particiones.
	- Pariciones primerias y logicas. (las logicas servian para extender las particiones primarias. Debido al limitante de particiones primarias que habia antiguamente)
	- Extensión del Sistema de archivos: tipo bitácora, swap
	- configuracion de grub
**Clase 3:**
- Capas y Vistas de un Sistema de Computación
- Maquina extendida: aftraen las complicaciones del hardware, cada unidad se aftrae con un metodo diferente (estandares)
- Multiprogramacion: Optimizar la memoria principal para poder tener multiples programas esten en la memoria principal, y con ello poder procesar multiples tareas "al mismo tiempo", saltando de tarea en tarea. Un nucleo puede procesar 1 tarea a la vez, solo q lo hace muy rapido
- MMU: administran la memoria para que las aplicaciones se administren entre la memoria principal y memoria virtual, permitiendo correlacionar memoria fisica y virtual (aftrae la memoria).
- Jerarquia en: velocidad y tamaño de la memoria.
	- El SO administra las memorias mas lentas.
- Estructura interna de un disco mecanico.
- El kernel esta compuesto de multiples drivers que permitan comunicarse con diversos dispositivos del hardware.
	- Puede necesitar drivers externos para que se comunique con los dispositivos.
- Arranque de la computadora: proceso que realiza la computadora para compilar el SO.
	- El grub es fundamental para iniciar los diferentes sistemas operativos. Las primeras lineas del disco sirven de guia para iniciar el SO (el grub que redirige o el windowsbootloader).
- Tipos de sistemas operativos destinados a diferentes funciones.
- Comandos en servidor y shell
- Los procesos son en jerarquia, un proceso en llinux es hijo de un proceso, el resultaod de un proceso es entrada de otro proceso. EL padre tiene control sobre el hijo proceso.
#### Clase 4
Se instala debian en VM y se realiza practico.
- Memoria de intercambio: sirve para usar de respaldo de la memoria principal, osea es la memoria virtual.
- Opciones para conectarse a la VPS de la facu:
	- Putty - console - combo con winsep
	- Winsep - combo con putty
	- terminus
- Los que no tienen pc se conectar mediante SSH server mediante modificar los puertos.
- Comandos comunes:
	- ls: Lista todo lo que hay dentro de la carpeta donde estas.
	- cd: Permite moverte entre directorios. ".." = dir padre, "." = dir actual. Combinacion: /../../ para retroceder mas carpetas.
	- cat: imprime por pantalla el contenido del archivo en cuestion
	- cp: copia el contenido de un archivo en otro, tambien puede crear el archivo.
	- pwd: Te indica el directorio donde estas parado.
	- touch: Crea un archivo con x extension. Se pueden crear multiples archivos con la misma intruccion:
		- touch f1 f2 f3, 3 archivos diferentes.
	- man: manual de comandos.
	- echo: escribe por consola.
		- echo (texto) > (archivo) = Escribe en un archivo.
		- echo (texto) >> (archivo) = Escribe añadiendo una nueva linea.
			- Si el archivo no existe lo crea.
- Directorios:
	- /home: usuarios
	- /etc: archivos de procesos internos del sistema.
	- /tmp: temporales.
	- /bin: archivos ejecutables del sistema.
	- /var2

### Clase 5
Comandos: 
- ls -la: Detalle de archivos y direcctorios, con los diferentes datos y permisos.
- mkdir: Crear directorio
- rm: Borrar archivos.
	- rmdir: borrar directorios vacios.
	- rm -r: borra todo.
- mv: Mueve un archivo a otro, corta y pega. Renombra el archivo (lo corta completo y lo pega en otro lado).
- mount: montar discos externos. Se puede usar como otro directorio.
	- Se necesita: mount + disco + direccion.
- unmount : desmonta discos externos.

Usos:
- Usar "/" es para indicar una carpeta que existe, no usar la barra sirve para crear direcciones:
	- /c1: busca de la raiz al c1.
	- c1: crea la carpeta c1.
- Comodines: Se pueden usar junto a las instrucciones para wmanipular gran variedad de archivos y filtrar por caracteres.
	- " * " sirve para mostrar todo lo que contenga los caracteres que indique, ej: ls file* => trae cualquier archivo que tenga file al primero.
		- Otros ejemplos: 
	- " ? ": trae un archivo que contenga exactamente 1 caracter mas, ejemplo: ls file? => el archivo file77 no lo traeria por ejemplo.
		- Se pueden agregar mas "?" para permitir mas caracteres: ls file?? => ahora si trae el file77
- Rutas:
	- Absolutas: Empiezan por "/", comienzan de la raiz.
	- Relativas: Depende donde estemos parados comienza.
### Clase 6
- Conceptos del SO - proceso: Aftraen la complejidad
- LS es un programa.
- PATH, es una variable global que permite redirigir a la ruta del archivo: ls = usr/bin/ls
- Comado file -direccion-: Muestra el cabezal del archivo y se muestra las caracteristicas de este.
- Proceso = programa en ejecución, se le asocia un espacio en memoria y un conjunto de recursos. Es un conjunto de cosas necesarias.
- fork y execv lo veremos en un practico de procesos. Son llamadas al sistema para crear procesos.
- se llama al sistema para solucionar los problemas q la aplicacion no pueden hacer.
- el ps permite ver los procesos de la pc con todos sus estados. Maneja los recursos (programas) subiendolos y bajandolos de memoria, para optimizar los recursos.
- El simbolo "&" sirve para seguir utilizando la computadora, mandandolo a segundo plano al proceso: sleep 5 &: duerme 5 segundos pero al mismo tiempo permite seguir utilizando la maquina.
- La terminal es un binario que permite hacer de intermediario entre el sistema y el usuario.
- Procedimiento al realizar un comando:
	- Se ejecuta el comando en la terminal.
	- Se usa laintruccion fork para clonar la terminal en otro espaio en memoria.
		- Se le agrega un pid, memoria y BCP diferente.
	- Al realizar este procedimiento le avisa al sistema que hay un nuevo proceso pendiente.
	- El sistema remplaza la terminal clonada por el proceso a ejecutar, de esta forma se crea el entorno independiente y luego se remplaza por el proceso a ejecutar.
- Los procesos tienen jerarquia entre padres e hijos, es util debido a que quiza un proceso necesita crear otro proceso para cierto fin.
- EL "#" es ROOT, el "$" es USUARIO en la consola.
- .SH permite ejecutar intrucciones directamente en un archivo. Es una extension, se basa en un script de bash.
- Se pueden meter señales a través del proceso.
	- Para matar un proceso se envian señales: se utiliza kill -9 -id-, sale directamente
	- Para detenerlo, se cambia el estado no lo mata directamente: kill 19 -id-
	- Para cambiarle el estado a activo: kill 18 -id-
- Espacio de direcciones: Conjunto de direcciones de memoria que un proceso puede usar.
	- En un ejemplo de redes: Se divide segun la base y la mascara, donde se aplica una base identificada con "/" + un numero, y la mascara son los valores que pueden variar, este "/"+numero actua como una carpeta donde hay multiples archivos:
	  ejemplo: 192.100.0.0 /24, donde quiza: 192.100.0 es la base representada por el "/24" y el ".0" final es o que puede variar, es la mascara. los "192" o "100" son valores que van desde "0 hasta 255", debido a poder usar 8 bits.
	- Un programa cree que tiene toda la memroia, sin embargo si el programa es mas grande q memoria, el SO sube una parte a la memoria principal y el resto queda en la memoria externa, luego  el SO se encarga de subir a memoria principal las partes escenciales.
	