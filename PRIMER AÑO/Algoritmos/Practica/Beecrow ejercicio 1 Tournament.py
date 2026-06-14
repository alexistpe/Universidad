#Beecrow ejercicio 1 Tournament.
n = int(input()) #Recibir cadena.
a = "@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_'abcdefghijklmnopqrstuvwxyz{|}" #Tabla ascii + 3 y -1.
sc = "" #Subcadena.
for k in range(n): #Iterar por la cantidad de veces necesarias.
    s = input() #Guardar cadena.
    for i in range(len(s)): #Iterar cadena.
        f = a.find(s[i]) #Buscamos la letra.
        if f != -1 and a[f].isalpha(): #Preguntamos por la letra.
            sc = sc + a[f+3] #Lo guardamos 3 lugares mas.
            #print(f"Cadena primer paso: {sc}")
        else: #SI no encontro una la letra.
            sc = sc + s[i] #Guardamos la cadena.

    mid = int(len(sc)/2) #Obtener la mitad truncada.
    r = list(sc)
    r.reverse() #Invertir.
    s = ""
    s = r[0:mid] #Obtener mitad de la cadena.

    for i in range(mid, len(sc)):
        f = a.find(r[i+mid]) #Buscamos el caracter.
        if f != -1: #SI lo encontro.
            s = s + a[f-1] #Concatenar caracter anterior.
            #print(f"Cadena formada hasta ahora paso 3: {sc2}")
    
    print(sc2) #Imprime el texto.
    sc2 = ""
    cs = ""