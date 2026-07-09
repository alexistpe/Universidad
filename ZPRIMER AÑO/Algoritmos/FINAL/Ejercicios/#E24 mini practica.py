#E24 mini practica.
#Debido al tiempo limitado, realizare un programa de mantenimiento:
#Intercambiar 2 matrices ingresadas.
#Recibir tamaño de las matrices.
#Rellenar matrices.
#Intercambiar valor a valor: obtener el valor de m1 en su pos, guardarlo, remplazarlo por m2, y remplazar el valor de m2 por el guardado de m1.

n = int(input())
m1 = [[int(input("M1: ")) for _ in range(n)]for _ in range(n)]
m2 = [[int(input("M2: ")) for _ in range(n)]for _ in range(n)]

#Imprimir.
print("M1")
for i in range(n):
    s = ""
    for j in range(n):
        s = s + str(m1[i][j]) + " "
    print(s)

print("--------------")
print("M2")
for i in range(n):
    s = ""
    for j in range(n):
        s = s + str(m2[i][j]) + " "
    print(s)
print("-------RESULTADO-------")

for i in range(n):
    for j in range(n):
        a = m1[i][j]
        m1[i][j] = m2[i][j]
        m2[i][j] = a

#Imprimir.
print("M1")
for i in range(n):
    s = ""
    for j in range(n):
        s = s + str(m1[i][j]) + " "
    print(s)

print("--------------")
print("M2")
for i in range(n):
    s = ""
    for j in range(n):
        s = s + str(m2[i][j]) + " "
    print(s)