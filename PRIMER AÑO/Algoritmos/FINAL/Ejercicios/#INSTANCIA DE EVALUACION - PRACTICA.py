#INSTANCIA DE EVALUACION - PRACTICA.

def existe(m,f):
    for i in range(len(m)):
        if m[i][4] == f:
            return(i)
    return -1
def mayor(m,f):
    fp = [0]*3
    f2 = [0]*3
    s = ""
    c = 0
    ind = -1

    #Fecha en indice.
    for i in range(len(f)):
        if f[i] == "/":
            f2[c] = int(s)
            c += 1
            s = "" #Reiniciarlo.
        else:
            s = s + f[i]
    f2[2] = int(s) #Año

    for k in range(len(m)):
        b1 = False
        b2 = False
        for i in range(3):
            if b1 == False and int(m[k][3-i]) < f2[2-i]:
                break
            elif b1 == False and int(m[k][3-i]) > f2[2-i]:
                b1 = True
            
            if fp[0] != 0 and int(m[k][3-i]) > fp[2-i] and b2 == False:
                b1 = False
                break
            elif fp[0] != 0 and int(m[k][3-i]) < fp[2-i]:
                b2 = True
            elif fp[0] == 0:
                b2 = True #Primera.
        if b1 == True and b2 == True:
            for i in range(3):
                fp[i] = int(m[k][i+1])
            ind = k
    return ind
            

def menor(m,f):
    fp = [0]*3
    f2 = [0]*3
    s = ""
    c = 0
    ind = -1

    #Fecha en indice.
    for i in range(len(f)):
        if f[i] == "/":
            f2[c] = int(s)
            c += 1
            s = "" #Reiniciarlo.
        else:
            s = s + f[i]
    f2[2] = int(s) #Año
    for k in range(len(m)):
        b1 = False
        b2 = False
        for i in range(3):
            if b1 == False and int(m[k][3-i]) > f2[2-i]:
                break
            elif b1 == False and int(m[k][3-i]) < f2[2-i]:
                b1 = True
            
            if fp[0] != 0 and int(m[k][3-i]) < fp[2-i] and b2 == False:
                b1 = False
                break
            elif fp[0] != 0 and int(m[k][3-i]) > fp[2-i]:
                b2 = True
            elif int(fp[0]) == 0:
                b2 = True #Primera.
        if b1 == True and b2 == True:
            for i in range(3):
                fp[i] = int(m[k][i+1])
            ind = k
    return ind

n = int(input()) #Filas.
m = [[input() for _ in range(5)] for _ in range(n)] #Matriz.
f = input() #Fecha.

v = existe(m,f)

if v > -1:
    print(f"Existe: {v}")
else:
    h = mayor(m,f)
    l = menor(m,f)

    print("No existe:")
    print(f"Mayor: {m[h][4]}, index: {h}")
    print(f"Menor: {m[l][4]}, index: {l}")
