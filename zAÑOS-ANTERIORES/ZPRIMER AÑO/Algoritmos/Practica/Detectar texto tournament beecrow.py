#Detectar texto tournament beecrow
u = int(input()) #Lineas a revisar.
v = "oulupukk" #Cadena.
t = len(v) #Tamaño de la cadena.
for j in range(u): #Iterar segun la cantidad de lineas.
    s = input()
    c = list(s) #La transformamos en una lista para operar mas eficiente.
    for i in range(len(s)-8):
        if s[i:(i+8)] == v: #Si encontramos la palabra.
            c[i-1] = "J"
            c[i+8] = "i"
    a = ""
    for i in range(len(s)): #Crear cadena.
        a = a + c[i]
    print(a)

