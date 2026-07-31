Algoritmo MediaArmonica
	Dimensionar  V[10]
	Definir S Como Real
	S <- 0
	e <- 0
	
	Para i <- 1 Hasta 10
		Escribir "Ingrese valor ", i
		Leer V[i]
	FinPara

	Para i <- 1 Hasta 10
		Si V[i] <> 0 Entonces
			S <- S + (1/V[i])
		Sino
			e <- e + 1
		FinSi
	FinPara

	Si S <> 0 Entonces
		S <- 10/S
		Escribir "Resultado: ", S
	Sino
		Escribir "Cantidad valores no calculados: ", e
	FinSi

FinAlgoritmo
