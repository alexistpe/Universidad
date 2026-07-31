#Listas VPL

def recursivo(n, start, e): #Recursividad para encontrar los nombres en la lista enlazada.
    if n == 0: #Devolver inicio.
        return start #Corta el bucle.
    else:
        a = recursivo(n-1, start, e)
        return e[a]


n = [] #Nombres.
e = [] #posicion (Indice).
e2 = [] #posicion inversa (Indice).
inicio = 0 #Indice inicial.
fin = 0 #Indice final.
a = "" #Input.

while a != "0":
    di = 0 #Indice actual.
    di2 = 0 #Indice actual.
    r = [] #Lista de repetidos.
    r2 = [] #Lista de repetidos inversos.
    a = input() #Recolectar nombres.
    if a == "0":
        break
    
    n.append(a) #Añadimos los nombres secuencialmente a la lista.
    e = [-1]*len(n) #Añadimos posiciones a la lista de indices, el ultimo se preguarda con -1.
    e2 = [-1]*len(n) #Añadimos posiciones a la lista de indices, el ultimo se preguarda con -1.

    for i in range(len(n)): #Iterar la lista para determinar las posiciones ordenadas de los indices.
        f1 = 0 #Flag menor.
        f2 = 0 #Flag mayor.
        
        for y in range(len(n)): #Elegir menor.
            if f1 == 0 and n[y] not in r:
                m = n[y] #Lo asignamos como menor inicial.
                f1 = 1
            
            if f2 == 0 and n[y] not in r2:
                m2 = n[y] #Lo asignamos como menor inicial.
                f2 = 1
        
        for j in range(len(n)):
            if m >= n[j] and n[j] not in r: #Si encontro uno menor.
                m = n[j] #Recuperamos nombre.
                di = j #Recuperamos indice.
        
        for j in range(len(n)):
            if m2 <= n[j] and n[j] not in r2: #Si encontro uno mayor.
                m2 = n[j] #Recuperamos nombre.
                di2 = j #Recuperamos indice.
            
        r.append(m) #Guardamos el nombre del menor encontrado. Mantenemos un registro secuencial.
        r2.append(m2)
        if len(r) > 1: #Si no es el primero.
            for k in range(len(n)): #Asignar indice siguiente.
                if r[len(r)-2] == n[k]: #Si encontramos el menor anterior (id).
                    e[k] = di #Asignamos el id del siguiente menor (el que encontramos en esta iteracion).
        else: #Si es el primer elemento.
            inicio = di #Guardamos el indice del primero.
        
        if len(r2) > 1: #Si no es el primero.
            for k in range(len(n)): #Asignar indice siguiente.
                if r2[len(r2)-2] == n[k]: #Si encontramos el mayor anterior (id).
                    e2[k] = di2 #Asignamos el id del siguiente menor (el que encontramos en esta iteracion).
        else: #Si es el primer elemento.
            fin = di2 #Guardamos el indice del primero.
    
    #IMPRIMIR DATOS DE LAS LISTAS.
    print("----------------------------------")
    print(f"Nombres: {n}")
    print(f"Siguiente: {e}")
    print(f"Anterior: {e2}")
    print(f"Inicio: {inicio}")
    print(f"Fin: {fin}")
    print("----------------------------------")

print("Recorrido ascendente:")
for i in range(len(n)): #Imprimir resultados.
    print(f" -> {n[recursivo(i, inicio, e)]}")

print("Recorrido descendente:")
for i in range(len(n)): #Imprimir resultados.
    print(f" -> {n[recursivo(i, fin, e2)]}")
        
        


        


