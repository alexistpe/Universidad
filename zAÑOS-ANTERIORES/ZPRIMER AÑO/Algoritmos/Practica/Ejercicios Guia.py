#Ejercicios Guia 10
def relleno(m,f,c):
    r = 0
    for i in range(f):
        for j in range(c):
            r = r + 1
            m[i][j] = r
    return m

def trans(m, m2,f,c):
    for i in range(f):
        for j in range(c):
            m2[j][i] = m[i][j]
    return m2
    #Bloque matrices cuadradas sin matriz extra.
    # for i in range(c):
    #     for j in range(f-i):
    #         j = j + i
    #         v = m[j][i] #Intercambio
    #         m[j][i] = m[i][j] #De
    #         m[i][j] = v #Valores
    # return m

def mostrar(m,m2,f,c):
    print("Matriz original:")
    for i in range(f):
        s = "" #String
        for j in range(c):
            s = s + str(m[i][j]) + " "
        print(s)
    
    print("Matriz transpuesta:")
    for i in range(c):
        s = "" #String
        for j in range(f):
            s = s + str(m2[i][j]) + " "
        print(s)

f = int(input())
c = int(input())
m = [[0 for _ in range(c)]for _ in range(f)]
m2 = [[0 for _ in range(f)]for _ in range(c)]
m = relleno(m,f,c)
m2 = trans(m, m2,f,c)

mostrar(m,m2,f,c)