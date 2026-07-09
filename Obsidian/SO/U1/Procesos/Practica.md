Aqui se indicaran los diferentes comandos utilizados a lo largo de la unidad para manipular procesos.
Esto se dividira en secciones, segun su uso, osea para que se usan.

### Compilar:
**C:** gcc nombre_archivo.c –o nombre_archivo_Ejecutable
	Se divide en 4 fases fundamentales: 
	- Se remplaza los #include con el contenido correspondiente guardado en el sistema, se borran los comentarios externos generando un archivo .i de C puro.
	- Se traduce el codigo C puro en ensamblador segun la arquitectura de tu procesador, generando un .s 
	- Ensamblado, donde el codigo se transforma de codigo ensamblador a codigo maquina binario, generando un .o (archivo objeto)
	- Se juntan los archivos objeto con las librerias correspondientes para hacer un unico ejecutable final.


## GUIAS:

### TP 3:
**Directivas:**
1. Crear el archivo. Ejemplo: nombre_archivo.c
2. Compilar el programa. gcc nombre_archivo.c –o nombre_archivo
3. Ejecutarlo. ./nombre_archivo
4. Identificar y analizar los resultados de los procesos padre e hijos.
5. Observar y comparar con resultados que propusieron ustedes con la salida obtenida.
Ejercicio 1:
![[Pasted image 20260517193558 1.png|225]]
![[Pasted image 20260517193619 1.png]]
![[Pasted image 20260517193726 1.png]]

Preguntas:
1. ¿Cuántas veces se imprime el mensaje?
2 veces.
2. ¿Por qué se imprime más de una vez?
Porque se clona el proceso y se ejecuta 2 veces por lo tanto la instruccion print.
3. ¿Cuántos procesos existen después del fork()?
2 procesos.

Ejercicio 2: EN EL DOCUMENTO.
Preguntas:
1. ¿Qué proceso imprime “Soy el
hijo”?
2. ¿Qué proceso imprime “Soy el
padre”?
3. ¿Qué valor devuelve fork() en
el hijo?
4. ¿Qué valor devuelve fork() en
el padre?