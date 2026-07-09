Algoritmo MediaGeometrica
	Dimensionar V[10]
	Definir S Como Real

	Para i <- 1 Hasta 10
		Escribir "Ingrese valor ", i
		Leer V[i]
	FinPara

	Para i <- 1 Hasta 10
		Si i <> 1 Entonces
			S <- S * V[i]
		Sino
			S <- V[i]
		FinSi
	FinPara

	S <- S ^ (1/10) //Equivale a raiz a 10
	Escribir "Resultado: ", S

FinAlgoritmo
