## U1
1) ¿Que es la probabilidad?
	Es una medida de cuan probable es que suceda un evento.
2) ¿Como se mide la probabilidad de forma basica? dame un ejemplo.
	La probabilidad clasica en este caso, se mide gracias al metodo de laplace, que propone dividir: casos favorables/casos totales
	Este metodo tiene en cuenta que todos los casos tienen la misma chance de salir.
	Ejemplo: tengo un dado de 6 caras y lo lanzo, me toca un 3, la probabilidad que toque es: 1/6 (1 caso especifico de 6 posibles).
3) Nombrame los tipos de eventos y que es un evento.
	Existen 3 tipos de eventos principales: Los mutuamente excluyentes, No mutuamente excluyentes, sucesos complementados
	Un evento es un conjunto de puntos muestrales especificos, que nace gracias a los puntos muestrales del espacio muestral original (total)
4) Defini la ley de complemento o A'
	La ley de complemento o sucesos complementados, se refiere a obtener todos los puntos muestrales que no pertenecen al evento en particular, su formula es:
	P(A') = 1 - P(A)
	El 1 se refiere a todos los puntos muestrales (el 100%), al restarlo con P(A) te resulta en todos los puntos muestrales menos los de P(A)
5) ¿Como calculas 2 eventos favorables de 6?
	Se utiliza la formula de laplace, la cual son evenetos favorables / eventos totales, por lo que: 2/6
6) ¿Como se calculan las posibilidades totales de los elementos en experimentos independientes?
	En los experimentos independientes las posibilidades no se calculan conjuntamente sino que se calculan como experimentos separados y luego se combinan.
	Se calcula el primer experimento, se calcula el segundo y se multiplican, el resultado es la probabilidad resultante de combinar ambos. 1/30 * 1/16 = probabilidad que sucedan ambos.
	Esto se debe a que al combinarlos solo se dio un caso favorable especifico entre ambos eventos.
7) ==Explicame la diferencia entre sucesos independientes y dependientes.==
	==Los sucesos independientes se refieren a que los valores son discretos, osea que son enteros y se calculan como tal.==
	==Los dependientes se refieren a que se interpretan con un rango, significa que entre 1 y 2 existen infinitos numeros fraccionales que alteran la probabilidad.==
	EXPLICAR MEJOR ESTA PARTE, REVISAR.
8) Dime los axiomas de la probabilidad y que significan.
	Existen 3 axiomas de la probabilidad:
	1) La probabilidad va de 0 a 1, el 0% o el 100% (Corrección: Si bien es correcto, el axioma estipula que debe ser positivo).
	2) (Correccion: Certidumbre, se refiere a que la probabilidad del evento es de 100% (1)).
	3) Tiene que ver con los sucesos complementados, se obtienen todos los puntos muestrales restantes del universo que no pertenecen al evento. (Correcion, no solo ese, se refiere a la "reglas" para para las sumas (Operaciones Aditivas): Esto se especifica para los tipos de evento: ME (Mutuamente excluyente) P(A) = P(B): NME: P(A)+P(B)-P(AnB) (Se resta la interseccion, ya que esos numeros de ambos ya estan repetidos), SC (Suceso complementario): 1 - P(A'))
9) Explicame las diferentes formulas de analisis combinatorio.
	El analisis combinatorio sirve para evaluar las diferentes combinaciones que pueden haber con los elementos de 2 conjuntos, existe:
	Variacion, Permutacion y Combinacion. Estas ormulas cambian dependiendo si es con repeticion o sin repeticion (Osea si se puede repetir elementos o no).
	Variacion dice que el orden importa, a,b != b,a (Dos casos individuales)
	Permutacion dice que el orden importa y se evaluan las combinaciones con el mismo conjunto, sin tomar otro externo, combinaciones de 'n' entre 'n'
	Combinatoria propone que el orden no importa, reduciendo los casos individuales debido a que: a,b = b,a
	Formulas: 
		Sin repeticion: P (n!), V (n! / (n-m)!), C (n! / (m!(n-m)!)
		Con repeticion P (n!/a!b!c!, osea dividido las letras que se repiten!), V (n elevado m), C ((n+m-1)! / (m!(n-1)!)
10) Explicar y ejemplificar teorema de bayes.
	El teorema de bayes propone una formula para calcular las probabilidades de que un evento sucediera segun una probabilidad previa de ese evento, se toma en cuenta tanto los puntos muestrales de ese evento y su probabilidad previa de suceder, esto permite aproximar que tan probable es que sucediera segun un evento especifico.
	P(A|Ak) = (P(A1) * P(A|A1)) / Espacio muestral con sus respectivas probabilidades (P(A1) * P(A|A1) + P(A2) * P(A|A2) + P(Ai) * P(A|Ai))
11) Explicame la probabilidad condicional.
	Simboliza que la probabilidad cambia si se añade información nueva relevante, dando a conocer las probabilidades de un evento, y por considiente, focalizar el espacio muestral en el evento correspondiente, dejando de lado los eventos donde su probabilidad es nula. Sintesis: Gracias a informacion nueva, se descartan puntos muestrales y se centraliza en evnetos particulares. Las probabilidades de un evento pueden alterar a las de otros.
	P(A) = P(A|B) / P(B)
	Donde lo que hacemos es centrar el espacio muestral total en torno al evento "B", debido a que se pudo saber que el evento "A" no tenia probabilidad. Dando como resultado que se analice la probabilidad de los eventos favorables / el espacio muestral del evento "B" (El que si tiene probabilidades).
	