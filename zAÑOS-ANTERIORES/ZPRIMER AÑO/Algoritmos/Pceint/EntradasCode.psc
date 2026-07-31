Algoritmo EntradasCode
	Definir personas Como Entero
	Definir entradasPasadas Como Entero
	
	Mientras entradasPasadas < 20
		Leer personasLector
		Si personasLector == 0
			entradasPasadas = 20
		Sino
			personas = personas + personasLector
			Leer entradas
			entradasPasadas = entradasPasadas + 1
		Finsi
		
	Fin Mientras
	
	Escribir personas
	
FinAlgoritmo
