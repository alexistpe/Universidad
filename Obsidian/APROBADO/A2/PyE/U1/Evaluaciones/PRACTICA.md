# **Guía de Trabajos Prácticos N° 1:** Probabilidades.
1) Determinar la Probabilidad P, o un estimador de ella, para cada uno de los sucesos
siguientes:
	a) La aparición de un siete, un rey, un dos de basto o un rey de oro al extraer una sola
	carta de una baraja común de 50 cartas.
		50 son las cartas totales.
		7 = 4 posibilidades
		Rey = 4 posibilidades
		2 de oro = 1 posibilidad
		rey de oro = 1 posibilidad (ya se contó)
		Teorema de laplace: 9/50 = 0.18 = 18%
	b) La suma 8 aparezca en un solo lanzamiento de un par de dados.
		Se determina que cada dado tiene "6", por lo cual las posibles combinaciones entre ambos son: $6^2$ = 36 (Variación con repetición **NO, esto se calcula mediante experimentos (combinatoria): N*M*K... simbolizan los exxperimentos realizados.****).
		Para conocer la probabilidad que suceda eso, debemos determinar todos los posibles casos de estos 36 totales, que dan como resultado 8.
		estos son: 2+6, 6+2, 5+3, 3+5, 4+4 = 5 casos favorables.
		5/36 = 0.138 = 13.8%
	c) Encontrar un tornillo defectuoso si después de haber examinado 600 tornillos se
	hallaron 12 defectuosos.
		12/600 
	d) Un 7 u 11 resulte en un lanzamiento de un par de dados.
		Se indica la totalidad de casos: $6^2$ = 36 (Variacion con repeticion)
		Casos favorables: 4+3, 3+4, 5+2, 2+5, 1+6, 6+1 = 6 casos para el 7
		Casos favorables: 6+5, 5+6 = 2 casos para el 11
		Sumamos casos favorables y nos da: 8/36 = 0.22 = 22% 
	e) Al menos una cara en tres lanzamientos de una moneda.
		Primero se define el universo, se utiliza variacion con repeticion: $2^3$ = 8 posibles combinaciones.
		Luego se ven los casos favorables, obtener CARA en alguno de los 3 lanzamientos, se puede pensar a la inversa, en vez de calcular cual es la probabilidad
		de que salga 1 cara en 3 lanzamientos, podemos calcular la probabilidad de que no salga ninguna cara en los 3 lanzamientos, y luego calcular la probabilidad
		del evento mediante Sucesos complementarios.
		- Calcular P(A′): 1/8 (de los 8 puntos muestrales posibles se obtuvo 1 evento) {X,X,X}
		- Calcular sucesos complementarios: P(A) = 1−P(A′) = P(A) = 1 - 1/8 = 0.875 = 87.5%

2) Se lanza un par de dados corrientes. Determinar la probabilidad P, de que la suma de los
números observados en la cara superior sea mayor que 4.
	Aqui utilizamos la metodologia de sucesos complemetarios:
	Primero analizamos la cantidad total de casos (puntos muestrales): $6^2$ = 36(Variacion con repeticion).
	Luego verificamos los casos favorables: Como los casos favorables (A = Suma > 4) son mucho mayores a los casos no favorables (A' Suma <= 4) calculamos A':
	Identificamos 6 casos donde Suma <= 4, entonces A' = 6
	Ahora calculamos mediante el metodo sucesos complementarios el valor de A: P(A) = 1 - P(A') => 1 - (6/36) = 0.83 = 30/36
	Una vez calculado simplemente lo exponemos: P(A) = 30/36 = 0.83 = 83%
3) Un lote consta de 10 artículos buenos, 4 con pequeños defectos y 2 con defectos graves.
Se elige un artículo al azar. Encontrar la P de que:
	a) No tenga defectos: 1 - 0.6
	b) Tenga un defecto grave 1 - 0.8
	c) Sea bueno o tenga un defecto grave 0.6

4) Se extraen dos bolas sucesivamente de una caja que contiene 10 bolas rojas, 30 bolas
blancas, 20 azules y 15 naranjas, reemplazando la bola después de cada extracción.
Hallar la probabilidad de que:
LOS EVENTOS SON INDEPENDIENTES, POR ESO SE MULTIPLICAN. Se analiza cada obtencion independiente, ya que: se agarra y se devuelve al total, siempre el total sera 75.
	a) Ambas sean naranjas,
		Se debe multiplicar las 2 posibilidades independientes: 15/75 * 15/75 = 0.04
	b) La primera roja y la segunda blanca,
		10/75 * 30/75
	c) Ninguna sea naranja,
		Sucesos complementarios: primero calculamos  los naranjas: 15/75 y restamos: 1 - 15/75
	d) Sean rojas o blancas o ambos colores,
		Multiplicar y sumar, cada combinacion independiente posible. En combinacion el orden importa, por lo que tenes que evaluar cada caso.
		4 casos posibles = RB, BR, RR, BB $2^2$
		$(10/75 * 10/75) + (30/75 * 30/75) + (10/75 * 30/75) + (30/75 * 10/75) = 64/225 = 0,2844$
	e) La segunda no sea azul:
		Proponemos que de total en los casos favorables sea cualquier bola, y en el segundo experimento individual, debe ser todas las bolas excepto las azules.
		$(1 * 55/75) = 11/15 ≈ 0.734$
	f) Al menos una sea azul,
		Obtener la probabilidad de que ninguna de las 2 sea azul y realizar el complemento de esa probabilidad, para obtener los casos donde al menos 1 de las 2 son azules.
		$55/75 * 55/75 = 0,537777778, complemento: 1 - 0,537777778 = 0,462222222, => 0,462222222$ es la probabilidad de que salga al menos 1 azul.
	g) Máximo una roja
		El unico caso no valio en esta propuesta es que salgan 2 rojas en el mismo experimento, por lo cual calculamos esa posibilia y la invertimos.
		prob 2 rojas: 10/75 * 10/75 = 0,017777778, ahora hacemos el complemento para obtener todos los casos posibles: 1 - 0,017777778 = 0,982 
	h) La primera sea blanca pero la segunda no
		Se calcula la prob e que la primera sea blanca y se multiplica por la prob de que salga cualquier otra bola excepto la blanca.
		$(30/75 * 45/75) = 0,24$
	i) Solamente una roja.
		Para este calculo me interesan 2 casos para descartar: que salgan 2 rojas o que no salgan rojas, asi que se plantea: calcular que salga al menos 1 roja y restarle la probabilida que salgan 2 rojas, asi de esa forma queda solo los sucesos que salga 1 roja.
		prob que salga al menos 1 roja: prob que no salgan rojas complementada: $(65/75) * (65/75) = 0,751 => 1 - 0,751 = 0,249$
		Ahora restamos la prob de que salgan 2 rojas: $(10/75 * 10/75 = 0,017777778 => 0,249 - 0,017777778 = 0,231222222)$
		**El camino directo es sumar ambos casos (que salga 1 en el primero o segundo saque):**
			Caso A (Roja, No Roja): (10/75⋅65/75)=26/225.
			Caso B (No Roja, Roja): (65/75⋅10/75)=26/225.
			Sumás ambos: 26/225+26/225=52/225≈0,2311.

5) Entre los números 1, 2, 3,……., 50, se toma un número al azar. Determinar la P de que el número seleccionado sea divisible por 6 o por 8.
	El espacio muestral es de 1-50, por lo que debemos encontrar todos los casos favorables onde 6 o 8 dividan los numeros del espacio muestral.
	Para simplificar el analisis, detectamos que los multiplos de 6 y de 8 son los casos favorables (devuelven un entero luego de diviirlos por 6 u 8), una vez que los detectemos, podemos agrupar los casos favorables y obtener la probabilidad.
	multiplos de 6: 6, 12, 18, 24, 30, 36, 42, 48.
	multiplos de 8: 8, 16, 24, 32, 40, 48.
	Reagrupano los numeros repetidos quedan que los casos favorables son: {6,8,12,16,18,24,30,32,36,40,42,48}, resultando en 12 casos favorables:
	12/50 = 0.24 = 24%
	TIP: La Regla Aditiva permite eliminar los valores redundantes (las interesecciones) donde los numeros (casos favorables) se repiten, pero se deben contar individualmente para la probabiliad ya que son elementos individuales. P(A∪B)=P(A)+P(B)−P(A∩B)

6) Una clase consta de 10 hombres y 20 mujeres, de los cuales la mitad de los hombres y la mitad de las mujeres tienen ojos castaños. Hallar la probabilidad P de que una persona
escogida al azar, sea un hombre o tenga ojos castaños.
En este enunciado se propone un espacio muestral de 30 personas. De las cuales se distingen 2 subespacios muestrales (eventos) donde uno son hombres y otro son mujeres con 10 y 20 personas cada uno respectivamente.
Se sabe que dentro de estos eventos existen subconjuntos, donde la mitad de  puntos muestrales de cada evento principal (hombre o mujer) se encuentran personas con hojos castaneos, por lo cual determinamos que 15 personas de este espacio muestral tienen ojos castaneos.
Para calcular la probabilidad de que sea hombre o tenga ojos castañaos se debe calcular individualmente las 2 probabilidades, sumarlas y restar la interseccion entre hombres y ojos castaneos.
Phombre: 10/30
Pcastaño: 15/30
Pcastañoyhombre (interseccion): 5/30 (de 10 hombres (espacio muestral reducido, se divide por 2, se multiplican ambas probabilidades si son independientes)).
**Calculo final:** 10/30 + 15/30 - 5/30 = 0.66 = 66%


7) Se toman dos dígitos diferentes del 1 al 9. Determinar:
	a) La P de que 2 sea uno de los números escogidos, si la suma de estos fue impar.
		Se debe calcular la probabilidad mediante una condicion, si el resultado es impar (espacio muestral reducido), recien ahí se calcula si fue 2:
		Se deben calcular como las posibilidades de que esta suma pueda devolver un valor impar sumando pares e impares.
		Se calcula espacio muestral = 5 * 4 = 20 combinaciones posibles: - Impares: {1, 3, 5, 7, 9} ; Pares: {2, 4, 6, 8}.
		Una vez que tenemos todas las combinaciones se plantea los casos favorables (donde aparece un 2 y resulta en impar: Casos: {2,1}, {2,3}, {2,5}, {2,7}, {2,9}: Son 5 casos principales ()
		numero de valores impares.
		**Ahora se calcula con el metodo de laplace: 5/20 = 0.25 = 25%**
- **Total de casos favorables (H):** 5. 
	b) La P de que la suma sea impar, habiendo sido 2 uno de los dígitos seleccionados.
		Se debe calcular la probabilidad condicional a la inversa. Prob (A) de que la suma sea impar dado que fue seleccionado "2" (B)
		Primero obtenemos las posibilidades de obtener un 2 (nuestro nuevo espacio muestral). El espacio muestral total (9) se reduce en una unidad debido a que "se toman 2 digitos diferentes", si ya se tomo el numero "2", entonces el espacio muestral se reduce en 1, resultando en: 8 dígitos disponibles {1,3,4,5,6,7,8,9}
		Y los casos favorables para la suma son: 5: {1,3,5,7,9}, resultando en:
		P(Impar|Salio el 2)= 5/8 = 0,625 (62,5%).
		
		
8) Una urna contiene 3 bolas blancas y 4 negras, 7 personas van extrayendo sin reposición
de modo que gana la persona que saca la primera blanca. Hallar la P de ganar de cada
una de las personas.
	Desarrollo en hoja/apunte.

# U2 - Variables Aleatorias y Esperanza Matemática


