### **Síntesis**

- **Definición y Modos:** El SO como administrador de "fierros" y la diferencia entre modo usuario y kernel.
- **Hardware y CPU:** Registros clave, jerarquía de memoria y cómo arranca la máquina.
- **Conceptos Centrales:** Procesos, archivos (bloque vs carácter) y la shell.
- **Entrada/Salida:** Técnicas para avisarle a la CPU que terminó un laburo (Polling, Interrupciones, DMA).
    
- **Llamadas al Sistema:** La "ventanilla" legal para pedirle cosas al kernel.
    
- **Estructuras del SO:** Desde el bloque único (monolítico) hasta las máquinas virtuales.
    
---
### **Cuestionario General: Unidad 1 - Sistemas Operativos**

#### **I. Definiciones y Modos de Ejecución**

1. **¿Qué diferencia hay entre la visión "Top-down" y "Bottom-up" de un SO?**
    Esto tiene que ver con la forma en la que se visualiza los diferentes componentes y procedimientosque se llevan a cabo en una computadora, Top-down es mirar esto desde la vitsta mas aftracta (una aplicacion), que vee al sisterma operativo como base para enviar las intrucciones, donde este ultimo es el quien se encarga de organizarlas.
    Y la vista bottom-up, propone analizar esta jerarquia desde la parte menos aftraida, que recibe las intrucciones basicas traidas por el SO y traducidas por los drivers para que el hardware trabaje correctamente con ellas.
2. **Modo Kernel vs. Modo Usuario:** ¿Por qué un proceso de usuario no puede tocar directamente el hardware?
	El modo kernel permite tener acceso y control de todos los recursos de la computadora, sin limitaciones, el SO funciona en este modo.
	EL modo usuario es un modo limitado que no permite interactuar directamente son el hardware, limitandose a intrucciones basicas o de alto nivel. El usuario no toca el hardware ya que existirian conflictos entre aplicaciones que buscar utilizar la misma parte del hardware.
3. **Abstracciones:** Nombrá qué recurso de hardware abstraen los "Procesos", el "Espacio de Direcciones" y los "Archivos".
    **CORREGIDO:** 
	    **Proceso:** Habla de un programa ejecutandose: Se le asigna cierta memoria utilizable (generica, de 0 a n); habla con el SO, es parte de el; tiene una relacion jerarquica entre los demas procesos; Se pueden ejecutar por multiples medios.
	    **Aftraccion de direcciones:** Espacio de direcciones, se le aftrae al proceso la memoria dandole una memoria "personal", este proceso utiliza una memoria virtual. Esto permite organizarla y administrarla de mejor forma. El SO se encarga de mapear (interpretar) las direcciones relativas y transformarlas en las reales.
	    **Archivos:** Se interpreata su direccion de formas diferentes, direccion absoluta, relativa, etc... Se manejan por un arbol jerarquico de diferentes directorios, estos se utilizan para organizar al archivo.
		    Existen multiples formas de archivo como: Bloque (son unidades de almacenamiento fisicas como un SSD), caracter (se reciben en rafajas, como por ejemplo el movimiento del mouse), y por utilimo (pipes)) tuberias (sirve para conectar 2 procesos, que la salida del primero sea la entrada del siguiente).

   

#### **II. El Hardware desde el punto de vista del SO**

4. **Registros del CPU:** Explicá para qué sirven el **PC** (Program Counter), el **SP** (Stack Pointer) y el **PSW** (Program Status Word).
    
5. **Jerarquía de Memoria:** ¿Por qué usamos una pirámide de memoria en lugar de tener 64GB de registros, que son más rápidos?
    
6. **El "Arranque":** Describí brevemente los pasos desde que apretás el botón de encendido hasta que el Kernel toma el control.
    

#### **III. Conceptos de SO (Procesos, Archivos, E/S)**

7. **Procesos:** ¿Qué información básica contiene el "contenedor" de un proceso para poder ejecutarse?
    
8. **Archivos:** Diferenciá un "Archivo de Bloque" de uno de "Carácter" con un ejemplo de hardware para cada uno.
    
9. **Técnicas de E/S:**
    
    - ¿Por qué el **Polling** se considera un "desperdicio" de CPU?
        
    - ¿Qué ventaja tiene el **DMA** cuando tenés que mover un volumen gigante de datos?
        

#### **IV. Llamadas al Sistema (Syscalls)**

10. **El flujo:** Cuando una aplicación llama a `read()`, ¿qué pasos sigue la instrucción antes de llegar al código del kernel?
    
11. **API POSIX vs Win32:** ¿Cuál es el equivalente en Windows de las syscalls `fork` y `execve`?
    
12. **Grupos de Syscalls:** Si quiero crear una carpeta y luego cambiarle los permisos, ¿qué llamadas al sistema debería usar?
    

#### **V. Estructuras del SO**

13. **Sistema Monolítico:** ¿Por qué se dice que es el más rápido pero el más frágil ante errores (bugs)?
    
14. **Microkernel:** ¿Qué servicios del SO se sacan del kernel y pasan a correr en "Modo Usuario"?
    
15. **Virtualización:** ¿Qué función cumple el **Hipervisor (VMM)** en este esquema?
    

---
