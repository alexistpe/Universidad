Algoritmo cartaEnvio
	Escribir "¿Tenes una carta? S = si | N = No "
	Leer Carta
	
	Si Carta = "N" Entonces
		Escribir "Comprar carta."
	Fin Si
	
	Escribir "Escriba el contenido de la carta: "
	Leer Contenido
	
	Escribir "¿Cual es la direccion de la carta?"
	Leer Direccion
	
	Escribir "La Carta dice: ", Contenido, " Y sera enviada a: ", Direccion
	Escribir "¿Desea cambiar algo? C = Contenido / D = direccion / A = Ambas / N = No"
	Leer  pregunta
	
	Si pregunta = "C" Entonces
		Escribir "Añada el contenido nuevo: "
		Leer Contenido
	SiNo
		si pregunta = "D" Entonces
			Escribir "Añada la direccion nueva: "
			Leer Direccion
		FinSi
	Fin Si
	
	Si pregunta = "A" Entonces
		Escribir "Escriba el nuevo contenido: "
		Leer Contenido
		Escribir "Escriba la nueva direccion: "
		Leer  Direccion
	FinSi
	
	Escribir "¿Tiene estampilla? S = Si | N = No"
	Leer estampa
	
	Si estampa = "N" Entonces
		Escribir "Comprar estampa."
	FinSi
	
	Escribir "Pegando estampa..."
	Escribir "Cerrando sobre..."
	Escribir "Entregando sobre para...", Direccion
	Escribir "¡Listo!"
	
FinAlgoritmo
