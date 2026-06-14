#Pre parcial - Matrices.
f = int(input())  #Recibir columnas.
c = int(input())  #Recibir filas.
m = [[0 for _ in range(c)]for _ in range(f)] #Definir matriz
for i in range(f): #Obtengo la matriz
    for j in range(c):
        m[i][j] = int(input())

v = [-5]*(c*f*3)
d = 0
cd = 0 #Contador.

for i in range(f): #Itero la matriz para poder obtener valores distintos a 0
    for j in range(c):
        if m[i][j] != 0:
            print("Este valor se aprobo: ", m[i][j], "Indice: ", i, j)
            v[d] = i + 1
            v[d+1] = j + 1
            v[d+2] = m[i][j]
            d = d + 3

s = "" #Para imprimir
v2 = [0]*3 #Valores y pos mayor.
cd = d #Cuenta el tamaño del vector.
d = 2 #Verificar el valor del elemento.

print("Vector antes de la impresora", v)
for i in range(cd): #Itero el vetor para el print y el mayor.
    s = s + str(v[i])
    if cd > d+1:
        if v2[0] < v[d]:
            v2[0] = v[d]
            v2[1] = v[d-2]
            v2[2] = v[d-1]
            d = d + 3
print(s)
print(f"posicion mayor [{v2[1]},{v2[2]}]")