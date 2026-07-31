#Acortador de texto.
def aco(b, cr, cv, s, k): #Acortar texto.
    b.lower() #Normalizar.
    n = ""
    t = len(s)
    for i in range(4):
        if  cv[i] == b: #Si encontro una palabra que se puede resumir.
            b = cr[i] #La remplazamos.
            for j in range(t): #Iterar el texto og.
                n = n + s[j] #Va guardando el texto correcto.
                if j == k: #Si llego al punto donde hay que corregir la psalabra.
                    u = len(cv[i]) #Guarda el tamaño que ocupa la palabra.
                    print(f"PALABRA LONG {u}, letra en K: {s[k]}")
                    for f in range(t-(k+u)): #Iterar el resto del texto no validado, para ir guardando la parte validada e remplazarlo luego.
                        print(f"Longitud texto: {t}, Iteraciones en {k+u + f} letra {s[k+u + f]}, iteraciones a realizar: {t-(k+u)} desde {k+u}")
                        n = n + s[k+u + f]
                    
                    return n
    
    return s
                    

s = input() #Texto original.
new = s #Texto a modificar.
cr = ["q","l","d","s"]
cv = ["que", "lo", "de", "se"]
c = 0 #Definir contador.
b = 0

while c < len(s): #Detectar palindromo.
    if s[c] == " " or s[c] == "," or c == 0: #Si termino la palabra o recien comienza la oracion.
        c1 = c
        if c > 0: #Si NO es el inicio, empeza desde la palabra.
            b = c + 1 #Comenzamos en la palabra.
            c1 = c1 + 1 #Comienza en la palabra.
        
        while s[b] != " " and s[b] != "." and s[b] != "," and b < len(s)-1:
            b = b + 1

        if b < len(s)-1 or s[b] == ".": #Si se detuvo por un espacio.
            b = b - 1 #Se decuenta.
        
        #c+1 y b son las posiciones donde comienza y termina una palabra.
        sub = ""
        for i in range((b - (c1))+1): #Iterar tamaño de la palabra.
            sub = sub + s[(c1)+i] #Guardo la sub cadena.
        
        print(f"Enviando estos datos: {sub} (palabra), {new} (cadena modificada), {c1} (Lugar de la primera letra que es: {s[c1]})")
        c1 = c1 - ((len(s)-1) - (len(new)-1)) #Ajustamos el indice.
        p = aco(sub, cr, cv, new, c1) #LLamo a la funcion para que lo analice.
        new = p

        c = b #Pasa al fin de la palabra.
    
    c = c + 1 #Va recorriendo, es un sub indice, toma el siguiente espacio.

print("ans =", new)
print("diferencia =", (len(s)-len(new))+1)