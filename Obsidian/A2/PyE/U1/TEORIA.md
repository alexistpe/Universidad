- Que es la probabilidad.
- Formas de obtener la probabilidad.
- Definiciones de conjuntos.
	- Tipos de eventos.
- Axomas y formula.
- Probabilidad condicional.
- Tipos de sucesos.
- Análisis combinatorio.
(APUNTES CARPETA).
### U2: Variables aleatorias y esperanza matematica.
#### **Variable aleatoria:**
- Una variable aleatoria suecede cuando el resultado del experimento es una probabilidad o evento aleatorio.
- Una variable X es variable aleatoria si el valor que toma corresponde al resultado de un experimento es una probabilidad o evento aleatorio.
	Pueden ser **discretas o continuas:**
	- Depende en que valor puede tomar las variables, si un valor determinado (entero) de un eje real o todos los valores del eje real (flotante)
	- Discreta (1,2,3,4) (Entero, determinados valores) | Continua (1,01; 16,3; 2,5; 2,063) (Flotante, todos los valores)
	Se identifican las variables aleatorias con "X;Y;Z"
	**Funciones en las variables aleatorias:**
		**Funcion de probabilidad (f(x)):** Es una probabilidad puntual, dice que chance hay que la variable tome ese valor especifico.
			**Discretas:** Sirve cuando contamos con todos los valors de la variable aleatoria y la probabilidad de cada valor. A esto se le llama funcion de probabilidad o distribucion de probabilidades.
				P(X = x) = f(x)
				![[Pasted image 20260331152634.png|238]]
			**Continuas:** Donde X es una variable aleatoria continua
				![[Pasted image 20260331152751.png|276]]
		**Funcion de distribucion (F(x)):** Es la acumulada, calcula que chances hay de que la variable toma un valor igual o menor, acumula (suma) las posibilidades anteriores.
			**Discretas:** La funcion acumulada por suecesos anteriores posibles.
				![[Pasted image 20260331154745.png|302]]
			**Continuas:** Consiste en el area abajo de la curva de la funcion de desidad a la izquierda de "X", acumula los infinitos casos posibles anteriores.
				![[Pasted image 20260331155039.png|438]]
		**Distribución Conjunta :** Antes se estudiaba una sola variable aleatoria, aqui se estudia en conjunto de 2 variables aleatorias y como se afectan entre si. Es necesario para estudios mas realistas y complejos, debido a que normalmente un conjunto de variables dependen entre si.
			**Funcion de probabilidad conjunta:** Un valor especifco, que probabilidad hay que suceda "y" e "X" al mismo tiempo.
				**Discretas:** Se analizan en "grilla", la probabilidad de que ocurran de forma exacta simultaneamente.
					Probabilidades marginales: Se suma solo una columna o solo una fila para determinar la probabilidad de una sola variable. Se utiliza este concepto para determinar la probabilidad de una variable con respecto a otra.
					![[Pasted image 20260331161040.png|353]]
				**Continuas:** Se analiza la superficie en 3D, al haber infinitas probabilidades necesitas calcular el "volumen" que queda encerrado entre las variables la probabilidad final.
					![[Pasted image 20260331161532.png|456]]
					Usamos integrales dobles para ello.
			**Funcion de distancia acumulada conjunta:** 
				**Discreta:** Suma todas las celdas anteriores al punto (atras y a la izquierda)
					![[Pasted image 20260331161814.png|303]]
				**Continuas:** Acumula todo el volumen anterior (viene desde el infinito negativo hasta el punto x,y) todo el volumen a la izquierda y abajo del punto.
					![[Pasted image 20260331162129.png|412]]

#### **Esperanza matematica:**
Es el valor esperado, se divide entre la variable aleatoria discreta y continua.
Se obtiene mediante la suma de los productos de todos los valores posibles de la variable aleatoria con su correspondiente probabilidad.
Osea se realiza la suma de productos de todos los valores posibles en una variable aleatoria, junto a la probabilidad de cada uno.
- **Discreta:** Funcion descrita: (probabilidad de la variable * variable aleatoria), sumadas entre si.
	𝐸 (𝑥) = 𝑥1 ∙ 𝑓 𝑥1 + 𝑥2 ∙ 𝑓 𝑥2 + ⋯ + 𝑥𝑛 ∙ 𝑓 𝑥𝑛
- **Continua:** Aqui al tener infinitos valores posibles se utiliza la integral.
	![[Pasted image 20260331162842.png|192]]
**Caso especial:** En caso de que ambas probabilidades sean iguales la esperanza matemática queda dada por:
	![[Pasted image 20260331162936.png|292]]
##### **Axiomas y propiedades**
1) Para: Q(x), donde x = variable aleatoria: 
	$E(x) = \sum Q(x_i) \cdot f(x_i) = Var. discreta$
	$E(x) = \int Q(x) \cdot f(x) \ dx = Var. continua$

2) Para E(k) = k donde K = constante, X una var. aleatoria en E(x):
![[Pasted image 20260403174122.png|709]]

3) La esperanza de la suma es igual a sumar esperanzas, para variables X,Y independientes o no.
	Osea la esperanza total al: sumar variables = sumar esperanzas.
	$E (X+Y) = E(X) + E(Y)$
4)  La esperanza del producto es igual a multiplicar esperanzas, para variables X,Y independientes o no.
	$E (X.Y) = E(X) * E(Y)$

#### Varianza y desviación Estándar 
