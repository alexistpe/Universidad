#E26 Beecrow Identificar aliteraciones.
#Consiste en identificar iniciales de palabras consecutivas iguales.

c = input() #Obtener cadena.
c = c.upper() #Todos los caracteres valen lo mismo.
t = 0 #Total contador.
f = False #Flag para evitar repeticiones.
s = c[0] #Caracter previo.

for i in range(len(c)):
    if i > 0 and c[i-1] == " " and c[i] != " ": #Si encontro el inicio de la palabra.
        if s == c[i] and f == False: #Si encontro un patron y no es repetido.
            t = t+1
            f = True #Habilitar stop a la repeticion.
        elif s != c[i]: #Si rompio la secuencia.
            s = c[i] #Guardamos nuevo caracter previo.
            f = False #Reiniciamos variable bloqueo.
print(t) #Escribir cantidad.
