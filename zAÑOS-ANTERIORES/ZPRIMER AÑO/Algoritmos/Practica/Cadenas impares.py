#Cadenas impares.
s = input()
i = 0
c = 0
t = 0
while i < len(s): #Mientras no llegue al limite.
    if s[i] == " " or i == 0: #Si encontro un espacio o es el inicio.
        if i != 0: #Si es el inicio, entonces que no arranque desde el siguiente.
            c = i + 1
         
        while c < len(s)-1 and s[c] != " ": #Registrar caracteres de la palabra.
            c = c + 1 #Sumar cantidad de caracteres.

        #if c == len(s):
        #    c = c - 1

        if s[c] == " ":
            c = c-1 #Descontamos el espacio.
        
        if i == 0:
            i = -1 #Compenzar resta.

        #print(f"Encontre {c-i} caracteres desde la posicion {i+1} a la posicion {c+1}")

        if c-i > 1 and (c-i)%2 != 0: #Es impar.
            t = t + 1
        
        i = c #Lo deja en la ultima letra de la palabra.

    i = i + 1 #Continua buscando.

print(t) #Mostrar cantidad de palabras impares.