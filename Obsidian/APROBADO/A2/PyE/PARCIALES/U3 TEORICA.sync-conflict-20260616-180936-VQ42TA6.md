Bien, aqui describiremos la metodologia y teoria a estudiar sobre Probabilidad y estadistica en la tercera unidad.
Explicaremos la estrategica para expandir y estudiar todos los temas de forma teorica.
### Agenda:
- Distribución normal o de Gauss.
- ~~Distribución binomial o de Bernoulli.~~ Propiedades.
	- Relación entre la binomial y la normal.
- Propiedades.
- Distribución de Poisson. Propiedades.
	- Relaciones entre Poisson y la normal.
- Teorema del límite central.
- Distribuciones hipergeométrica, Chi-cuadrado

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

EXTENDER PORCENTAJES DE VALORES COMUNMENTE UTILIZADOS: 68.3% una desviacion, 95.4% dos desviaciones, etc... ARRIBA (CARACTERISTICAS).
