#Detectar anagramas y palindromos.
def pal(s): #Palindroma.
    m = len(s) - 1 #Obtenemos el tamaño de la subcadena iterable.
    f = 0 #Bandera de no palindromo.
    c = s.lower()
    for i in range(int((m+1)/2)): #Intercambiar palabra (Invertirla).
        if c[i] != c[m-i]: #Si la posicion de la primera mitad no es la misma que la segunda mitad.
            f = 1
    
    if f == 0 and m > 0: #Si es igual a la inversa.
        print(s) #Imprimir palabra.



def ana(g, s): #Anagrama, g = subcadena, s = cadena.
    c = b = 0 #Definimos indices.
    t = 0 #Flag y break.
    p = g.lower()
    while c < len(s) and t != -1: #Detectar anagramas.
        if s[c] == " " or c == 0: #Si termino la palabra o recien comienza la oracion.
            c1 = c
            if c > 0: #Si NO es el inicio, empeza desde la palabra.
                b = c + 1 #Comenzamos en la palabra.
                c1 = c + 1
            
            while s[b] != " " and s[b] != "." and s[b] != "," and b < len(s)-1:
                b = b + 1

            if b < len(s)-1 or s[b] == ".": #Si se detuvo por un espacio.
                b = b - 1 #Se decuenta.
            
            #c+1 y b son las posiciones donde comienza y termina una palabra.
            sub = ""
            for i in range((b - (c1))+1): #Iterar tamaño de la palabra.
                sub = sub + s[(c1)+i] #Guardo la sub cadena.

            sub = sub.lower()

            if len(sub) == len(g) and sub != p: #SI tienen la misma longitud y no son la misma palabra.
                t = len(p)
                for i in range(t): #Iterar caracter por caracter.
                    f = 0
                    for j in range(t): #Verificar con todos los caracteres de la palabra.
                        if sub[i] == p[j]: #SI encontro un caracter igual.
                            #Comprobar lo inverso, para confirmar que comparten los mismos caracteres.
                            for u in range(t):
                                if p[i] == sub[u]:
                                    f = 1                 
                    
                    if f == 0:
                        t = 0 #Break, ya no son anagramas.
                
                if t != 0: #Si no hubieron errores.
                    print(g, "-", sub) #Son anagramas.
                    t = -1

            c = b #Pasa al fin de la palabra.
        
        c = c + 1 #Va recorriendo, es un sub indice, toma el siguiente espacio.


s = input()
c = 0
b = 0
print("Palíndromas:") #Primera iteracion.
while c < len(s): #Detectar palindromo.
    if s[c] == " " or c == 0: #Si termino la palabra o recien comienza la oracion.
        c1 = c
        if c > 0: #Si NO es el inicio, empeza desde la palabra.
            b = c + 1 #Comenzamos en la palabra.
            c1 = c + 1
        
        while s[b] != " " and s[b] != "." and s[b] != "," and b < len(s)-1:
            b = b + 1

        if b < len(s)-1 or s[b] == ".": #Si se detuvo por un espacio.
            b = b - 1 #Se decuenta.
        
        #c+1 y b son las posiciones donde comienza y termina una palabra.
        sub = ""
        for i in range((b - (c1))+1): #Iterar tamaño de la palabra.
            sub = sub + s[(c1)+i] #Guardo la sub cadena.
        
        pal(sub) #LLamo a la funcion para que lo analice.

        c = b #Pasa al fin de la palabra.
    
    c = c + 1 #Va recorriendo, es un sub indice, toma el siguiente espacio.

print("Anagramas:") #Segunda iteracion.
c = 0
b = 0
while c < len(s): #Detectar palindromo.
    if s[c] == " " or c == 0: #Si termino la palabra o recien comienza la oracion.
        c1 = c
        if c > 0: #Si NO es el inicio, empeza desde la palabra.
            b = c + 1 #Comenzamos en la palabra.
            c1 = c + 1
        
        while s[b] != " " and s[b] != "." and s[b] != "," and b < len(s)-1:
            b = b + 1

        if b < len(s)-1 or s[b] == ".": #Si se detuvo por un espacio.
            b = b - 1 #Se decuenta.
        
        #c+1 y b son las posiciones donde comienza y termina una palabra.
        sub = ""
        for i in range((b - (c1))+1): #Iterar tamaño de la palabra.
            sub = sub + s[(c1)+i] #Guardo la sub cadena.
            #print(f"Guardando la palabra pal: {sub}, desde {c1} a {b+1}")
        
        ana(sub, s) #LLamo a la funcion para que lo analice (subCadena, cadena).

        c = b #Pasa al fin de la palabra.
    
    c = c + 1 #Va recorriendo, es un sub indice, toma el siguiente espacio.

