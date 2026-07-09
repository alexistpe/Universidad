Algoritmo IntervaloMaxMin
		Dimensionar V[10]
		Definir max, min, S Como Real
		
		Para i <- 1 Hasta 10
			Escribir "Ingrese valor ", i
			Leer V[i]
		FinPara
		
		max <- V[1]
		Para i <- 2 Hasta 10
			Si max < V[i] Entonces
				max <- V[i]
			FinSi
		FinPara
		
		min <- V[1]
		Para i <- 2 Hasta 10
			Si min > V[i] Entonces
				min <- V[i]
			FinSi
		FinPara
		
		S <- max - min
		Escribir "Resultado: ", S


FinAlgoritmo
