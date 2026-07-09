#E21 Parcial promocion.
#Determinar segun una matriz, si la fecha ingresada existe, e imprimir su fila, sino buscar fecha mayor y menor mas cercana con sus filas.
def buscar(m,f):
    for i in range(len(m)): #Buscar fecha en las filas.
        if m[i][4] == f: #Si es la misma fecha.
            return i #Retorna el indice.
    
    return -1 #Retorna error.


def mayor(m,f): #Fecha mayor mas cercana.
    fb = [] #Fecha buscada.
    index = -1 #Indice de la fecha.
    s = "" #String a retornar.

    for i in range(len(m)):
        b = False #Bandera valido.
        b2 = False #Bandera buscado.
        b3 = False #Bandera de numero correcto.
        for j in range(3):
            k = 3-j #Itera las columnas de año, mes, y dia respectivamente.
            if b3 == False and int(m[i][k]) < int(f[2-j]): #Si es menor a la fecha base, se descarta.
                b = True #Activamos bandera.
                break #Salimos de esta iteracion
            elif fb == [] or int(m[i][k]) < int(fb[2-j]): #Si encontro una alternativa mas pequeña (trival -sin alretnativas- o logica).:
                b2 = True #El valor encontrado es mas cercano.
            
            b3 = True #Sirve para que se siga analizando mas alla del año.
        
        if b == False and b2 == True: #Mientras el valor obtenido sea valido y mas cercano.
            e = [m[i][1], m[i][2], m[i][3]] #Recolectar fecha en formato vector.
            fb = e #Remplazamos fecha buscada.
            index = i #Obtenemos la fila.
    
    if index != -1:
        s = m[index][4] #Obtenemos la fecha directamente.
    
    return s #Retorna la fecha.

def menor(m,f): #Fecha menor mas cercana.
    fb = [] #Fecha buscada.
    index = -1 #Indice de la fecha.
    s = "" #String a retornar.

    for i in range(len(m)):
        b = False #Bandera valido.
        b2 = False #Bandera buscado.
        b3 = False #Bandera de numero correcto.

        for j in range(3):
            k = 3-j #Itera las columnas de año, mes, y dia respectivamente.
            if int(m[i][k]) > int(f[2-j]): #Si es mayor a la fecha base, se descarta.
                b = True #Advertimos.
                break #Salimos de esta iteracion
            elif fb == [] or int(m[i][k]) > int(fb[2-j]): #Si encontro una alternativa mas grande (trival -sin alretnativas- o logica).
                b2 = True #Habilitamos.
            
            b3 = True #Sirve para que se siga analizando mas alla del año.
        
        if b == False and b2 == True: #Si es valido y mas cercano:
            e = [m[i][1], m[i][2], m[i][3]] #Recolectar fecha en formato vector.
            fb = e #Remplazamos fecha buscada.
            index = i #Obtenemos la fila.
    
    if index != -1:
        s = m[index][4] #Obtenemos la fecha directamente.
    
    return s #Retorna la fecha.

t = int(input("Tamaño filas: "))
m = [[input() for _ in range(5)]for _ in range(t)]
print(f"Matriz: {m}")
f = input("Ingresar fecha: ")

a = buscar(m,f)
if a != -1:
    print("EXISTE")
    print(f"FILA: {a}")
else:
    #Convertir cadena a lista.
    e = [f[0:2],f[3:5],f[6:]]
    
    #Alternativa algoritmica:
    #e = []
    #c = 0 #Contador vector.
    #a = "" #Subcadena.
    #for i in range(len(f)):
    #    if f[i] == ":":
    #        e[c] = int(a)
    #        a = "" #Reiniciamos cadena.
    #        c = c + 1 #Aumentamos indice.
    #    else:
    #        a = a + f[i] #Concatenamos.
    ma = mayor(m,e)
    lo = menor(m,e)
    print(f"Mayor mas cercana: {ma}")
    print(f"Indice: {buscar(m,ma)}")
    print(f"Menor mas cercana: {lo}")
    print(f"Indice: {buscar(m,lo)}")


