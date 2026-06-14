#Acortar URL.
url = input() #Url og.
t = len(url) #Tamaño de la url.
b = "" #Nueva cadena.
c = 0 #Contador bucle.
while c < t: 
    if c < (t-1) and url[c] == "/" and url[c+1] == "/": #Si encuentra el protocolo.
        for i in range(t - (c+2)): #Guardar texto sin protocolo.
            if url[(c+2)+i] == "/": #Terminar de guasrdar direccion.
                b = b + url[(c+2)+i]
                break
            b = b + url[(c+2)+i] #Parte de lo posterior al protocolo y direccion.
        c = (c+2) + i
    elif url[c] == "/" and c <= t-1:
        j = c + 1 #Empieza desde el caracter.
        while j < t-1 and url[j] != "/": #Mientras no llegue al final o encuentre /
            j = j + 1 #Recorrer url.

        if j < (t) and url[j] == "/": #Si encontro algo valido.
            for i in range(j-c): #Iterar texto valido.
                b = b + url[c+i+1] #Guarda el url valido.
        c = j #Continua en el siguiente caracter despues de j.
    else:
        c = c + 1
print(b)