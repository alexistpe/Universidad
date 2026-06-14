Algoritmo DosproblemarioLibro
	Dimensionar vec[10]
	definir p1, p2, d, dp Como Entero
	
	para i <- 1 hasta 10
		leer vec[i]
	FinPara
	
	para i <- 1 hasta 10
		si i <> 1
			dp = vec[i] - vec[i-1]
		FinSi
		
		si dp > d
			d = dp
			p1 = i-1
			p2 = i
		FinSi
	FinPara
	
	Escribir "Diferencia: ", d, " Posicion: ", p1, " Numero: ",vec[p1], " y Posicion: ", p2, " Numero: ",vec[p2]
FinAlgoritmo
