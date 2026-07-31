#PRACTICA FINAL - SIMULACION
n = 1
while n != 0:
    n = int(input()) #Cantidad camisetas.
    m = [["" for _ in range(3)]for _ in range(n)]
    id = 0 #Indice matriz.
    for i in range(n):
        a = input() #Nombre
        b = input() #Color y tamaño.
        m[id][2] = a #Asignar en columna 3.
        s = "" #Obtener columna 1 y 2
        for j in range(len(b)):
            if b[j] == " ":
                m[id][0] = s #Almacenar color.
                s = ""
            else:
                s = s + b[j]
            
            if j == len(b)-1:
                m[id][1] = s #Almacenar tamaño.
        id += 1
    
    #Ordenar por nombre.
    s = "" #Inicial previa.
    c = "" #Inicial comparacion.

    for i in range(n):
        for j in range(n-1): #Burbuja.
            s = m[j][0] #Comparar elemento actual.
            s = s[0] #Inicial.
            c = m[j+1][0] #Comparar elemento siguiente.
            c = c[0] #Inicial.
            if s > c: #Si rompe el orden acendente.
                for k in range(3):
                    a = m[j][k]
                    m[j][k] = m[j+1][k]
                    m[j+1][k] = a
    
    #Ordenar por tamaño.
    s = "" #Inicial previa.
    c = "" #Inicial comparacion.

    for i in range(n):
        for j in range(n-1): #Burbuja.
            s = m[j][1] #Comparar elemento actual.
            c = m[j+1][1] #Comparar elemento siguiente.
            if m[j][0] == m[j+1][0] and s < c: #Si rompe el orden decendente y es el mismo color.
                for k in range(3):
                    a = m[j][k]
                    m[j][k] = m[j+1][k]
                    m[j+1][k] = a
    
    #Ordenar por tamaño.
    s = "" #Inicial previa.
    c = "" #Inicial comparacion.

    for i in range(n):
        for j in range(n-1): #Burbuja.
            s = m[j][2] #Comparar elemento actual.
            s = s[0]
            c = m[j+1][2] #Comparar elemento siguiente.
            c = c[0]
            if m[j][0] == m[j+1][0] and m[j][1] == m[j+1][1] and s > c: #Si rompe el orden acendente y es el mismo color y tamaño.
                for k in range(3):
                    a = m[j][k]
                    m[j][k] = m[j+1][k]
                    m[j+1][k] = a
    
    #Imprimir matriz.
    for i in range(n):
        s = "" #Obtener fila matriz.
        for j in range(3):
            s = s + m[i][j] + " "
        print(s)
                