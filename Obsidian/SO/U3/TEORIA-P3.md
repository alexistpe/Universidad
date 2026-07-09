En este archivo vamos a extender la teoria de la unidades 5 y 6 para el tercer parcial de SO.
Al ser mucho contenido, se divide en 4 diapositivas diferentes, 3 para la quinta unidad y 1 para al sexta unidad.

Se seguira esta metodologia para poder llegar bien al parcial:

## Metodologia Estudio:
- Repasar diapositiva.
	- Conectar con lo hablado en el libro.
- Explicar informacion con mis palabras.
- Repetir el proceso hasta terminar las diapositivas de esa presentacion.
- Realizar ejercicios practicos sobre el tema.

## Metodologia Repaso:
- Explicar significado de cada punto.
	- Antoar puntos individuales.
	- Definirlo con mis palabras.
- Realizar ejercicios practicos sobre el tema.
	- Formular y resolver cuestionarios.

# Resumen:
## Unidad 5 (Tres partes): E/S
### Primera parte: Interrupciones.
- Se explica que son las interrupciones al procesador.
#### ¿Porque se realizan las interrupciones?
La CPU se realiza actividades siguiendo 3 instrucciones basicas: **Fetch, Decode, Execute** (Traer instrucción, decodificar, ejecutar), pero a velocidades demenciales.
Cuando un proceso E/S entra como una instruccion para la CPU, esta, si no existiera la interrupcion, quedaria en bucle esperando que el proceso de E/S (que es extremadamente lento) terminara, enviando consultas sobre el estado (Busy waiting) al dispositivo constantemente para ver si termino.
Este mecanismo claramente desperdicia una locura de potencial en la CPU. Por lo que el SO implementa la interrupcion.
- La interrupcion no es mas que un mecanismo que utiliza el SO para poder detener el procesamiento inutil del proceso E/S en el procesador, permitiendo que la CPU utilice ese tiempo para otros procesos utiles. Posteriormente cuando el proceso bloqueado de E/S termina, este vuelve a la CPU gracias a una interrupcion, donde la CPU deja lo que estaba haciendo, y trae el proceso de la cola de espera (rutina de servicio provocada por el "manejador") para terminar de procesarlo.

#### Clases de interrupciones. 4 tipos
- **De programa:** 
	- **Origen:** Interno y sincrono, ocurre exactamente cuando se ejecuta la instruccion que provoca una falla.
	- **Causas:** El propio codigo genera un problema sin querer por una mala codificacion.
		- Overflow.
		- Division por cero.
		- Instruccion en codigo maquina corrupto.
		- Referencias fuera de su espacio de memoria. (Fallo de paginacion o violacion de un segmento externo).
- **Temporizador:** 
	- **Origen:** Externo y asincrono. Ocurre de forma ajena a la instruccion que se este ejecutando.
	- **Causa:** Un chip de reloj de hardware envia pulsos electricos en tiempos regulares, cada cierta cantidad de milisegundos.
	- Permite la multiprogramacion, este metodo le avisa al SO cuanto tiempo lleva el proceso ejecutandose. Al momento de cumplir su quantum el temporizador lo avisa y permite que se despierte el kernel para quitar el proceso de CPU y regresarlo a la cola de listos.
- **De E/S:**
	- Origen: Externo y asincrono.
	- Causa: La placa de control de los perifericos (mouse, teclado, etc...) le avisa al procesador:
		- Que la operacion concluyo correctamente. Osea de forma normal.
		- Que la operacion tuvo alguna falla durante su ejecucion.
			- Condicion de error: Impresora sin papel, falla de lectura, disco CD corrupto, etc...
- **Fallo de hardware:**
	- **Origen:** Electrico, fisico.
	- **Causa:** Alerta de emergencia maxima por un fallo critico en el hardware de la maquina.
		- **Suministro de energia:** La fuente de poder detecta un desenso bruzco en la energia mediante los capacitores, debido a esto, se lanza una alerta al procesador ultraprioritaria para que intente guardar los datos en la ram antes que deje de ingresar energia. Todo esto sucede en milisegundos.
		- **Error de paridad en memoria:** Algun bit de memoria RAM muto debido a una cierta situacion (ruido cosmico (partículas subatómicas de alta energía), degradacion de silicio, etc...) y provoco que se corrompieran los datos.

**Existen 2 tipos de Interrupcion para E/S.**
- **Entrada:**
	- Cuando la CPU recibe una interrupcion por un dispositivo de E/S para avisar que termino, al entrar en la CPU, esta detiene el proceso actual, ejecuta el "manejador de interrupcion" que recupera los datos del buffer del controlador del dispositivo de E/S, los lleva a memoria RAM antes de que el dispositivo de E/S los pise, y limpia este buffer para su proximo uso.
	- Interrupcion -> Detiene proceso -> Recupera los datos del buffer del controlador -> Guarda esos datos en la RAM-> Vacia el buffer del controlador.
- **Salida:**
	- La CPU copia el buffer que guardo en la RAM hacia el controlador. La CPU se desentiende y el controlador del dispositivo se encarga de grabar los datos de una forma "permanente" en alguna memoria secundaria.
	- Cuando este controlador termina, le envia una interrupcion de salida a la CPU, y esta borra la "copia de seguridad" que realizo en la RAM.
	- CPU copia los datos de la RAM en el BUFFER del controlador -> El controlador guarda los datos en el "disco" -> Envia una interrupcion de salida al finalizar -> La CPU borra la copia que tenia en la RAM.

#### Ciclo de interrupcion modificado:
- Consiste en una modificacion a la UC (Unidad de control de la CPU) para permitir crear el modelo descrito anteriormente.
- El ciclo basico de procesamiento de instruciones de 2 fases, muta a uno de 3 fases:
	- **Busqueda (fetch):** El procesador lee la instruccion anotada en el PC (Program counter) desde la ram.
	- **interpretacion y Ejecucion (execute):** La UC (unidad de control) interpreta la instruccion y la ejecuta con la ALU.
	- **Interrupcion (interrupt stage):** Consiste en una nueva etapa que utilizan los procesadores modernos que consiste en verificar los pines fisicos de interrupciones en el procesador para ver el PIC (controlador programable de interrupciones) envio alguna interrupcion, aqui pueden suceder 2 cosas:
		- Sin voltaje en alto: Significa que no hay interrupciones pendientes y la CPU continua sus actividades normalmente. El costo del control es casi cero.
		- Señal electrica en alto: El procesador suspende la terea actual y realiza 3 tareas atomicas de emergencia.
			- **Salva el contexto minimo actual:** Guarda el valor del PC (Program counter) y de la palabra de estado del programa (PSW) en una pila de control del sistema.
			- **Carga un nuevo valor de PC:** El procesador busca la direccion donde arranca el manejador de interrupciones (interrupter handler) para recolectar el pedido del controlador que lo llamo.
			- **Conmutacion:** La CPU pasa a modo kernel y atiende la solicitud dada por el periferico de E/S en cuestion. (Arranca la rutina de servicio).
- El manejador de interrupciones mencionado es parte del SO (Software), y permite facilitar la tarea de atender a los perifericos (dispositivos de E/S) con sus pedidos.

#### Independencia entre modulos:
- La CPU y el modulo de E/S son independientes entre si, pueden y funcionan simultaneamente.
- La CPU manda una instruccion de E/S al modulo, y este se encarga mediante su propio sistema, controlar fisicamente el periferico indicado, permitiendo completa independencia de la CPU para que esta pueda procesar instrucciones utiles de forma mucho mas rapida.
- El modulo de E/S esta integrado como un modulo independiente en el mismo chip de la CPU.
	- A su vez el modulo de E/S esta integrado en la placa madre, componente llamado "chipset" que se encarga de regular los pasos de informacion entre la CPU y los dispositivos.

**Atomicidad de las intrucciones:**
- Aunque suceda una interrupcion de E/S, la CPU continuara hasta terminar la instruccion atomica que estaba realizando, deja los **registros estables** y recien ahí atiende la interrupcion.
- Esto esta hecho de esta forma para que no se corrompan los registros de la ALU al terminar una instruccion a la mitad.

#### PSW: Habilitar interrupciones:
- El SO no siempre esta de acuerdo en atender una interrupcion, debido a esto se creo un registro en la CPU especializado en habilitar o deshabilitar la lectura de interrupciones, para hacerles caso o no.
- El registro de control se llama **PSW (process status word):** Dentro de la palabra del registro, existe un bit especializado en esta tarea: interrupt enable flag (IF).
- Los casos posibles son:
	- IF = 1: Las interrupciones estan habilitadas, el procesador termina la tarea, revisa las interrupciones, guarda el PC y pasa al manejador, etc...
	- IF = 0: Las interrupociones estan deshabilitadas, cuando el SO manda al procesador a tocar datos criticos de la computadora, u el kernel, este manda una instruccion de bajo nivel (Ej: CLI) para poder poner este bit en cero y no poder ser interrumpido por otros dispositivos.
		- En este caso se saltea la tercera opcion (Interrupt stage)

#### Multiples interrupciones simultaneas: Formas de abordarlo.
- Normalmente sucede que en el uso comun, se ejecuten varias interrupciones diferentes al mismo tiempo, el manejador de interrupciones solo procesa una a la vez, asi que aplica 2 metodos para poder abordar este problema.
	- **Secuencial:** Se encarga de atender a las interupciones una a la vez.
		- La CPU termina de ejecutar un programa de usuario y llega una interrupcion.
		- La CPU deshabilita las interrupciones IF = 0 y despierta el manejador.
		- Llega otra interrupcion, pero al estar el detector de interrupciones desactivado, se ignora y queda en una zona de espera guardada en un registro fisico del PIC (Controlador de interrupciones).
		- El manejador de interrupciones termina de atender la solicitud y habilita el bit IF = 1, la CPU vuelve a repasar e identifica que hay otra interrupcion pendiente, y repite el proceso.
		El problema con este metodo es que es estrictamente secuencial, la CPU no le importa si la interrupcion que esta esperando es critica para el sistema, o mucho mas urgente que la actual para ese dispositivo.
	- **Proridades:** Cada dipositivo de hardware tiene su nivel de prioridad, y permite gracias a esto identificar que interrupcion es mas urgente que otra.
		- La diferencia clave es la comparativa y anidamiento.
		- Cuando llega una nueva interrupcion, la compara con la actual, si tiene un nivel de prioridad mayor, ejecuta el anidamiento.
		- El anidamiento es un metodo donde la CPU detiene el manejador que esta atendiendo la interrupcion actual, guarda los datos del "PC" (Program counter), y atiende la nueva interrupcion mas urgente.
		- Luego de terminar la interrupcion mas urgente, atiende a las menos prioritarias, y carga los PC de las que fueron interrumpidas.
#### Escala de prioridades:
SImbolizan a los dispositivos que tienen mayor prioridad o menor en cierta escala, para que el dipositivo de E/S pueda abordar los mas esenciales.
La escala se mide en 2 factores clave.
- Importancia para el sistema.
- Velocidad de procesamiento.
Entre mas prioritaria sean estas caracteristicas, mas alto en jerarquia va a estar, osea va a tener una prioridad mas alta.
Ejemplos de niveles de prioridades: Mayor a menor.
- **Clock:** Esencial para que el SO no pierda el ritmo de tiempo real. La hora del sistema es esencial para que no se descalibren planificadores, cuantums, firmas criptograficas y muchas cosas esenciales del dispositivo que dependen del tiempo.
- **DIspositivos de red o discos rapidos:** Estos son esenciales, debido a que su buffer se llena super rapido. Provocando una perdida de datos inminente debido a su constante flujo de informacion.
- **Terminales y puertos de serie:** Transmiten datos mediante los buffers y controladores y sus buffers tardan cierto tiempo en llenarse que permite un abordaje veloz de los dispositivos con mayor prioridad.
- **Dispositivos interactivos:** Son todo tipo de dispositivo que utiliza el ser humano, estos dispositivos son de baja prioridad, debido a que la cantidad de bits por segundos que puede llegar a transmitir un dispositivo controlado por los sentidos humanos, es miles de veces inferior a la velocidad de un dispositivo masivo como la red. Esto lleva a que los dispositivos que dependan de los sentidos humanos transmitan datos a la velocidad que un sentido humano puede lograr, como por ejemplo mover un mouse, dando una brecha gigante de tiempo entre cada bit nuevo que el dispositivo entrega.
- **Dispositivos lentos y de bajo riesgo:** Principalmente las impresoras, los datos se dirigen de la RAM al dispositivo, en este caso, si el kernel se tarda en transmitir los datos, el dispositivo se quedara esperando, no hay perdida de informacion ni riesgo fisico. El kernel delega su instruccion de pedido de informacion, hasta que termine de procesar lo mas importante.
### Segunda parte: Diferencias y administracion de E/S
Inicialmente se separa a la CPU-RAM del resto de dispositivos, tanto la CPU como la RAM manejan velocidades demenciales con respecto a los demas diapositivos de E/S, tan es asi, que el SO utiliza un sistema para aplicar interrupciones al procesador cuando se esta relalizando una operacion con estos dispositivos externos, debido a que gastan valioso tiempo de trabajo de la CPU.

##### Clases de los dispositivos de E/S: Clasificacion funcional.
Se organizan los dispositivos de E/S en estas clases: Clasificacion funcional.
- **Legibles para el usuario:** Dispositivos que interacturan de manera directa con el humano, necesitan traducir los datos en un formato entendible para los sentidos del humano.
	- Mouse, teclado, pantalla, etc...
- **Legibles para la maquina:** Dispositivos electronicos que interactuan entre si, estos se manejan normalmente por cadenas binarias u otro tipo de comunicacion, aqui no hace falta traducir a un lenguaje legible para el humano, ya que toda la comunicacion ocurre fuera del acceso humano y se utilizan directamente los datos crudos. Su objetivo es la velocidad y densidad de bits.
	- Discos rigidos, placa madre, etc...
- **Comunicacion:** Son dispositivos diseñados para interactuar con otros dispositivos externos a su sistema interno, se comunican con otras computadoras o sistemas remotos, mediante el uso de dispositivos fisicos (medios fisicos): Placa de red, fibra optica, radiofrecuencia, etc...
	- Red ethernet, modem, WI-FI.

#### Escala temporal:
- Los dipositivos de hardware transmiten bits por segundos en cantidades muy dispares entre dispositivos. Y este es un gran problema para el SO.
	- La medida de transferencia es en bps: bits por segundo.
	- **Lento (10¹ - 10³):** Un dispositvo como el mouse y teclado envian 10¹, 10² respectivamente bps, esto es increiblemente lento para la CPU, y eso es debido a que dependen de nuestros reflejos biologicos.
	- Rapido (10⁶ - 10⁹): Componentes como el disco duro, ethernet o pantalla grafica transmiten bps en formas de rafragas repletas de bits de informacion constantemente.
- Debido a que existe esta disparidad entre dispositivos lentos y rapidos, existen diferentes formas de manejar esta entradas de datos.

#### Clasificacion de dispositivos: para el SO.
- El sistema operativo divide a todos los dispositivos de E/S en 2 grandes tipos:
	- **Bloque:** Dipositivos que funcionen como un disco.
		- La informacion se divide y transmite en bloques estructurados independientes de tamaño fijo.
		- Direccionabilidad: Cada bloque tiene una direccion logica independiente. Que permite el acceso directo.
		- Busquedas: Permiten el uso de syscall "seek" para buscar un dato en cualquier parte del dispositivo.
	- **Caracter:** Dipositivos de envio, osea todo lo que no se comporte como un disco.
		- No hay datos estructurados ni fijos, el dispositivo acepta una rafaja de bytes sueltos.
		- No son direccionables, eso significa que viajan en un flujo continuo.
		- No acumulan datos, no existe la funcion "buscar".
#### Objetivos del software de E/S. 4 metas
- Se requiere que los dispositivos de E/S queden aftraidos tanto para el usuario como para el resto de procesos, para permitir una fluidez en la comunicacion y no depender de saber el modelo, instrucciones y dinamica especifica del modelo del dispositivo de E/S.
- Se necesita que todo pueda funcionar por syscalls.
- Las metas del SO con respecto a este diseño de software son:
	- **Idependencia de dispositivos:** Que un cierto comando pueda ejecutarse en cualquier dispositivo, al interpretar todo como un archivo, incluido los dispositivos, el SO permite moldearlos para poder recibir, manipular o enviar señales de estos de forma sencilla.
		- Consiste en que se pueda leer o escribir en cualquier dispositivo sin importar que modelo o tipo sea en especifico, Ej: no impora si es un hdd de kingstone o un sdd de pepito, el SO sabe que es un almacenamiento secundario, como funcione dentro no importa.
	- **Independencia de denominacion:**
		- Se debe poder acceder a los dispositivos mediante rutas logicas comunes (arbol jerarquico del sistema), no debe depender del nombre o caracteristica del dispositivo en cuestion.
	- **Manejo de errores locales:** Ante cualquier error en los dispositivos de E/S, se deben intentar resolver de forma local, osea sin escalar el problema a capas superiores (CPU, SO, KERNEL, etc...), todo se debe resolver en el silicio, solo cuando la situacion es imposible de solucionar, escala a capas superiores (datos perdidos o hardware destruido). Los errores locales ocurren constantemente. "**delegar y resolver el error lo más abajo posible**."
	- **Transferencias sincronas y asincronas:** 
		- Consiste en la manera de administrar el tiempo y las tareas a realizar.
		- **Sincronas:** Consiste en bloquear a un proceso que ejecuto una operacion de E/S, y quede bloqueado hasta que los datos este fisicamente en la ram. El flujo es lineal.
		- **Asincronas:** El proceso lanza una operacion E/S y sigue ejecutando sus demas lineas de codigo independientes a esa lectura. Cuando verdaderamente llegan los datos de la llamada (el buffer se guarda en la RAM), el proceso recibe una señal por una interrupcion de hardware.
		- El metodo asincrono es increiblemente mas rapido, que el sincrono, pero complejo de coordinar.

#### Tecnicas de E/S: Evolucion tecnica
Se describe la evolucion que tuvieron los dispositivos de E/S y la organizacion del SO para quitarle trabajo a la CPU.
- **E/S programada (Polling):** Es uando un proceso tira una llamada de E/S y la CPU se queda esperando que termine, preguntando constantemente si termino.
- **E/S dirigida por interrupciones:** El proceso ejecuta una operacion de E/S, luego se bloque al proceso para dejar disponible a la CPU, y posteriormente cuando el dispositivo de E/S termina de hacer su trabajo, envia una interrupcion por hardware y el proceso que hizo esa llamada, es puesto como listo, subiendolo a la CPU.
- **Acceso directo a memoria (DMA):** Si bien la E/S por interrupciones parece resuelto, en realidad el dispositivo de E/S envia interrupciones para que la CPU vaya guardando pequeños bytes que recolecta, esto provoca que la CPU se interrumpa constantemente. Para solucionar esto, se aplica un modulo externo a la CPU llamado DMA, que se encarga de recibir estas constantes interrumpciones de los dispositivos de E/S, y guardar los datos. La CPU solo le envia la instruccion al DMA, y este hace el trabajo de mover cada pequeño byte.
#### Evolucion del sistema E/S: Como se menejan las E/S
- Solo procesador: El procesador controla al periferico en cuestion. Solo se permite cuando el dispositivo es controlable por un microprocesador.
- Controlador: Se añade un controlado al dispositivo para que la CPU no tenga que hacer el trabajo de manipular el dipositivo de E/S.
- Interrupciones: Sigue la misma dinamica, pero ahora la CPU no se tiene que quedar esperando a la respuesta del dispositivo, sino que bloquea al proceso, y espera la interrupcion del dispositivo cuando termine.
- DMA: Se añade un modulo capaz de mover los datos que le envia el dispositivo de E/S a la RAM de forma autonoma, sin necesidad que la CPU tenga que ser interrumpida para eso constantemente.
- Modulo idependiente de E/S: Se actualiza el modulo de E/S para convertirse en un procesador independiente, adquiere su propio juego de instrucciones (ISA), este se vuelve capaz de procesar instrucciones mas complejas relacionadas con los dipositivos de E/S, permitiendole a la CPU realizar una planificacion con diversas intrucciones de lectura, escritura, y organizacion, permitiendo delegarsela al modulo de E/S para que este se encarge de completarla, solo avisando a la CPU cuando todo el proceso finalizo.
- Modulo E/S complejo: El modulo de E/S adquiere mayores capacidades, permitiendo delegarse casi todas las tareas de E/S, permitiendo que el modulo se encarge de controlar multiples dipositivos de E/S, y sin necesitar instrucciones dadas por la CPU, teniendo capacidad de desicion, se trata como un "procesador alternativo" especializado en las E/S. Comunmente se utiliza para la interaccion entre diversas terminales.

#### Capas de software sobre E/S:
- Nivel de usuario.
- Software independiente: Se encarga de que todos los perifericos hablen el mismo idioma, con las mismas instrucciones genericas.
- Controladores.
- Manejadores de interrupciones.
- Hardware.

#### Software independiete para E/S:
Es un software encargado de unificar la comunicacion entre los dispositivos para una mayor eficiencia.
Funciones clave:
- Interfaz uniforme para los drivers: Todos los drivers traduzcan la instruccion generica (read, write and open) a su intruccion especifica.
- Buffers: Se utilizan buffers en la RAM para mitigar las diferencias de velocidades.
- Reporte de errores: Traduce errores particulares del dispositivos en errores entendibles para el sistema.
- Tamaño de bloque: Permite que el sistema de archivos vea bloques de 4k (Tamaño fijo), permitiendo una facilidad de manipulacion, aunque el dispositivo maneje otro tipo de tamaño.
Esto lo permite la interfaz de controlador estandar, sin ello, el sistema debe comprender a cada dispositivo individualmente con sus caracteristicas, lo que lo haria muy propenso a errores.

## Tercera parte: Gestion de E/S y administracion de disco.
#### Objetivos de diseño.
Se plantean 2 caracteristicas fundamentales para el diseño del subsistema de E/S:
- **Eficiencia:** Al administrar los dispositivos de hardware mas lentos del sistema, la eficiencia es un punto fundamental en la filosofia del diseño, impactando directamente en 3 puntos.
	- **Arrastrar a la CPU:** Un sistema E/S mal optimizado, puede contendar a la CPU a esperar multiples entradas sin procesar ni un dato util.
	- **Multiprogramacion:** El software de E/S debe ser capaz de coperar de forma perfecta con planificador de procesos, esto permite exprimir cada ciclo reloj de la CPU al maximo al organizar las tareas de forma inmediata. (Conmutar contexto).
	- **Intercambio:** Al llenarse la memoria RAM, el sistema necesita utilizar parte del disco como memoria de intercambio, sin embargo si el software y algoritmos de escritura no son optimos, provocan un cuello de botella terrible.
- **Generalidad:** Se busca que sea facil y directo interactuar con los dispositivos. Se busca que resulte sencillo interactuar con los dispositivos.
	- **Simplicidad en la utilizacion:** Un comando simple debe ocultar la complejidad de comandos mas complejos: Un read() debe ser suficiente para leer en el dispositivo, sin importar lo que deba hacer atomicamente para lograr esa accion.
	- **Aftraccion:** El sistema de E/S debe ser capaz de mostrar los datos de forma homogenia entre dispositivos, pudiendo ver a los dispositivos bajo interfaces logicas identicas e uniformes. Donde 2 dispositivos tecnicamente diferentes puedan representar el mismo dispositivo logico: Ej: hdd y sdd, completamente diferentes internamente, pero se le pueden realizar las mismas operaciones.
#### Estructura logica E/S: inteligencia de las capas
En la estructura de las E/S nacen las capas.
Entre mas alta una capa, mas inteligente es, y a su vez, mas lenta de procesar.
Entre mas baja una capa, mas "tonta" es, pero mas rapida.

**Gradiante de velocidad:**
- **Capa baja:** El hardware realiza operaciones en milisegundos, demencialmente rapido, utilizando transistores y componentes electronicos que permiten operaciones mediante corriente electrica.
- **Capa alta:** Aqui sucede un cambio interesante, a medida que vamos escalando el software, este debe lidiar con mayores problemas logicos: Permisos, carpetas, archivos, y necesidades que las capas bajas simplemente no tienen. Al delegar esta complejidad del sistema a las capas altas, se vuelven mucho mas lentas en procesar la informacion.

#### Elementos: Mediadores 2 tipos
**E/S logica:** Es la que atiende las instrucciones del usuario y comunica las peticiones a los dispositivos de hardware.
	Su trabajo es:
	- Identificar a los dispositivos y vincularlos con el sistema de archivos (VFS).
	- Brinda comandos sencillos: open(), close(), etc...
	- Controla los permisos y derechos de acceso.
**E/S de Dispositivo:** Se encarga de recibir la instruccion y traducirla en una serie de pasos a realizar.
	Se encarga de traducir esa instruccion general en una serie de instrucciones precisas para el dispositivo en cuestion.
	Su objetivo es maximizar la organizacion fisica y la optimizacion de transferencias.
	- Uso de buffers: Acumula los datos que llegan del hardware en la memoria RAM del kernel, para evitar que se desborde antes de pasarselos al proceso.
	- Secuencias de intrucciones de E/S (Traductor): Traduce una instruccion logica generica en una lista de pequeñas instrucciones (ordenes tecnicas) adaptadas al hardware.
	- Planificacion y control: Es la capa encargada de decidir el orden en el que se van a atender los procesos realizados por el usuario, para no marear al dispositivo elegido.

- El **orden jerarquico** parte de: Proceso de usuario <-> E/S logica <-> E/S dispositivo <-> Planificacion y control <-> Hardware

#### Importancia de los buffers de E/S:
En una situacion donde no existieran los bufffers de E/S, un proceso que este funcionando en la ram, puede emitir una lectura de E/S, y al delectar esa lectura al modulo DMA (que solo realiza su funcion de mover bytes), si la memoria RAM esta saturada y ve que el proceso se bloqueo por alguna razon (espera de E/S), lo elimina de la ram transladandolo a la memoria swap, remplazando el lugar en la RAM del primer proceso por otro proceso externo. El problema es que cuando el modulo DMA termine de leer los bytes del dispositivo, los guardara en la misma posicion de memoria que le indicaron (donde esta el nuevo proceso), pisandolo y corrompiendolo.
- En resumen:
- Proceso pide lectura de bytes.
- Se activa el DMA "tonto".
- Se bloquea el proceso.
- El planificador quita al proceso de la ram.
- El planificador añade un nuevo proceso en el mismo lugar.
- El DMA termina de recibir los datos y los coloca en la direccion de memoria del nuevo proceso.
- Se corrompe el proceso y el sistema.
Si se quiere evitar esta situacion sin buffers, se debe bloquear el proceso en la RAM si esta ejecutando una solicitud de E/S, sin embargo esto lleva a un falta de eficiencia terrible si tienes muchas solicitudes E/S lentas.
Para solucionar esto nace el buffer, este consiste en:
- Se guardan los bytes entregados por el DMA en un bloque de ram protegido por el kernel.
- El planificador puede quitar al proceso si lo ve necesario debido a que los bytes recolectados se guardan en el buffer del kernel.
- Cuando el proceso vuelva, y se cargue en cualquier otra direccion de ram, el kernel realiza una operacion atomica para cargarle los bytes que recolecto.
Gracias a esta tecnica, la consistencia del sistema queda segura.

- **Doble buffer:** Existe un metodo de doble buffer que se usa actualmente.
	- Consiste en dividir el buffer entregado por el kernel en 2 partes.
	- El kernel recibe los datos del DMA y los almacena en un buffer.
	- Cuando termina, interrumpe a la CPU para que procese los datos recolectados.
	- Mientras hace eso, el DMA carga el resto de datos en el buffer 2.
	- Y cuando la CPU termina de procesar los datos del primer buffer, procesa los datos del siguiente.
	Esto permite que el proceso no se quede esperando estando bloqueado, y pueda estar procesandose la mayor parte del tiempo, eliminando los tiempos muertos.
	Se eliminan los tiempos muertos de transferencia intermedia.

#### Algoritmos de planificacion de disco:
Estos algoritmos se basan en 3 variables fundamentales, que determinan cuanto se tarda en buscar informacion en unidades externas.
Esto se basa en discos rigidos (con plantillos).
- Tiempo de busqueda (seek time):  El tiempo necesario para mover el brazo al lugar indicado del disco.
	- Exige mucho tiempo debido al acto de tener que moverlo fisicamente.
	- Es la variable mas critica del proceso debido a esta desventaja fisica.
- Retardo rotacional: Es el tiempo que tarda el disco en girar para obtener la informacion deseada, que puede agravarse si esta en la el lado opuesto donde lee el brazo.
- Tiempo de transferencia: Mide el tiempo que pasa desde que el primer byte fue recuperado por el cabezal, hasta el ultimo-
	- Incluye tambien el envio de datos al controlador.

**Existen 4 algoritmos principales:** Estos algoritmos son utilizados para decidir que dato se lee primero en el disco.
- **FIFO:** El mas justo, sigue el orden estricto en el que llegaron las solicitudes. (Facil de implementar)
- **SSTF:** Busca la operacion que este mas cerca del cabezal, permite reducir el movimiento, pero aumentar los problemas de inanicion de procesos que nunca se atienden. (Rapidas lecturas)
- **SCAN:** El brazo del disco se desplaza de un lado al otro, recolectando todos los datos importantes que encuentre. Cambia la direccion solo al llegar al limite. Limpia el disco de forma ordenada. (Evita inanicion)
- **C-SCAN:** Atiende solicitudes de una sola direccion, una vez que llega al final, ejecuta un viaje rapido sin leer nada, permite uniformidad en los tiempos de espera, pero es el mas lento. (Justo, tarda lo mismo para todos)
#### RAID:
Es un metodo donde se combinan multiples discos en uno solo en busca de aumentar la velocidad.
El RAID parte de 3 puntos fundamentales.
- **Un unico espacio logico (Mapeo logico unificado):** Para el sistema operativo, no existen 3 discos diferentes, existe un gran espacio unificado. 
	- Corresponde a un conjunto de unidades fisicas de disco, donde el SO lo trata como un unico dispositivo logico.
- **Distribucion de datos (Striping):** Los datos se escriben en bloques que se distribuyen a lo largo de todos los discos disponibles.
	- Los escribe de forma aleatoria.
	- El rendimiendo llega cuando al querer leer una archivo grande, este es buscado por todos los discos a la vez.
- **Redundancia por paridad:** Consiste en la capacidad redundancia, donde si un disco falla, los archivos se pueden obtender del otro.
	- No consiste en una simple copia, para niveles altos como RAID 5, se utiliza la paridad y operaciones como XOR para idenitifica que bits se encontraban en el disco que se descompuso.
	- De esa forma, realizando operaciones matematicas se puede determinar el contenido del disco roto sin necesidad de duplicar datos.

**Niveles de RAID:**
- 0: Distribucion de datos: los bloques que representan a los datos se reparten en todos los discos secuencialmente. Es muy eficiente en lectura pero inseguro relacionado a las fallas en los discos.
- 1: Espejo, Consiste en duplicar bit por bit los datos de un disco en el otro, permitiendo lecturas rapidas al leer de ambos, y seguridad ante la falla de uno de los discos, el problema es el desperdicio criminal de espacio.
- A partir de aqui son diferentes combinaciones de estas dos.
- 5: Paridad mediante compuertas XOR, donde se distribuye la paridad a lo largo de una serie de discos, gastando el total de un solo disco de almacenamiento repartido en todos los discos, util para servidores.
- 6: Una actualizacion del RAID 5, donde en vez de utilizar una ecuacion de paridad, se utilizan dos funciones de paridad diferentes. Estas se distribuyen a lo largo de los discos, permiten resiliencia abosluta al poder romperse la mitad de los discos y recuperar la informacion, sin embargo requiere como minimo 4 discos.
- 10: Combinas el RAID 1 con el RAID 0, agrupas discos de a pares, y luego a esos pares los distribuis a lo largo de todos los discos. Termina siendo super seguro y eficiente en termino de velocidad, pero costoso en terminos de almacenamiento redundante.

#### Cache de disco:
Por mas algoritmos que utilices, el disco sigue ocupando milisegundos de lectura por su situacion fisica.
Debido a esto, la forma mas rapida de obtener los datos, es no ir al disco si no es necesario.
Para esto se idea el cache de disco, encargado de recolectar los datos segun el principio de cercania, para no tener que acceder a un proceso lento como la busqueda en disco.
**Existen 2 tipos ya vistos:**
- Cache de la CPU, donde se guardan en el cache integrado a ella.
- Cache de disco: Un cacho de ram que se utiliza para almacenar datos relevantes extraidos del disco.
**Exito de cache:** Se encuentra el dato en la cache, no se accede al disco.
**Fallo de cache:** Se busco en la cache y no se encontro, se busca en el disco.

**Algoritmos de remplazo de la cache:**
Vistos en arquitectura, consiste en algoritmos que remplazan los datos de la cache cuando esta esta llena, parten de 2 principales:
- **LRU:** Se identifica cual es el dato menor utilizado recientemente, y se remplaza por el nuevo. (Se remplaza el que menos se utilizo recientemente). Mantiene a los visitados recientemente.
- **LFU:** En vez de medir el menos reciente, se mide el que menos accesos tiene, osea la frecuencia de acceso al dato se registra, y cuando se debe remplazar, se elige el que menos accesos tenga. Mantiene a los mas frecuentados.

## Sistemas distribuidos
Consiste en como funciona la interconexion de multiples dispositivos.
Salto brutal en la computacion: Se paso de tener una supermaquina hiper costosa que ejecutaba 1 instruccion por segundo, a tener microprocesadores comerciales que resultan economicos para la astronomica cantidad de instrucciones que pueden realizar por segundo: mas de 10 millones.
- Este salto fue posible debido a avances clave en la tegnologia, la colaboracion de componentes y materiales clave.
- Hoy en dia la idea de una "super computadora" (hiper mainframe) quedo obsoleta, debido a que comprando multiples equipos pequeños conectados entre si, se obtiene una potencia mayor o similar. Por una fraccion del costo.

#### Formacion del sistema distribuido
Para la formacion de un sistema distribuido se deben poder comunicar multiples equipos entre si:
- Muchas maquinas con diferentes componentes al mismo tiempo y de forma coordinada.

Para eso, se plantearon 2 inventos clave:
- **Redes de area local (LAN):** Tegnologia de conexion de alta velocidad y bajisima latencia para distancias cortas. Permitiendo un rendimiento masivo ideal para clusters (grupo) de computacion locales.
	- Ethernet, WI-FI.
- **Redes de area amplea (WAN):** Estas tegnologias compartes distancias inmensas (ciudades, paises o el planeta). Tienen mayor latencia y menor velocidad debido a que para lograr estas grandes distancias, necesitan el enrutamiento, osea conectarse a multiples nodos hasta llegar al destino.

#### Ventajas y desventajas de los sistemas distribuidos:
Los sistemas distribuidos permiten a un grupo de equipos con hardware independiente, convertirlo en un unico gran equipo.
- **Nivel hardware:** Cada computadora procesa segun su logica interna, sus propios buces, memoria, procesador. No comparte memoria con ninguna otra maquina.
- **Nivel de software:** El software se encarga de organizar a estas computadoras de una forma elegante para poder distribuir una tarea entre todos estos equipos, dispersando las tareas para maximizar el poder de computo conjunto y convirtiendolo en un sistema potente. El programa, o instruccion no sabe que equipo lo esta procesando, para el es un unico gran equipo.

**Ventajas:** 
- **Poder de calculo:** Al combinar multiples procesadores (miles) comerciales en un unico sistema distribuido, obtenes una potencia de calculo brutal, que supera por ampleo margen a cualquier supercomputadora. Y por una fraccion de su costo.
- **Desentralizacion y tolerancia a fallas:** El poder de calculo se distribuye por multiples equipos en diferentes lugares (incluso en regiones diferentes), permitiendo una resiliencia abosluta ante fallos especificos en alguno de los equipos, cosa que una super mainframe central, provocaria una falla total. En los sitemas distribuidos, la falla en un equipo no bloquea a toda la red. Todo se maneja por nodos.
- **Escalabilidad simple:** En caso de necesitar mas procesamiento, en una mainframe deberias cambiar componentes fisicos, siendo costoso: Escalabilidad vertical. En los sistemas distribuidos basta con compra otra computadora comercial, mucho mas barata que el nuevo hardware de una mainframe, y se obtiene el rendimiento necesario: Escalabilidad horizontal/modular.
	- Principalmente permite facilitar la escalabilidad del sistema, sin tener que remplazar el sistema ya construido.
- **Se comparten los datos facilmente:** Cualquier base de datos masiva, periferico caro, o archivos especificos de configuracion, pueden ser solicitados por cualquier nodo de la red, debido a su naturaleza unificada y colaborativa. Cualquier nodo puede acceder a la informacion de forma directa, sin necesidad de depender de un nodo central.

**Desventajas:**
- **Software distribuido:** Se debe ajustar el software a un dispositivo con sistema distribuido, donde ya no se puede utilizar una unica memoria central para ejecutar el programa, sino que se debe adaptar a que el programa se pueda particionar en cientos de procesos diferentes con memoria repartida en cientos o miles de maquinas. Se debe adaptar para que la comunicacion pueda fluir entre maquinas.
- **Dependencia de la red:** La potencia de la red de comunicacion es el nuevo bus de datos. Si ocurre alguna falla con esta red de comunicacion, el sistema distribuido se fragmenta. La velocidad depende de las conexion entre dispositivos.
- **Acceso a la informacion:** Al estar todos los equipos interconectados, las vulnerabilidades escalan exponencialmente, debido a que se debe tener en cuenta las vulnerabilidades de cada equipo, y el filtrado de datos personales, se debe lidiar con encriptacion, autenticacion, y denegaciones que permitan una comunicacion de equipos segura, siendo resiliente a ataques de nodos maliciosos.

#### Aftracciones: Transparencia.
- **Localizacion:** El usuario accede a el de forma comun a la informacion, independientemente del nodo en el que este, y el sistema operativo le oculta cual es la direccion real de IP del equipo donde provino ese inodo. El usuario solo sabe que el sistema lo tiene, no sabe donde exactamente lo almacena, osea en que equipo.
- **Migracion:** Los recursos se puede transladar entre equipos a voluntad sin mutar su nombre. Si un equipo esta saturado, el SO puede agarrar una parte o el proceso entero y pasarlo "en caliente" a otro dispositivo, la aplicacion seguira llamandolo e interactuando de forma comun, pero por atras ese proceso cambio de equipo. El nombre del proceso no cambia, solo se traslada.
- **Replica:** Se clonan archivos criticos para aumentar la velocidad y seguridad. Al un nodo necesitar este archivo, buscara al nodo mas cercano que lo tenga. Comunmente hablando de servidores. Esto permite tanto rapidez como resiliencia para mantener los datos. El usuario no puede determinar que equipo le envio el archivo, ni tampoco sabe cuantas copias hay, el solo ve el unico archivo.
- **Concurrencia:** Se permite compartir y modificar archivos en simultaneo entre 2 o mas equipos, el SO se encarga de gestionar los bloqueos y la consistencia de los cambios, aunque los equipos esten lejanos entre si. Dando la sensacion de que cada individuo tiene exclusividad en el archivo.
- **Paralelismo:** Las actividades pueden dividirse en multiples subactividades. Cuando un proceso se debe ejecutar, este se puede dividir en multiples subprocesos que se ejecutaran individualmente en cada equipo de la red, esto permite un procesamiento en simultaneo, y genera un nivel de velocidad y eficiencia brutal, sin que el usuario sepa que esta pasando internamente. EL resultado es un procesamiento fluido y veloz.

#### Aspectos de diseño:
- **Flexibilidad:** Se define como que tan facil es agregar, modificar o quitar servicios del sistema.
	- A medida que el cluster avanza y crece, esto se vuelve mas complejo.
	- Se plantean 2 estructuras para abordar esta situacion:
		- **Microkernel:** Todos los servicios externos al kernel basico funcionan fuera del espacio del usuario, como servidores independientes.
			- Se busca llevar al kernel a su minima expresion, donde solo es el encargado de administrar la memoria, hilos y poco mas.
			- Todos los servicios como el sistema de archivos, drivers, permisos corren de forma independiente al kernel.
			- Util para los sistemas distribuidos, debido a que permite resiliencia y flexibilidad en los nodos. Permite modificar y actualizar diferentes servicios de forma directa sin tener que apagar el nodo.
		- **Monolitico:** El kernel funciona como un unico binario con todos los servicios.
			- Esto permite una velocidad brutal al no tener que esta gastando operaciones de contexto y comunicacion de servicio.
			- Provoca dependencia, debido a que si un servicio o proceso falla, entonces todo el kernel falla.
			- La rigidez de este formato provoca que no se pueda actualizar los servicios con tanta facilidad, debido a la necesidad de modificar el nucleo del kernel.
- **Confiabilidad:** El sistema debe ser capaz de delegar las tareas si un nodo esta ocupado.
	- Esto se logra en base a 2 metricas.
		- **Disponibilidad:** La la fraccion de tiempo que el sistema esta disponible y accesible para el usuario.
		- **Tolerancia a fallas:** El sistema debe ser capaz de arreglar los errores criticos en tiempo real. Si un nodo que esta procesando una operacion falla, el SO debe poder extraer el contexto de la operacion y pasarle esa misma tarea a otro nodo disponible.
- **Desempeño:** Depende enormemente de la velocidad de la red, si mover los datos de un nodo a otro tarda milisegundos, esa operacion se debe optimizar al maximo para que sea lo menos costosa posible en tiempo.
	- Si el sistema depende de comunicarse constantemente con los otros equipos en cada milisegundo, una velocidad de transmision mas lenta que eso, provoca un cuello de botella terrible.
	- Se habla del concepto de granularidad: Elegir el punto medio ideal.
		- Grano fino: Dividir el proceso en subprocesos independientes lo mas pequeños posibles, esto permite un paralelismo absoluto, pero a costa de sufrir la latencia de la comunicacion (latencia).
		- Grano grueso: Lo contrario, dividis el proceso en partes robustas y pesadas, llevando a que cada equipo procese una gran tarea y se envien un mensaje de confirmacion al finalizar. Esto permite minimizar la latencia pero descarta la ventaja del paralelismo.
#### Comunicacion entre dispositivos:
La comunicacion entre los diferentes dispositivos debe seguir reglas rigidas para coordinarse de forma correcta. Para ello se plantean los pasos que se deben realizar para la comunicacion y los pilares del protocolo efectivo.

**Pasos obligatorios (Capas):** Pasos que deben realizar las computadoras independientes para poder comunicarse efectivamente.
- **Fisica/red:** Activa el enlace fisico (activar la comunicacion de los datos) e informa la identidad del destinatario (IP).
- **Estado:** Verifica el destino. Debe estar encendido y listo.
- **Aplicacion:** Validar la aceptacion del programa receptor. Que el otro dispositivo de la red lo acepte para la transmision. El demonio del dispositivo receptor debe estar cargado y listo para procesar ese envio.
- **Formato:** Traducir arquitecturas binarias por si son incompatibles entre si. Si las dos maquinas tienen diferente sistema binario, entonces alguna de ellas debe aplicar la funcion de traduccion para esa arquitectura.

**Pilares fundamentales del protocolo:**
- **Sintaxis:** El como se dicen las cosas, el formato de los datos, la estructura del paquete, codificacion de señales, etc...
- **Semantica:** El que significan las cosas. Especifica el significado de cada patron de bits y que accion se debe accionar la CPU.
- **Temporizador:** Es el cuando se dicen las cosas, se debe poder sincronizar los dispositivos en tiempo y en flujo de datos (control de flujo). Una correcta temporalidad se adapta a las limitaciones de cada maquina.

#### Middleware:
Es el servicio de los sistemas distribuidos.
El middleware permite mediar entre el usuario y el cluster de equipos. Esto permite que las aplicaciones se aftraigan de manejar la logia de los sistemas distribuidos, y que solo ejecuten instrucciones generales. EL middleware se encarga de organizar las maquinas para poder ejecutar esas instrucciones de forma efectiva y sin complicar a la aplicacion.
El middleware se ve como una "API" de alto nivel en el sistema.
Es un conjunto de procesos y mecanismos internos propios de los sistemas distribuidos, que en conjunto colaboran para permitir un procesamiento eficiente y efectivo.
![[Pasted image 20260630141254.png]]

#### Pasos de mensajes:
**Concepto:** El procesador emisor ejecuta el modulo de paso de mensaje, el cual empaqueta la informacion en una estructura basica (idProceso|mensaje), y lo envia por la red de transporte hasta el proceso receptor del mensaje. Donde este lo recibe y sube a la aplicacion.
Esto sucede debido a que si un procesos e esta ejecutando en 2 equipos diferentes, va a necesitar comunicacion entre ambas partes, ahí nacen los protocolos de mensajes y el sincronismo.

Aqui entran 2 protocolos miticos de la transmision de datos: TCP y UDP.
**TCP: Fiable** Consiste en un protocolo de verificacion, la parte receptora y emisora estan pendientes de que se transmitio el dato correctamente, si la parte receptora recibio el dato corrupto (codigo de redundancia), entonces pide a la receptora que se lo envie nuevamente. Es la mas "segura", ya que permite que los datos sean enviados correctamente.
**UDP: No fiable** Consiste en el desentendimiento de los dispositivos, el emisor envia la informacion y se desentiende del receptor, y el receptor recibe la informacion y la interpreta como puede. Esta mecanica, a pesar de parecer poco confiable, resulta simple y efectiva cuando el tiempo de transmision es critico, y no se puede andar perdiendo tiempo entre verificaciones.
 
**Sincronismo del emisor:**
Se define como la maquina emisora se comporta cuando envio el mensaje, esto se divide en dos categorias principales:
- **Bloqueante:** Consiste en la recepcion de un ACK.
	- Consiste en que cuando el proceso necesita enviar un mensaje, este se bloquea, se envia el mensaje por la red, y se espera a que vuelva la confimacion del mensaje ACK (acuse de recibo). cuando se recibe esa interrupcion del ACK, se despierta el kernel y regresa el proceso a la cola de listos.
	- Es seguro y facil de programar.
	- Pero la CPU pierde millones de ciclos de CPU culpa de esperar ese mensaje.
- **No bloqueante:** No se bloquea al proceso esperando el mensaje.
	- El proceso entrega los datos al buffer del kernel. Una vez hecha la syscall por parte del proceso, el kernel le devuelve el control a la CPU. El proceso se sigue ejecutando en sus proximas lineas de codigo. Y en paralelo la "placa de red" o el dispositivo indicado se encarga de transmitir los datos.
	- Permite una velocidad y aprovechamiento de la CPU totales.
	- El problema llega cuando fallo algo en la transmision de los datos. Al haber avanzado mucho en las lineas de codigo del proceso, el programa debe estar preparado tecnicamente para en cualquier momento de este identificar los datos obtenidos y cuales faltan para volverlos a pedir.
En ambas el encargado de preparar el mensaje, es el programador.
#### Procedimiento remoto RPC:
Este protocolo busca simplificar las complicaciones de la emision de mensajes, para q al proceso le parezca lo mismo llamar a una funcion que esta en otro dispositivo o que esta en la misma maquina.
El objetivo es la transparencia de localizacion absoluta, no importa en que parte estes ni que tengas a mano, el proceso puede ejecutarse como si estuviera en una unica maquina completo.
Esto permite que el software no tenga que estar diseñado para tener que volver hacia atras en caso que la llamada generara un fallo. Deja de obligar al programa a ser desarrollado con los parametros "enviar()" y "recibir()".
**El proceso RPC se divide en 2 etapas:**
	El objetivo de este protocolo es "engañar" al proceso extrayendo unicamente los datos del parametro y traer el resultado, no todo el bloque de informacion.
- **Ida:** 
	- El proceso ejecuta una funcion con un cierto parametro.
	- El esqueleto local o RPC del cliente se activa y actua como si fuera la funcion, recibiendo el parametro.
	- Luego el hilo del proceso se bloquea y se envia el parametro mediante el SO por la red hacia el proximo dispositivo (mandandolos de forma estructurada: serializacion).
- **Vuelta:**
	- El receptor, recibe el mensaje y lo sube al esqueleto local o mecanismo del RPC. Se desarma los datos crudos y se arman los parametros de interes.
	- Se llama a la aplicacion que se encuentra en ese dispositivo que contiene la funcion real.
	- La funcion calcula los datos, y devuelve la informacion hacia el emisor.
	- Cuando el emisor recibe la informacion, debloquea al hilo del proceso para que continue con su logica. El proceso lo ve como una respuesta local. Se aftrae la complejidad de la comunicacion.
La principal desventaja de este metodo es lo que le pasa al metodo basico bloqueante: Se bloquea el proceso hasta que la respuesta venga de vuelta.
Sin embargo la principal diferencia es la facilidad que se le brinda al programador, este metodo RPC se encarga de manejar toda la "burocracia" del SO distribuido, permite abrir la conexion, estructurar los arrays, forzar el envio, manejar errores de transmision, todo eso lo aftrae el RPC, brindandole una interfaz limpia y simple al progrmador, sin tener que encargarse de toda esta logica.
- Cosa que en el procedimiento de bloqueo, caia en manos del programador.

¿Esto no lo realizaba el middleware? Si, lo realiza el middleware en conjunto al RPC, el RPC ES PARTE del middleware, el middleware se encarga de organizar el RPC para que el hilo no termine siendo bloqueado, sino que se saltee la instruccion en especifico y se delege a otras instrucciones independientes de ese proceso. La instruccion critica queda congelada.

![[Pasted image 20260630144247.png]]


## Seguridad:
Consiste en como se protege el hardware y los sistemas de todo tipo de ataques y vulnerabilidades.

#### Tipos de vulnerabilidades:
**Fisica:**
- Consiste en las vulnerabilidades fisicas.
- Existen prevenciones de todo tipo:
	- Control de acceso perimetral: Consiste en no permitir que las personas accedan al area critica.
	- Protección ambiental: Evitar el sufrimiento del silicio mediante refrigeracion y metodos especificos para apagar silencios.
	- Respaldo energetico: Tener un respaldo energetico para que no se apagen los dispositivos.

**Logica:**
- Consiste en garantizar la seguridad interna, busca minimizar vulnerabilidades y por lo tanto ataques que se provoquen via software.
- Existen 3 tipos principales:
	- **Autenticacion:** Consiste en mecanismos que permitan autenticar la identidad del usuario.
	- **Control orientado a datos:** Consiste en asignar controles a los datos especificos.
	- Criptografia: Consiste en un metodo de cifrado que permita ocultar los datos bajo algoritmos de encriptacion.

#### Requisitos basicos:
Consiste en 4 conceptos fundamentales:
- **Confencialidad:** Consiste en que la informacion no sea expuesta a personas que no deben ver los datos. Normalmente se utiliza criptografia.
- **Integridad:** Los datos solo puedan ser modificados por los usuarios autoridad.
- **Disponibilidad:** Busca que los usuarios tengan la capacidad de acceso a los recursos cuando lo necesiten.
- **Autenticacion:** Garantizar que un usuario/proceso/entidad es quien dice ser, verificarlo de forma infalible.
	- El atacante se le llama enmascaramiento.

#### Tipos de peligro:
- **Interrupcion:** Se corta la disponibilidad, el flujo de datos deja de entregarse. El objetivo es realizar una denegacion de servicio, osea en sintesis interrumpir la entrega de datos de forma adecuada.
- **Intercepcion:** Consiste en obtener informacion sin provocar ningun daño en los sistemas, solo observar y recolectar informacion.
- **Modificar:** Un ataque activo, consiste en interceptar los datos, modificarlos y regresarlos para que llegen al destino en estado modificado.
- **Fabricacion:** Consiste en que un usuario no autorizado se hace pasar por un usuario legitimo de la red, provocando que se trasmita informacion nueva (fabricada) provocando problemas en el sistema al trasmitir informacion problematica para el sistema.
	- Se conoce como enmascaramiento.

#### Seguridad relacionada a los componentes clave de un sistema.

| Componentes  | Disponibilidad                                                            | Privacidad                                                                                                                   | Integridad/Autenticacion                                                                                                                          |
| ------------ | ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Hardware     | Equipamiento robado fisicamente                                           | No hay directamente                                                                                                          | Tampoco hay directamente                                                                                                                          |
| Software     | Borrar las aplicaciones, quitar el acceso a los usuarios.                 | Consiste en robar datos sensibles de las aplicaciones o organizacion.                                                        | Modificar el programa para provocar su fallo mediante un datos/metodos externos. Se busca cambiar el comportamiento del software.                 |
| Datos        | Borrar archivos o denegar los permisos de otros usuarios a esos archivos. | Lectura no autorizada, eso provoca un espionaje de datos sensibles.                                                          | Modificar o crear nuevos archivos criticos para el sistema. Afectan directamente a los usuarios propietarios.                                     |
| Comunicacion | Consiste en que la transmision de los datos este interrumpida o corrupta. | Se observan como se trasmiten los datos, permitiendo idenitificar ciertas vulnerabilidades o identificando conexiones clave. | Modificacion, borrado, en sintesis alteracion del mensaje para el destino, permitiendo crear mensajes falsos o duplicarlos para fines malisiosos. |
#### Tipos de ataques:
- **Pasivos:** Consiste en la lectura de la informacion para x fin, corresponde a la parte mas basica de un ataque pero no por eso deja de ser critica.
	- Analizar trafico, leer documentos.
- **Activos:** Consiste en alterar el material directamente, provocando fallos o modificaciones provocadas a proposito con fines malisiosos.
	- Reenvio, modificaciones denegaciones de servicio, enmascaramiento, etc...

#### Proteccion:
Es el mecanismo que utiliza el sistema operativo para ser resistente a amenazas externas.
**Multiprogramacion:** Aqui los procesos se ejecutan unos milisegundos en la CPU, eso lleva a que cualquier programa malisioso pueda utilizar ese beneficio para perjudicar el equipo de alguna forma.
- Por esa razon para que este metodo se pueda utilizar correctamente, se implementan reglas estrictas para que un proceso malisioso o mal programa no pueda modificar datos de otro proceso, pueda ocupar tiempo de procesamiento por demas provocando inanicion, leer datos sensibles en el dispositivo ni tampoco borrar otro proceso, etc...
- La matematica de la proteccion no es un añadido, es parte del diseño del sistema, ya que sin proteccion, el sistema no funciona.

**Recursos a proteger:**
- **Memoria:** Los procesos utilizan la misma ram fisica, se deben dividir de forma estricta para no pisar los datos de otros procesos.
- **Dispositivos E/S:** Se protege las llamadas a los dispositivos de E/S, debido a que dos o mas procesos pueden enviar llamadas al mismo tiempo, eso provoca que se pueda corromper la señal. el SO restrigen esto, provocando que los procesos no se superpongan entre si.
- **Programas:** El SO utiliza metodos jerarquicos para que los binarios (librerias) disponibles para todos los procesos, no sean alterados por un proceso malisioso.
- **Datos:** Los archivos, bases de datos, y diferentes tipos de informacion son criticas para los procesos que la utilizan, una modificacion o lectura no autorizada de estos datos puede provocar errores o vulnerabilidades graves, por eso el SO implementa perfiles basado en roles para identificar atomicamente si un proceso tiene un ID autorizado antes de permitirle interactuar con los datos. El SO administra esto mediante las Listas de control de acceso ACL.

**Niveles de proteccion:**
El sistema operativo maneja un nivel de granularidad entre los permisos asignados, no es un "todo o nada", se regula la proteccion en base a los niveles.
**Nivel hardware:** 
- Plantea la diferencia de modo usuario y modo kernel. Utiliza la logica de nivel maximo de privilegio al SO, y un nivel basico con multiples funciones sensibles deshabilitadas para los modo usuario.
**Nivel usuario/proceso:** Se identifica mediante kernel cual es el propietario de la orden, se puede dar permiso de lectura y prohibicion de escritura al mismo archivo, etc... Son protecciones internas a nivel del usuario.

#### Proteccion a memoria:
Consiste en el concepto explicado de la multiprogramacion, se exponen diferentes metodos para la proteccion de la memoria de otros procesos.
- Se exige que solo se pueda acceder a la memoria de otro proceso si esta explicitamente compartida.
- Se fija en los permisos rwx, si se quiere ejecutar alguna funcion que no es compatible con los permisos asignados, se deniega la instruccion.

**Control de acceso orientado a usuarios:** 
Consiste en un control para permitir el paso al sistema o no.
- **Identificacion usuario/password:**
	- Se ingresa un usuario y contraseña, que se entregan en formato de texto plano, se aplica una funcion criptografica y posteriormente se verifica si es valida comparandola con el hash almacenada en la base de datos protegida del sistema.
- **Single sing-on: (SSO):**
	- Funciona como una "Cookie", en sintesis te logeas una unica vez, luego el sistema te verifica y genera un "Token" que utilizas para verificarte las proximas veces. El token es una clave criptografica firmado digitalmente.

**Control de acceso orientado a objetos:**
Este enfoque determina que recursos puede manipular y de que forma el usuario que entro al sistema validando su identidad.
- **Perfiles RBAC:**
	- Se le asignan los permisos a los roles especificos, y estos roles se le asignan a los usuarios.
	- El enfoque esta en los usuarios.
- **Listas de control de acceso ACL:** 
	- Cada objeto del sistema (archivo) tiene una lista de los usuarios autorizados con sus permisos correspondientes para interactuar con el objeto.
	- Ese archivo extra, o lista se le llama ACL.
	- El enfoque esta en el recurso.
- **Tickets (Kerberos):**
	- Sirve especificamente para los sistemas distribuidos.
	- Consiste en un verificador externo KDC, que hace de intermediario para verificar que ese dispositivo que esta queriendo acceder a la informacion, realmente es quien dice ser.
	- El usuario en cuestion pide una verificacion (ticket de acceso) a esta entidad separada llamada KDC, esta le devuelve un ticket comprobando que su credencial es real, y se lo envia al dispositivo de destino para verificar realmente quien dice ser. Todo se maneja por encriptacion.

#### Intrusos y tecnicas de intrusion:
Se expande los tipos de intrusos junto a sus tecnicas para la instrusion.
**Intrusos:**
- **Enmascarados:**
	- Utiliza la cuenta de un usuario legitimo para meterse en el sistema.
	- Su estrategia no es romper el kernel ni su seguridad tecnica, sino que aprovecharse de la vulnerabilidad del usuario.
	
- **Trasgresor:**
	- Un interno autorizado que realiza acciones malisiosas.
	- Es alguien autorizado por el sistema, pero que sus intenciones son malisiosas para este, accediento a los recursos para fines negativos este autorizado o no.
	
- **Clandestino:** 
	- Domina el modo administrador para encubrir su rastro en el sistema, puede ser un agente interno o externo al sistema.

**Tecnicas y relacion:**
- Ingenieria social: Manipulacion psicologia o de cualquier tipo al usuario autorizado para obtener sus credenciales.
	- Es utilizada principalmente por el enmascarado.

- **Eliminacion de registros/bitacora:** Los intrusos pueden aprovecharse de los privilegios que obtuvieron para borrar su rastro y permitir pasar desapercibidos.

**Buenas practicas**
- **Proteccion de constraseñas:** El utilizar contraseñas muy seguras (complejas), o obligar a que los usuarios se logeen como usuarios planos sin privilegios, permite evitar a los enmascarados y los transgresores, debido a que se le quita su principal arma contra el sistema, los privilegios.
- **Bitacoras:** Se utilizan las bitacoras para identificar quien hizo cada cosa, provocando que toda actividad de los intrusos quede registrada en el sistema.
	- Las bitacoras solo deben ser accesibles por el kernel.
	- Esto frenta principalmente a los transgresores y enmascarados.


#### Malware (Software Malicioso) y antivirus
Son procesos y aplicaciones que buscan explotar las vulnerabilidades del kernel.
Se clasifican segun 2 variables criticas:
- Si necesita un programa huesped para sobrevivir.
- Como se propaga a traves de los buses de datos y redes.

**Backdoors:**
- Consiste en una "vulnerabilidad" obviada por desarrolladores que provoca saltarse las rutinas de verificacion y autenticacion del sistema.
- Se te entrega control absoluto.

**Bomba logica:**
- Consiste en un programa pasivo inicialmente, que espera a un detontante particular para corromper el sistema.

**Troyano:**
- Es un programa que fije ser inofensivo (programa completo), busca ganarse la confianza del usuario para ser ejecutado y provocar que se le delege el control al programa.

**Virus:**
- Consiste en un programa que se va propagando a lo largo de la maquina, esto provoca que el codigo malicioso se propage por diferentes archivos del dispositivo, provocando que al ejecutarlos se propage aun mas. Necesita un huesped.

**Gusanos:**
- Es un programa autonomo que no necesita huesped. Principalmente se utiliza en los sistemas distribuidos, donde escanea las maquinas buscando vulnerables (que esten en modo falla o reinicio), cuando encuentra alguna entra en ella aprovechando el fallo, levanta su propio proceso, escanean la red y envian sus replicas a todos los nodos posibles, provocando una propagacion exponencial.

**Zombie:**
- Es un programa que proviene de un externo, como un troyano, este se almacena en el dispositivo con los privilegios necesarios pero inactivo. Este programa esta conectado a un servidor central, que al pedirlo, realiza una llamada generalizada a todos estos dispositivos infectados para, comunmente, un ataque DDOs distribuida. En busca de tirar la red de comunicacion marcada como objetivo.




## Practica
La parte practica consiste en encriptar y desencriptar archivos mediante gpg.
Phil Zimmermann hizo el software de encriptacion PGP.
Existe una copia codigo abierto llamada OpenPGP.
Que muto en una implementacion de GnuPG.

Comandos disponibles:
-c: Cifrado simétrico
-a: Salida ASCII (BASE64)
--gen-key: Generar par de claves
--export: Exportar claves
--import: Importar claves
-kv: Ver claves en el keyring
-kvc: Ver huella (fingerprint) del keyring
--encrypt: Cifrar con criptografía asimétrica
-r: Especificar destinatario
-s: Firmar digitalmente
-b: Firma separada
--clearsign: Firma sin cifrado
#### Se describen las operaciones posibles a realizar con este software de encriptacion:
**Invocar el programa y acceder a la ayuda.**
- man gpg
- Listado de opciones
**Cifrar y descifrar documentos con criptografía simétrica y asimétrica.**
- Simetrico:
	- gpg -c archivo.txt -> genera -> archivo.txt.gpg
	- gpg -ca archivo.txt -> genera -> archivo.txt.gpg
	- Se solicitara una constraseña.
- Asimetrico:
	- gpg -a --encrypt documento.txt
	- Para varios destinatarios: gpg -a -r Paco -r Pepe --encrypt documento.txt
	Se decifra ambos mediante: gpg documento.txt.asc -> Osea el gpg y el archivo cifrado.
**Crear y compartir claves públicas y privadas.**
- Crear clave publica y privada.
	- gpg --full-generate-key
	- Se genera un ID de usuario y una constraseña.
- Exportar clave:
	- gpg -a --export "Tu Nombre" > nombre_apellido.asc
- Importar clave recibida de otra persona:
	- gpg --import clave_de_otro.asc
- Ver claves importadas:
	- gpg -kv
**Firmar digitalmente documentos y verificar firmas**
- Crear firma:
	- gpg --clearsign archivo.txt (Forma clara)
	- gpg --sign archivo.txt (Binaria)
	- gpg -b archivo.txt (separada)
- Verificar firma del documento:
	- gpg --verify archivo.txt.asc
	- gpg --verify "y el nombre del archivo cifrado y firmado".