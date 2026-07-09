Se borro el progreso en el cuestionario anterior, asi que se continua aqui.
##### Continuamos unidad 1:
- Repasamos unidad 1.
- Todos los dispositivos para linux son un archivo.
- El comando ">" permite guardar la salida en un archivo, osea se lo pasa a un archivo.
	- Se indica ">>" para guardar en salto de liea.
	- >: Pasa el resultado exitoso del proceso, 2>: pasa el resultado de error del proceso.

##### Empezamos unidad 2:
Repazamos toda la guia de procesos, se debe repasar y extender.
Los parciales son teoricos pero van a tener contenido practico.

# clase 3
Repaso procesos unidad.
sd -> discos 
	xy -> x (disco), y (particion)
	Formatear el sistema de archivos adecuado
Analisis de los procesos /dev/
	Salidas estandar. FIlesdescriptors, cada proceso tiene uno.
	0 stdin: Entradas.
		Espera el input del teclado.
	1 stdat: Salida.
		Toda la salida estandar se escribe en la pantalla.
	2 stderr: Error
	Cuando empezás un proceso nuevo, arranca con tres descriptores de archivo estándar (o flujos, o como se les llame en otros idiomas). Estos son: stdin, que es el flujo de entrada estándar del programa, de donde se espera que lea su input; stdout, que es el flujo de salida estándar del programa, donde se espera que escriba su output normal; y stderr, el flujo de error del programa, donde se espera que escriba cualquier mensaje de error.
	Los tres se heredan automáticamente del proceso padre a menos que el proceso padre haga algo al respecto.
	https://www.reddit.com/r/learnprogramming/comments/ugwwbq/what_exactly_are_stdout_stdin_and_stderr/?solution=8b58e51305e2a9418b58e51305e2a941&js_challenge=1&token=bbbe4bf1c9a2b5160829c4be34da58610e3993006a620156e22168de2c737232&jsc_orig_r=&_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc
- Se pueden redirigirlas salidas de los archivos hacia otros archivos en vez de la salida estandar, eso provoca que el mensaje de salida sea redirigido a otro proceso/archivo y en la terminal no aparezca nada.
- Se puede manipular el filesdescriptor redirigiendo su salida y pudiendo no mostrar ciertas salidas especificadas.
- La entrada estandar es el input, ejemplo "cat".
	- No es comun la redireccion de entradas estandar.
	- Se puede redirigir la entrada a un archivo, ejemplo: cat > ~/archivo.txt
- En la instruccion top: load average: 0,77, 1,26, 1,10, determina el promedio de carga de la cpu, el primer valor es de los utimos 15, el segundo de los 10 y el tercero del ultimo.
- Repaso de estados:
	- Ejecutando.
	- suspendido:
	- Bloqueado.
	- zombie: proceso hijo que no es atendido por su proceso padre. Linux lo va delegando a procesos de mayor jerarquia.
¿Que son las dll? ¿Librerias?

La memoria no se debe compartir, pero en la practica los SO la comparten para ser mas optimos, como por ejemplo en las librerias comunes para los programas.
Si el proceso padre no muere, el hijo queda infinitamente reportando al padre, posteriormente queda zombie, si el proceso padre muere y el hijo no, entonces la responsabilidad se delega al abuelo (padre del padre).

## Clase 4
El parcial sera teorico - practico, pero principa, mente teorico.
bcp tabla, se guardan los logs del proceso.
	esta conectado con las llamadas al sistema operativo.
EL "cambio de contexto" es pasar de un espacio a otro, cpu -> memoria -> disco  -> etc... se debe copiar de forma exacta como esta el proceso.
Taza combinada de procesos: tiempos deliminados para el proceso.
Los procesos tienen estados. Necesitan los diferentes componentes e identificadores de los procesos para luego cambiarle a un estado como disco, ejecutable, etc...
Los hilos permiten un pocesamiento pseudo parealelo.
Un proceso se puede apropiar de un dispositivo, cuando este esta escribiendo datos, para terminar con exito.
	Aqui entra el concepto de condiciones de carrera.
	Comunicacion de procesos, varios procesos escriben de forma organizada en la misma spooler, segun en que grilla esten y que turno le toque a cada uno para escribir.
Exclucion mutua: Los procesos se evitan entre si, eso significa que se respetan entre si,para no ocupar el trabajo del otro.
La region critica es la zona donde se intenta acceder a una parte compartida entre procesos.

## 5)
no vine.
Vieron fork exec y proc

## 6)
Comunicacion entre procesos: Util para el acceso a recursos del sistema.
Tuberia.
No sacar a proceso hasta que termine su tarea atomica (mientras este interactuando en la zona critica).
	O se procesan de forma completa o no se hacen.
Region critica: Recurso compartido entre procesos.
	Alternancia estricta: Metodo para intercambiar los procesos que usan los recursos.
	Peterson: Si alguen no necesita usar ese recurso, pasa al siguiente. (Similar a ALTERNANCIA ESTRICA pero con esa condicion).
Semaforo.
	Es una variable que me permite determinar la cantidad de recursos disponibles para que los procesos utilicen.
		Se va modificando la variable a medida que mas procesos lo utilizan a la vez. Cuando es = 0, significa que no hay recursos disponibles para los procesos. Y se tiene que liberar al menos uno para los procesos.
	Se usan wait y signal (P, V respectivamente).

Mutexes, Monitores, Pasaje de mensajes.
Barreras.

Planificador: Segun el estado de los procesos toma cierta decision. Son las estrategicas para organizar la ejecución de los procesos.
	- Segun el tipo de proceso mayoria cambia la estrategia (comportamiento) para ejercutarlos (criteriospara sacarles el privilegio o dejarlos)
	- Existen tipos de algoritmos para la planificacion y manipulacion de procesos.
		Apropiativos:
		NO apropiativos: Normalmente util para procesos en tiempo real o donde es peligroso si un proceso no se termina de ejecutar.
		- Existen multiples metas para los diferentes algoritmos de planificacion.
			- Se definen metricas a maximizar (Una cierta medicion para obtener una estadistica)
	- Algoritmos: Los algoritmos utilizan ciertas varaibles para aplicar estrategias y organizar la ejecucion de los diferentes procesos.
		- FIFO: No apropiativos.
		- Procesamiento por lotes: No apropiativo. Eficiente si la metrica es trabajos terminados.
			- Hay tipo iterativo: Metrica de tiempo de retorno. (Cuanto tarda un procesos en volver)
			- Y real time: Tiempo limite del proceso.
		- Por turnos: Round robin, Noble, simple, equitativo. ==¿Que es un quantum?==
		- Cola por prioridades: Se va resolviendo segun la prioridad. Van rotando la prioridad para que se ejecuten todos.
		- Planificacion garantizada:
		- Por partes equitativas:
		- Sorteo: 

==EN EL PARCIAL NECESITO UNA PC CON WINDOWS. PUEDO INSTALAR UNA MAQUINA VIRTUAL.
EL LUNES SACAMOS DUDAS.
ES EN COMPUTADORA. No hay consola, sino responder. Examen comun.==

#### INTERBLOQUEOS
Se busca adquirir recursos mediante bloques a diferentes procesos.
Se adquiere, libera y utilizan diferentes recursos.
Existen procesos apropiativos y no apropiativos.

La adquisiscion de recursos son:
- Semáros o mutexes asociados al recurso
	- 
- Adquisión de manera secuencial
	- 
- Abrazo Mortal: cada uno de los procesos involucrados se bloquea hasta conseguir el recurso que tiene el otro proceso.
	- Es un conjunto de procesos, no liberan recursos debido a que un proceso tiene un recurso y requiere otro recurso que lo esta usando otro recurso y debido a eso, no libera el primer recurso. Ej: Recurso 1 (de A) -Quiere> Recurso 2 (de B) y B quiere otro recurso que esta ocuado y asi.
Condiciones interbloqueos:
1- Exclusión mutua (Un recurso se asigna a un solo proceso en un Tiempo o está libre)
2- Contención y espera. (Si un proceso tiene un recurso puede solicitar otro) 
3- No apropiativa. (No se puede quitar por la fuerza un recurso, se deben liberar)
4- Espera circular. (Debe haber una cadena circular donde cada uno espera por el recurso del otro).

**Algoritmos:**
Aveztruz: Ignora que sucedan os interbloqueos.
Se detectan los interbloqueos segun determinada condicion.
**Recuperacion de procesos:**
- Medio de aprobacion: Manual en algunos casos, es casi imposible de recuperarse.
- Retroceso: Snapshots, osea capturas del sistema en ese momento periodicamente guardadas en archivos.
- A travez de la eliminacion de procesos: Se elimina un proceso buscando liberar un recurso que libere mas recursos de otros procesos.
Estrategicas para evitar interbloqueos.
Prevenir interbloqueos.

==MEMORIA NO ENTRA EN EL PARCIAL==

HAY QUE PREGUNTAR COMO SE REALIZA LA PARTE PRACTICA DE ESTA UNIDAD.

ACTUALIZAA
