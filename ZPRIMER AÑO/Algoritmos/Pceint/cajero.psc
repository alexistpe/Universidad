Algoritmo cajero
	Dimensionar b[6]
	Escribir "Valor de los tipos de billetes: 1 = 1000 | 2 = 500 | 3 = 100 | 4 = 50 | 5 = 20 | 6 = 10"
	Para i = 1 Hasta 6
		Escribir "Definir cantidad de billetes del tipo: ", i
		leer b[i]
	FinPara
	
	Definir f, u, t, d, m, mx Como Entero //Bucle, u = opciones, total, dinero, maximo, maximobilletes
	Dimensionar b2[6]
	f = 0
	Escribir "Defina monto maximo de retiro: "
	Leer m //Monto maximo a retirar
	Escribir "Defina monto maximo del tipo billetes por retiro: "
	Leer mx //Monto maximos billetes
	
	Dimensionar c[1000] //Crea las cuentas (1000)
	Para i <- 1 hasta 1000
		c[i] = 1000 + i //Ingresa un pin diferente para cada una de las 1000 cuentas.
	FinPara
	definir h, a, p como entero //Intentos, acceder, Pin
	
	Mientras f == 0
		Mientras a = 0
			Escribir "Ingrese su Pin de 4 numeros, tiene ", (3 - h), " Intentos."
			Leer p
			Para i <- 1 Hasta 1000 //Itera por los usuarios.
				si c[i] == p
					Escribir "Bienvenido usuario ", i
					a = 1 //Accede
				FinSi
			FinPara
			
			si a <> 1 //Suma 1 error.
				h = h + 1
			FinSi
			
			si h == 3 //Si llego a 3 intentos fallidos.
				f = 1
				a = 1
			FinSi
		FinMientras
		
		Escribir "Eliga las opciones: "
		Escribir "1: Retirar dinero | 2: Consultar estado de dinero | 3: Salir"
		Leer u //Opciones
		
		Segun u
			1: 
				Escribir "Ingrese monto a retirar"
				Leer d //Dinero
				si d MOD 10 <> 0 o d > m
					Escribir "Error, ingrese multiplos de 10 y un monto menor a ", m
				SiNo
					t = b[1] * 1000 + b[2] * 500 + b[3] * 100 + b[4] * 50 + b[5] * 20 + b[6] * 10
					si di > t
						Escribir "Saldo del cajero insuficiente"
					sino
						para i <- 1 Hasta 6 //Se le asigna la cantidad previa de dinero al vector b2 para compararlo.
							b2[i] = b[i]
						FinPara
						
						Mientras mx < 30 y d > 0
							para i <- 1 hasta 6
								mx = 0
								si b[i] > 0
									mientras i == 1 y d >= 1000 //Analiza los de 1000
										d = d - 1000
										b[i] = b[i] - 1
										mx = mx + 1
									FinMientras
									
									mientras i == 2 y d >= 500 //Analiza los de 500
										d = d - 500
										b[i] = b[i] - 1
										mx = mx + 1
									FinMientras
									
									mientras i == 3 y d >= 100 //Analiza los de 100
										d = d - 100
										b[i] = b[i] - 1
										mx = mx + 1
									FinMientras
									
									Mientras i == 4 y d >= 50//Analiza los de 50
										d = d - 50
										b[i] = b[i] - 1
										mx = mx + 1
									FinMientras
									
									Mientras  i == 5 y d >= 20//Analiza los de 20
										d = d - 20
										b[i] = b[i] - 1
										mx = mx + 1
									FinMientras
									
									Mientras  i == 6 y d >= 10//Analiza los de 10
										d = d - 10
										b[i] = b[i] - 1
										mx = mx + 1
									FinMientras
								FinSi
							FinPara
						FinMientras
						
						Para i <- 1 Hasta 6
							Mostrar "Billetes de tipo ", i, " retirados: ",(b2[i] - b[i]) //Cantidad billetes restantes
						FinPara
						
					FinSi
					
				FinSi
				
			2: 
				Para i <- 1 hasta 6
					Escribir "Billetes de tipo ", i, ": ",b[i] //Cantidad de billetes de cada uno
				FinPara
				
				t = b[1] * 1000 + b[2] * 500 + b[3] * 100 + b[4] * 50 + b[5] * 20 + b[6] * 10
				Escribir "Monto total: ", t
				
			3:
				f = 1 //Salir del programa.
		FinSegun
	FinMientras
	
	Escribir "Adios."
	
FinAlgoritmo
