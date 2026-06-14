#Juego del ahorcado.
s = input() #Cadena original.
s = s.upper() #Lo convierte en mayuscula.
c = "" #Cadena de intentos.
p = 6 #Contador de intentos.
while p > 0: #Mientras tenga intentos.
    k = input()
    k = k[0] #Solo toma la primera letra.
    c = c + k.upper() #Concatenar a la cadena de intentos y lo convierte en mayuscula.
    b = "" #Reiniciamos b.
    for i in range(len(s)):
        f = "_" #Caracter a concatenar.
        for j in range(len(c)): #Verificar si acerto alguno.
            if s[i] == c[j]: #Si encontro coincidencia.
                f = c[j] #Remplaza el caracter a concatenar.
        
        b = b + f #Concatena el caracter.
    for i in range(len(b)): #Verificamos la cadena formada.
        if b[i] == "_": #Si aun no completo la palabra.
            f = "0" #Activamos bandera.
            break #Sale del iterar.
    if f != "0": #Si completo la palabra.
        print(f"Gano con {p} intentos restantes")
        print(b)
        p = -1
    else:
        print(f"{c}  {b}  intentos: {p-1}") #Imprime la cadena formada, la cadena original, y los intentos restantes.
        p = p - 1 #Descartar el intento.

if p == 0: #Si perdio.
    print(f"Perdio, la palabra era: {s}")