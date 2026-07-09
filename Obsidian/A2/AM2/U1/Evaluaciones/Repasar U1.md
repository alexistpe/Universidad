- Explicacion teorica.
- Explicacion practica.
- Sesiones de cuestionarios recall.
#### Se realizar este procedimiento **DIARIAMENTE** **minimo 1h 30m** hasta el dia del parcial. Repasando mi**nimo 2 temas por dia.**

### Contenido:
RA1:
- **FUNCIONES VECTORIALES**
	- ~~Funciones Vectoriales Reales~~
	- ~~Funciones Vectoriales de Variable Real~~
	- ~~Funciones de Campo o Campos Vectoriales~~
	- ~~Curvas de Nivel~~
	- ~~Superficies de Nivel~~
	- ~~Limite y continuidad~~
	- ~~Derivadas parciales~~
- **DERIVADA DE FUNCIONES VECTORIALES**
	- ~~Matriz jacobiana~~
	- ~~Diferencial total~~
	- ~~Incremento~~
- ~~**DERIVADA DIRECCIONAL - GRADIENTE**~~
- **VALORES EXTREMOS**
	- ~~Valores extremos locales~~
	- ~~Puntos criticos~~
	- ~~Extremos relativos, Hessiano~~
		- ~~Tipo de punto encontrado (Minimo, maximo, silla).~~
	- ~~Extremos condicionados (Multiplicadores de lagrange)~~
RA2:
- **INTEGRALES DOBLES.**
	- Calculo de volumen Verticalmente y Horizontalmente.
	- Calculo de area.

- Abordar temas esenciales, no extenderse en temas muy especificos.
	- Tener en cuenta las resoluciones de la guia para guiarnos sobre los "temas esenciales".
	- NO abarques todo debido al poco tiempo, conviene practicar y que quede super claro los temas esenciales.
### Metodologia para Estudiar:
Consiste en una serie de 3 pasos muy simples:
- Elegir el tema y estudiarlo.
- Explicarlo con mis palabras.
- Realizar ejercicio practico.
Se realiza ese procedimiento con todos los temas a abarcar, se expande uno por uno divido en categorias y subcategorias, de forma organizada se divide y aborda el problema.
- **Realizar mini cuestionario practico (problema simple) de cada tema al inicio de cada sesion. Lo que buscamos es estudiar y recordar lo aprendido de cada tema.**
Luego de repasar todos los temas, nos ponemos a practicar con preparciales.s

---
# Estudio: 2 temas minimo
## RA1:
### Funciones Vectoriales
- Hay que partir de las **funciones escalares**, las cuales son de un real a otro. Estas funciones consisten en la relacion entre 2 conjuntos, ambos no vacios, donde un elemento del primer conjunto esta relacionado exactamente con un elemento del segundo conjunto. A los elementos en el segundo conjunto se determinan como imagen y a los elementos del primer conjunto como dominio, el primer conjunto es el conjunto de entrada, y el segundo conjunto el de salida.

- Una **funcion vectorial** por otro lado, $f:U R^n  -> R^m$, **asocia un vector determinado de U con un vector determinado de f(x) en Rm**; Significa que en vez de asociar un numero, asocian una serie de numeros organizados logicamente, un vector.
	$f(x) = (f1(x), f2(x), fn(x))$
	**La funcion se representa con una "f" en minuscula.**

**Practica:**
	𝑓 (𝑥, 𝑦) = (2𝑥2, 3𝑦𝑥2, −2𝑥𝑦)
	Los valores de las variables se remplazan para obtener las coordenadas finales. Ej con valores xy: {2,2}
	2 * (2²), 3 * (2 * 2) * 2, -2 * (4) = (8,24,-8) 
#### - Funciones vectoriales reales:
- El caso particular de las funciones vectoriales reales, consiste en la dimension de destino: $R^n -> R$, la dimension de destino da como resultado un numero, osea f(x,y,z,etc...) es un numero real en vez de otro vector. 
- Dominio: $R^n$, Osea todos los valores del primer conjunto que es el de partida.
- Imagen: $R$, Todos los numeros reales.
- La representacion se realiza en: R elevado a n+1

**Practica:**
	$f(x,y) = x² + y²$
	Aqui se definen las variables para el calculo y gracias a ello se obtiene un numero real en una unica funcion final.
	Ej: (x,y) = {2,3}; 2² + 3² = 13
	13 es el valor real del conjunto de salida (imagen) que esta relacionado con el conjunto de entrada (dominio) formado por 2 variables.
	(2,3) -> 13
	El grafico se haria en 3D, superficie en el espacio.

#### - Funciones vectoriales de variable real
- **Es el inverso de la funcion vectorial real**, Pasa de un numero a un vector: $R -> R^m$
- **Dominio:** Numero real (Primer conjunto).
- **Imagen:** Vector de m coordenadas (Segundo conjunto).
- Cada coordenada esta **construia por funciones escalares**. g(t) = (g (t), g (t), .......g (t))
- **La representacion se realiza en R ^ 1+m**, Y representan curvas en el plano o espacio. A esta funciones se le llaman **parametricas**.

**Practica:**
	g(t) = (t-5, t³), **R -> R²**
	Donde el valor real es 7 (t):
	(7-5, 7³) = (2, 343)

#### - Funciones de campo o campos vectoriales
- Consiste en una funcion vectorial, donde las dimensiones del conjunto de entrada y salida son identicas y diferentes a 1: $R^n -> R^m, n=m, n != 1$
- Se representa graficamente como flechas con origen en el dominio y fin en la imagen.
- Gracias a este tipo de funciones se forman los "campos vectoriales". Se utilizan para magnitudes vectoriales, direccion, sentido, intencidad.
- f(x,y) = (M,N), $R^2 -> R^2$

**Practica:**
	f(x,y) = (-x,y²), R² -> R². 
	Si las variables (x,y) fueran: (3,2):
	(-3,2²) = (-3,4) Para ese punto (3,2) en particular del dominio, su imagen en el conjunto de salida seria: (-3,4), donde su origen se ubica em (3,2)

#### - Curvas de nivel:
Sirve para funciones de R² -> R, grafican los cortes de la superficie en un plano 2D.
**Definicion:** Curvas proyectas en un plano xy (una dimension menor), se obtienen al cortar la superficie con un plano paralelo a xy a diferentes alturas de z.
- Se calcula igualano la variariable dependiente a una constante o la funcion a una constante. f(x, y) = k
- ![[Pasted image 20260427133654.png|525]]
- Se utiliza cuando por ejemplo la superficie es muy compleja de graficar y se debe analizar de forma mas precisa en un plano.
- Se debe encontrar una forma canonica manipulando la funcion para permitir determinar su forma.
**Formas:**
- **Circunferencia (mismo coeficiente):** x²+ y² = R²
- **Elipse (divide o multiplica terminos diferentes):** (x² / a²) + (y² / b²) = 1
- **Parabola (se multiplica con k):** y=ax² o x=ay² (Guia x: abre hacia arriba/abajo; y: habre para los costados 'horizontalmente') Una variable está al cuadrado y la otra está lineal.
- **La Hipérbola**: (x²/a²) - (y²/b²) = 1 (Dos curvas que se escapan una de la otra).

**Practica:**
	carpeta.

#### - Superficies de Nivel:
Mismo concepto que curvas de nivel, pero en una dimension extra.
Para valores constantes en f(x,y,z) = k0, k1, k2, etc... Se obtiene una superficie en R³, El grafico es en R4
En caso que se quiera apoyar un plano sobre un punto de la superficie la ecuacion a utilizar es:
![[Pasted image 20260427145040.png]]
Ejemplo:
f(x,y,z) = x²+y²+z² = k
Se obtienen superficies de una esfera de radio Raiz(k)
- Se extiende mas en grandiante y matriz jocabiana.

Superficies posibles: Tip para encontrar la forma: Aisla las variables y luego fijate sus signos/exponentes.
- Paraboloide Eliptico: z = x²+y² ; Similar a una copa de vino, entre mas grande el valor de z, mas grande sera la copa. (Circuenferencias/elipses cada vez mas grande).
- Cono: z² = x² + y² (puede estar con raiz): Las circunferencias/elipses crecen de forma proporcional, a diferencia del paraboloide que no.
- Paraboloide hiperbolico (silla de montar): z = y²-x² ; Al haber un signo negativo, te quedan hiperbolas.
- Esfera: x² + y² + z² = R² (tambien puede estar sobre una raiz) ; En el ecuador comeizan en su maximo diametro y lo van redujendo por ambos lados hasta llegar a un solo punto.
**Practica general:**
- Diapositiva 11
	Identificar:
	- Dominio e imagen:
		- Conjunto de vectores del primer espacion que contienen una imagen real en el segundo espacio. f: R² -> R / D C R²
	- Espacio de representacion.
		- Consiste en la suma de los espacios del primer y segundo conjunto.
	- Relacion con z, con los tipos de superficies y conicas con su desarrollo correspondiente (trazas, figuras, etc...).
		- La funcion f(x,y) = (...), se puede representar como z = (...), de esta forma la funcion se puede despejar para poder encontrar una conica que permita graficar la funcion en el espacio.
		Ej: f(x,y) = x² + y²
		-  z = x² + y²
		- intercambiamos la variable dependiente "z" por una constante "k"
		-  k = x² + y²
		- Y depejamos las variables para que nos quede como una conica.
		- Luego le vamos asignando valorea a "k" (concepto curvas de nivel), para formar una figura en un plano xy.
#### - Limite y continuidad:
Concepto de limite R -> R: Analizar la funcion en un punto determinado aproximandose infinitamente a el sin tocarlo. Lim (x->0) 1/x; por ejemplo. (X -> Xo)
**Definicion:** Decir que el límite de f(x) , cuando X -> Xo 0 , es L, significa que estando x cerca de Xo (en el dominio) se tiene f(x) cerca de L (en la imagen). El concepto de “cercanía” en la recta lo podemos establecer con la idea de “entorno”: un entorno de centro Xo y radio δ.

En limites de R -> R existen solo 2 formas de acercarse (izquierda o derecha), para limites de R² -> R, se puede acercar al punto desde infinitas formas diferentes (infinitas rectas con diferentes posiciones e inclinaciones que lo intersectan).
- El limite se posiciona en un disco abierto.
- Un disco (D) abierto es el conjunto de puntos que satisface: ![[Pasted image 20260427153806.png]]
	- Puede estar abierto o cerrado segun si aparece <= (cerrado) o < (abierto)

**Tipos de punto:**
- Se condidera un punto frontea al punto que se encuentra en el limite de un disco cerrado, Analiticamente es cuando al realizar un circulo en el punto que estas, sea del tamaño que sea, tomas puntos que no estan dentro del disco (No pertenecen a D).

**Calculo de limite:**
- Definicion de limite: ![[Pasted image 20260427155500.png|644]]
	- Definir el limite por definicion es la unica forma real de confirmar si el limite existe o no.
- Otros metodos: Cuando la funcion es compleja y no se puede verificar por definicion, entonces usamos otros metodos para probabilizar si el limite existe o no. (Si cualquiera de los motods arrojan que el limite no existe, entonces se descarta).
	- **Simultaneo:** Se considera y remplaza simultanealmente a las variables que contiene el limite (Remplazas por las variables).
		- Lim (x->0;y->0) = $3^x - 5y$ = 1
		- Si da una indeterminacion, se busca operar la funcion, factorizarla, simplificarla para poder levantar la indeterminacion (resolverla).
	- **Secuencial:** Se evalua los limites de forma secuencial: Uno por variable, despejando asi y dejando una unica variable para remplazar al final.
		Lim(x->0;y->0) = Lim(x->0)[ Lim(y->0) = (y+x) / (x-y) = x / x ] = Lim (x->0) = (x/x) = 1
		Lim(x->0;y->0) = Lim(y->0)[ Lim(x->0) = (y+x) / (x-y) = y / -y ] = Lim (y->0) = (y/-y) = -1 (Diferentes, no existe limite).
		Se evaluan de ambos lados, si coinciden, entonces es mas probable que exista.
	- **Limite radial:** Consiste en remplazar una de las variables por una funcion, y de esa forma poder acercarse por todas las rectas que pasan por ese punto.
		Se utiliza la ecuacion y = xm, para remplazar "y". Se pueden usar cualquier otra trayectoria (cubica, cuadratica) mientras pase por el origen.
		- Si xm queda como una funcion dependiente (el resultado del limite depende de como varie "m"), entonces el limite no existe.
		- "m" se debe simplificar o no alterar el resultado del limite para determinar que el valor resultante exite.
		- Lim (x->0;y->0) = (5y-x)/x²+y => Remplazamos 'y' por mx (recta lineal) => (5mx-x)/x² haciendo factor comun nos queda el limite dependiente de m, no hay limite.
**Conclusiones:** 
- Si el limite doble no existe pero el resto de limites dan iguales: Entonces el limite 'L' es posible que exista como limite de la funcion.
- Si no es igual en alguno de estos metodos, entonces el limite NO EXISTE.

**Continuidades:**
Se deben cumplir 3 condiciones para que exista el limite:
- La funcion debe existir: Si me paro en el punto (Xo,Yo) y remplazo los valores en la funcion, esta debe arojar un valor valido.
- El limite doble debe existir: Todas las trayectorias deven llevar al mismo valor.
- El valor obtenido al evaluar el punto en la funcion tiene que ser igual al obtenido en el limite.

**Discontinuidades:**
Cuando la continuidad no se cumple, entran los casos especificos.
- **Discontinuidad Evitable**: El limite existe pero la funcion da un valor no valido en ese punto. El limite levanta la indeterminacion.
- **Discontinuidad Esencial**: Cuando el limite NO EXISTE, entonces se descarta el analisis. La funcion esta irremediablemente rota.

#### - Derivadas parciales:
**R -> R: En AM1** las planteabamos como una herramienta que mide el **ritmo de cambio instantáneo** entre una cosa y la otra, el valor de la derivada da como resultado el valor de la pendiente de la recta tangente en un punto (Xo, f(Xo)).
Representan la velocidad a la que sube o baja la superficie si te movés únicamente en una dirección, el valor resultante obtenido es exactamente la pendiente de la recta propuesta.
![[Pasted image 20260428153544.png|299]] Cuando el limite existe, entonces ese punto es diferenciable.

**f: R²-> R Ritmo de cambio en funciones de 2 variables.**
	Al haber 2 variables, se analizan de forma parcial, verificando el ritmo de cambio individual de cada variable. El ritmo de cambio de la funcion z = f(x,y) en base a una variable se le llama derivada parcial con respecto a -variable correspondiente-
	Primeras derivadas parciales (si el limite existe): ![[Pasted image 20260428154218.png|240]]
	Para derivar con respecto a una variable debemos:
		- Tomar como constante la variable opuesta, convirtiendo la otra variable de la funcion como "delta" de la variable a derivar.
	Para resolver una derivadas parciales se utilizan conceptos de AM1 pero aplicados a las derivadas parciales como:
		- Tabla.
		- Despejes e distribuciones.

**Interpretacion geometrica:**
Cada derivada parcial con respecto a una variable da como resultado una pendiente: La combinacion de pendientes fy(Xo,Yo) es la pendiente de la recta que esta "apoyada" sobre el punto. (T2)
Se forma la "funcion" o "curva" debido a una interseccion de un plano perpendicular al eje. Determinanfo un punto de analisis para poner en practica la derivada.
![[Pasted image 20260428160509.png|145]]

**Practica:**
f(x,y) = ln(x²-2sen(y)) = Desarrollo por tabla y regla de la cadena, carpeta: Fx(2x/(ln(x²-2seny))); Fy((-2cosy)/(ln(x²-2seny)))

**Plano Tangente – Función Afín**
EL plano tangente es el plano que mejor aproximala superficie S cerca del punto P, se lo conoce como funcion afin.
Se construye a partir de las rectas tangentes T1​ y T2​ generadas por las derivadas parciales de la función en un punto específico.
	El punto pertenece a la superfice.
	La funcion cuienta con derivadas parciales en el punto.
	Al intersectar los planos verticales de X = Xo y Y = Yo, se obtienen las curvas de la superficie. Estar curvas permiten trazar las rectas.
Es un plano que contiene ambas rectas.

Ecuacion explicita (partiendo de la ecuacion general del plano):
![[Pasted image 20260428171417.png]]
	Procedimiento: Se debe realizar la derivada parcial de ambas variables, evaluarla en el punto, y luego remplazar en la ecuacion explicita junto al punto.
	Se debe tener el dato de: La funcion original y el punto a evaluar.
Se usa para aproximaciones, extremos, puntos criticos, etc...

**Practica:** Carpeta

**Derivadas parciales de orden superior:**
Consiste en hallar las derivadas segundas, terceras, etc...
Para lograr esto, se debe derivar 2 o mas veces segun la derivada de orden que se quiera.
Ejemplo para derivada segunda: Fxx: Se deriva Fx y el resultado se vuelve a derivar con respecto a x. De forma analoga con Y.

**Derivadas parciales mixtas/cruzadas:**
Consiste en derivar parcialmente por una variable y luego derivar por la otra, representado por ejemplo en la funcion f(x,y): Fxy(x,y) o Fyx(x,y).
Existe un teorema que afirma que Fxy = Fyx, por lo que los resultados en ambas derivadas parciales mixtas deben ser iguales.
Esto aplica tambien a casos donde se derive mas de 2 veces, pero manteniendo la relacion entre variables, ejemplo:
![[Pasted image 20260428173625.png|269]] **Teorema de Clairaut**
	Las derivadas parciales involucradas deben ser **continuas** en la región donde estás trabajando.

#### - Derivada de funciones vectoriales:
**Derivada totales.**
Consiste en derivar cada una de las funciones componentes en todas las direcciones posibles.
f: $R^n -> R^m$: f(X) = (f1(X), f2(X), fm(X)); para cada X = (x1, x2, x3) 
De aqui nace el determinante/jocabiano que permite agrupar todas las derivadas en una unica estructura:

Es una tabla organizada que contiene todas las derivadas parciales posibles de una función que tiene varias entradas y varias salidas.
Representa la derivada total de las multiples entradas y salidas correspondiente a su dimension.
- Si tenés n variables de entrada y m funciones de salida, la matriz tendrá **m filas** y **n columnas**.
	- Columnas: Representan las variables de entrada.
	- Filas: Representan las diferentes funciones que devuelven la salida
- Cada funcion componente, es sometida a una derivada parcial de cada variable, y se organiza en una estructura matricial.
![[Pasted image 20260330165130.png|357]]
**Gradiante de una funcion vectorial**: Es un caso especial donde la matriz jocabianan tiene una unica fila, resultando en un vector resultante llamado **Gradiente** (∇f)
	 $f:R^n -> R$
	 El Gradiente es un vector que vive dentro del Jacobiano. Si la función es simple (una sola salida), el Jacobiano "colapsa" y se convierte en el Gradiente. Se puede tener multiples derivadas parciales dentro de un mismo Jocabiano, pero cada una individualmente es un gradiante.
	![[Pasted image 20260428202811.png|273]]

**Diferencial/incremento de una funcion:**
$f:R^n -> R^m$
- Ambos calculan lo mismo pero de diferente forma: Calculan el cambio exacto que ocurre en la funcion: Geometricamente es el cambio de altura de un punto a otro (Todo pasa en el eje vertical). (En una funcion plana el incremento Δf es "0")
	**El diferencial $df$:** Lo calcula el cambio mediante una aproximacion, multiplicando la derivada total (la pendiente de la recta tangente/jocabiano) multiplicada por la diferencia en x a calcular (cuanto tenes que avanzar). El resultado de esa multiplicacion es un valor.
	**El incremento verdadero** Δf​: Es el cambio exacto y real de la funcion, y se calcula mediante, **Δf=f(x+Δx)−f(x)** (Lo que avanzamos vs el inicio). 
- Cuando los cambios/deltas son muy pequeños, (Δx, Δy), el diferencial y el incremento son muy similares.
- Cuando tenes multiples coordenadas, el resultado del incremento verdadero es un vector de resultados.
- ![[Pasted image 20260428202544.png|256]]

Se define el diferencial total de una funcion como: ![[Pasted image 20260428193714.png|342]]

#### - Derivada direccional, gradiante
Permite medir la inclinacion (pendiente) en cualquier direccion que existe:
Tanto Fx(x,y) como Fy(x,y) nos sirven para calcular la derivada direccional.
Se definen 3 componentes para la derivada direccional:
- La funcion.
- Un punto para evalular la funcion.
- Un versor.
Definimos las derivadas direccionales como: Producto punto entre el jocabiano (gradiente) y el versor.
![[Pasted image 20260429161016.png|437]]
- **Descripcion:**
	- Se encuentra a la matriz jocabiana evaluada en un punto, dando como resultado un vector: f'(Xo)
	- Se identificar un vesor que multiplica la matriz jocabiana: 'u' es un vector unitario, osea que su modulo es 1. Sirve para indicar hacia donde ser quiere mirar.
	- Estas derivadas deben cumplir con las condiciones de diferenciabilidad.

La formula para calcular la derivada direccional evitando usar el limite es: Producto punto entre la matriz jocabiana que representa (para una funcion real) el gradiante y el vector direccion (indica hacia donde hacer la derivada, seria la direccion), debe ser unitario, osea su modulo debe valer 1.
Se puede calcular para cada funcion derivada que se encuentre en la matriz, si hay una unica funcion (R² -> R), entonces le llamamos "Gradiante".
- Para transformar un vector a unitario se debe:
	- Dividir cada componente por su modulo. u = (Xo/(||v||), Yo/(||v||))
	- Su modulo se obtiene de pitagoras: Abs(v) = Raiz(x²+y²)

**Interpretacion geometrica:**
- La ecuacion z = f(x,y) representa la superficie.
- En esta superficie se plantea un plano, que pasa por el punto 'p' y siguiendo en direccion del vector u
- Al realiza este corte con la figura, se crea una "curva" en la superficie.
- La derivada direccional es la pendiente de la recta tangente que toca al punto y a la curva formada.
	- Para determinar cual es la derivada direccional se debe obtener la pendiente de la recta apollada en la curva y que pase por el punto 'p', te dice que tan empinada esta la recta.
**Casos particulares:**
Para los vectores canonicos (0,1) y (1,0), coinciden exactamente con las derivadas en 'x', o 'y'.
Esto demuestra que la derivada direccional se forma a partir de la derivada en x e y.

**Practica:**
Carpeta. Consiste en realizar la derivada de ambas variables, evaluarlas en un punto, quedando (Xo,Yo) y evaluar cada coordenada de u individualmente, luego de haber transformado u en versor.
Osea se multiplican y luego suman los resultados.
(Fx(Xo,Yo), Fy(Xo,Yo)) * (Ux,Uy) = Derivada direccional. = Fx(Xo,Yo)Ux + Fy(Xo,Yo)Uy

**Gradiante de una funcion vectorial:**
Consiste en determinar al **vector gradiante** como la **derivada total** de una **funcion vectorial** **evaluada** **en Xo**.
Osea es la derivada total de una funcion, evaluada en Xo.
**El Gradiente (∇f):** Es el nombre específico que le damos a ese vector de derivadas parciales cuando trabajamos con funciones que devuelven un solo número.
Es equivalente a la matriz jocabiana * el versor, solo que el Gradiante tiene una unica fila.
![[Pasted image 20260429172759.png]]

Determinando la derivada direccional en terminos del gradiante como:
![[Pasted image 20260429172930.png|232]]

**Diferencias Gradiante y matriz jocabiana:** Es el ritmo de cambio de las diferentes funciones, solo que diferenciado por cantidad.
- Jocabiano: Se visualiza como un vector fila, que utiliza la multiplicacion matricial con el versor para obtener la pendiente.
	- En el caso de **multiples funciones** ($R^n -> R^m$) en vez de ($R^n -> R$) la pendiente **deja de ser un numero real y pasa a ser un vector.**
	- Cada fila (cada funcion) tiene su correspondiente pendiente, ubicada en su coordenada. Habra funciones como cantidad de filas de la matriz como cantidad de coordenadas de la funcion resultante.
- Gradiante es un vector columna que al realizar el producto punto permite multiplicar con el versor y obtener la pendiente.
	- El gradiante se denomina con una unica funcion, cumpliendo: ($R^n -> R$) 

**TEOREMAS: Determinar direcciones de crecimiento minimas, maximas y neutras:**
1) **Terreno plano (Neutro):**  Si el gradiante es 0, entonces la pendiente es 0 para todo U. Si todas las derivadas parciales del vector gradiante dan cero.
	![[Pasted image 20260429190741.png|431]]
	Tambien, te moves en direccion PERPENDICULAR al gradiante, la pendiente seguiria neutra, ya que estas caminando por una curva de nivel (corte con el plano).
	![[Pasted image 20260429193754.png|383]]
2) **Direccion de maximo crecimiento (Maximas):** La direccion esta dada por ∇𝑓 (Xo) (el vector gradiante es la direccion de mayor crecimiento), el valor maximo que alcanza la derivada en ese punto es: ||∇𝑓(Xo)||
	Consiste en despejar y buscar el maximo valor de esta funcion: ∇f(Xo)⋅u = ∣∣∇f(Xo)∣∣ ⋅ ∣∣u∣∣ ⋅cos(θ) -> El maximo de u = 1, El maximo de cos = 1 y sucede cuandoel angulo es de 0 grados (Sin cambiar la direccion del gradiante).
3) Direccion de minimo crecimiento (Minimo): Es el opuesto al gradiante: -∇𝑓 (Xo), el valor minimo que alcanza esta dado por -||∇𝑓 (Xo)||
	Consiste en ir en sentido contrario al gradiante: Lo que significa que el angulo que debes tomar en el cos, es de 180, que simboliza el valor minimo que puede tomar: '-1'.

#### - Valores extremos:
Consiste en los maximos y minimos de una region definida.
	¿Region abierta o cerrada?
	¿Como se calcula un maximo y un minimo? ¿Que significa geometricamente?
	¿Que son los valores extremos? ¿Existen de diferentes tipos (locales, totales, etc...)?

**Valores extremos locales:**
- Se expresan en funciones f(x,y) R² -> R, definida en una region abierta D, conteniendo un punto(Xo,Yo).
	Se dice que:
	- Existe al menos un punto de la zona D, que la funcion f(x,y) alcanza un valor maximo local en Xo, si se cumple que:
		- ![[Pasted image 20260430152401.png|375]]
		- Ningun otro punto (x,y) de la grafica cercano a f(Xo,Yo), es mas alto.
	- Existe al menos un punto en D donde f(x,y) representa un valor minimo local en Xo, cumpliendo con:
		- ![[Pasted image 20260430152548.png|374]]
		- Ningun otro punto (x,y) de la grafica cercano a f(Xo,Yo), es mas bajo.
	Denominamos a f(Xo) como punto extremo de la funcion.
	Si se encuentra un punto relativo/local, entonces son puntos critico.

**CONDICION NECESARIA**: Determinar puntos criticos
- Existencia de los puntos criticos: Son puntos "candidatos" para ser considerados criticos.
	- este es un punto critico si
		1) f(x,y) es una funcion **definida y continua** en una region abierta D que contiene el punto (Xo,Yo).
			- Debe ser, sobretodo continua, ya que si es discontinua estas tratando partes de la funcion, y no podes derivar alli porque no tenes funcion para derivar.
		2)  ![[Pasted image 20260430154225.png]] Si el gradiante es igual a "0", Si todas las derivadas dierccionales son 0.
			Hay un plano tangente en el punto. La pendiente es "0", por lo tanto es perfectamente horizontal.
		3)  ![[Pasted image 20260430155104.png]]
			Si la superficie tiene una punta o arista que no permite calcular la pendiente.

**Calculo de los puntos criticos:** Esto sirve debido a que estas diciendo que la derivada en ese punto vale "0", osea su pendiente es "0", una vez planteado eso, despejas la variable para encontrar en que coordenada se ubica el "0".
- Se realiza la derivada de las 2 variables (x, luego y)
- Se iguala a "0" y despeja la variable correspondiente.
- El valor resultante se asigna a la coordenada de un vector, y gracias a ello se consigue el punto critico.

**CONDICION SUFICIENTE:** (Naturaleza de los extremos relativos):
- Para esto usaremos el criterio de la segunda derivada o el hessiano.
- Formula determinante:
	- ![[Pasted image 20260430161351.png]]
	- Se realiza derivada segunda de ambas variables y se resta por su derivada cruzada al cuadrado (ya que ambas derivadas cruzacas valen lo mismo).
- Hessiano: Es una aproximacion de segundo grado.
	- ![[Pasted image 20260430161448.png|280]]
	- Es un metodo para calcular el determinante de forma mas grafica, se plantean las diferentes derivadas dobles y cruzadas y se multiplican de forma cruzada.
	- Este es una matriz hessiana con todas las derivadas se segundo grado.
	- Para obtener el determinante, que es un valor y se utiliza para evaluar si es maximo/minimo/silla, se debe: Multiplicar cruzado y restar resultados, como indica la formula del determinante.

**INTERPRETACION PUNTOS CRITICOS (MAXIMO, MINIMO O SILLA):** 
- Consiste en identificar 4 posibles situaciones:
- ![[Pasted image 20260430161641.png|412]]
- Si el resultado del determinante es > 0
	- Si la derivada segunda es tambien > 0 entonces es un MINIMO RELATIVO (en el punto (Xo,Yo)), La concavidad es habia abajo, estoy en un maximo: n
	- Si el resultado de la derivada segunda es < 0, entonces es un MAXIMO RELATIVO. La concavidad de la funcion abre hacia arriba, asi que estoy analizando un minimo. u
- Si el determinante es < 0, entonces se denomina punto silla, osea no existe maximo ni minimo. (En diferentes direcciones marca un tipo de punto diferente, Ejemplo: Izquierda es maximo, hacia delante es considerado minimo).
- Si el determinante es = 0, entonces no se puede determinar que es, el criterio no es concluyente.
	- Esto sucede cuando las derivadas segundas no llegan a identificar el cambio de pendiente, debido a que son muy chatas.
	- Para identificar si es maximo o minimo se deben evaluar las derivadas terceras/cuartas.


**Extremos condicionados (Multiplicadores de lagrange)**
Consiste en encontrar los pujntos criticos para determinar si es maximo o minimo o punto sillla pero bajo una restriccion (una funcion).
Utilizamos los multiplicadores de lagrange para encontrar los puntos bajo la restriccion.
𝐹(𝑋, 𝜆𝑖) = 𝑓 (𝑋) + 𝜆1𝐺1(𝑋) + 𝜆2𝐺2(𝑋) + ⋯ + 𝜆𝑛𝐺𝑛(𝑋)
	Compuesta por:
	- F(x): La funcion a evaluar.
	- G(x): La funcion restriccion, puede ser una o varias. SE EXPRESAN DE FORMA IMPLICITA.
	- 𝜆: Los multiplicadores de lagrange, cada funcion restriccion lleva uno diferente. Permiten encontrar los puntos criticos cuando el gradiante es proporcional a la restriccion.
Pasos para **encontrar los puntos criticos de la funcion con restricciones:**
1) Realizar derivadas parciales de todas las variables incluido 𝜆.
2) Resolucion del sistema: Consiste en despejar, normalmente '𝜆', para luego igualar las 2 ecuaciones y con eso encontrar la relacion entre 'x' e 'y'.
3) Remplazas la relacion encontrada en la restriccion, para obtener los puntos criticos.
**Evaluar puntos criticos de funciones condicionadas:**
- Se debe despejar la funcion condicion y evaluar las derivadas dobles en ella: Se realiza con la funcion condicion ya que es la que delimita el espacio de la funcion original.
- El metodo consiste en simplificarla a una funcion de una variable:
	- Se define la funcion condicion.
	- Se despeja una variable.
	- Se remplaza la variable despejada de la funcion condicion (Metodo sustitucion).
	- Se opera hasta obtener la derivada primera y luego la segunda, y tambien las cruzadas.
	- Se evalua en el punto para obtener las derivadas segundas y cruzadas evaluadas.
	- Se remplazan en la funcion del determinante y se verifica si es maximo/minimo/silla,etc...

## RA2:
### Integrales dobles:

#### - Definicion integrales dobles:
- Las integrales definidas sirven para medir magnitudes de todo tipo, como: area, volumen, longitud, superficies, etc...
- Las integrales dobles amplian su uso utilizando 2 variables en vez de 1.
- Las integrales dobles $\int \int$ representan el estado R² -> R
	- Partimos de 2 variables y nos devuelve un unico valor.
- Calcularemos en esta unidad integrales DEFINIDAS.

**Interpretacion geometrica:**
Considerando una ecuacion z = f(x,y) continua en una region del plano xy:
- Nuestro objetivo es hallar el volumen del solido, comprendido entre la region del plano xy y la superficie.
- Osea basados en una funcion de 3 dimenciones, delimitamos un plano entre los ejes xy para luego obtener el volumen entre ese plano y la superficie representada por la ecuacion de 3 dimensiones.
- ![[Pasted image 20260502133845.png]]
La region del plano xy se subdivide en multiples rectangulos pequeños (lados: Δx; Δy).
- En base a un punto (xi,yi) en el rectangulo contruimos lo llamado como "prisma rectangular", que parte desde el plano xy hasta tocar a la superficie. Teniendo una altura de f(xi,yi)
- El volumen de cada prisma sera: V =f(xi,yi)Δxi,Δyi, osea el volumen esta dado por: Altura * base (Altura * Ancho * Largo)
- Utilizando la suma de riemman podemos determinar una aproximacion del volumen total de la region del plano xy determinada con respecto a la superficie.
	- ![[Pasted image 20260502134428.png]]
	- Cuanto mas pequeño los rectangulos, mayor sera la aproximacion. Como ya sabemos, esa sumatoria se transforma en la integral.
- Definimos la integral doble como:
- ![[Pasted image 20260502134520.png]]
- **Si el limite existe, entonces la funcion es integrable en la region.**
- Determinamos la integral doble que se operara por partes (primero se integra por una y luego por la otra).

**Calculo:**
Para calcular el volumen de una cierta area del plano xy con respecto a la superficie, se utiliza esta formula de integrales.
![[Pasted image 20260502134708.png]]

La primera integral a calcular es la de las funciones, la segunda integral a calcular es la de los limites.
Esta hecho de esta forma para que el resultado si o si devuelva un valor numerico.

**Propiedades:**
![[Pasted image 20260502134739.png]]

#### - Regiones de integracion rectangulares.
- Se especifica la formula para calcular esta integral doble, que es no mas que realizar la integral doble por partes, inicialmente con un d y luego con el otro d.
- Si se realiza la integral doble al revez, tambien da el mismo resultado.
![[Pasted image 20260502155248.png]]

#### - Regiones de integracion NO rectangulares.
- Consiste en integrar cuando el plano no es un rectangulo perfecto.
![[Pasted image 20260502155801.png|343]]

En base a esto se plantea el teorema de fubini: Que permite demostrar una forma de resolver integrales dobles en base a regiones no rectangulares.
![[Pasted image 20260502155915.png|471]]
- Consiste en que una integral doble se divide en el calculo de 2 integrales individuales, mientras la funcion a calcular sea continua en los intervalos.
- Estan delimitadas por 2 valores que permiten definir la zona de integracion.
Existen 2 tipos de regiones NO recangulares:
1) **Region Verticalmente simple:**
	- Aqui el area de integracion esta entre medio de 2 funciones, que a vista son horizontales, pero donde su integral se visualiza de abajo para arriba.
	- Se basa en la variable y, se calcula en base al eje y, osea verticalmente..
	- ![[Pasted image 20260502160732.png|297]]
	- La region esta delimitada por 2 valores (a, b) que permiten delimitar el volumen a calcular.
	- ![[Pasted image 20260502161018.png|403]]
2) **Region Horizontalmente simple:**
	![[Pasted image 20260502161203.png|267]]
	- Se calcula de izquierda a derecha, comienza en izquierda y se termina de calcular en derecha.
	- Se basa en la variable X, se calcula en base al eje x, osea horizontalmente.
- La razon de porque se calcula de izquierda a derecha o de abajo hacia arriba es que se debe integrar en direccion donde crecen los ejes. Sin embargo se puede calcular de forma inversa a donde crecen los ejes (ejemplo primero derecha y luego izquierda) pero esto provoca que el volumen o area final quede en negativo.
- Siempre se espera que vayas del valor mas chico al mas grande.
Se debe interpretar el grafico y buscar la mejor forma para integrar, osea la mas simple, esto provocara que se deba elegir un metodo, ya se vecticalmente simple o horizontalmente simple.

#### - Calculo de area:
Para esto debemos considerar la funcion f(x,y) = 1, esto simboliza que la "altura" es 1, que representa el area. Esto es la base teorica.
- El calculo es igual a las integrales dobles comunes, solo que no hay una funcion base, sino que simplemente se evaluan las funciones de la integral.
- Se debe determinar la funciones.
- Se determinan los rangos o valores.
- Y se grafica todo para determinar con que funcion nos estamos enfrentando.
- En base a eso se plantea la integral correcta. Organizandola y utilizando el metodo mas simple para los calculos.
	- Esto incluye encontrar una zona que no tenga diviciones y permita un calculo limpio.
- Se calcula y evalua para obtener el valor final del area.

- **Se debe aprender a graficar el resinto.**
Practica: Carpeta.

# EJERCICIOS PRACTICOS:
### 1) Detallar pasos a seguir en cada resolucion para una mayor comprension.
### 2) Justificar la resolucion mediante funcion generica (teoria).

### Plantear rutina para la practica de todos los temas.
Bien, aqui el tema es claro, tengo 4 dias completos para practicar AM2, preparme para ser capaz de resolver cualquiera de los 5 temas individuales que hay.
Hay que implantar un plan de estudio infalible que abarque todas las unidades y me permita estar preparado para el momento del parcial.

Primero debemos plantear que necesito:
- Ser capaz de resolver cualquier problema de cualquier unidad, osea dominar todas las unidades.
- Ser capaz de combinar teoria y practica de diferentes temas en un mismo pacial.

En base a esto planteamos la **mecanica a seguir**:
**RUTINA PRACTICA:**
- **Realizar una practica intensa de la unidad en cuestion.**
	- Priorizar temas a practicar, enlistados en la pestaña cuestionario repaso.
	- Minimo 5 ejercicios por dia.
- **Realizar un preparcial que agrupe varios temas.**
	- Tomar preparciales de la catedra.
	- Fotos whatsapp.
	- Pedir a la IA preparciales.
- **Repasar teoria basica, recall.**
	- Que significa geometricamente.
	- Porque se realiza de esa forma (metodo a seguir).
	- Terminologia (ecuaciones generales).

**Todo lo que no se entienda o genere un error, corregirlo, repasarlo y entenderlo.**

### Guia de propiedades basicas de la matematica
> **Potencias:** Reglas para combinar exponentes (sumar en productos, restar en divisiones, multiplicar en potencias de potencias).
    
- **Límites:** El comportamiento de las funciones cuando te acercás a un punto, respetando las operaciones básicas.
    
- **Fracciones:** Cómo operar "paquetes" de números, desde la suma cruzada hasta la multiplicación directa.
    
- **Divisiones:** El arte de repartir el denominador (distributiva) y simplificar términos.
	
- Logaritmos: Calcula el exponente al que se debe elevar la base para obtener el resultado.

---

#### 1. Propiedades de las Potencias (El motor del álgebra)

Para laburar con derivadas parciales, estas reglas son la posta para simplificar antes de derivar:

- **Producto de igual base:** $x^a \cdot x^b = x^{a+b}$
    
- **Cociente de igual base:** $\frac{x^a}{x^b} = x^{a-b}$
    
- **Potencia de otra potencia:** $(x^a)^b = x^{a \cdot b}$
    
- **Distributiva (SOLO en producto y división):** $(x \cdot y)^a = x^a \cdot y^a$ y $(\frac{x}{y})^a = \frac{x^a}{y^a}$.
    
- **Exponente negativo:** $x^{-a} = \frac{1}{x^a}$ (Esto te salva la vida para derivar fracciones como potencias).
    
- **Exponente fraccionario:** $x^{a/b} = \sqrt[b]{x^a}$ (Clave para funciones como la que vimos de la raíz cúbica).
    

---

#### 2. Propiedades de los Límites (El borde de la función)

Si el límite de $f(x,y)$ y $g(x,y)$ existe, entonces se portan bien:

- **Suma y Resta:** $\lim (f \pm g) = \lim f \pm \lim g$
    
- **Producto:** $\lim (f \cdot g) = \lim f \cdot \lim g$
    
- **Cociente:** $\lim (\frac{f}{g}) = \frac{\lim f}{\lim g}$ (siempre que el de abajo no sea cero).
    
- **Constante:** $\lim (k \cdot f) = k \cdot \lim f$
    
- **Potencia:** $\lim (f^g) = (\lim f)^{\lim g}$
    

> **Ojo en Análisis II:** Para que el límite exista en varias variables, te tiene que dar lo mismo por **cualquier camino** que elijas. Si por dos caminos distintos te da diferente, chau, no hay límite.

---

#### 3. Fracciones y Divisiones (Repartiendo el bardo)

- **Suma/Resta (Mariposa):** $\frac{a}{b} \pm \frac{c}{d} = \frac{ad \pm bc}{bd}$
    
- **Multiplicación (Derecho):** $\frac{a}{b} \cdot \frac{c}{d} = \frac{a \cdot c}{b \cdot d}$
    
- **División (Cruzado o "Oreja"):** $\frac{a}{b} : \frac{c}{d} = \frac{a \cdot d}{b \cdot c}$
    
- **Distributiva del denominador:** $\frac{a + b}{c} = \frac{a}{c} + \frac{b}{c}$.
    - _Importante:_ Al revés **NUNCA** se puede: $\frac{c}{a+b} \neq \frac{c}{a} + \frac{c}{b}$.

---
#### Guía de Propiedades de los Logaritmos

Che Alexis, estas son las herramientas que te van a salvar las papas cuando tengas que descular integrales o despejar variables en el parcial de la UTN.

1. **Logaritmo de la unidad**
    $$\log_b(1) = 0$$
    Cualquier número (base) elevado a la $0$ siempre te va a dar $1$.
2. **Logaritmo de la base**
    $$\log_b(b) = 1$$
    En ingeniería vas a ver mucho el logaritmo natural ($\ln$): $\ln(e) = 1$, porque la base es el mismo número $e$.
3. **Logaritmo de un producto**
    $$\log_b(M \cdot N) = \log_b(M) + \log_b(N)$$
    Si tenés cosas multiplicándose adentro, las podés separar sumando.
4. **Logaritmo de un cociente**
    $$\log_b\left(\frac{M}{N}\right) = \log_b(M) - \log_b(N)$$
    Esta es clave. La usamos recién para resolver la integral de $\frac{1}{x+1} - \frac{1}{x+2}$ y llegar al resultado final de $\ln(25/24)$.
5. **Logaritmo de una potencia**
    $$\log_b(M^k) = k \cdot \log_b(M)$$
    Esta es la propiedad "baja-exponente". En los ejercicios de **Extremos Condicionados**, cuando tenés algo como $e^x = e^{2-x}$, aplicás $\ln$ a ambos lados y los exponentes bajan para que los puedas despejar tranqui.
6. **Logaritmo de una raíz**
    $$\log_b(\sqrt[n]{M}) = \frac{1}{n} \log_b(M)$$
    Acordate que una raíz es lo mismo que un exponente fraccionario ($M^{1/n}$), así que es una derivada de la propiedad anterior.
7. **Cambio de base**
    $$\log_b(a) = \frac{\log_c(a)}{\log_c(b)}$$
    Generalmente se usa para pasar todo a base $e$ ($\ln$) o base $10$, que son las que manejan las calculadoras y los lenguajes de programación que usás en Sistemas.

---

### Tiempos:
**Para el preparcial de la U1, me tarde 3h 30m en los 3 primeros puntos (sin expandir el tercero).**
	Si bien extendi el tiempo al buscar informacion extra y complementar bien, los conceptos me quedaron claros.
	Debo aprender bien a como hacer el ejercicio antes del parcial, hoy puedo pausar y buscar, pero para ese momento debo estar preparado.
Preparcial U1: Tarde 1h en 2 puntos, y realmente la mayor parte del tiempo me la tarde extendiendo la informacion. 
	La cuestion es que lo aprendi a resolver bien y con caracter terminologico/teorico, permitiendome justificar bien las respuestas. Me queda practicar los demas temas mas complejos, como integrales dobles (y graficar en planos), pero por ahora vengo bastante bien. Ademas de eso, me queda reforzar la resolucion variada de ejercicios y resolver diferentes situaciones matematicas.



## Funciones vectoriales:
