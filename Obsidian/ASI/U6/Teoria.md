Aqui se desarrolla la teoria de la sexta unidad de ASI. Todo lo relacionado a:
- Paradigma orientado a objetos.
- Diagrama de clases.
- Diagrama de casos de uso.
Se expandiran los temas uno a uno secuencialmente.

### FALTA
Falta por extender:
- Modelización: Importancia –Modelos.
- Máquinas de Estados. 
- Requerimientos ágiles: Historias de Usuarios y Criterios de Aceptación.
- Patrones de diagrama de clases.

---
### Paradigma orientado a objetos
Parte de la necesidad de revolucionar la industria del software, buscando mejorar los aspectos de la construccion de sistemas:
	- Mas complejos.
	- Mas grandes.
	- Mas confiables.
	- En menos tiempo.
	- Menor costo.
Se logro manejar la complejidad, aumentar la velocidad de desarrollo y reducir los costos a partir de:
- Utilizar componentes reutilizables.
- Ensamblar software a partir de componentes de multiples proveedores diferentes.
- Creando una gigantesca biblioteca de componentes.
#### Que es un paradigma:
La forma de ver y entender el mundo: Una forma de interpretar la realidad.
Consiste en nuestra propia forma de aftraccion.
Se define la palabra paradigma como: Un conjunto de teorias, estandares y metodos que juntos representan la forma de organizar el conocimiento.

### Paradigma estructurado vs paradigma Orientado a Objetos.
Pasamos de un paradigma estructurado a un paradigma dinamico y muy optimizado.

| Estructurado                          | Orientado a objetos                                         |
| ------------------------------------- | ----------------------------------------------------------- |
| Se siguen pasos                       | Componentes independientes y reutilizables                  |
| Dinamica secuencial                   | Comunicacion con colaboradores                              |
| Algoritmos lineales                   | Bloques de objeto-clase                                     |
| Divide los procesos y los datos       | Los objetos se hacen cargo de sus propios datos y funciones |
| Complejidad en software a gran escala | Permite abordar la complejidad.                             |
| Dificultad en el mantenimiento        | Mejor capacidad de mantenimiento.                           |
### ¿Que es?
Es un paradigma de la programacion.
Es una forma de entender el problema, de aftraerlo para su posterior resolucion.
- Se busca encapsular las entidades principales del problema en un objeto.
Se deben conocer las caracteristicas de estos y las acciones que realizan.
"Todo es un objeto"

Surje de los lenguajes de programacion: 
- Organiza el software como una coleccion de objetos discretos.
	- Estos objetos encapsultan: Estructura de datos y comportamiento.
- Funciona mediante la colaboracion de objetos que se comunican entre si.
El concepto se extiene al analisis y diseño de sistemas:
- Se utilizan objetos del mundo real para construir modelos.
- Los elementos que forman los sistemas del mundo real corresponde con los objetos de software.
#### Objetos: 
Son entidades del mundo real que combinan tanto estados, identidad y comportamiento.
- **Comportamiento:** Los metodos que contiene el objeto en cuestion. Osea las operaciones que se pueden realizar con ese objeto.
- **Estado:** Representan atributos que se le asignaron ciertos valores, osea diferentes "caracteristicas" con determinador valor.
- **Identidad:** Es la identidad del objeto, el identificador que lo diferencia del resto.

### Clase
Llamamos clase a los objetos que comparten caracteristicas, no necesariamente con el mismo valor.
	Ejemplo: Zapatillas: Pueden haber de un monton de tipos (objetos), pero todos pertenecen a la clase "zapatillas" por sus diferentes atributos (caracteristicas).
La clase determina las caracteristicas del objeto, sin determinar sus valores finales.
Esta compuesta por caracteristicas y comportamientos: Atributos y propiedades; Acciones y metodos.
	Determinados por el contexto del problema o escenario, osea depende de nuestr aftraccion.
**Terminologia de las clases:**
	**Estado:** Valores que tienen los atributos del objeto.
	**Interfaz:** atributos y metodos que ofrece.
	**Implementacion:** Codigo utilizado para construir las clases.

#### Resumen:
**CLASE**
- Atributos
- Comportamiento
- Responsabilidades

**OBJETO**
- Estado
- Comportamiento
- Identidad

## Especificacion de requerimentos
El objetivo de esta especificacion es guiar el desarrollo hacia el sistema correcto, teniendo en cuenta tanto la mirada de los clientes, como la de los desarrolladores.
Se consigue mediante una descripcion lo suficientemente buena y clara de los requerimentos del sistema.
- Debe estar redactado en un lenguaje que el cliente entienda. Para que pueda comprender estos requisitos.

#### Descubrir requisitos:
Los pasos para el descubrimiento de los requisitos son:
- **Enumerar requisitos candidatos.**
	- Ideas o caracteristicas.
- **Comprender contexto del sistema.**
	- Modelo de dominio (MODP)
	- Modelo de negocio.
- **Requisitos funcionales.**
	- Identificarlos mediante los casos de uso.
- **Requisitos no funcionales.**
	- Lista de requisitos adicionales.
#### Modelado y diagrama casos de uso:
Los diagramas de casos de uso permite entender el comportamiento de un cierto sistema o subsistema modelandolo.
Es la entrada principal para el posterior analisis, diseño y pruebas del sistema.
En pocas palabras, se describe el comportamiento de la organizacion segun sus distintos procesos, y eso permite tener un mapa claro para luego analizar que puntos fundamentales modificar o adaptar.
- Se utiliza el modelo UML de tipo Comportamiento, estatico, logico.
- Su principal funcion es:
	- Detallar alcance.
	- Proveer informacion de todo o una parte de los requerimentos de un sistmea u organizacion.

**Esto contiene normalmente:**
- Casos de uso.
- Actores.
- Relaciones.
- Paquetes.

##### Objetivos fundamentales:
- Modelar contexto del sistema.
- Modelar requerimentos/requisitos del sistema.

##### Extension de los diferentes componentes:
- **Actor:**
	- El rol que juega un usuario con el sistema.
	- Un usuario no esta atado a una persona fisica, sino que puede transformarse en una maquina, otro sistema u otra entidad que interactue en el rol del usuario.
	- El diagrama de casos de uso permite determinar como se comporta el sistema para cada tipo de usuario.
	- **Actores:** Un actor puede representar uno o mas actores
		- **Actor primario:** Es el que plantea el objetivo, y es ayudado por el sistema de informacion para resolverlo.
			- Plantea objetivo al sistema.
		- **Actor secundario:** Es el actor que el sistema necesita para poder cumplir el objetivo impuesto por el actor primario.
			- Ayuda a resolver el objetivo planteado aportando al sistema.
- **Casos de uso:**
	- Representa la forma en la cual los actores utilizan el sistema.
	- Son fragmentos de funcionalidad ofrecido por el sistema con el objetivo de aportar valor a sus actores.
	- Pueden ser de dos tipos principales:
		- **Esenciales:** Funcionalidad principal/esencial. Comprenden los principales procesos de la organizacion.
		- **Soporte:** Funcionalidades que surgen para poder cumplir una funcionalidad esencial. Permiten satisfacer los requisitos de las funcionalidades principales.
	- Una sintesis de los casos de uso pueden ser:
		- Son descripciones de las funcionalidades del sistema.
		- Describen limites del sistema y relaciones entre sistema y entorno.
		- Definen el conjunto de requerimentos segun el/los usuarios que participan.
		- El comportamiento del sistema se particiona en forma de acciones y relaciones segun el punto de vista del usuario.
			- El sistema se divide en partes segun su comportamiento y se relaciona/organiza segun las interacciones del usuario.

##### Relaciones:
Hace referencia a relaciones entre casos de uso.
**Inclusion:**
- Relaciona dos casos de uso, uno base y otro adicional, donde el base incorpora el comportamiento del adicional.
- Permite reutilizar ciertos eventos en un mismo flujo.
- Se dibuja yendo desde el caso base al caso extension.
- ![[Pasted image 20260707113520.png]]

**Extension:**
- Se utiliza para modelar un camino alternativo no obligatorio en el diagrama.
- Permite darle mas opciones al actor para continuar el flujo y diferencia el flujo obligatorio del opcional.
- Se dibuja yendo desde el caso extension al caso base.
![[Pasted image 20260707114059.png]]

**Generalizacion:**
- Funciona igual que las clases, el caso hijo adquiere (hereda) el comportamiento del caso padre.
- El hijo puede modificar o agregar algun comportamiento heredado del padre.
- Se dibuja con una flecha que apunta desde el hijo al padre.
- Se puede utilizar la generalizacion en actores, permitiendo que el comportamiento de un actor general se transmita a actores especializados que adquieran y modifiquen ese comportamiento.
- ![[Pasted image 20260707114652.png]]

#### Sintesis para la construccion de diagrama de clases:
- Identificar los actores.
- Definir casos de uso, donde se especifique la funcionalidad esencial relacionada al actor.
- Identificar partes de las funcionalidades en los casos de uso, clasificarlas y relacionarlas.
- Definir funcionalidad soporte que apoye a la funcionalidad principal para que se cumpla.

## Diagrama de clases
Es un metodo de modelaje por UML que permite describir de forma tecnica como opera el sistema por dentro.
Se clasifica como: Estructura, estatico, logico.

**Su uso comun parte de 3 items principales:**
- Explorar conceptos del dominio. (Caracteristicas del problema a resolver)
- Analisis de requerimentos.
- Diseño detallado del software (SW) orientado a objetos.

**Normalmente contiene:**
- Clases
- Interfaces (tipo especial de clases)
- Relaciones

#### Identificar las clases:
Se debe explorar el dominio del sistema para poder derivar el diagrama de clases.
Esto incluye lo que el sistema administrara y utilizara.
**Pueden ser:**
- Cosas tangibles.
- Roles de personas.
- Lugares.
- Transacciones.
- Eventos.
- Otras entidades/organizaciones.

#### **TIPS PRACTICOS para el diagrama de clases:**
Para poder crear un buen diagrama de clases, se detallan los conceptos fundamentales del diseño:
- **Multiplicidad:** Se refiere a cuantas instanacias se relacionan con cuantas instancias entre 2 objetos.
	- La multiplicidad puede ir en ambos extremos, sin embargo debe estar especificada obligatoriamente en el extremo de la navegabilidad.
	- Se debe evitar que sea de MUCHOS a MUCHOS, en ese caso se debe crear una clase extension que permita dividir una clase mas grande y evitar la multiplicidad * .. *
- **Diferencia agregacion y generalizacion:** La agregacion se denomina "Tiene un", mientras que la generalizacion se denomina "Es un".
- `**Cuadro de aclaracion:** Se debe aclarar al momento de especificar los metodos que se generaliza para todas las clases.` <- REVISAR CUANDO Y PORQUE SE APLICABA ESTO.
#### Relaciones del diagrama de clases:
Las clases pueden asignarle un nombre a la relacion que tengan, como tambien un nombre de rol (aclaracion de que hace cada persona/rol involucrado en esta relacion).
**Asociacion:**
- El vinculo entre 2 objetos es una relacion de asociacion.
- Se representa conectando ambos objetos mediante una relacion simple.
- Se representa por una flecha.
![[Pasted image 20260708102143.png|433]]
![[Pasted image 20260708102608.png|434]]

**Reflexiva:**
- Ocurre cuando la clase tiene una relacion consigo misma.
- Se representa por una flecha que sale y entra en la misma clase.
![[Pasted image 20260708102729.png|277]]

**Agregacion:**
- El destino de la relacion es parte del origen.
- Se refiere a que la clase origen tiene un "anexo" en el destino de la relacion. Permite expandir una clase en subclases mas pequeñas, relacionandolas con la agregacion.
- Es la relacion entre "el todo" y sus partes.
- Se dibuja un rompo en el origen y una flecha en el destino. Va desde la clase base hacia la clase extension.
- En esta relacion se diferencian 2 tipos: Por valor y por referencia.
	- **Composicion (Rombo relleno):** Se refiere a cuando la relacion es DEPENDIENTE entre si.
		- El todo no puede existir sin alguna de las partes.
		- Hay exclusividad, osea que la extension del padre solo se relaciona con el padre.
		- Se denomina agregacion fuerte.
	- Por referencia (Rombo vacio): Consiste en la independencia de ambas clases.
		- Cada parte es independiente de la otra. Si se destruye una, la otra puede seguir en el sistema.
		- NO hay exclusividad, osea que el hijo se puede seguir relacionando sin importar el padre. Compartida por muchos "todos" al mismo tiempo.
		- Se denomina agregacion debil.

| Característica                    | Composición "Por Valor"                                                                                                                                                                                 | Agregación "Por Referencia"                                                                                                                                                                                                                         |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Rombo UML**                     | **Relleno (Negro)**                                                                                                                                                                                     | **Vacío (Blanco)**                                                                                                                                                                                                                                  |
| **Ciclo de vida**                 | **Dependiente**. La parte muere con el todo.                                                                                                                                                            | **Independiente**. La parte sobrevive al todo.                                                                                                                                                                                                      |
| **Relación de pertenencia**       | **Fuerte** (es parte del todo).                                                                                                                                                                         | **Débil** (hace referencia al todo).                                                                                                                                                                                                                |
| **Compartición**                  | **Exclusiva**. La parte pertenece a un solo todo.                                                                                                                                                       | **Compartida**. La parte puede pertenecer a varios todos a la vez.                                                                                                                                                                                  |
| **¿Cuándo usarla en tu trabajo?** | Cuando la parte no tiene razón de ser por sí sola. Ej: Un **Pedido** y sus **Líneas de Pedido**; un **Auto** y sus **Ruedas** (si el auto se destruye, las ruedas específicas de ese auto desaparecen). | Cuando la parte es un catálogo o un objeto maestro. Ej: un **Curso** y sus **Estudiantes** (si un estudiante se da de baja, el curso sigue); un **Proveedor** y los **Productos** que ofrece (el producto existe aunque ese proveedor desaparezca). |
![[Pasted image 20260708102914.png|513]]

**Generalizacion:**
- Conecta las clases mas generales con clases especializadas (padre con hijo).
- Una clase padre tiene diferentes atributos y metodos que se heredan a las clases hijas que permiten especializarse cambiando o agregando metodos u atributos.
- Sirve para especificar diferentes tipos de una clase general.
- Mientras aparezca el padre, los hijos se pueden emplear, sin embargo si son los hijos los que se relacionan, el padre no puede intervenir.
- Se dibuja como una flecha de triangulo sin rellenar. Que va desde el hijo hacia el padre.
- Tipos de herencia.
	Se exanden las diferencias en los tipos de herencia.
	- Herencia simple: Cada clase hija tiene un solo padre directo.
	- Herencia Multiple: Un hijo puede tener varios padres.
		- Este tipo de herencia puede ser perjudicial si los metodos de ambos padres son similares.
![[Pasted image 20260708104640.png|661]]

#### Patrones:
Los diagrama de clase tienen patrones que permiten resolver ciertas situaciones generales.
Los patrones permiten la capacidad de "REUSAR", osea realizar la solucion una unica vez y reutilizarla cada vez que haga falta.
Estos se basan en principios basicos de "buenas practicas", para la facil comprension del modelo.
- Filosofia de objetos.
	- Reutilizacion.
		- Experiencias.
		- Soluciones de analisis y diseño.
		- Codigos.
Cada patron se enfoca en un aspecto del problema general.
Se indica cuando y como debe aplicarse.
Se narran las consecuencias que puede generar.

Los patrones orientados a objetos se basan en resolver problemas relacionados con la estructura y/o comunicacion de los objetos y clases. Resuelven problemas de contexto.

##### Estructura del patron:
**Un buen patrón:**
⇒ Plantea una solución al problema.
⇒ Provee conceptos (captura soluciones)
⇒ Permite derivar soluciones desde primeros principios.
⇒ Describe relaciones.
⇒ Debe tener en cuenta al componente humano.

**En la orientación a objetos el patrón enfoca un solo aspecto de un problema, y debe enfocarlo identificando:**
⇒ Clases participantes.
⇒ Instancias
⇒ Roles
⇒ Colaboraciones
⇒ Distribución de Responsabilidades.

**El patrón, también debe especificar:**
⇒ Cuando aplicarlo
⇒ Si debe o no ser aplicado. Es decir debe especificar las restricciones de uso para dicho patrón.
⇒ Consecuencias de la aplicación.
⇒ Que debe tenerse en cuenta cuando se lo está aplicando.
⇒ Debe formularse estableciendo la relación entre un contexto, un sistema y una configuración que permita resolver
el problema.
**Componentes de un Patrón:**
1. Nombre
2. Propósito
3. Sinónimo
4. Colaboraciones
5. Contexto
6. Explicación
7. Fuerzas
8. Motivación
9. Ejemplos
10. Patrones Relacionados
11. Aplicabilidad
12. Estructura
13. Participantes
14. Consecuencias

##### Patron fundamental:
1. Patrón: "Colección-Trabajador"
	![[Pasted image 20260709102950.png|390]]
	Es el patron fundamental del modelo de objetos.
	Los demas patrones son variaciones de este.

##### Patrones transaccionales:
Son los patrones compuestos de una transaccion, varias transacciones o que interactuan con un elemento que interactua con transacciones.
![[Pasted image 20260709103206.png|409]]

Existen las siguientes combinaciones, las cuales varian los nombres de las clases, pero consiste en lo mismo, la relacion entre transacciones.
Dos. **Actor-Participante:**
	![[Pasted image 20260709105913.png]]
Tres. **Participante-Transacción:**
	![[Pasted image 20260709110006.png]]
A partir de aqui se trata de separar el objeto en dos o mas para poder abordar una situacion de muchos a muchos.
Seis. Transacción-Detalle de Transacción
	![[Pasted image 20260709110242.png]]
Siete. Transacción-Transacción Subsiguiente
	![[Pasted image 20260709110307.png]]
Ocho. Detalle de Transacción-Detalle de Transacción Subsiguiente
	![[Pasted image 20260709110340.png]]
Once. Item -Item Específico
	![[Pasted image 20260709110407.png]]

##### Patrones de agregacion:
Estos patrones consisten en relacionar grupos con padres.
Utilizan otros patrones para encontrar soluciones mas complejas.

Resumen de los patrones de agregacion fundamentales:
![[Pasted image 20260709110915.png|486]]

##### Patrones de plan:
Como anexo se encuentran los patrones de plan, que consiste en patrones referidos a modelar un plan a realizar:
![[Pasted image 20260709111027.png|325]]

### Máquina de Estados
Por ultimo, se expandira la teoria de maquina de estados para poder abordar toda la teoria de la catedra.
Se expande la teoria de los diagramas de maquinas de estados en UML.

**¿Que es?** Es un diagrama de estados, que modela el comportamiento de cierto objeto especificando los estados que atravieza durante su tiempo de vida.
Se detallan los siguientes items:
- **Estado:** Se representa como una situacion que transcurre un cierto objeto en un momento dado.
	- Pueden ser estados simples o compuestos (subestados).
- Transicion: Un objeto cambia de un estado a otro en respuesta a un evento.
- Evento: Es un estimulo o suceso que transiciona de un estado a otro.
- Acciones: Se pueden asociaciar con las transiciones para poder determinar que hacer cuando ocurre una transicion.
	- Pueden ser operaciones/acciones internas del sistema, llamadas, metodos, etc...
- Estados iniciales y finales: Se tienen 2 estados fundamentales, el estado inicial que indica que comenzo, y el estado final que indica que finalizo el proceso.
- Jerarquia de estados: Los procesos mas complejos utilizan estados organizados en jerarquias para poder representar comportamientos mas complejos.
	- Los estados compuestos contienen subestados que a su vez pueden tener transiciones o eventos propios.

#### Definiciones tecnicas de los estados:

