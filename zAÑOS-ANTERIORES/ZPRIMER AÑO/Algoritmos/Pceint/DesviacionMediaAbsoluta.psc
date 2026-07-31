Algoritmo DesviacionMediaAbsoluta
	Dimensionar V[10]
	Definir X, DMV, T Como Real
	DMV <- 0
	X <- 0

	Para i <- 1 Hasta 10 
		Escribir "Ingrese valor ", i
		Leer V[i]
	FinPara


	Para i <- 1 Hasta 10 
		X <- X + V[i] //Calcular promedio
	FinPara
	X <- X / 10

	Para i <- 1 Hasta 10
		T <- V[i] - X //formula
		Si T < 0 Entonces
			T <- T * (-1)
		FinSi
		DMV <- DMV + T
	FinPara
	
	// Paso 5: Promedio
	DMV <- DMV / 10
	Escribir "Resultado: ", DMV
FinAlgoritmo
