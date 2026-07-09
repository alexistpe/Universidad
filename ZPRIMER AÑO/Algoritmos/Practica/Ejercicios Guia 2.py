#Ejercicios Guia 12
def relleno(m,f,c):
    r = 0
    for i in range(f):
        for j in range(c):
            r = r + 1
            m[i][j] = r
    return m

def multi(m,m2):
    for i in range(3):
        for j in range(3):
            m[i][j] = m[i][j] * m2[i][j]
    return m

def mostrar(m):
    for i in range(3):
        s = ""
        for j in range(3):
            s = s + str(m[i][j]) + " "
        print(s)

m = [[0 for _ in range(3)]for _ in range(3)]
m2 = [[0 for _ in range(3)]for _ in range(3)]
m = relleno(m,3,3)
m2 = relleno(m2,3,3)
m = multi(m,m2)
mostrar(m)

