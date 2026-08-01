# Temario
- **[Variables aleatorias](https://cvirtual.frvm.utn.edu.ar/mod/resource/view.php?id=136401 "Variables aleatorias"). Ley de distribución.**
	- Función de densidad y de distribución, casos discretos y continuos. 
	- Distribuciones conjuntas.
- **Definición de la Esperanza Matem.. Propiedades. Teoremas.**
	- La varianza y la desviación típica. Propiedades. Teorema.
- **[Variables aleatorias](https://cvirtual.frvm.utn.edu.ar/mod/resource/view.php?id=136401 "Variables aleatorias") normalizadas. Momentos, Función generatriz.**
- **Desigualdad de Chebyshev. Ley de los grandes números.**
- **Otras medidas de centralización y de dispersión.** (moda, mediana, etc...)

### Metodologia:
Esta sera la forma de adquirir el conocimiento:
- Estudiar y repasar tema.
- Explicar con mis palabras.
- Practicar ejercicio para afianzar.
Se realiza eso con cada tema visto.
- Se realizara un pretest rapido sobre lo visto anteriormente.
- Una vez visto todos los temas se haran pre parciales y cuestionarios de diferentes temas de forma espaciada para recordarlos. Entre mas se repasen mas solido es el conocimiento.

### Estudio:
#### - Variable aleatoria
Es una variable que toma un valor proveniente de una probabilidad o evento aleatorio por un experimento realizado.
El proceso por el cual se obtienen una secuencia aleatoria se le llama "metodo aleatorio".
	**Sintesis:** Es una "funcion" que asgina un valor numerico a cada evento posible del espacio muestral.
	Estudia el comportamiento de todos los resultados posibles, no de forma aislada.

- **Definición formal:** Una variable aleatoria, es una función real-valorada, definida a partir de los eventos elementales de un espacio probabilístico, a cada evento elemental le corresponde un número real, que es el valor de la variable aleatoria en ese evento elemental. Además para todo número real, el conjunto de eventos elementales que asume dicho valor también es un evento, así como todos los eventos elementales que se encuentran comprendidos entre un par de valores reales también forma un evento
- Usamos las utlimas letras del alfabeto para **representarlas**: X, Y, Z...

**Pueden ser discretas o continuas:**
- Pueden asumir valores determinados (Discretas). Finito, infinito contable.
- Pueden asumir cualquier valor entre un rango/intervalo del eje real (Continuas). Infinito no contable.

**Como ejemplo:**
	Se plantea un espacio muestral con diferentes elementos y combinaciones.
	A cada combinacion se le asigna un valor numerico. Este valor numerico pertenece a la variable X.
	Ahora la funcion esta creada, los puntos muestrales (resultado individual e indivisible de un experimento) estas asociados a unico valor numerico.
	No hace falta que sea un valor fijo, pueden convertirse en operaciones entre los diferentes puntos muestrales.
	Se pueden establecer condiciones asociadas a los puntos muestrales: Ej: Si en un dado sale un nro > 3: Ganas, sino Perdes:
		Entonces la variable X puede tomar 2 valores posibles en puntos muestrales.

**Relacion con los eventos:**
Se concluye que cualquier valor de la variable aleatoria es un evento.
Cada evento tiene una probabilidad, por lo cual los valores de las variables aleatorias asociados a cierto evento, tambien adquieren esa probabilidad.

**Diferencia cualitativa y cuantitativa:**
La diferencia radica en lo que se esta midiendo:
- La cualitativa trata cualidades, osea conceptos, atributos.
- La cuantitativa trata cantidades, numeros, valores determinados.
El proposito de una variable aleatoria es convertir un evento cualitativo en cuantitativo: Pasar de Cara-Cara -> 1
#### - Distribución de Probabilidades discretas
Debido a que las valores de las variables aleatorias tienen una cierta probabilidad asociada: Entonces se interpteta como una funcion de probabilidad o distribucion de probabilidad.
Se define analiticamente la funcion de probabilidad: P(X = xk) = f(xk) -> P(X=x) = f(x)
	Donde X es una variable aleatoria y los valorea posibles a tomar son x1, x2, x3, xn...
	Debe cumplir estas condiciones: 
		1 - f(x) >= 0; La probabilidad de todos los valores/eventos deben ser positivas.
		2 - Σ f(x) = 1; La suma de todas las probabilidades deben dar 1.

Se puede graficar por un esprectro o histograma.
	En un plano xy:
	- Eje x: Representa la variable aleatoria.
	- Eje y: Representa la probabilidad f(x)
![[Pasted image 20260426212754.png|388]]

#### - Funciones de distribución para las variables aleatorias discretas
Habla de una funcion de distribucion de una variable aleatoria X: Representa la probabilidad acumulada de una variable X de que tome un valor menor o igual a un numero real.
- Se define como: P(X < x) = F(x)
- La funcion distribucion se puede obtener de la funcion probabilidad notando: F(x) = P(X <= x) = Sumatoria(f(u)); u <= x


#### Distribucion conjunta:
Analiza el comportamiento de 2 o mas eventos aleatorios en el mismo espacio probabilistico.
- Se mantiene las condiciones de que: f(x,y) >= 0 (Las posibilidades son positivas) y F(x,y) = 1 (Funcion distribucion conjunta debe ser igual al total de posibilidades).
- Analiza el la probabilidad de que sueceda el evento de la Variable X, AL MISMO TIEMPO que sucede el evento de la variable Y.

**DISCRETA:** Si los valores se pueden contar
- Se organiza en tabla.$$P(X=x; Y=y) = f(x;y) \text{ [cite: 72, 152]}$$
- ![[Pasted image 20260518183727.png]]
- Cada celda tiene su probabilidad.
- Para la funcion de distribucion cumulada, se define como:
- ![[Pasted image 20260518184609.png|315]]

**CONTINUA:** Los valores son rangos no contables.
Pasa a ser una integral que permite determinar la probabilidad conjunta en un espacio en 3D.
Se debe realizar una integral doble entre las 2 variables, evaluandolas en un cierto rango.
![[Pasted image 20260518184300.png]]
Para la funcion de distribucion conjunta acumulada, se define como:
![[Pasted image 20260518184357.png|465]]

### Variables Aleatorias Independientes:
**CONDICION DE INDEPENDENCIA:** 
- Si son dependientes entre si, se puede hacer el calculo de la probabilidad condicional:
- f(x,y) = f1(x) * f2(y)
### Esperanza matematica:
La esperanza matematica son todos los posibles valores de la variable aleatoria multiplicados por su probabilidad.
Para el caso de las variables continuas, utilizamos la integral de la variable.
![[Pasted image 20260518184901.png|608]]

- DATO: Cuando las probabilidades son iguales entre si, la esperanza (E(x)) es igual a la media (u).

**Axiomas y Propiedades:**
Si f(x) es la funcion de x, y si x es una variable aleatoria:
![[Pasted image 20260518185126.png|808]]
- En la discreta es una sumatoria de la probabilidad de ese valor de x por la funcion evaluada en x, y en continua es la integral de esa misma operacion.
Si la variable aleatoria X con su E(X) esta intervenida por una constante k:
![[Pasted image 20260518185419.png|821]]

**La esperanza de dos variables aleatorias (sean independientes o no), se calcula como:**
**Multiplicacion** = E(X * Y) = E(X) * E(Y)
**Suma** = E(X + Y) = E(X) + E(Y)

#### Varianza y Desviación Estándar:
**Varianza (Var):**
Miden cuanto varian (se dispersan) los datos con respecto al promedio.
Osea: Miden la distancia promedio entre cada punto posible y su esperanza matematica, de esa forma pueden determinar cuanto "caos" hay dentro de esa variable.
	Miden si el sistema es estable y predecible o si es variante y riesgoso.
	Ej: A = (9,10,11); B = (-100, 10, 120) E(A) = E(B) = 10, tienen la misma esperanza, pero sus valores y secuencia son radicalmente diferentes.
- Si los valores son cercanos a 0: Todos los valores estan cerca del promedio, y simboliza un sistema estable y predecible.
- Si los valores son muy altos: Los valores son muy variantes con respecto al promedio y simboliza un sistema erratico e impredecible (incertidumbre).
Ecuaciones de varianza: Var(x) = E(X-u)², donde u = E(x), esto nos lleva a: Var(x) = E(x²) -  E(x)²
**V. Discretas:** Las esperanzas se calculas mediante la sumatoria del valor de la variable en ese punto por su probabilidad.
![[Pasted image 20260519171606.png|456]]
**V. Continuas:** Las sumatorias se convierten en integrales:
![[Pasted image 20260519171646.png|429]]

**Desviacion estandar ($\sigma$):**
Si se quiere calcular algo del mundo real, osea que no aplica la regla del "elemento al cuadrado", entonces se usa la desviacion estandar, que se calcula aplicandole una simple raiz a la varianza:
![[Pasted image 20260519171948.png]]
![[Pasted image 20260520160907.png]]

**Axiomas y propiedades:**
Calcular Var(x):
- Var(x) = E(x²) - u²
- ![[Pasted image 20260520160222.png|485]]
**Situacion constante Var(x):**
- Var(k) = 0
- ![[Pasted image 20260520160340.png|594]]
- Var(x+k) = Var(x)
- ![[Pasted image 20260520160401.png|680]]
- Var(k * x) = k² * Var(x)
- ![[Pasted image 20260520160431.png]]
**Situacion doble varaible:**
- Var(X + Y) = Var(X) + Var(Y)
- Var(X * Y) = Var(X) * Var(Y)
- ![[Pasted image 20260520160449.png]]
- Esta propiedad se generaliza para un número infinito de variables aleatorias independientes.


### Momentos:
Son medidas estadisticas (parametros) que describen caracteristicas geometricas y la forma de distribucion de probabilidad.
	Mide como se distribuye la probabilidad a lo largo del eje X, es analogo al (Momento de una fuerza, torque) en fisica.
La formulas se dividen en 2 categorias principales segun lo que se quiera medir (punto de apoyo):
#### Respecto al origen: (u'r)
Miden distancia con respecto al punto 0 del eje real.
	La formula es la Esperanza de la variable elevada a la potencia.
		$r(E(X^r))$
	![[Pasted image 20260520172429.png]]
	El momento mas importante es la Esperanza matematica, o media: r = 1
		u'1 = E(x¹) = u
	Otro momento relevante puede ser cuando r = 0, dando por definicion: "1":
		u'0 = E(x⁰) = 1
#### Respecto a la media: (ur)
Aqui se mide en base al promedio de la propia variable real, osea: u.
Se miden como varian los datos segun la propia variacion del sistema.
Formula: $E(X-u)^r$
	![[Pasted image 20260520172852.png|396]]

Esto denota claras propiedades del mismo calculo:
![[Pasted image 20260520173450.png|366]]

#### Relacion entre momentos: Binomio de newton.
Relacion de momento con respecto a la media y el momento con respecto al origen: ![[Pasted image 20260520174009.png]]
![[Pasted image 20260520174044.png|221]]
	Permite transformar momentos con respecto al origen (faciles de calcular) con momentos con respecto a la media (complejos de calcular).
	Usamos el **binomio de newton** para calcular el momento en r con respecto a la media. Se desarrolla el binomio de u3 = E(X-u)³ para u3 por ejemplo.
		Regla del cubo de un binomio, regla del cuadrado de un binomio, regla del binomio. SI fuera u4 seria a la cuarta potencia.
		![[Pasted image 20260520181921.png|847]]
		![[Pasted image 20260520182339.png]]

#### Funcion geratriz de momentos:
El objetivo de la funcion es generar momentos.
Es una funcion que almacena la estructura geometrica de la variable aleatoria.
La variable del problema sigue siendo la X, solo que usamos un parametro t para armar la funcion exponencial.
**Formulas:**
- Discreto: ![[Pasted image 20260520185215.png]]

- Continuo: ![[Pasted image 20260520185253.png]]

Usamos la tecnica de maclaurin para desarrollar:
![[Pasted image 20260520185450.png]]
![[Pasted image 20260520185504.png]]
Y aplicamos la esperanza matematica a ese termino $e^u$
![[Pasted image 20260520185517.png]]
	Esto nos permite, por propiedad de la esperanza matematica, calcular cada E($X^n$) individual. Extrayendo fuera los terminos constantes.
	**Caso practico:** 
		Luego se deriva por "t" y se busca igualar t = 0, esto permite eliminar "t" y quedarnos solo con las Esperanzas matematicas. Se deriva segun la potencia "r" indicada. 
		Cantidad de veces que se deriva = r
### Otras medidas estadisticas:
#### Centralizacion:
**Moda:** Es el caso donde mas probabilidad hay de que X tome ese valor, en la funcion densidad, representa el punto mas alto.
	Puede tener varios puntos mas altos, eso representa un tipo de distribucion bimodal o multimodal.
**Mediana:** Es el valor de X donde tanto su lado izquierdo como lado derecho (osea valores en positivo o negativo) son iguales, representando la mitad.
	P(X <= x) = P(X >= x) = 1/2, divide JUSTO  a la mitad la probabilidad.
	Es un valor que separa 2 mitades iguales (Separa una curva de densidad en 2 partes) que contienen la misma area, ademas esto solo existe en el caso de las variables continuas, NO existe mediana en variables discretas. (Puede no ser la unica de cada lado). Esto lleva a que pueda caer en un cierto valor o tener mas de un lado que del otro.
	Es el valor de la X que separa la probabiliadad exactamente al medio (50 - 50)% de cada lado
	EN EL PLANO CARTESIANO es una ordenada (valor de x, recta), al cortar el area en 2 mitades perfectas (1/2), permite dividir el area original en 2 mitades equivalentes.
		Es un valor numerico del eje horizontal, corta el area debajo de la curva, la corta en 2 partes iguales.
	Para el 3D se utiliza la distribucion conjunta: Se toman las medianas marginales de "X" e "Y", por separado.
		Se lanza un plano en cierto valor con respecto a X, y luego con respecto a Y.
#### Posicion:
**Percentilas:** Es una ordenada (Linea vertical) en el grafico de distribucion que divide a la probabilidad segun un cierto porcentaje determinado por la variable a.
	Determina que parte de los elementos estar por arriba y que partes de los elementos supera en ese punto especifico:
	Ejemplo: Un percentil de 10 (X10) es: Un elemento que supera al 10% y que es superado por el 90%. Un percentil de 50 (X50) es la media (Supera al 50% y es superado por el 50%) un percentil de 70 (X70): supera al 70% y es superado por el 30%.
	En sintesis un percentil supera a un Xa elementos y es superado por (100 - Xa) elementos.
	**EN LA PRACTICA:** Se pide hallar el percentil en base a una funcion de densidad, esto significa que el valor a encontrar es el limite superior, la incognita "a", se plantea la integral igualada al determinado porcentaje de percentil que se quiere encontrar.
	![[Pasted image 20260521150632.png]]
#### Dispersion:
**Recorrido:** Es la diferencia entre el valor mas grande y el valor mas pequelo de la funcion.
	Si uno de estos es infinito, el calculo carece de sentido.
	Mide la distancia desde el fondo hasta el techo de su dominio.
	R = Xmax - Xmin
	Es tosco y fragil, un dato exepcional te tira el recorrido al extremo.
**Recorrido intercuartilico:** Soluciona los problemas de el recorrido comun, manipulando las percentilas:
	Se calcula eliminando el 25% mas alto y bajo y quedandose con el 50% mas cercanos al centro de distribucion.
	RIC = X75 - X25 (Descarta los 25% superiores y le resta los 25% mas extremos, obteniendo justo los valores centrales).
	Se obtienen las percentilas de ambos valores mediante integrales, luego se restan obteniendo el valor final.
	Se obtiene una persepcion real del universo a calcular.
**Recorrido Semi-intercuartílico (RSI):**
	Consiste en obtener un valor promedio de la anterior estadistica (recorrido intercuartilico) permitiendo obtener una nocion de la desviacion promedio entre los datos del centro con respecto a la mediana del sistema estando completamente libres de los valores extremos.
	Se calcula como RI / 2, o (X75 - X25) / 2
**Desviacion media:** Es una forma de medir la dispersion. Calcula un promedio, de las distancias absolutas entre cada valor de la variable con su medida aritmetica.
	Mide a cuantas unidades de distancia se encuentra cada punto con respecto al promedio, todo eso en promedio.
	El valor absoluto permite que los datos que estan a la izquierda u derecha no se cancelen entre si dando un resultado erroneo = 0.
	Se realiza mediante D.M = E|x-u|.
	Para el caso **CONTINUO** esto se debe integrar segun el intervalo: 
	![[Pasted image 20260521153400.png]]
	La integral se separa en terminos para calcular el valor absoluto de la esperanza matematica.
	Esto lleva a calcular tanto la integral desde los rangos tomando de pivo a u (la media): (-inf, u) y otra integral del rango (u, inf).
	La integral del rango negativo (-inf, u), daria valores negativos, debido a que la media es mas grande, asi que se multiplica por -1, para poder obtener el valor real en positivo.
	Para valores **DISCRETOS**: ![[Pasted image 20260521154012.png]]
	Es simplemente la sumatoria de cada valor de X - u (media = E(x)) en valor absoluto por la probabilidad en ese valor (f(xi)). 

**Sesgo:** Analiza la distribucion de valor en una funcion, las probabilidades de estos valores rara vez son simetricos con la media, sino que estan mas inclinados hacia un cierta direccion, a raiz de esto nace el sesgo, que es **hacia donde se inclina la probabilidad con respecto a la medida.**
	Sesgo a la izquierda (La mayor probabilidad es hacia la **izquierda**, osea resultado **NEGATIVO**), permitiendo ver una "cola" mas larga en la funcion de lado derecho.
	Sesgo a la derecha (Mayor probabilidad es habia la **derecha** osea un resultado **POSITIVO**), llevando la cola de lado izquierdo.
	Distribucion simetrica: Es cuando el sesgo es igual a "0", osea no esta sesgada para ningun extremo.
	![[Pasted image 20260521155028.png]]
	El tercer momento te permite identificar el sesgo. Se normaliza con la desviacion estandar³ permitiendo normalizar los valores.
		Esto permite tener los valores a una escala adimensional.

**Curtosis:** Es una medida estadistica que permite ver el grado de aplastamiento de la distribucion de probabilidad comparada a su forma estandar.
	Mide que tan concentrdados se encuentran los datos cerca del promedio. Frente a que tan probables son los valores extraños/lejanos al promedio.
	Permite saber si la curva sera puntiaguda o plana (relativamente).
	Se encuentra con el cuarto momento, esto permite obtener valores que exageran mucho los valores extremos (estan elevados a la cuarta).
	![[Pasted image 20260521160155.png]]
	**Tipos de curtosis:** Existen 3 medidas universales para asignar un diagnostico al resultado del coeficiente a4
		**Leptocurtica (a4 > 3):** Curtosis grande: Los valores estan muy concentrados en el centro, pero sus colas laterales son gruesas y pesadas, conteniendo valor criticos extremos que pueden afectar al sistema (Eventos raros pero muy destructivos).
		**Mesocurtica (a4 = 3):** Es un punto neutro perfecto, representa la silueta clasica de distribucion normal estandar (simetrico).
		**platicurtica (a4 < 3):** Curtosis pequeña, el grafico es chato y estirado hacia las puntas, **similar a una meseta**, muestra **datos** **homogenios** entre si y **sin** **sobresaltos** o **concentracion a lo largo del eje.** SIn grandes picos ni sorpresas.

EXPANDIR: Chebyshev, LEY DE GRANDES NUMEROS Y VARIABLES ALEATORIAS NORMALIZADAS.
![[Pasted image 20260521164554.png|421]]