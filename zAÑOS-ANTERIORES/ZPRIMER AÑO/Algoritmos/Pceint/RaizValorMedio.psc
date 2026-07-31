Algoritmo RaizValorMedio
	Dimensionar V[10]
	Definir S Como Real
	S <- 0
	
	Para i <- 1 Hasta 10
		Escribir "Ingrese valor ", i
		Leer V[i]
	FinPara
		
	Para i <- 1 Hasta 10
		S <- S + V[i]*V[i]
	FinPara
	
	S <- (1/10) * S
	S <- RC(S)
	Escribir "Resultado: ", S

FinAlgoritmo
