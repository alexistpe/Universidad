Bien, aqui describiremos la metodologia y teoria a estudiar sobre Probabilidad y estadistica en la tercera unidad.
Explicaremos la estrategica para expandir y estudiar todos los temas de forma teorica.
### Agenda:
- ~~Distribución normal o de Gauss.~~
- ~~Distribución binomial o de Bernoulli.~~ Propiedades.
	- ~~Relación entre la binomial y la normal.~~
- ~~Propiedades.~~
- ~~Distribución de Poisson. Propiedades.~~
	- ~~Relaciones entre Poisson y la normal.~~
- ~~Teorema del límite central.~~
- ~~Distribuciones hipergeométrica, Chi-cuadrado~~

### Distribucion binominal o de bernoulli:
Consiste en una distribucion discreta. Que consiste en asociar los datos de los experimentos realizados con su correspondiente base teorica.
- Nace de la repeticion de eventos individuales.
- Tiene 3 puntos fundamentales para considerarlo "ensayo de bernoulli":
	- Espacio dicotomico: Se detecta un evento particular en cada prueba realizada, llamado "Exito" con problabilidad "p", si el evento no ocurre, se toma como "fracaso" con probabilidad 1-p. El exito significa que suceda lo que estas midiendo, sin especificar que situacion exactamente.
	- Independencia: Cada experimento independiente a los demas. Osea no se alteran la probabilidad entre si.
	- Estabilidad: El valor de exito se mantiene siempre en el mismo, no varia hasta el final.
Cuando se agrupan el conjunto de pruebas realizadas, se obtiene la funcion binominal, donde:
Se basa en eventos mutuamente excluyentes (solo puede suceder uno), y colectivamente exaustivos (al menos unos de los dos ocurrira).
La funcion de probabilidad queda definida por la "formula de la caja": f(x) = (X = x) = (n x) * $p^x$ * q^n-x
- El recorrido de la variable va desde: x = 0 (fallar todos los intentos), hasta x = n (tener exito en todos los intentos).
- Se utilizan diferentes variables, las cuales significan:
	- Numero combinatorio (n x): Formas de combinar el valor de x con los experimentos disponibles n. 
		- Simbolizan la combinatoria, siendo: ![[Pasted image 20260607183526.png|95]]
	- p^x Probabilidad que ocurran x exitos que queres conseguir.
	- q^n-x la probabilidad de que el resto de casilleros se conviertan en puros fracasos.
Significado de cada variable:
- P: Probabilidad de exito, es una medida fija que se repite en cada experimento.
- Q: La probabilidad de que no ocurra el evento exito, determinada por 1-p
- x: Determina la cantidad de casos de exitos que se esperan conseguir.
- n: Simboliza la cantidad de casos totales.
Todos los temas aprendidos en la unidad anterior vienen a esta para adquirir el significado de cada variable:
Expresiones simplificadas: 
- Esperanza matematica: u = n * p, centro de localizacion, el promedio de exitos que esperas tener.
- varianza: var = a² = n * p * q, mide que tan desparramado estan los valores.
- desviacion tipica: a = raiz(n * p * q)
- Sesgo: a³ = q-p / raiz(n * p * q)
	- Segun la probabilidad de exito (p) y fracaso (q), la cuspide del grafico se va distribuyendo a lo largo del grafico. Mas cerca de la izquierda o de la derecha.
- Curtosis: m4 = 3 + (1-6pq) / (npq)², mide que tan achatado esta al grafico. Con respecto a la curva normal.

Esta distribucion binominal de eventos discretos, permite identificar la probabilidad que suceda ciertos eventos y sobretodo, cuantos deberian suceder.
Te permite calcular, si tenes los datos disponibles, la probabilidad para casos particulares donde tengas n escenarios totales y quieras obtener la probabilidad para unicamente x escenarios favorables. La diferencia con laplace, es que aqui calculas en base a probabilidades ya conocidas, y buscas un numero entero. O por el contrario, una probabilidad en base a un caso particular y datos ya especificados.
La cuestion es encontrar los datos, asociar las variables x, p, q, a su correspondiente objeto del problema, y de esa forma, obtener la probabilidad consecuente.
Ejemplo: Basquet:
- Un tipo va a lanzar 5 veces, por lo cual debemos calcular cuantos tiros deberia escestar mediante la probabilidad binominal. Por lo tanto, tenemos estos datos:
	- Su probabilidad de escestar es 80%. Esa probabilidad es fija debido a un promedio anterior.
		- Por lo tanto su porcentaje de fallar es el 20%.
	- La cantidad de tiros que hara son 5.
Si se quiere analizar para ese caso, simplemente usamos la formula de la media y obtenemos la cantidad de veces que encestaria en promedio: 
- u = n * p 
- u = 5 * 0.80 = 4
- El deportista encestaria 4 veces en promedio.
Sin embargo esta distribucion brilla cuando queremos calcular cual es la probabilidad que enceste cierta cantidad de pelotas. Permitiendo identificar la probabilidad de cada caso individual, tomando en cuenta la probabilidad de exitos promedio impuesta.
- Para el caso de que enceste 2 bolas, calculamos con la formula:
	- F(2) = (X = 2) = (5 2) * p² * q³
	- Da como resultado: 0,33.., que equivale a 33%.
	- Se relaciona con la grafica, siendo una posibilidad baja, del lado de la cola de la grafica.

#### Relacion distribucion normal:
Cuando el valor de n es muy grande se define la formula relacionada a la distribucion normal:
![[Pasted image 20260611142324.png]]
- X = variables de exitos en las pruebas de bernoulli.
- p = probabilidad de exitos
Aqui la distribucion binominal TIENDE  a la normal.

#### Distribuciones normales:
- Es una distribucion de variable continua.
- Tiene una forma acampanada su grafica. como si fuera una montaña simetrica. Se le dice funcion gaussiana.
- Es simetrica con respecto a la media.
- Es una de las graficas mas utilizadas en estadistica debido a la facil adaptacion que tiene a su entorno.
Su formula es:
![[Pasted image 20260607191205.png]]

![[Pasted image 20260607191303.png]]

**Caracteristicas:**
- Parametros que la definen: la **distribucion normal** tiene una **serie de funciones**, que se diferencian unas a otras por medio de:
	- La media: u
	- La desviacion estandar: a
- El **punto mas alto** de la curva normal es justo en la media: u, esta coincide con la mediana y la moda.
- La **mediana en una distribucion normal** puede tener cualquier valor: negativo positivo o incluso cero.
	- Puede variar su media y mantenerse constante su variacion estandar.
	![[Pasted image 20260607191618.png|424]]
- La **distribucion normal es simetrica**, osea que siempre un lado sera simetrico al otro, osea, cada lado con respecto a la media, equivale a el 0.5 del total que es 1.
	- Las colas de ambos lados se extienden hasta el infinito sin total el eje horizontal, osea sin valer "0".
	- Al ser simetrica, esta distribucion normal no esta sesgada, por lo tanto equivale a cero.
	- Se dividen en lado izquierdo y derecho con respecto a la media:
		- De lado izquierdo se encuentra la forma de la curva normal.
		- De lado derecho la imagen especualar.
- **Desviacion estandar:** Determina que tan plana o ancha es la curva, teniendo valores mas concentrados cerca de la media, o "planchados" y distribuidos a lo largo de todo el grafico.
	- Las desviaciones grandes, osea un a grande, corresponde a curvas mas planas y anchas, osea valores mas distribuidos entre si. Esto indica mayor variabilidad en los datos recolectados.
	- Las desviaciones pequeñas. corresponden a una acumulacion de valores en el lugar de la media. Los valores son mas predecibles, osea no hay tantos casos extremos.
- Al ser una funcion de variable aleatoria continua, la probabilidad de esta se calcula mediante el area debajo de la curva, la cual en su total es 1.
	- Al ser simetricas ambas mitades de la grafica con respecto a la media "u", se determina que ambas mitades, tanto izquierda como derecha tienen una probabilidad de 0.5 cada una.
- Nos guiamos de las tablas, las cuales determinan un cierto rango de esta distribucion normal, para determinar el porcentaje de probabilidad que hay en ese punto particular.
	- Al modificar las deviaciones estandar, se modifica la probabilidad final.

**Puntos de inflexion teoricos:** Ocurren cuando cambia la curvatura de la campana, estos ocurren en ciertos puntos con respecto a la media, exactamente:
- En una desviacion tipica con respecto a la media en ambos lados.
- x = u - a
- x = u + a
- Esto se demuentra gracias a la derivada segunda de la funcion densidad (osea la funcion de la grafica, de la probabilidad).

**Calcular la distribucion normal: Distribución Normal Estándar**
Si se quiere saber el area debajo de la curva de la funcion de densidad de la distribucion normal, se debe integrar, el problema es que al querer integrarla por metodos convencionales, la integral queda sin solucion analitica limpia. Provocando que no se pueda aplicar barrow.
Por lo tanto se plantea una formula que permite estandarizar esta integral en una funcion compacta utilizando la variable Z:
- **Z = (x - u)/a**
- Esta formula mide la cantidad de desviaciones estandar de distancia hay entre el dato "x" y la media "u".
- ESE VALOR SE DEBE BUSCAR EN LA TABLA CORRESPONDIENTE PARA DETERMINAR LA PROBABILIDAD.
	- Ese valor determina el punto determina el limite para calcular el area debajo de la curva. Debido a que no se puede aplicar Barrow, se utilizan las tablas para encontrar la probabilidad precalculada anteriormente.
	- Puede ser positivo o negativo, y las tablas se adaptan para ambos valores por su simetria.
	- La media "u" de la variable estandarizada Z siempre es cero 0, debido a la simetria antes vista.
		- Puede variar en el problema, pero al pasarlo por la formula, se normaliza la media y la desviacion tipica.
- **COMO MEDIR POR TABLAS:**
	- Se obtiene un valor de Z mediante el uso de la formula estandarizada.
	- Se busca la tabla corresponde segun el criterio:
		- Tabla 1: Toma desde -infinito hasta Z. (se puede calcular todo directamente de esta).
		- Tabla 2: Toma desde "u" (cero), hasta Z.
		- Tabla 3: Toma desde Z hasta 1.
	- Al ser simetricas permite un calculo limpio utilizando la tabla mas conveniente independientemente del signo.
- **Porcentajes de intervalos comunmente utilizados:**
	- Para determinar el porcentaje de elementos que se encuentran entre las desviaciones de la media (valores de distancia de la media, osea valores en positivo y negativo que se alejan de la media), se determina el porcentaje de elementos se se encuentra entre esos rangos: x desviaciones de la media: Rango +-x con centro en la media.
	- Determina una distancia de valores reales en el eje x. Osea pasos hacia los costados.
	- ![[Pasted image 20260611131427.png]]
	- Se dice que para:
		- 1 desviacion estandar de la media se encuentran los 68.3% de valores.
		- 2 desviaciones estandar de la media, 95.4%
		- 3 desviaciones estandar: 99.73%

## Distribucion de poisson:
- Cuenta la ocurrencia de eventos independientes entre si, a lo largo de un intervalo continuo, a lo que se refiere es:
	- Es considerada una funcion limite de la distribucion binomnal, un caso especial cuando N es muy grande y P muy pequeño.
	- Cuenta cuantas veces sucedio algo a lo largo de una variable constante continua, como por ejemplo el tiempo, espacio, volumen, etc...
	- En un periodo determinado cuantas veces sucedio algo especifico.
	- Ej: cuanto goles metio x jugador en un intervalo de 90 min.
	Se la asocia a "eventos raros".
	Calcula que tan probable es que ocura X cantidad de eventos en un intervalo fijo, ejemplo: que mesi meta 3 goles en un partido de 90 minutos, siendo x = goles, y el intervalo continuo el tiempo.
	- Se necesita conocer de antemano el promedio historico de ocurrencias, denominado como lambda.
	La formula clave es la variable de euler (e).
	Usos comunes:
	- Numero de vehiculos que pasan por el peaje por hora.
	- Numero de bacterias en un milimetro de agua.
	Para todas estrar preediciones se debe tener un promedio de cuanto suele suceder ese evento.
- Funciones:
	El intervalo va desde x = 0 (que no ocurra ningun evento en ese tiempo) a infinito teorico x = inf. La formulas principales son:
	- **Formula de probabilidad puntual (cuantia):** ![[Pasted image 20260611133537.png|314]]
		Expansion de los diferentes elementos:
		- Lambda: Numero promedio de los eventos que se esperan. PARA ESE INTERVALO.
		- e: Constante de euler, referenciada a los logaritmos naturales.
		- x! = Factorial de la cantidad de exitos buscados.
	- **Relacion con los momentos:**
		- Esperanza matematica: E(x) = λ.
			- El calculo pasaria a ser como T * P = u = λ;
				- Donde T = Total de elementos; P = promedio de elementos condicionados. En sintesis x * f(x)
		- Varianza: Var(x) = a² = λ.
		- Desviacion tipica = a = Raiz(λ).
		- Sesgo (coeficiente): 1/raiz(λ).
			- El sesgo es siempre positivo debido a la raiz, siempre es asimetrico hacia la derecha.
		- Curtosis: 3 + (1/λ).
- Situacion con λ GRANDE:
	- Cuando λ, los eventos promedios crecen hasta tender a infinito, la funcion formada y desplazada a lado izquierdo pasa poco a poco al lado derecho, provocando que tome forma campanular, asimilandoce a la distribucion normal.
	- Cuando λ tiende a ser muy grande, se puede usar la probabilidad utilizando las tablas de la curva normal.
	- Combinas la formula de Poisson en la formula de la variable Z:
		- ![[Pasted image 20260611134653.png]]
		- Remplazas la media u por λ
		- Remplazas la desviacion tipica a por Raiz(λ).
			- Explicado anteriormente con la relacion de momentos.
- Ejemplo: 
	- Fabrica quiere determinar la probabilidad de que hayan 3 productos defectuosos en una produccion de 100.
	- Se determinan los datos:
		- n = Total de productos: 100
		- p = Probabilidad de defectuosos: 0,2
	- Realizar los calculos necesarios:
		- λ = n * p = 2
		- x = cantidad solicitada a evaluar = 3
	- Formula:
		- P(X = 3) = (2³ - e⁻²) / 3!
		- Nos da como resultado: 180447 = 18% aproximadamente.

### Aclaraciones:
#### Coeficiente de curtosis y relacion con la distribucion normal: 
- Te dice que tantan frecuente son los valores alejados del promedio (desvios), si los elementos se centran en la media o si estan dispersados por los extremos.
- Tanto en binominal como en poisson el coeficiente de curtosis se va acercando al 3 teorico a medida que las muestras crecen y se normalizan.
	- Para poisson sucede cuando λ -> Inf o un numero grande.
	- Para binominal: cuando n -> inf o un numero grande.
- Se le dice que es "normal asintoticamente" cuando estas distribuciones tienen a comportarse como la distribucion normal.

## Teorema del limite central:
Es un teorema que habla de la relacion entre los promedios de las muestras y la distribucion normal. Donde al extraer cierto numero n de muestras, al promediarlo obtenes una distribucion normal muy confiable.
Para calcularlo existen 2 enfoques:
- **Promedio de la muestra: (X)**
	- Se modifica la variable estandarizada Z para calcularla mediante la division de las desviaciones con la raiz de las muestras:
	- ![[Pasted image 20260611144318.png]]
- **Suma total de los datos: (Sn)**
	- Esto se utiliza cuando te interesa la suma iterada de los datos, osea la suma de todas las muestras n. El centro se multiplica por n:
	- ![[Pasted image 20260611144611.png]]
Esto significa que poblaciones de datos diferentes, al realizar el teorema del limite central, se vuelven todas distribuciones normales a partir de un tamaño de muestra de 25 a 30 elementos, independientemente de su grafica original.
- Esto se debe a que al extraer elementos particulares de cualquier tipo de grafica de poblaciones, al aumentar este numero de "muestras" se termina comportando como la distribucion normal. Un grupo pequeño de ese universo termina representando la distribucion normal.
Se identifican los elementos:
- N = universo de elementos.
- n = tamaño de la muestra a extraer de ese universo.

## Distribucion Hipergeometrica:
Mide la cantidad de exitos (x), al extraer una muestra de tamaño (n), sin reposicion, osea que las probabilidades se vuelven dinamicas e dependientes entre si.
- Es una distribucion util cuando la binominal queda corta con los la probabilidad constante.
- Esta distribucion permite obtener una probabilidad dinamica al no reponer los elementos que sacas.
	- La binominal repone los elementos.
**Desarrollo:**
- Total de elementos.
- Y diferenciarlos en 2 grupos:
	- Favorables.
	- Neutros.
**Formula:**
- Numerador (casos favorables), formas de elegir los elementos deseados y no deseados.
- Denominador (casos totales), determina los casos totales a elegir.
	Expandiendo la formula:
	- **Componentes de la formula:**
		- N: Numero total de elementos: (N = m + b)
		- b: Cantidad de elementos favorables o a estudiar.
		- m: Cantidad de elementos comunes.
		- n:  Tamaño de la muestra a extraer, o tambien la cantidad de extracciones.
		- x: Cantidad de exitos que estas buscando calcular.
	- La formula principal consiste en la combinatoria conjunta:
		- ![[Pasted image 20260611154004.png|338]]
		- Cada termino significa:
			- (N n) simboliza la cantidad de elementos totales, siendo todas las formas posibles para elegir un grupo de n elementos de un total de N. Sin importar el oden (Combinatoria).
			- (b x):  Calcula todas las combinaciones posibles de elegir los diferentes elementos favorables de b en un subconjunto x.
			- (m n-x): Son todas las formas de elegir una cantidad n-x del total de elementos comunes m. Osea quitando a los elegidos.
**Propiedades:**
Como el resto de distribuciones, las propiedades se encuentran ya especificadas.
- Esperanza matematica: Media: u
	- ![[Pasted image 20260611154813.png]]
- Varianza: Var(X) = a²
	- ![[Pasted image 20260611154840.png]]
**Caso de ejemplo:**
- Empanadas, se compra una caja con 12 empanadas, de las cuales 4 son de pollo y 8 son de jamon y queso. Estas tienen una forma identica, lo que significa que no se sabe cual es cual. Se agarran 3 empanadas y se quiere determinar la probabilidad que 2 de estas empanadas agarradas fueran de pollo.
- Se utiliza hipergeometrica debido a que necesariamente son probabilidades dependientes, al reducirse el total de elementos en cada extraccion (Empanada comida).
- Se calcula de la siguiente forma:
	- Identificar variables:
		- N = 12 Total.
		- n = 3 Muestra.
		- x = 2 Cantidad a determinar la probabilidad.
		- b = 4 Grupo de interes.
		- m = 8 Grupo comun.
	- Se realiza la formula: Laplace
		- P(X = x) = ((b x) * (m n-x)) / (N n)
		- P(X = 3) = ((4 2) * (8 3-2)) / (12 3) = 0,2181 = 21,81% aproximadamente de que alguna de esas 3 sean de pollo.

## Chicuadrado:
Sirve para medir de forma positiva si un proceso es estable en su dispersion, refiriendose a los valores fuera del promedio.
**Formula:**
- ![[Pasted image 20260611161208.png]]
- Expandiendo los componentes:
	- S²: Varianza real calculada con los datos de la muestra.
	- a²: Varianza teorica/historica de la poblacion completa (de todos los elementos).
	- n - 1: Los grados de libertad, son los diferentes elementos que pueden variar su comportamiento antes que el promedio los congele, se calculan como el tamaño de la muestra menos 1.
- **EXPLICACION GRADOS DE LIBERTAD:**
	- Consiste en los valores que pueden adoptar cualquier valor sin restriccion, eso se debe a que:
		- Una muestra de tamaño n si o si tiene de promedio: sumatoria/n = promedio.
		- Por lo que si el promedio se sabe de antemano que valor es, al momento de definir los valores de "n", unicamente podras definir los que no sean el utlimo valor, debido a que el ultimo valor acomodara la sumatoria para que el promedio de el numero correcto:
			- Ejemplo: n = 8, el promedio es 120, asi que: sumatoria = 8 * 120 = 960.
				- Eso significa que la suma de todos los elementos debe dar como resultado si o si 960, por lo que se le puede asignar valores libres a los primero 7 elementos, y el 8 sera el elemento que equilibra la balanza, y no lo podes elegir aleatoriamente, definido por ejemplo como:
				- 1 + 5 + 67 + 3 + 4 + 2 + 100 + x = 960, el valor "x" sera el que equilibre esa sumatoria.
	- **Se definen como gl = n-1**
	
- **Significado geometrico:**
	Depende de la cantidad de gl (grados de libertad) que tengas:
	- Si tenes poca cantidad de valores de grado de libertad: Ej 3 valores, la grafica muestra una curva ASIMETRICA, con un pico pequeño, tirada para un lado y con una gran cola.
	- Si tienes una gran cantidad de valores de libertad: Ej 30 o mas, la grafica se asemeja mucho a una distribucion normal (campana), pudiendo obtener valores desde la tabla, osea por la normal.
- Utilizamos la Tabla de funcion de distribucion chi-cuadrado para calcular los valores.

### Propiedades de la funcion gamma:
Casi ni la vemos pero por las dudas, hay 3 propiedades fundamentales:
- r(n) = (n-1)!
- r(n+1) = n * r(n)
- r(1/2) = raiz(PI)


# A REPASAR:
- Practicar formulas de cada distribucion. APRENDERSELA. ¿Cuando utilizar cada una?
- Responder preguntas del profe tovo.
- Identificar formulas esenciales a desarrollar.
Debo cumplir esas tareas antes del parcial para identificar que me falta y estudiarlo.

Metodologia de la mañana: 4h seguidas
Al tener poco tiempo dividiremos las tareas en 3 fases: ==Urgente==, **Semi Urgente**, No Urgente, para organizar los temas primarios a abordar.
El objetivo es resolverlos todos.
- ~~==Resolver ejercicio Chi-cuadrado.==~~
- ~~==**Anotar formulas y memorizarlas (reescribirlas acordandose).**==~~
	- ~~**Acordarse relaciones con la distribucion normal. ¿Para que casos sirven? ¿Porque son utiles?**~~
	- ~~Desarrollar caso de Corrección por Continuidad~~
- **Resolver problemas que el profe haya dado.**