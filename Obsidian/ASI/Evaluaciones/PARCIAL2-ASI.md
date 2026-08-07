Aquí se expandirá la teoría y el repaso con las unidades relacionadas al segundo parcial de ASI.}

## Agenda:
**Unidad 4, 5 y la mitad de la 6 (sólo Paradigma orientado a objetos y MODP).**
- **Requerimentos.**
	- Concepto.
	- Ingeniera de requerimientos/Elicitación de Requerimientos.
	- Tipos (Concepto): Funcionales y no funcionales
- **Paradigma Orientado a Objetos.**
	- Diagrama de clases (MODP).
	- Interpretación como objetos.

### Metodología:
**Teoria:**
- Identificar tema.
- Resumir tema.
- Explicar tema y aplicarlo a un ejemplo.
**Practico:**
- Identificar caso de estudio.
- Realizar diagrama de clases correspondiente.
- Corregir caso realizado.


# Estudio

## Requerimientos:
Un requerimiento consiste en una característica que debe incluirse en un sistema. Esa condición o capacidad es necesaria para que el usuario pueda cumplir el objetivo propuesto.

### Ing. en requerimientos:
Para cumplir este objetivo se propone la ING. en requerimientos (IR)
- Propone un proceso iterativo y colaborativo con el cliente para poder determinar de forma adecuada los requerimientos del sistema.
- Se analiza el problema, documentan soluciones, se realizan modelos y verifican con el cliente.

### Tipos de requerimientos:
Existen 2 tipos principales de requerimientos:
- **Funcional:** Considera lo que el sistema deberá hacer sin tomar en cuenta la implementacion de este.
	- Ej: El sistema deberá registrar los datos del cliente.
- **No funcional:** Considera como se implementaran los requerimientos funcionales en el sistema a desarrollar. 
	- Determina las limitaciones al momento de implementar esta funcionalidad.
	- Ej: Los datos del cliente se guardan en una base de datos comunicada a los servidores de x servicio.

### Proceso de la ing. en requerimientos:
Es un proceso iterativo que depende de 4 pasos fundamentales, que luego de concluirse y llegar a un consenso, se realiza un documento llamado ERS, que permite especificar que requerimientos y funcionalidades tendrá el sistema final.

Los 4 pasos fundamentales que se realizan de forma iterativa son:
- **Análisis Factibilidad.**
	- Consiste en un análisis sobre la factibilidad del desarrollo para determinar la continuación el proyecto o cancelarlo.
	- Esto incluye 3 subtipos de factibilidad: Técnica; Económica; Operativa.
- **Elicitación.**
	- Se consultan, obtienen y organizan las necesidades del cliente. Existen múltiples métodos para obtener esta información.
	- Entrevistas, cuestionarios, observación, entre otros.
- **Especificación.**
	- En este punto, los requerimientos recolectados del cliente se detallan en un documento determinado como "Especificación de requerimientos (ERS)".
	- Sirve como documento legal para validar el desarrollo a realizar. Es la especificación formal utilizada por todo el equipo para el desarrollo y validación.
- **Validación.**
	- La validación sirve para corroborar que el trabajo y diseños realizados (Requerimientos) van acorde a lo que el cliente desea.
	- Permite la modificación o restructuracion de los requerimientos si es necesario para el cliente.
	- Es el punto final donde comienza el bucle iterativo nuevamente.
	- Existen múltiples métodos para determinar esta validación: Prototipos, animaciones, lenguaje natural, sistemas expertos, etc...


## Paradigma orientado a objetos POO.
Se refiere a interpretar todo como un objeto, con sus atributos y sus valores propios.

Se plantea este metodo en base a 2 situaciones fundamentales ocurridas en el mundo del software.

### Necesidad en el desarrollo:
En el desarrollo de software, en los tiempos actuales se vio la necesidad de desarrollar un software:
- A menor costo.
- A mayor velocidad
- Con capacidad de manejar la complejidad.
Esto llevo a la necesidad de reutilizar componentes de todo tipo.

### Revolucion de paradigma:
Debido a las necesidades de la industria, se propuso un paradigma que solucionara los problemas principales de ese momento, y permitiera mucha mayor flexibilidad.

#### ¿Que es un paradigma?
- Es una forma de entender el mundo que nos rodea, y de aftraerlo con un cierto proposito.
- “Un conjunto de teorías, estándares y métodos que juntos representan una forma de organizar el conocimiento, es decir, una forma de ver el mundo”.

#### Tipos de paradigma:
**Estructurado:**
- Consiste en un algoritmo lineal, el cual sigue pasos secuenciales.
- Se divide en procesos y datos.
- La principal desventaja es que añade mucha complejidad en softwares grandes y dificulta el mantenimiento.

**Orientado a objetos:**
- Consiste en la filosofia de que "todo es un objeto".
- Su principal beneficio es la reutilizacion y comunicacion entre entidades.
- Los objetos administran sus datos y funciones, permitiendo independencia entre ellos.
- Sin embargo el objetivo de este paradigma es integrar estos objetos en clasificaciones (clases), permitiendo integrar multiples objetos (entidades) diferentes en una misma clase de objeto general.
- Este paradigma permite reducir la complejidad al proponer una estructura de trabajo y flujo de datos mucho mas dinamico.

### POO, conceptos:
Consiste en una forma de ver las cosas, para entender un problema e identificar las entidades principales de este.
Permite reducir la complejidad al:
- Identificar la entidad principal.
- Sus caracteristicas.
- Sus acciones.
- Y se identifica como interactua con el resto de entidades.
Nace de la programacion y consiste en una coleccion de objetos discretos que encapsulan:
- Estructuras de datos.
- Comportamientos.
#### Caracteristica de los objetos:
Un objeto tiene una serie de componentes clave y los combinan en una unica entidad:
- **Comportamiento:** Las operaciones que puede realizar dicho objeto; Sus metodos.
- **Estado:** Uno o mas atributos que se le asignaron valores concretos; Sus datos.
- **Identidad:** Una propiedad del objeto que lo hace unico y diferenciable del resto; Su identificador.

#### Clase:
La clase consiste en la "clasificacion" de los objetos, visto con una analogia, se refiere al "molde" de cada objeto.
La clase permite agrupar mutliples objetos que contienen los mismos atributos pero con valores diferentes.
- Una clase puede ser "mesa", sin embargo existen multiples objetos "mesa" que contienen diferentes valores.
	- Mesa de madera, mesa de plastico, mesa de plastico con patas de aluminio, etc...

##### Componentes de una clase:
Los componentes pertenecientes a una clase son:
- Caracteristicas (Atributos, propiedades).
- Comportamientos (Acciones o metodos).

A los valores asignados a los atributos de los objetos se los conoce como "Estado".
A los atributos y metodos de estos objetos (sin valor especifico) se los conoce como "Interfaz".
Y al codigo utilizado para construir esta clase se conoce como "Implementacion".

Una clase siempre tiene metodos (Acciones) del tipo:
- Crear()
- Mostrar()

## Diagrama de clases (MODP)