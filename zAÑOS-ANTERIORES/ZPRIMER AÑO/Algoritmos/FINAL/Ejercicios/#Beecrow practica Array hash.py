#Beecrow practica Array hash
#Consiste en obtener un cierto numero en base a sumar las diferentes caracteristicas de una cadena.
#Se obtiene el valor en base a: posicion ene l alfabeto + posicion en la cadena + nro de la linea ingresada.
#Extension en papel. 
# 35 min. tardamos.

n = int(input()) #Valor casos.
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #ABCEDARIO EEUU.
for i in range(n):
    m = int(input()) #Cant de cadenas por caso.
    t = 0 #Total.
    for j in range(m):
        s = input() #Recibir cadena.
        for k in range(len(s)): #Recorremos la cadena.
            t+= j
            t+= k
            b = abc.find(s[k])
            t+= b #Recuperar el valor de la posicion donde se encuentra.
    
    print(t) #Se imprime el valor.

#OPTIMIZADO:
n = int(input()) #Valor casos.
for i in range(n):
    m = int(input()) #Cant de cadenas por caso.
    t = 0 #Total.
    for j in range(m):
        s = input() #Recibir cadena.
        #EN LA LINEA DE SUMAR TODAS LAS POSICIONES REALIZAR UN FIBONACCI:
        #u = (1+(5**0.5))/2 #Fibonacci.
        #t+= ((u**len(s))-((1-u)**len(s)))/(5**0.5) #Suma de todas las posiciones.
        for k in range(len(s)):
            t+= k
        t+= len(s)*j #Sumar el valor de la linea en cada elemento.
        t+= sum(map(ord, s))-(65*len(s)) #Recuperar el valor en la posicion del ABECEDARIO usando ascii y restando para obtener valores lineales.
    print(t) #Se imprime el valor.
