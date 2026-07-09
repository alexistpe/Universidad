En este documento expandieremos la teoria sobre las Ecuaciones diferenciales.

Para estudiar para la presentacion seguiremos una metodologia de este tipo:
### Metodologia:
- Explicar y expandir tema teoricamente.
- Realizar ejercicios sobre ecuaciones diferenciales.
- Realizar cuestionarios y preguntas teoricas.
- Practicar la presentacion.

## Temas:
- Ecuaciones diferenciales concepto.
	- EDO y EDP
- Homogeneas y no homogeneas.
- Orden de las ecuaciones diferenciales.
- Variables separables y no separables.

## Explicacion de los temas:
Cada tema a expandir es una caracteristica particular del concepto fundamental de las ecuaciones diferenciales, por lo que vamos a ir anexando cada tema a este concepto.

### Ecuaciones diferenciales:
- Al necesitar describir ciertos fenemenos, la fisica utilizo diferentes modelos matematicos, que terminaron por convertirse en ecuaciones diferenciales al tener derivadas y operaciones que afectan a una funcion incognita.
- La definicion formal se describe como: En toda expresion en forma H(x,y,y',....,y^n) = 0 que contiene diferenciales o derivadas, Y en el caso particular donde se relacione con una variable independiente "x" con valores de f(x) de una funcion y sus "n" derivadas, se les llama: **Ecuaciones diferenciales Ordinarias de orden n.**
- Si esta misma ecuacion tuviera **mas** de una **variable independiente** ("x", "y", "f(x,y)"), entonces se encontrarian **derivadas parciales**, por lo que se llamaria **Ecuaciones diferenciales parciales.**
- **En sintesis**, las **ecuaciones diferenciales** son una igualdad en la que la incognita deja de ser un numero y pasa a ser una funcion, la cual esta afectada por derivadas que aparecen en la ecuacion.
	- Se dan casos donde se dice "la derivada de "y" es este termino '''": y' = 2x²
	- La solucion deja de ser un numero fijo para pasar a ser una familia de ecuaciones que varian segun un termino constante.
- Se busca obtener la **solucion general** resolviendo la derivada (integrando), permitiendo determinar la **funcion madre** denominada **y = f(x)**, la cual **representa** una **familia** de **funciones** que **difieren** en el **termino constante C.**

¿Que calcula la ecuacion diferencial?
- Permite imponer una regla geometrica, donde cada punto de la grafica, el valor de la funcion y la recta tangente mantengan una proporcion matematica estricta.
	- Impone una igualdad a la derivada, donde esta derivada (recta tangente) sea estrictamente igual a la funcion impuesta.
	- dy/dx = 2y -> Buscame una funcion y(x) donde su derivada en cada punto sea exactamente el doble de la altura donde se encuentra la funcion.
- Traslada el "comportamiento del movimiento" a una formula predictiva "solucion general".
- La ecuacion diferencial es el molde/restriccion donde quedan afectadas la derivada y la funcion en cada punto.
- La funcion de estado simboliza al modelo en un instante especifico (punto especifico), representando sus resultados.
- **Lo que hacemos al calcular la integrar es encontrar esa funcion original que cumple con esa restriccion geometrica.**

### Homogenias y no homogenias:
La definicion es muy simple en este caso para las ecuaciones diferenciales.
- Homogenias: Contienen unicamente la variable "y" al operar, todos los terminos contienen a "y" o a sus derivadas. g(x) = 0
	- y′+3y=0
	- No pueden haber terminos solos con una variable independiente.
- No homogenias: Hay mas de una variable igualada, sucede cuando hay terminos independientes con otra variable diferente a "y", por lo que g(x) != 0.
	- $y′+3y=e^x$ 
	- Pueden haber terminos solos con variable independiente.
Esta definicion es EXCLUSIVA de **EDOs Lineales con coeficientes constantes**, lo que significa que para los otros casos existen:
- **Coeficientes variables:** Es cuando los terminos que acompañan a la variable "dependiente" "y" eson multiplicados por funciones de la variable independiente.
	- $a(x)y′′+b(x)y′+c(x)y=f(x)$ => $xy′′+(1/x)y′+y=0$ 
	- En este caso utilizas otros metodos para poder resolver estos terminos que dejan de ser constantes y provocan que las raices dejen de ser constantes (impidiendo usar el polinomio caracteristico).
- **EDO No lineales:**  Esto se utiliza en el calculo avanzado, aqui se debe verificar si el grado final del parametro "t" son del mismo grado en todos los terminos.
	- Esto se verifica realizando este procedimiento, deja de tener relacion los las EDOs lineales, ya que pasan a tener otro significado para homogenio.
		- Deben tener este formato: **M(x,y)dx + N(x,y)dy = 0**
		- Luego se agrega el termino "t" a las variables "x" e "y" en cada termino acompañante de M(x,y) e N(x,y).
			- Quedando: M(tx, ty)dx + N(tx,ty)dy = 0
		- Se calcula "t", y verifica sus grados, si todas las "t" tienen el mismo grado, entonces es HOMOGENIA, sino, no es homogenia.
			- **Mismo grado en "t" = Homogenia.**
			- **Diferente grado en "t" = NO homogenia.**

### Orden:
El orden de las ecuaciones diferenciales queda bien definido por el grado de la derivada.
- El orden se rige por: La cantidad de veces que es derivada la funcion (la mayor derivada).
	- y' = grado 1 (primer grado)
	- y'' = grado 2 (segundo grado)
	- y''' = grado 3 (tercer grado)
- En el caso que se encuentren varias derivadas, la mayor sera el orden de esa ecuacion diferencial.
	- y' + y''' = x -> Grado 3 (tercer grado)

### Variables separables y no separables:
Se refiere a la situaciond onde podes o no podes separar las variables con su correpsondiente dx e dy.
- **En las variables separables:** Podes operar algebraicamente la ecuacion para separar las variables en ambos lados del igual, e integrar de forma directa ambos lados.
	- **M(x)dx + N(y)dy = 0.**
- **En las variables NO separables:** No podes operar algebraicamente para separar las variables, y te queda utilizar el metodo del **operador diferencial.**
	- No son homogenias.
	- Se utiliza el metodo del operador diferencial en el caso de las EDO de coeficiente lineal.
	- Si el coeficiente que acompaña a la variable "y" (dependiente) es variable: Ejemplo (ay; donde a = x² -> x²y), en ese caso al no ser constante, **NO SIRVE** el **metodo** del **operador diferencial**, se utiliza otro como el **factor integrante.**


## Bloque 1: Fundamentos y Conceptos (Filmina 2)

**1. La diferencia entre la regla y el resultado** En tu filmina 2 decís que una ED "plantea una ley de cambio" y que permite encontrar una "función de estado".

- **Pregunta:** Si yo te doy la ecuación $\frac{dT}{dt} = -k(T - T_m)$, ¿por qué a esa expresión la llamamos "ley de cambio" y no me sirve para saber directamente la temperatura de la taza a los 10 minutos? ¿Qué representa geométrica y físicamente la "función de estado" que obtenés al final del ejercicio en comparación con esa derivada original?
    
- Respuesta: La llamamos ley de cambio debido a que simboliza la restriccion impuesta sobre la funcion con respecto a la derivada, donde se impone como cambiara la funcion con respecto a la derivada.
    
    - Esta Ecuacion diferencial no permite determinar la temperatura directamente, debido a que es una restriccion, al integrar ambas variables luego de separarlas, nos permite encontrar la funcion original (funcion madre) que cumple con este “capricho” de la restriccion.
        

**2. El límite del método** Mencionaste que existen ecuaciones de varios órdenes, pero en este problema usaron "variables separables".

- **Pregunta:** Si yo te planteara una ecuación que modela un sistema con aceleración (segundo orden), como $y'' + 2y' = 0$... ¿por qué es matemáticamente imposible resolverla usando el método de variables separables que mostrás en la presentación? ¿Qué restricción fundamental tiene ese método?
    
- Respuesta: El meotodo de separar solo se puede realizar en primer orden, con variables separables y derivadas simples de primer grado del estilo dy/dx. Esto permite "separarlos" algebraicamente cruzando términos para integrar ambos miembros una sola vez ($f(y)dy = g(x)dx$).
    - Si fuera de otro grado mayor, al querer integrar de ambos lados quedaria una ecuacion del esto: ∫d²y = ∫−2dydx; Esto no permite integrarlo con una unica integral, provocando que se llegue a una absurdo/imposibilidad matematica.
    - Ademas al pasar a un segundo orden, la derivada segunda ($y''$ o $\frac{d^2y}{dx^2}$) ya no es una fracción simple, sino un operador aplicado dos veces: $\frac{d}{dx}(\frac{dy}{dx})$. No podés desarmar eso pasando un "$dx^2$" multiplicando, porque romperías la linealidad y las reglas elementales del cálculo integral. Por eso, al no poder separar, la matemática te obliga a cambiar de paradigma: se abandona la integración directa y se usan herramientas como el Polinomio Característico o el Operador Diferencial ($D$) para transformar el problema de cálculo en un problema de raíces algebraicas.
    - Para resolver una ecuacion de segundo orden se utilizan metodo como el operador diferencial e^ax, donde a = -raiz, y se utiliza “D” para representar la derivada y utilizarlo como un operador en la resolucion de la ED.

**3. La legalidad de los diferenciales** En el paso 2 de la filmina 5, pasás el término $(T - T_m)$ dividiendo y el $dt$ multiplicando.

- **Pregunta:** Un profesor te frena ahí y te dice: _"Alumno, el diferencial_ $dt$ _es parte de la notación de la derivada_ $\frac{dT}{dt}$_, no es un número. ¿Con qué justificación teórica o bajo qué convención matemática usted asume que puede tratar al_ $dT$ _y al_ $dt$ _como si fueran fracciones independientes que se pueden multiplicar y dividir cruzado en la ecuación?"_
    
- Respuesta: Formalmente la derivada no es una fraccion comun, sin embargo gracias a la notacion de Leibniz nos permite expresar la derivada de la funcion de una forma dT/dt, que al aplicar la integral en ambos lados del igual, nos permite utilizar sustitucion del lado izquierdo para poder simplificar dT/dt * dt = dT, y solo aplicar “dt” de lado izquierdo. Este metodo matematico colapsa el bloque de “dT/dt * dt” a “dT”.
    
    - El uso de “multiplicarlo de ambos lados” es un atajo visual para saltarse el uso del metodo de sustitucion.
        
    - $$\int \frac{1}{T - T_m} \cdot \left( \frac{dT}{dt} dt \right) = \int -k \, dt$$
    - Donde du = (derivada de u) * dt; Al tomar a “T” como “u”, nos queda dT = ((derivada de T) = 1) * dt; Resultando en que dT = dt.
**4. El nacimiento de la constante gigante** Mirá el salto del paso 4 al paso 5 en tu filmina 5. Pasás de tener $e^{Ln(T-Tm)} = e^{-kt+c}$ a escribir directamente $T(t) = T_m + e^{-kt} \cdot A$.

- **Pregunta:** Explicame paso a paso, aplicando propiedades de la potenciación de Análisis I, qué pasó exactamente con esa $+ c$ minúscula que estaba en el exponente para que de repente se transforme en una $A$ mayúscula multiplicando a toda la función exponencial. ¿Por qué es legal hacer eso?
- Respuesta:
	- Lo que sucedio en este punto es una simplificacion visual, asignamos el termino " $e^c$ " a una constante llamada "A", siendo A = $e^c$
	- Es legal debido a que al ser ambas letras "constantes" que no cambiaran su valor a lo largo de las operaciones, las colapsamos en una sola letra constante A.

## Bloque 3: Física y Análisis del Modelo (Filminas 6 a 10)

**5. El signo de la muerte térmica** En tu ecuación general de la filmina 8, el exponente de la $e$ es negativo ($-0,0688t$).

- **Pregunta:** ¿Qué pasaría con la gráfica de la filmina 10 y con la realidad física de la taza de café si por un error de distracción te olvidabas de poner el signo menos en el planteo de la integral y la constante $k$ te quedaba positiva en el exponente? Analizalo matemáticamente: si $t$ empieza a crecer, ¿hacia dónde se iría el resultado de $T(t)$?
- Respuesta: La constante de enfriamiento "k" es negativa en el exponente por una simple razon, al enfriarse el cafe, este exponente de "e" en negativo permite ir reduciendo la temperatura final del objeto con el tiempo, debido a que "k" esta multiplicada por "t", y al ser menor que uno, entre mas crezca el numero "t" mas pequeño sera el numero final de k * t.
	- Si fuera positivo el exponente, tendria un aumento exponencial de la temperatura en vez de un desenso.

**6. El comportamiento Asintótico (La pregunta de fuego)** En tu gráfica (Filmina 10), marcaste una línea roja en $y = 18$ y la curva azul se va acercando a ella a medida que pasa el tiempo.

- **Pregunta:** Si dejas la taza de café en esa habitación durante 5 años seguidos (un tiempo $t$ tendiendo a infinito)... demostrame de forma estrictamente matemática, usando la fórmula de tu solución general ($T(t) = 18 + 70 \cdot e^{-0,0688t}$), por qué la temperatura del café jamás va a poder bajar a $17^{\circ}C$ ni cruzar esa línea roja, sin importar cuántos millones de minutos pasen. ¿Qué le pasa al término exponencial cuando $t \to \infty$?
- Respuesta: Al ser el tiempo la unica variable que se modifica, cuando t -> infinito, el exponente negativo en numeros muy grandes convierte al termino $e^kt$ enn valores muy cercanos a cero, sin ser exatamente cero o menor en ningun momento (debido a la ley de exponentes), provocando que se acerca infinitvamente al valor de 18 sin tocarlo.