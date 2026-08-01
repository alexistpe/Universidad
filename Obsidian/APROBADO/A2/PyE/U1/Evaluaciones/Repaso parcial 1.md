### **Temario**
- **Teoría de conjunto**. Espacios muestrales. Sucesos.
- **Definición de Probabilidad**, axiomas, **teoremas importantes.**
- **Probabilidad Condicional. Teorema de Bayes. Diagrama de árbol.**
- Permutaciones y combinaciones. Simples y con repeticiones.
- Aplicaciones.

### Metodologia
Resolver problemas y teoria elemental. Que me permita identificar no solo probabilidades, sino que tambien cuestiones matematicas puras.
- Poder plantear ecuaciones genericas analizando el caso.
- Identificar:
	- Espacio muestral.
	- Conjuntos.
	- Relaciones (mutuamente excluyentes, intersecciones, etc...).
	- Independiencia o dependencia.
- Definir conceptos aftractos como:
	- Que es la probabilidad.
	- Que es la incertidumbre.
	- Tipos de probabilidad (ejemplos sesgos).
	- Probabilidad clasica.

**PONERSE LAS PILAS, REPASAR Y RESPONER.**
	**ANALIZA CADA CONCEPTO Y DEFINELO, MINI CUESTIONARIO TEORICO.**
	- Primero vamos a definir toda la teoria propuesta en el temario, para repasar, luego vamos a ir a los conceptos particulares en forma de cuestionario.
	- Lo nuevo que respondamos en el cuestionario va a ir de teoria.
	- Usaremos el aprendizaje espaciado y recall para repasar los temas.

**Preguntas preparcial:**
- Que significa q sea independiente y dependiente?
- Esta unidad que estamos viendo es la modelizacion de la incertidumbre
- Determinar si es mutuamente exluyente o no
- Que tipos de probabilidades hay?
- Usar analisis combinatorio para determinar casos favorables

## Repaso teorico U1:
==**¿Que es la probabilidad?**==
	La probabilidad es la medida del grado de incertidumbre para que suceda un cierto evento.
	Los valores que puede tomar son de 0 hasta 1.
	Medida numerica de la probabilidad que un evento suceda.
	El comportamiento de las variables de estudio no se puede predecir de antemano, lo que provoca que sea un modelo probabilistico, no deterministico.
	No esta sujeto a leyes fisicas.

**Conceptos fundamentales:**
- **Experimento aleatorio:**
	Si un proceso de cambio (un experimento), produce dos o mas resultados posibles, los cuales son inciertos, a este experimento se le denomina "aleatorio" o "estocástico", debido a tener 
	caracteristicas que permitan la incertidumbre (medida de duda de valores posibles).
	a) El proceso se efectúa de acuerdo a un número bien definido de reglas.
	b) Es de naturaleza tal que se repite o puede concebirse la repetición del mismo.
	c) El resultado de cada ejecución depende de la “casualidad” o sea de influencias que no pueden ser controladas y por lo tanto no se puede predecir un resultado único.
- **Espacio muestral (Espacio Probabilístico o Conjunto Fundamental)**
	En base a un experimento aleatorio "E", se denomina "Espacio muestral de 'e'" a todos los posibles resultados del experimento aleatorio "E". Es el CONJUNTO UNIVERSAL (Diagramas de venn).
	Cualquier prueba realizada a un experimento aleatorio devolvera un resultado que **corresponde exactamente** a un elemento del **espacio muestral.**
	**EJEMPLO:** Lanzamos una moneda al aire y observamos que el resultado puede ser C o S, entonces definimos el espacio muestral como el conjunto: U = {C;S}
	**U de EXPERIMENTOS INDEPENDIENTES:** Si realizaramos un experimento aleatorio E que consiste en realizar 2 experimentos aleatorios independientes (B;C respectivamente), entonces podemos calcular el espacio muestral total como 
	TODAS las posibles combinaciones entre los resultados de ambos experimentos aleatorios (producto cartesiano de UB por UC).
	Por lo tanto: quedaria: UE = UB * UC, donde 'U' es el universo (espacio muestral), y 'E,B o C' son los experimentos en cuestion.
	Tambien se puede definir con subindices: U1 = U2 * U3
		**Mutuamente excluyentes:** Cada elemento del espacio muestral es mutuamente excluyente del restante, eso significa que no pueden ocurrir simultaneamente. 
		**Colectivamente exhaustivos:** A su vez, estos elementos consituyen el total del espacio muestral.
	**U de EXPERIMENTOS DEPENDIENTES:** Para el espacio muestral de experimentos aleatorios dependientes, estos comienzan con un espacio muestral fijo (definido por combinatoria, NO por multiplicacion), sin embargo, en cada repeticion del experimento, el espacio muestral se reduce, debido a lo que sucedio en el anterior experimento. Para el espacio muestral total se calculan utilizando metodos de combinatoria (variacion con repeticion o combinacion), De esa forma calculas el numero de puntos muestrales (combinaciones VALIDAS para ese experimento aleatorio)
	Existen varios tipos de espacios muestrales, segun como se analicen los elementos y si contiene valores discretos o rango de valores.
		==**Tipos de Espacios muestrales:**==
			- Finito | también | DISCRETO
			- Infinito contable | también | DISCRETO
			- Infinito no contable | también | CONTINUO
		Si el espacio muestral puede tomar un rango de infinitos valores entre un invervalo lineal, entonces se denomina un espacio muestral continuo (infinito no contable). 
		Para dos valores cualesquiera que elija, siempre hay un tercer valor entre ellos.
			Ej: valores entre 1 y 2: 1.1, 1.11, 1.1111, 1.00000001, etc...
			Se asocian a mediciones físicas como tiempo, estatura, peso, distancia y volumen, etc...
- **Eventos o sucesos:**
	Es un subconjunto del espacio muestral.
	**Tipos de sucesos:**
	-  Suceso simple: Es un suceso que contiene un unico punto muestral. Un unico elemento de todos los elementos del espacio muestral.
	- Suceso compuesto: A un evento le pertenecen mas de un punto muestral. Tambien se le llama simplemente suceso.
	- Suceso imposible (nunca ocurre): Contiene un punto muestral que no pertenece al espacio muestral, ejemplo m = {1,2,3,4,5,6} donde el evento es = {7}, eso es imposible.
	- Suceso cierto o seguro (ocurre siempre): El evento contiene todos los elementos (puntos muestrales) posibles del espacio muestral.
	Un evento ocurre si al menos un punto muestral perteneciente al evento sale de resultado.
	Ditribuciones: 
	- **Mutuamente excluyentes o disyuntos:** Ningun elemento entre ambos eventos coincide, ejemplo: A = {1,2,3}; B = {4,5,6}, Entonces A y B son disyuntos. A n B = Nulo 
	- No mutuamente excluyentes: Si algun punto muestral/elemento esta contenido en ambos conjuntos: A = {1,2,}; B = {2,3}, Entonces A y B son NME. A n B = 2 
	- **Colectivamente Exhaustivos:** Dos o mas eventos son Colectivamente Exhaustivo si la suma de todos los demas eventos dan como resultado el espacio muestral original (U).
	- **Sucesos complementarios o contrarios:** El suceso A' (A complementado) es el que posee los elementos del espacio muestral que no se encuentran en A.
- ==**Concepto de probabilidadad:**==
	- Existen 3 'Escuelas' de pensamiento para definir a la probabilidad.
		- **Clasica: Se basa en la teoria de Laplace.**
			- Se basan en los resultados igualmente probables de un experimento azar. Tdos los resultados deben tener la misma posibilidad de suceder.
			- Si hay N resultados posibles igualmente probabDles, la probabilidad individual de cada uno es: 1/N
			- Si en un espacio muestral de N eleementos igualmente probables, se encuentra un evento con H elementos probables, entonces
				H/N es la probabilidad de que cualquiera de los elementos (puntos muestrales) del evento sean obtenidos de resultado.
				Ejemplo: A = {1,2,3} U = {1,2,3,4,5,6} => A/U = 3/6 = 0.5 = 50% de probabilidad que ocurra el evento A.
			- Cuando el modelo perfecto no se asocia a la realidad (Dado con pesos), usar el metodo de la probabilidad clasica resultan en ligeros errores, por
				lo que se recurre a la Teoría Frecuencial para estos casos inperfectos.
		- **Frecuencia relativa/Teoria frecuencial:  Pruebas y analisis para determinar la probabilidad.**
			- Propone realizar un experimento aleatorio bajo las mismas condiciones un numero "n" de veces, donde se propone obtener la probabilidad real en base al experimento. 
			- Entre mas veces se realice el experimento mas cercana sera la probabilidad calculada a la real.
			- Si un experimento es ejecutado 'n' veces en las mismas condiciones y hay 'ni' resultados, ni <= n, en que ocurrió un hecho, entonces una estimación de la probabilidad de ese suceso es la razón ni/n.
			- La verdadera probabilidad se calcula como: P(A) = Lim ni/n (n -> Infinito)
			- En la realidad obtenemos una aproximacion de P(A), debido al uso de un n grande.
				- Por lo que tratamos a la estimacion de P(A) como la verdadera probabilidad.
				- P(A) = ni/n = hi, y: 0 <= ni/n <= 1, Por lo tanto: 0 <= P(A) <= 1
		- **Subjetiva: Usa el punto de vista personalista**
			- La probabilidad se deduce de forma subjetiva por la persona que analiza la situacion, basandose en sus conocimientos anteriores sin necesariamente fundamentos matematicos.
			- Es la medida de confianza personal en una proposicion particular. Asigna un grado de 1 a 0 segun su creencia.
			- Esto se da en casos donde el experimento es rara vez repetible a gusto o masivo.
			- Si se tiene el doble de menos confianza en el suceso "A" a comparacion del "B", donde A y B son los unicos sucesos posibles, su probabilidad queda como: A = {1/3}; B = {2/3}
	**La probabilidad de frecuencia realtiva y clasica son llamadas definiciones objetivas, debido al metodo utilizado para llegar a la probabilidad.**

- **Axiomas y propiedades:**
	Se crearon para realizar operaciones con los sucesos.
	Existen multiples axiomas y propiedades, se diferencian en el la forma de pensamiento pero coinciden en la logica matematica (a nivel matematico son correctos).
	**Axiomas:**
		**Familia (F) sucesos:**
			F1: El suceso imposible y el suceso cierto pertenecen a la familia de sucesos.
			F2: La interseccion de un conjunto numerable de sucesos tambien es un suceso A1 n A2 PERTENECE A F
			F3: La union de un conjunto numerable de sucesos tambiene s un suceso.
			F4: El complemento de un evento A perteneciente a F, tambien es un suceso que pertenece a F: A' PERTENECE a F.
			F5: Si 'A' y 'B' son sucesos, entonces la diferencia entre A y B es tambien un suceso (A - B es un suceso perteneciente a F).
		**Referida a la probabiliad de sucesos:**
			P1: Cada suceso se le asocia una probabilidad (A pertenece a F => Existe un valor de probabilidad para A descrito como P(A))
			P2: Positivdad, No existe probabilidad negativa P(A) >= 0
			P3: Certidumbre P(LAMBDA) = 1; Probabilidad de todo el espacio muestral.
			p4: Regla de adicion, Si existen n sucesos mutuamente excluyentes enumerables, la probabilidad de la union de los conjuntos equivale a la suma de sus probabilidades
				provocando que la suma de todos los sucesos de la probabilidad del espacio muestral (1 = certidumbre, abarca todos los puntos muestrales en los diferentes subconjuntos).
	==**Propiedades:**==
		1) Restar 2 conjuntos es igual a: P(B - A) = P(B) - P(A), donde P(B) = P(A) + P(B - A).
		2) Ley del complemento: P(A') = 1 - P(A).
		3) El espacio nulo o imposible es representado como un circulo con un palo enmedio y su probabilidad es '0', por lo que P(LAMBDA) + P(NULO) = P(LAMBDA) = 1.
		4) La probabilidad de que suceda un evento va desde 0 (imposible) a 1 (cierto): 0 <= P(A) <= 1, Si A es un subconjunto de LAMBDA, entonces la probabilidad de 'A' es: P(A) <= P(LAMBDA).
		5) Demostrar que A es mas pequeño que B, Si A es un subconjunto de B y ambos perteneces a LAMBDA, entonces: A c B => P(A) <= P(B); P(A) >= 0 => P(B - A) >= 0, por axioma p2.
		6) Demostrar la union entre 2 conjuntos (NME): A U B = A U (B - (A n B)) (Eliminas los elementos repetidos). P(A U B) = P(A) + P(B) - P(A n B).
		7) Obtener un suceso en base a combinaciones, Dos sucesos A y B: A = (A n B) u (A n B') => A = (A n B) + (A n B')
		8) Si un susceso A se forma en base a eventos mutuamente excluyentes: P(A) = P(A n A1) + P(A n A2) + .... + P(A n An) (Union de las diversas intersecciones.
			Permite calcular el evento A en base a sus diferentes intersecciones (pedacitos en otros conjuntos).
		9) SI hay un conjunto infinito numerable de eventos no necesariamente mutuamente excluyentes: (Por Propiedad 6)= ![[Pasted image 20260413195553.png]]
			Se denomina desigualdad de boole: Es la generalizacion de la probabilidad total. La unión nunca va a ser más grande que la suma de las partes. Esto debido a que pueden haber eventos no mutuamente excluyentes que sumen elementos doblemente, provocando que se dupliquen y la suma llege a ser mas grande que la probabilidad real (sin los elementos repetidos).
			Ejemplo de mutuamente excluyentes: ![[Pasted image 20260413195651.png]]
			Aqui ningun evento se solapa con otro, por lo que ningun elemento se repite, y es equivalente a sumar las partes.

==**Probabilidad Condicional:**== (FUNDAMENTALES)
- Consiste en el concepto de que cierta informacion puede alterar las probabilidades iniciales, y por lo tanto reducir el espacio muestral a un subconjunto, donde la probabilidad de ese suceso en el subconjunto puede aumentar, mantenerse o reducirse comparado al espacio muestral total.
- Las probabilidad asociada a un subconjunto (subpoblaciones) se denominan probabilidades condicionales.
- Sucede cuando ocurre un evento:
	- Se tiene en el espcio LAMBDA los eventos: A (a sucesos favorables elementales), B (b sucesos favorables elementales), AnB (c sucesos favorables elementales)
	- Caso: Ocurrio el evento B y se pide la probabilidad de que tambien haya ocurrido el evento A => El nuevo espacio probabilistico (subconjunto o subespacio) sera B con b sucesos elementales, de los cuales "c" de "AnB" corresponden a los casos favorables. Esto se escribe como P(A|B), y se defini el nuevo espacio probabilistico como:
			- P(A|B) = c/b = Suscesos favorables (AnB) / Sucesos favorables a B (subespacio, espacio reducido).
			Simbolizandose como: P(A|B) = c/b = P(A|B) / P(B)
- Reduce el margen de elementos favorables/posibles y si nos centramos en analizar a eventos externos que intersecten al subespacio del evento que sucedio, entonces obtenemos la probabilidad de que el elemento perteneza a la interseccion de otro evento en ese espacio muestral reducido, osea en sintesis descarta todo evento restante que no participe del evento en cuestion, por eso la interseccion entre eventos se toma como valida, la parte que intersecta al evento que sucedio es una posibilidad, y son los casos favorables que se evaluan.
- Se le llama: Probabilidad de A dado B. (Dado que sucedio b.)
	**Probabilidades MARGINALES y CONJUNTAS: Aqui analizamos la independencia y dependencia de probabilidades.**
	![[Pasted image 20260414173200 1.png|408]]
	- Las probabilidades de los eventos segun como se relacionen con los diversos eventos del espacio muestral, caen en la clasificacion de marginales o conjuntas:
	- **Marginales:** Ocurre cuando las probabilidades se definen por otros eventos, cuando se la suma de probabilidades en 2 eventos devuelven la probabilidad del tercer evento.
		- P(A) = P(AB)+P(AD) = 0,083+0,017 = 0,1, Una P. marginal es una suma de p. conjuntas.
	- **Conjuntas:** Es la ocurrencia simultanea de 2 sucesos. Se define con la interseccion entre 2 eventos.
		- P(A n B)=0,083

==**Probabilidad Compuesta o Probabilidad de Ocurrencia Conjunta (Regla Multiplicadora General):**==
- Es la herramienta para que podamos calcular la probabilidad de varios sucesos de forma consecutiva (al mismo tiempo).
- El orden no importa en la intersección. A∩B = B∩A
- Antes de esto se debe determinar que es un suceso independiente y un sueceso dependiente.
	Se relacionan con la naturaleza del proceso aleatorio de selección (muestreo: seleccion alazar de n unidades en un conjunto).
	==**Independiente:**== 2 eventos son independientes si la ocurrencia de uno no afecta al otro. Se generan por muestro aleatorio con reposicion.
	==**Dependiente:**== 2 eventos se consideran dependientes si la ocurriencia de uno afecta a otro. Se generan por muestreo aleatorio sin reposicion. Se reduce el espacio muestral en cada experimento.
- La Ley que rige la Probabilidad compuesta o de ocurrencia conjunta de A y B se da por: **Regla Multiplicatoria General**
	P(AnB) = P(B).P(A|B) (1)
	P(BnA) = P(A).P(B|A) (2)
	- Donde P(A/B) = P(AnB) / P(B) y P(B/A) = P(BnA) / P(A) 
	- En base a la definición de Probabilidad Condicional despejada resulta la **Ley de Probabilidad Compuesta**
	- Define que: Para que 2 cosas pasen, primero debe pasar una y bajo esa premisa sucede la siguiente (A dado que B es un hecho).
	- **Independencia (Caso Especial):**
		- Si P(A|B) = P(A), dado que los eventos no se afectan entre si, la condicion se simplifica, obteniendo la expresion de: P(AnB) = P(B).P(A|B) => **P(AnB) = P(B).P(A)**
		- Esta expresion permite calcular la probabilidad que ocurran 2 sucesos independientes. Esto ocurre debido a que si ocurre B, en teoria no afecta las probabilidades de A, entonces "A dado que sucedio B" es igual a la probabilidad inicial de A. Es logica.
		- Matematicamente P(AnB) = P(A) * P(B) => P(A|B) = (P(A) * P(B))/P(B) = P(A) (Se cancelan las P(B)).
	==**Generalizacion para multiples eventos simultaneos (mas de 2):**== 
	- Se utiliza el concepto de cadena, debido a que se debe tomar encuenta las probabilidades anteriores.
	- Ejemplo: P(AnBnC) = P(A) * P(B|A) * P(C|(AnB))
- Permite hallar la probabilidad de la **intersección** (A∩B), es decir, que ocurran ambos sucesos. Donde la probabilidad es condicional.

**Sucesos independientes:**
- Es un caso especial de la ley multiplicatoria general, donde 2 sucesos son independientes entre si.
- Se extendera la cuestion de sucesos independientes.
- **Detectar si son independientes:** 2 sucesos pertenencientes al mismo espacio muestral son independientes si la probabilidad de su ocurrencia conjunta (de A y B), es igual al producto de sus probabilidades individuales: P(AnB) = P(A) . P(B)
	- P(A|B) = P(A) y P(B|A) = P(B) siempre que P(A) != 0 y P(B) != 0
	- **Desarrollo:** 
		P(AnB) = P(BnA)
		reemplazando por sus iguales
		P(A|B).P(B) = P(B|A).P(A)
		y si los sucesos son independientes:
		P(A).P(B) = P(B).P(A)
- Un suceso es DEPENDIENTE si: P(AnB) != P(A).P(B)
- Sirve para calcular la probabilidad de un numero n de sucesos independientes: P(AnBnC) = P(A).P(B).P(C)

==**Teorema de bayes:**==
- Calcula la probabilidad a posteriori, osea para determinar que causa pudo actuar ante x evento que haya sucedido. Se basa en los eventos sucedidos para calcular la causa de estos.
- Es una formula para calcular probabilidades condicionales.
- Consiste en dividir la probabilidad compuesta por la marginal, y para esto sirve tener una tabla donde se encuentren estas probabilidades.
**Calculo:**
- Si queremos conocer la causa del evento A, y este evento A esta compuesto por multiples sucesos mutuamente excluyentes, donde:
	A = A1 u A2 u A3 u ... u An = A = (A n A1) u (A n A2) u (A n A3) u ... u (A n An)
- Y se puede expresar mediante la igualdad: P(A n B) = P(B).P(A|B)
	(A n Ak) = P(Ak).P(A/Ak) para k = 1,2,3,....n.
- Expresamos la probabilidad marginal como:
	![[Pasted image 20260414192141 1.png]]
- Y si queremos calcular la probabilidad condicional:
	(Ak n A) = P(A).P(Ak/A)
	![[Pasted image 20260414192515 1.png|416]]
**El numerador de cada una de las probabilidades es una probabilidad compuesta y el denominador es la probabilidad marginal.**

**Analisis combinatorio:**
REPASAR.
## Repaso practico-teorico
Especificar preguntas teoricas sobre los diferentes temas, extender sobre eso y reforzar con ejemplo practico.
#### Temas fundamentales para amplear:
- **¿Que es la probabilidad?**
    SI
- **Tipos de Espacios muestrales:**
    SI
- **Concepto de probabilidadad, como se calcula:**
    SI
- **Propiedades:**
    SI
- **Probabilidad Condicional:**
     **ACLARAR CALCULOS: AnB y A|B, justamente para interpretar graficamente y analiticamente como son.**
	    SI
	SI
- **Probabilidad Compuesta o Probabilidad de Ocurrencia Conjunta (Regla Multiplicadora General):**
    SI
- **Independiente:**
    SI
- **Dependiente:**
    SI
- **Generalizacion para multiples eventos simultaneos (mas de 2):**
    SI
- **Teorema de bayes:**
- SI
**SE LE DICE SUBCONJUNTO (HABLANDO DE LA TEORIA DE CONJUNTOS, VENN) NO SUBESPACIO, es SUBCONJUNTO.**
## Repaso practico:
#### 1) 
**Metodologia:**
	- ==Repasar problemas generales (al menos 4 simples). (20m)==
	- ==Elegir problemas duros o que llamen la atencion por dificultad o resolucion. (1 o 2) (30m)==
	==- Elegir problemas segun los temas particulares. (Todos los temas). (1h 30m)==
	
Un fabricante tiene tres máquinas, que se llaman X,Y y Z que producen piezas idénticas. Se sabe que el 5 % de las piezas producidas por la máquina X son defectuosas (D), y que
los porcentajes de piezas defectuosas que producen Y y Z son el 10 y el 15 % respectivamente. Se mezclan los productos y no hay manera de reconocer cual ha sido producido por cual máquina. Pero se sabe que las tres máquinas tienen igual capacidad y que funcionan al mismo ritmo de producción. Si se toma una parte producida, al azar y se la encuentra defectuosa, ¿Cuál es la probabilidad de que provenga de la máquina Y? Es decir, calcular P(Y/D).