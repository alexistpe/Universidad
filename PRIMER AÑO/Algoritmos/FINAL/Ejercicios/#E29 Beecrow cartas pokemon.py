#E29 Beecrow cartas pokemon.
def binaria(lista, v): #Busqueda binaria.
    der = len(lista)-1
    izq = 0
    while izq <= der:
        medio = (izq + der) // 2 #Se obtiene el medio entre esa parte del array.
        val = lista[medio]
        if val == v: #Si se repite el valor.
            return True #LO ENCONTRO.
        elif val > v: #Esta a la izquierda el valor buscado.
            der = medio - 1 #Movemos el puntero de la derecha.
        else: #Esta a la derecha el valor buscado.
            izq = medio + 1 #Movemos el puntero de la izquierda.
    
    return False #No lo encontro.

def busqueda(v1, v2): #Valores para realizar busqueda.
    #Recorrer mediante busqueda binaria, ya que se encuentran en orden.
    intercambio = 0 #Intercambio contador.
    l1 = [] #Repetidos.
    for i in range(len(v1)):
        if binaria(l1,v1[i]) == True: #Comprobamos si se repitio anteriormente.
            continue #Prueba con el siguiente.
        
        if binaria(v2,v1[i]) == False: #Comprobamos si no existe en el otro mazo.
            intercambio += 1 #Aumenta la cantidad de intercambios..
        
        l1.append(v1[i]) #Añadimos el valor analizado a lista de repetidos.
    return intercambio #Retorna la cantidad de posibilidades.

cant = ""
while cant != "0 0":
    try:
        cant = input()
        if not cant or cant == " ": break
    except EOFError:
        break #Finalizo
    a = 0 #Total para salir.
    for i in range(len(cant)):
        if cant[i] != " ":
            a = a + int(cant[i])
    
    if a == 0: #Si mandaron la secuencia de salida.
        break


    c1 = input() #Primer mazo
    c2 = input() #Segundo mazo
    c1 = c1 + " "
    c2 = c2 + " "
    v1 = [] #Primer mazo procesado.
    v2 = [] #Segundo mazo procesado.

    l1 = [] #Mazo repetidas.
    l2 = [] #Segundo mazo de repetidas.

    it = 0 #Intercambio primer mazo.
    it2 = 0 #Intercambio segundo.

    s = "" #Subcadena.
    for i in range(len(c1)):
        if c1[i] == " ":
            v1.append(int(s))
            s = ""
        else:
            s = s + c1[i]
    s = ""
    for i in range(len(c2)):
        if c2[i] == " ":
            v2.append(int(s))
            s = ""
        else:
            s = s + c2[i]

    it = busqueda(v1, v2)
    it2 = busqueda(v2, v1)
    if it > it2:
        print(it2)
    else:
        print(it)

