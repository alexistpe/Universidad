Algoritmo MCD
	Definir A, B Como Entero
	Leer A
	Leer B

	Contador = 0
	Salida = 0
	
	Mientras Salida = 0 Hacer 
		Si B <> 0 Entonces
			Resto = A / B 
		SiNo
			Salida = 1
		FinSi
		
		Contador = 0
		Mientras Contador < Resto Hacer
			Contador = Contador + 1
		FinMientras 
		
		Si Contador = Resto Entonces
			Salida = 1
		SiNo
			Resto = A
			Mientras Resto >= B Hacer
				Resto = Resto - B
			FinMientras 
			A = B
			B = Resto
		FinSi 
	FinMientras 
	
	Mostrar "Valor MCD: ", B
	
FinAlgoritmo
