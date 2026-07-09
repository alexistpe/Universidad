<#### **Funciones vectoriales**
Una funcion vectorial es una relacion entre un vector del primer espacio con otro del segundo espacio vectorial.
Las funciones coordenadas son las coordenadas que contiene la funcion en cuestion F(X) = (F1(X),F2(X),Fn(X))
**Espacios:** Se refiere a las dimensiones donde se encuentran las funciones.
	La operacion entre ambas funciones se encuentra en el espacio (Dimension) n + m, donde n pertenece a la dimension del dominio y m a la dimension de la imagen.
- **Funciones vectoriales reales:** Consiste en funciones vectoriales que van de un espacio "n" a 1, de n-dimensional a unidimensional.
- **Funciones vectoriales de variable real:** Funciones parametricas, parten de un valor real y lo convierten en una funcion de n dimensiones. Se plantea una funcion especifica para cada coordenada (ejemplo: F(t) = ( t , 2t , t/3 ), pasa de un real "t" a una función con 3 variables (coordenadas))
- **Funciones de campo:** Transicionan en la misma dimensión (Ej: R2 -> R2). No puede ser la dimension 1, osea M = N != 1. Se representan como un conjunto de vectores, estos se encuentran en la imagen y su punto de origen es el punto del dominio que los relaciona, osea al transicionar a la misma dimension simplemente un punto en el primer conjunto se "movio de lugar" en el segundo conjunto, las dimensiones siguen siendo las mismas.
**Curvas de nivel:** Son proyecciones de superficies en un plano. Una superficie de dimensión m se representa en la dimensión m-1, permitiendo un análisis mas conciso. Se obtiene al cortar la superficie con planos paralelos a los ejes X,Y (para el caso del 3D) sucesivamente.

#### **Limites**
Estudiar los extremos de un punto en la función. En 2D se podía acercar de los laterales únicamente, en el 3D se permite acercarse de infinitas direcciones posibles. Provocando que deban existir métodos para comprobar si es valido. Por temas de simplicidad, usaremos el punto a analizar como el (0,0)
- Por definición: Es un método que permite verificar al 100% que el limite exista. Esto requiere aplicar la definición de limite a la función y punto en cuestión.
- Simultaneo: Remplazar en el limite las 2 variables y determinar resultado, este también permite saber si existe al 100%.
- Sucesivo: Consiste en hacer los 2 limites sucesivamente, osea primero el de una variable y luego la otra, se realiza nuevamente ese procedimiento pero al reves (se hace 2 veces con diferente variable) y se determina si los limites dieron un numero y son iguales.
- Radial: Consiste en remplazar "Y" por una función (Ej: y = mx + b), para poder simplificar y verificar de esa forma si el limite depende de la función (No existe el limite) o si es independiente de la función (Si puede existir.)
Aquí únicamente Por definición y simultaneo pueden asegurar que exista el limite al 100%, sin embargo todos pueden asegurar que no existe si el resultado no da.
Diferentes continuidades: Continua, discontinuidad escencial, discontinuidad salvable.
Las reglas de limites siguen intactas, solo que con otra dimensión agregada.

#### **Derivadas parciales**
Consiste en la tasa de cambio de la función en ese punto. Siendo un plano cuando muchas variables se utilizan.
Se utilizan la tabla de derivadas o la definición, sin embargo se debe afrontar de diferentes formas:
- Obtener derivada de la función en base a una variable: Fx, Fy; Esto lo logramos interpretando a la otra variable como una constante, generando un plano perpendicular al eje constante y provocando que corte en algun punto a la superficie. 
- Derivada de orden superior (derivar 2 o mas veces) o derivada cruzada: Fxy, Fyx, Fxx, Fyy, las derivadas parciales cruzadas en los casos comunes, DEBE dar IGUAL.
La ecuacion del plano tangente, sirve para tocar la superficie en un unico punto, este se realiza mediante 2 rectas trazadas por los planos de las derivadas Fx e Fy.
- Z = Fx(Xo, Yo)(X-Xo) + Fy(Xo,Yo)(Y-Yo); Donde 'Fx' e 'Fy' son las derivadas.
- El plano tangente se guía por un punto: P(Xo, Yo, Zo); Funcion del plano tangente en un punto.
**Sea cual fuera el número de variables, las derivadas parciales siempre**
**pueden interpretarse como ritmos de cambio.**

**Plano tangente:**
Consiste en un plano formado por la recta tangente de ambas derivadas parciales de la funcion. Normalmente se analiza en 3D, y al cruzar estas 2 rectas, dan la base para el plano tangente, que en el punto a analizar, permite abarcar todas las infinitas rectas tangentes que pasan por ese punto de la superficie (el plano tangente y la superficie en esa zona son casi indistingibles).

**Derivadas Parciales de orden superior:**
Consiste en derivar funciones 2 o mas veces en base a una variable, ejemplo: Fyy, Fxx
tambien existen:
- **Derivadas mixtas:** Consiste en derivar una funcion por una variable y luego por otra, ejemplo: Fxy, Fyx

**Derivadas parciales de 3 o mas variables:**
Consiste en una derivada de una funcion con 3 o mas variables, la particularidad de esto es que se agregan mas variables a la funcion, sin embargo siguen vigente los mismos metodos de interpretar 1 unica variable como independiente, y ver a las demas como constantes.

## Tema 2: **Derivada de funciones vectoriales**
#### **LINEALIZACIÓN- FUNCIÓN AFÍN**
Es el metodo de aproximar una curva mediante una recta, esto se logra gracias a que al acercarse lo suficiente, la curva parece simular una recta, provocando que se pueda trazar una recta en esta, simplificando la figura.
La cuestion parte de 3 items importantes:
- Linealización: El acto de aproximar mediante una recta (2D) o un plano (3D) una curva particular.
- Función Afín: Es el nombre que se le da a esa funcion. Es la función que mejor aproxima a una curva cerca de un punto Xo
- Diferenciabilidad: Método/formula que justifica que la aproximación sea legal y útil. Aqui lo importante es que el error r(Δx) debe hacerse "0" mas rapido de lo que el desplazamiento Δx se hace cero en ese lugar.
Es el mismo concepto de AM1, solo aplicandole las derivadas parciales de mas variables:
**AM1: L(x)=f(x0​)+f′(x0​)(x−x0​)**
**AM2: 
	z−f(a,b)=fx​(a,b)(x−a)+fy​(a,b)(y−b)** (Funcion R2 -> 3) (La funcion que mejor aproxima es la del plano tangente).
	**A(Xo) = L(Xo) + Yo** (Funciones Rn -> Rm)

La funcion es diferenciable en Xo si existe:
![[Pasted image 20260330160425 1.png]]

Para que una funcion Rn -> Rm sea diferenciable en ->Xo debe cumplir con estas 4 condiciones:
- ->Xo punto interior del Df
- E A(->X) que aproxima a f cerca de ->Xo
- f(->Xo) A(->Xo)
- Exigimos que f(X) - A(X) tienda a cero más rápido que (->X) - (->Xo)

**Las funciones Afín de Rn -> Rm se realizan mediante matrices jocabianas, debido a las dimensiones extras.**
#### Matriz jocabiana:
La matriz jocabiana organiza todas las derivadas parciales de primer orden.
Representa la derivada total de las multiples entradas y salidas correspondiente a su dimension.
- Columnas: Representan las variables de entrada.
- Filas: Representan las diferentes funciones que devuelven la salida.
En cada interseccion pones la derivada parcial (se deriva la funcion) correspondiente con esa entrada (la fila) y se deriva con respecto a la variable de salida (la columna).
![[Pasted image 20260330165130 1.png]]

**Caso especial "gradiante":**
Si, la funcion va de n dimensiones a 1 dimension (Rn -> R), la matriz jocabiana queda "aplastada" teniendo una unica fila, y a ese vector resultante se lo llama: **Gradiente** (∇f)

#### Diferencial de una funcion vectorial.

**Diferencial Total de una Función para funciones R -> R:** Geometricamente es el cambio de altura de un punto a otro (Todo pasa en el eje vertical). (En una funcion plana el incremento Δf es "0")
Δx o Δy se llaman incremento de variables independientes.
Se puede calcular de 2 formas el cambio de un punto a otro en una funcion:
**Incremento verdadero Δf**: Es el calculo completo y pesado que te da el valor exacto entre ambos puntos: Δf=f(x+Δx)−f(x)
**DIferencial df:** Se usa una recta tangente para aproximar el valor, permitiendo una mayor simplicidad de calculo a costa de un rendimiento mucho mayor: df=f′(x)⋅Δx (Derivada por el paso).

Diferencial total de una funcion para funciones de varias variables:
- **Incremento:** Δf(X)=f(X+ΔX)−f(X). Evaluás la función en la coordenada nueva y le restás la función en la coordenada vieja.
- **Diferencial (df):** (Matriz * ΔX). En vez de usar una sola derivada, agarrás la **Matriz Jacobiana** y la multiplicás por el vector desplazamiento ΔX. 

**Extension del Incremento:** 
La matriz jocabiana se usa exclusivamente para calcular el diferencial total (df).  
- **La Realidad (Δf):** Lo calculás con la fórmula Δf=f(X+ΔX)−f(X). Acá no hay atajos, es fuerza bruta pura. Reemplazás los números en la función y restás.
- **La Estimación (df):** Lo calculás armando la Matriz Jacobiana de derivadas y multiplicándola por tu paso ΔX.
Cuando Δx se aproxima a "0": df y Δf se aproximan a un valor unico.
El incremento verdadero consta de 3 pasos:
- Obtener la funcion a evaluar y evaluarla en el punto.
- Luego evaluarla en el punto incrementado: F(x + Δx) = F((x + Δx),(y + Δy),(z + Δz)... Donde la funcion tiene "n" variables.
- Una vez evaluada en ambos puntos (sin y con incremento), se restan para obtener el incremento verdadero en y: Δf
Para multiples ecuaciones se debe realizar ese procedimiento para cada funcion.

**Ejemplo:**
 Función: $f(x,y)=(x^3y^2,2x,x^2−y)$
- Punto inicial (X): (1,2)
- El paso en el piso (ΔX): (0.1,0.2)
Primero determinamos las ecuaciones: Son 3, equivalen a una matriz de 3 filas y 1 columnas (los resultados de las funciones van en las filas).
Y luego identificamos su valor en el punto (1,2)
	$x^3y^2$ = 1 * 4 = 5
	$2x$ = 2
	$x^2−y$ = 1-2 = -1
Segundo calcular el punto incrementado (1.1,2.2).
	$x^3y^2$ = 1.331 * 4.84 = 6.44
	$2x$ = 2.2
	$x^2−y$ = 1.21 - 2.2 = -0.99
**Tercero se restan entre si:**
	**(6.44,2.2,-0.99) - (5,2,-1) = (1.44, 0.2, 0.01)**
El incremento real es: (1.44, 0.2, 0.01)

#### Derivada direccional:
Antes de expandir la teoria de la derivada direccional, se debe determinar un concepto fundamental: 
**Vector gradiante:**
	Es el jocabiano de una funcion vectorial real evaluado en un punto Xo: EN $R^n$ -> $R$
	Donde el resultado de la funcion da un unico valor entero. Este vector es el unico valor resultante.
	Este gradiante es la direccion con mayor tasa de cambio de la derivada direccional.
	La derivada total de una función vectorial real ($R^n$ -> $R$), evaluada en un punto Xo, recibe el nombre de **VECTOR GRADIENTE**
**Derivada direccional:**
	Simboliza la tasa de cambio en cualquier direccion. Te dice la pendiente en ese angulo especifico, a comparacion de las derivadas comunes que permiten obtener la pendiente 
	pasando estrictamente por los ejes.
	EN UN PUNTO DE UNA SUPERFICIE EXISTEN INFINITAS DERIVADAS DIRECCIONALES, pero solo la GRADIANTE es capaz de crecer mas rapidamente.
	**La Fórmula:** Se calcula haciendo el producto escalar (punto) entre el **Vector Gradiente de la función** (evaluado en el punto) y el **vector dirección** hacia donde querés caminar.
		$Dûf(X0​)=∇f(X0​)⋅û$
		**Aqui distinguimos:**
			Se utiliza el vector gradiante para poder identificar la funcion que mas tasa de cambio genera.
			Derivada direccional, **FUNCION ORIGINAL:** Sea 𝑓 una función de dos variables 𝑥 ∧ 𝑦, sea 𝑢 un vector unitario y 𝑋0un punto que ∈𝐷𝑓
			![[Pasted image 20260409172749.png|217]]
			La definición de arriba nos permite escribir que: $(af/au)x̄0 = f'(x̄0​)⋅û$
			**Donde:**
			- F'(X0) es la **matriz jacobiana de una función real**, que evaluada en un punto nos da un **vector fila** de dimensión 1xN, y 
			- û es un versor ∈ R^𝑛.
			.
			**DEFINICION POR GRADIANTE:** Se utilizan unicamente en casos de Rn -> R (Maximo crecimiento definido en una unica variable).
			$f(x̄0​)= ∇f(x̄0​)⋅û$ 
			**Donde:** 
			- ∇f(x̄0​) es: El vector gradiante, resultado de evaluar las derivadas den un punto.
			- û es: El versor donde se evalua la direccion tomada.
	Al calcular la derivada direccional en terminos del gradiante surgen estas divisiones:
	**Por ejemplo para 2 variables XY:** $(af/au)x̄0 =𝑓𝑥(𝑥𝑜, 𝑦𝑜)𝑢1 + 𝑓𝑦(𝑥𝑜, 𝑦𝑜)𝑢2$
	**Por lo que se determinan casos particulares:**
		Cuando los versores (û) son **CANONICOS**: (0,1) o (1,0): $(af/au)X0 =𝑓𝑥(𝑥𝑜, 𝑦𝑜)0 + 𝑓𝑦(𝑥𝑜, 𝑦𝑜)𝑢2$ ; $(af/au)X0 =𝑓𝑥(𝑥𝑜, 𝑦𝑜)u1 + 𝑓𝑦(𝑥𝑜, 𝑦𝑜)0$; Eliminando un termino.
		Aplicacion coseno y seno (cos0,sen0): (𝑋𝑜)=𝑓𝑥 𝑥𝑜, 𝑦𝑜 𝑐𝑜𝑠𝜃 + 𝑓𝑦(𝑥𝑜, 𝑦𝑜)𝑠𝑒𝑛𝜃
		![[Pasted image 20260409181457.png|274]]
	**COMO CALCULARLO:**
		Nos dan los datos: 𝑓 (𝑥,𝑦) = $(x^2 + y^2)$; punto (2,−1), ū = (2,5)
		Debemos para esto seguir una serie de pasos:
		1) Calcular el vector gradiante (derivadas parciales de la funcion con las diferentes variables) y evaluarlo en el punto.
		2) Calcular el versor en base al vector ū.
		3) Ordenar todo para calcular la derivada direccional.
		--- Aplicacion:
		Primero se encuentra el vector gradiante:
			a'x = (2x) ; a'y = (2y) === (a'x,a'y) = (2x,2y) => (2 * 2, 2 * -1) = (4,-2) Vector gradiante.
		Segundo encontrar versor: El versor es im vector de longitud 1 exactamente, sirve para mostrar la direccion.
			Aqui se debe utilizar el "modulo", concepto de algebra que permite obtener el versor en cuestion.
			||ū|| = $\sqrt{2^2 + 5^2} = \sqrt{29}$
			Una vez obtenido el modulo, se debe realizar la siguiente formula.
			$û = \frac{1}{\|ū\|} \cdot ū = \frac{1}{\sqrt{29}} \cdot (2,5) = \frac{2}{\sqrt{29}},\frac{5}{\sqrt{29}}$
			Asi se obtiene el versor û
		Tercero y ultimo, utilizamos el producto punto para calcular la funcion derivada junto al versor obtenido.
			$DF/Dû (X0,Y0) = Fx(X0, Y0) \cdot û1 + Fy(X0, Y0) \cdot û2$ = ∇f(x̄0​) $\cdot$ û = NRO real. (**Vector gradiante** por **versor**)
			$DF/Dû (2,-1) = (2 \cdot 2 + -1 \cdot 2) \cdot (\frac{2}{\sqrt{29}},\frac{5}{\sqrt{29}}) = -0.37$
		**La mayor tasa de cambio es -0.37 y se encuentra en el vector gradiante (4,-2)**	
	Demostraciones:
		Que la derivada direccional maxima se encuentra cuando ū tiene la misma direccion de gradiante mediante el producto escalar (punto).
		$∇f(x̄0​) \cdot û = \|∇f(x̄0)\|\|ū\|cosO$
		.
		Si 𝑓(𝑥, 𝑦) es diferenciable en 𝑥𝑜, 𝑦𝑜 , el ∇𝑓 𝑥𝑜, 𝑦𝑜 es perpendicular a la curva de nivel que pasa por (𝑥𝑜, 𝑦𝑜)

#### Valores Extremos:
- Consiste en evaluar la funcion en diferentes puntos para determinar cuando se encuentra un punto denominado maximo o minimo.
- Se realiza un procedimeinto de ciertos pasos para inicialmente encontrar los puntos criticos (conde cambiaria la concavidad de la funcion) para luego decidir si es un maximo o un minimo analizando sus lados.

**¿Que es un extremo?**
Es un punto que se destaca de los demas por sel el mas alto o bajo con respecto a sus vecinos.
Definicion de terminos:
	Region abierta D: Zona de analisis. Zona delimitada al rededor del punto.
	Xo: Coordenada exacta donde se quiere comprobar que existe un extremo.
	X: Representa cualquier otro punto cercano a esa coordenada Xo
	f(X), f(Xo): Representan el valor de "z", son la Altura.

**Deteccion de extremos:**
Si **f(X) <= f(Xo)**, osea que el punto a analizar es mayor o igual a cualquier punto de la funcion cercana (delimitada por la region abierta D), entonces se denomina maximo. (Las alturas de tus puntos vecinos son menores o iguales al punto de analisis), se le llama **Maximo Local.** NO existe valor mas alto que el punto (Xo, Yo, Zo)
Si por el contrario: **f(X) >= f(Xo)**, esto significa que el punto de analisis es el punto mas pequeño encontrado con respecto a los puntos vecinos (es menor o igual a estos), se le llama **Minimo Local.** NO existe valor mas bajo que el punto (Xo, Yo, Zo)
- Estos son **MAXIMOS Y MINIMOS LOCALES**, debido a que estan dentro de una zona especifica de analisis, si tomaramos **toda la funcion**, estos puntos **MAXIMOS Y MINIMOS** son **ABSOLUTOS.**

**Condicion necesaria:** Existencias de Puntos Criticos:
Los extremos relativos/locales solo ocurren en puntos criticos.
- f(x,y) en la region abierta D, debe estar definida y continua.
	- Esto se verifica con: - Una división por cero (Ejemplo: f(x,y)=x−y1​ no está definida en el punto (2,2)).
	- Una raíz par de un número negativo
	- Un logaritmo de cero o de un número negativo.
	- _Regla de oro:_ Si es un polinomio normalito (tipo f(x,y)=x2+3xy−y3), está definida en todos lados.
- EL punto f(Xo, Yo) debe:
	1) Debe contener un vector nulo como gradiante: Osea que las 2 derivadas deben dar "0".
		- ∇f=0
	2) El gradiente no existe: Al intentar derivar o remplazar el punto la funcion queda en un indeterminante. Aunque la funcion original si existiera.
		- fx(Xo, Yo) o fy(Xo, Yo) no existe (significa que el gradiente no existe, ∇f(Xo,Yo) NO EXISTE )

**Condicion suficiente: Naturaleza de los extremos relativos:**
Se necesita cumplir inicialmente con la existencia de los puntos criticos:
 ∇f=0 ( fx(Xo,Yo)=0,  fy(Xo,Yo)=0)
	**Calcular extremos relativos, formula del DISCRIMINANTE:**
	![[Pasted image 20260419110348 1.png]]
	**Analisis:**
	![[Pasted image 20260419110453 1.png|521]]
	Si el Hessiano/Discriminante (el triangulo) es > 0 y la derivada segunda es > 0, entonces tiene un Minimo relativo en (Xo, Yo).
	Si Discriminante > 0 y Doble derivada < 0 tiene un Maximo relativo.
	Si el Discriminante es < 0, entonces la funcion en el punto es un punto silla.
	Si el Discriminante es = 0, no es concluyente, y se descarta.
	Aclaracion, se evalula en caso del Discrimante > 0, la derivada segunda de X, debido a que si se confirma lo primero, tanto Fxx, Fyy tienen el mismo signo. Por lo tanto se puede calcular
	tanto con Fxx como con Fyy para verificar EL SIGNO.
	Fxx o Fyy nunca pueden ser == 0 si el discriminante es > 0, debido a que segun la formula del discriminante, obliga a quedarse con un signo negativo:
		Δ = fxx​⋅fyy​−(fxy​)2 => Δ = 0​⋅fyy​−(fxy​)2 => Δ = −(fxy​)2 = Obliga a quedar negativo.
	**SE PUEDE USAR LA FORMULA DEL HESSIANO PARA CALCULAR EL DISCRIMINANTE:**
	Esta consiste en un determinante con las diferentes derivadas dobles y cruzadas, que se multiplican en diagonal y se suman los resultados.
	![[Pasted image 20260419113633 1.png]]

**Rol del polinomio de taylor:**
f(X) = f(X0​) + df(X0​) + 1/2​ d2f(X0​)
Este polinomio es la razon de porque se analiza los signos. Trae una logica detras que compara a la altura con el punto con curvatura plana.
la expresion se reduce a: f(X) - f(X0​) = d2f(X0​) (EL numero y df se vuelven 0, porque no afectan al signo y el diferencial se vuelve "0")
Aqui al estar la funcion (todos los demas puntos) menos el punto critico (a analizar), el resultado del segundo diferencial (d2f) permite determinar si fue un maximo o minimo segun esta logica:
**Positivo:** Entonces f(x) (los demas puntos de la funcion) son mayores, por lo tanto el punto critico analizado es menor f(Xo), entonces se determina como minimo (esta abajo de los demas).
**Negativo:** Entonces el resto de los puntos de la funcion f(x) estan por debajo (son menores) al punto critico analizado f(Xo), entonces este punto es un maximo (esta arriba de los demas). 

**Obtener Multiplicadores de Lagrange:**
Permite encontrar los puntos criticos de la funcion restringida, osea que otra funcion determina el "sendero" a recorrer o evaluar. Esas son las condiciones.
Lagrange planteo una funcion fundamental F(X), que permite encontrar estos puntos criticos, se compone de:
- Identificar la funcion original f(x), la funcion objetiva. Es la que queres maximizar o minimizar.
- Condicional, formula G:  Es la formula restriccion y debe expresarse en forma implicita, osea igualada a 0.
- Multiplicador (λ): Se añade un multiplicador universal (LAMBDA), esta variable desconocida la multiplicas por la condicion, entre mas condiciones mas lambdas.
**Funcion lagrange resultante: F(X) = f(X) + λ⋅G**
Luego se opera como una funcion normal para encontrar los valores criticos.
Se depejan e igualan las variables "x" e "y" para obtener su relacion.
**Pasos encontrar puntos criticos en funcion de lagrange:**
- Calular las derivadas de la funcion (dx, dy, dz) IGUALANDOLAS A CERO.
- Se forma un sistema de ecuaciones junto a la condicional inicial.
- Despejas las variables de las funciones y las LAMBDAS (λ)
	- Despejas las λ de ambas derivadas y las igualas para obtener la relacion entre y e x.
- Los valores de x,y,z que se obtienen son los puntos criticos.
	- f(x, f(x), f(x,y))
Una vez obtenidos los puntos criticos, se debe determinar si es un maximo o un minimo, esto se realiza usando la condicion de despeje:
- Se expresa la funcion en terminos de una sola variable (como AM1).
- Se calcula la derivada segunda de esa funcion (f'').
	- Si al remplazar por las coordenadas del punto critico la derivada queda positiva: Minimo.
	- Si queda negativa: Maximo.
	- SI es 0: No determinado (Se puede analizar un poco por la izq, derecha y determinar).
Si bien puede ser similar al determinante, aqui ya no se evalua en esa dimension, nos fuimos del espacio de las multiples variables.

## Integrales Dobles - Temario 2
Una integral es lo inverso a una derivada, viene a ser la suma de todos los cambios para darte el area debajo de la curva.
En sintesis sirve para calcular areas debajo de las curvas.

En este caso de integrales dobles, parte del mismo principio, solo que combinamos 2D y 3D resultando en un espacio R3. Son funciones del tipo: R2 -> R
Analizamos el area o volumen debajo de la superficie, con respecto a un cierto plano rectangular.
Definicion: El  objetivo es hallar el volumen del sólido S, comprendido entre la superficie y la región del plano.![[Pasted image 20260423170442.png]]
	Desarrollo: Se subdivide la region del plano en pequeños rectangulos de lados DELTAx, Deltay. Se toma un punto del rectangulo (x,y) y se contruye un prisma rectangular de altura f(x,y) (hasta chocar a la superficie).
	El volumen de cada prisma será V = f(x,y) DELTAx DELTAy, esto se aproxima al volumen de la region solida, gracias a la suma de riemman.
	![[Pasted image 20260423170522.png|145]]
	Cuanto mas pequeños sean los rectangulos, mayor sea la aproximacion. Siempre que el limite exista, la funcion es integrable en esa region.
	![[Pasted image 20260423171438.png|377]]
	Volumen: ![[Pasted image 20260423171449.png|185]]

**Teorema de Fubini:** Una integral doble puede escribirse como una integral iterada. Esto lo usamos para calcular.
![[Pasted image 20260423171628.png|619]]

**Regiones no rectangulares:**
	**Region verticalmente simple:**
		Se calcula dy primero y luego dx.
	**Region horizontalmente simple:**
		Se calcula primero dx y luego dy.
	**Formula:**
	![[Pasted image 20260423171921.png|506]]
	**Ambas calculan el mismo volumen, se elige la que sea mas conveniente para el calculo en cuestion.**
**CONDICION:** La integral de fuera debe ser si o si NUMEROS, osea CONSTANTES, debido a que se quiere obtener un valor de resultado de la integral.

**Metodo**
- Se define la integral doble: ![[Pasted image 20260423164705.png]]
- Se organiza y simplifica para poder integrar.
- Se integra por una variable (dy o dx segun corresponda), y se evalua esa variable con los respectivos valores, Ej: en un F2(x) - F1(x)
- Luego se resuelve.
- Se vuelve a integrar, pero esta vez por la segunda variable, y evaluando la variable restante de la segunda integral, Ej: F2(y) - F1(y)
- Se resuelve y queda el resultado final.

**Calculo de area:**
Se puede calcular el area usando integrales dobles, esto se logra igualando: f(x,y) = 1, el resultado de f(x,y) es igual a la altura del prisma, por lo que al igualarlo a 1 este pasa a ser el area de la region calculada.
Esto se debe a la formula basica del volumen: Volumen = Base * Altura, Si la altura (que es z) la igualas a "1", te queda: V = B * 1.
Aplastas el techo geometrico.