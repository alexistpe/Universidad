#Beecrow ascii caracteres repetidos
#Consiste en obtener los caracteres repetidos de una cadena y imprimir cuantas veces se repiten de forma acendente.
#55 minutos llevo, bien.
while True: #Beecrow EOF.
    try:
        c = input() #Obtener cadena de datos.
        if not c: break
    except EOFError:
        break #Finalizo
    
    v = [0]*94 #Caracteres disponibles en la entrada.
    #Detectar cantidad.
    for i in range(len(c)):
        v[ord(c[i])-33] += 1 #Sumar cantidad de veces que aparece.

    ma = [[0 for _ in range(2)]for _ in range(94)] #Matriz para optimizar espacios sin repeticion.
    id = 0 #Id matriz.
    for i in range(94):
        if v[i] > 0: #Si acumulo algo.
            ma[id][0] = i+33 #Almacena el indice real.
            ma[id][1] = v[i] #Almacena las repeticiones.
            id += 1 #Aumentar el indice.
    t = id #Cuenta los valores individuales que se repitieron.
    
    #Escrir acendentemente.
    m = 1 #Menor.
    pm = 0 #Menor anterior.
    while m > 0: #Condicion de salida en caso que no se encuentre un menor mayor.
        id = -1 #Indice del valor menor.
        for i in range(t): #Encontrar proximo menor.
            if ma[i][1] > pm: #Si se encontro un valor mayor al antiguo menor.
                m = ma[i][1] #Recuperar como menor inicial.
                id = i #Indice del posible menor.
                break
        
        if m == pm: #Si no se encontro un valor mayor al menor anterior (termino de imprimir).
            m = -1
            break #Salir del bucle.
        
        for i in range(t):
            if ma[i][1] > pm and ma[i][1] < m: #Si se encontro un valor mayor al antiguo menor (no repetido) y mas pequeño que el menor actual.
                m = ma[i][1] #Recuperar como menor.
                id = i
        
        pm = m #Actualizar menor anterior.
        print(ma[id][0], m) #Imprimir el caracter de forma acendente.


