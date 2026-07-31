#E23 tres en raya.
#Consiste en simular el juego 3 en raya, con sus reglas y manteniendo un bucle constante hasta que un jugador gane.
#Expandido en papel.

def mover(p, m, tar, pos): #Se encarga de mover las fichas en la matriz.
    m[tar[0]][tar[1]] = py[0] #Asigna la ficha del jugador.
    if p <= 0: #Si esta moviendo la ficha (no tiene mas fichas).
        m[pos[0]][pos[1]] = 0 #Libera el lugar.
    return m

def valido(p, m, position, target): #Validar movimientos y realizarlos.
    #Obtener coordenadas.
    pos = []
    if len(position) > 0:
        pos = [int(position[0]),int(position[2])]
    tar = [int(target[0]),int(target[2])]

    if m[tar[0]][tar[1]] != 0 or (len(pos) > 0 and m[pos[0]][pos[1]] != py[0]): #Si esta ocupada o quiere mover una ficha diferente.
        return [] #Invalidar movimiento.

    if py[1] > 0 or pos[0] == pos[1]: #Si estas eligiendo o estas en el medio.
        #Se posiciona directamente.
        return mover(py[1], m, tar, pos) #Llama a funcion de mover.
    elif (abs(pos[0] - tar[0]) + abs(pos[1]-tar[1])) < 2: #Si no quiso mover diagonalmente.
        return mover(py[1], m, tar, pos) #Llama a funcion de mover.
    else: #Si quiso mover diagonalmente.
        return [] #Invalidar movimiento.

def ganador(m): #Validar patrones ganadores.
    #Comprobar patrones posibles y devolver el jugador que gano.
    for i in range(3): #Iterar 3 veces para validar 3 en raya.
        if m[i][0] == m[i][1] == m[i][2] and m[i][0] != 0:
            return m[i][0]
        elif m[0][i] == m[1][i] == m[2][i] and m[0][i] != 0:
            return m[0][i]
    if m[0][0] == m[1][1] == m[2][2] and m[0][0] != 0:
        return m[0][0]
    elif m[0][2] == m[1][1] == m[2][0] and m[0][2] != 0:
        return m[0][2]
    else: #Si ninguno gano
        return 0 #Retornar ninguno.

def cambio(p, j): #Cambiar jugador.
    if p[0] == 1: #Si es el primer jugador.
        #Cambiamos por el segundo.
        p[0] = 2
        p[1] = j[1]
    else:
        #Cambiamos por el primero.
        p[0] = 1
        p[1] = j[0]
    
    return p

f = [3,3] #Definir fichas de los 2 jugadores.
py = [1,3] #Nro jugador y fichas disponibles.
m = [[0 for _ in range(3)]for _ in range(3)]
g = 0 # Toma el valor del Ganador.

while g == 0: #Mientras no haya ganador.
    #Imprimir matriz.
    p = t = ""
    for i in range(3):
        s = "" #Imprimir matriz con formato.
        for j in range(3):
            s = s + str(m[i][j]) + " "
        
        print(s)
    
    if py[1] <= 0:
        p = input("Posicion ficha a eleccion. Ej: 1,0: ")
    t = input("Posicion del destino. Ej: 2,0: ")

    a = valido(py, m, p, t)
    if a == []:
        print("salteando")
        continue #Saltar iteracion.
    else:
        m = a #Remplazamos matriz.
    
    g = ganador(m)

    if g != 0: #Si se encontro ganador.
        for i in range(3):
            s = "" #Imprimir matriz con formato.
            for j in range(3):
                s = s + str(m[i][j]) + " "
            print(s)
        print("El ganador es el jugador: ",g)
        break #Sale del bucle.

    if f[py[0]-1] > 0: #Si el jugador tiene fichas.
        f[py[0]-1] -= 1 #Al jugador actual, le restamos una ficha.
    py = cambio(py,f)