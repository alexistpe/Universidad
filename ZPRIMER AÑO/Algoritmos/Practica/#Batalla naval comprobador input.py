#Batalla naval comprobador input.
def verify(m,f,c):
    count = 0
    if f > 0:
        f = f - 1
    if c > 0:
        c = c - 1
    for i in range(3): #Verificar que no hayan barcos cercanos.
        for j in range(3):
            if (f+i <= len(m)-1) and (c+j <= len(m)-1) and m[f+i][c+j] == 1:
                count = count + 1
    if count >= 3:
        return True
    else:
        return False



cant = int(input()) #Cantidad de barcos.
vbarcos = input().split() #Tipo de barcos.
tabla = int(input()) #Tablero.
salir = False #Flag.

for i in range(2):
    if int(vbarcos[i]) > 3 or tabla > 128:
        salir = True

m = [[0 for _ in range(tabla)]for _ in range(tabla)]

for i in range(tabla): #Añadir fila.
    temp = input().split()
    for j in range(tabla):
        m[i][j] = temp[j]

for i in range(3):
    for j in range(tabla):
        if m[i][j] != 0 and salir == False:
            if verify(m,i,j) == True:
                salir = True

if salir == False:
    print("APROBADO")
else:
    print("DESAPROBADO")
