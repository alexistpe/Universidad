#Justificar texto.
def ver(n): #Verificar cadena enviada, para justificar a 20 caracteres.
    b =  len(n) #Tamaño subcadena og.
    s = "" #Subcadena.
    e = 0 #Espacios (Detectar casos).

    if b == 20: #Si ya esta justificado.
        return(n) #Lo retorna.
    
    if b == 21:
        return(caso3(n)) #Se retorna la correccion de punto o coma.
    
    if b > 20: #Si es mayor, recortar la ultima palabra.
        for i in range(b):
            if n[(b-1)-i] == " ": #Encontar el primer espacio en lo inverso.
                for j in range(b-(i+1)): #Guardar cadena antes del espacio.
                    s = s + n[j] #Guardar resto de la subcadena.
                break
    
    for i in range(len(s)): #Encontrar cantidad de espacios.
        if s[i] == " ":
            e = e + 1 #Cuenta los espacios.
    
    if e == 0: #Una sola palabra.
        return caso1(s)
    elif e >= 1: #Dos o mas palabras.
        return caso2(s)
    

def caso1(n):
    s = "" #Subcadena Modificada.
    for i in range(len(n)):
        s = s + n[i] #Agrega el texto.
        if len(s) + (len(n)-(i+1)) == 20: #Si la separacion mas lo que resta del texto, alcanzan.
            for j in range(len(n)-(i+1)):
                j = j + 1 #Comienza en el siguiente.
                s = s + n[i+j]
            return(s) #Retornar string acomodado.
        s = s + " " #Agrega el espacio.
        if len(s) + (len(n)-(i+1)) == 20: #Si la separacion mas lo que resta del texto, alcanzan.
            for j in range(len(n)-(i+1)):
                j = j + 1 #Comienza en el siguiente.
                s = s + n[i+j]
            return(s) #Retornar string acomodado.



def caso2(n):
    m = len(n) #Tamaño del string.
    k = 1 #Espacios a sumar.
    while k > 0:
        s = "" #Subcadena Modificada.
        for i in range(len(n)):
            s = s + n[i]
            if n[i] == " ":
                for b in range(k): #Va sumando cada vez mas espacios extra.
                    if (len(s) + (m - (i+1))) == 20: #Si el tamaño de 's' mas lo que resta de 'n' suman 20.
                        for j in range(m - (i+1)): #Itera lo que resta de texto.
                            j = j + 1 #Itera una vez menos porque j comienza en 1.
                            s = s + n[i + j]
                        return s #Retorna el texto justificado.
                    s = s + " " #Espacio extra.
                    
                    
        k = k + 1 #Se suma un espacio mas.
        if len(s) > 20:
            return "0"

def caso3(n):
    m = len(n) #Tamaño del string.
    k = 1 #Espacios a sumar.
    s = "" #Subcadena Modificada.
    for i in range(len(n)):
        s = s + n[i]
        if n[i] == "." or n[i] == ",": #Si el siguiente caracter es una coma.
            for j in range(len(n) - (i+2)): #Itera lo que resta de texto.
                    j = j + 2 #Itera una vez menos porque j comienza en 1.
                    s = s + n[i + j]
            return s #Retorna el texto justificado.

def indice(n): #Se encarga de reposicionar el indice.
    b =  len(n) #Tamaño subcadena og.
    if b == 21 or b == 20: #Si incluye a todo el texto.
        return 0 #Que no modifique el indice.
    else:
        for i in range(b):
            if n[(b-1)-i] == " ": #Encontar el primer espacion en lo inverso.
                return (i+1) #Retorna cuanto debe volver hacia atras.


s = input() #Cadena.
n = "" #Subcadena.
i = 0 #Contador.
while i < len(s):
    if len(n) >= 20 and s[i] == " ": #Una vez llegado a los 20, entrar cuando se encuentre el primer espacio.
        t = indice(n) #Valores extra al inicio de la ultima palabra de N.
        n = ver(n) #Concatenamos el texto justificado.
        print(n)
        n = "" #Reiniciamos la subcadena.
        i = i - t #Posicionamos en la primera letra de la ultima palabra de N.
    else:
        n = n + s[i]
    i = i + 1

if n != "":
    print(n)




