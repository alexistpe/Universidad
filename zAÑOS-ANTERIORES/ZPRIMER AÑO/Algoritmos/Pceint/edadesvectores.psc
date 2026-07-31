Algoritmo edadesvectores
	// Definir variables
    Dimensionar alumnos[90]
    Definir NEStudiantes, Sedades, Contador, AMaj, AMen Como Entero // prom, est, cont, mayor, menor
	Definir  promedio Como Real
    // Inicialización de variables
	promedio = 0
    Contador = 0
    Sedades = 0
    NEStudiantes = 0
    AMaj = 0
    AMen = 0
	
    // Bucle para leer las edades de los alumnos
    Mientras Contador < 90 Hacer // Asegurarse de no exceder el tamaño del array
        Contador =+ 1
		Escribir "Edad del alumno, (0 para finalizar): "
        Leer alumnos[Contador]
		
        Si alumnos[Contador] = 0 Entonces
            Contador = 90 // Forzar la salida del "Mientras"
        Sino
            Sedades = Sedades + alumnos[Contador] // Acumular edades
            NEStudiantes = NEStudiantes + 1 // Contar estudiantes
            Contador = Contador + 1
        FinSi
    FinMientras
	
	
	Contador = 0
    // Calcular el promedio
    Si NEStudiantes <> 0 Entonces
        promedio = Sedades / NEStudiantes
    Sino
        Contador = 1 //asignar un valor que indique que no se pudo calcular
    FinSi
	
	
    // Bucle para comparar edades con el promedio
    Mientras Contador < NEStudiantes Hacer // Recorrer solo los estudiantes que se ingresaron
        Contador =+ 1
		Si alumnos[Contador] > promedio Entonces
            AMaj = AMaj + 1 // Contar mayores al promedio
        Sino
            AMen = AMen + 1 // Contar menores o iguales al promedio
        FinSi
        Contador = Contador + 1
    FinMientras
	
    // Mostrar resultados
    Escribir "Mayores al promedio: ", AMaj
    Escribir "Menores al promedio: ", AMen
    Escribir "Promedio: ", promedio
	
FinAlgoritmo