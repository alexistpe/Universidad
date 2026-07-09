#E22 Integrador cifrado.
#Consiste en recuperar una cadena y ejecutar un algoritmo de cifrado por matriz.
#Expansion en hoja.
c = input() #Obtener cadena.
n = len(c) ** 0.5 #Elevarlo a 1/2, matematicamente lo opuesto a un cuadrado, una raiz.
a = 0 #Contador indice de la cadena.
if n > int(n): #Si el numero tiene coma.
    n = int(n)+1 #Suma uno.


m = [[_ for _ in range(n)]for _ in range(n)] #Crear matriz cuadrada.
for i in range(n): #Recorrer y guardar cadena en matriz.
    for j in range(n):
        if a < len(c):
            m[i][j] = c[a]
            a = a + 1 #Recorrer indice cadena.
        else:
            m[i][j] = "*" #Remplazamos con asteriscos.

s = "" #Subcadena cifrada.
for i in range(n):
    for j in range(n):
        s = s + m[j][i] #Guarda la cadena en formato vertical.

print(s)