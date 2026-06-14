#Algoritmos SIMULACION INSTANCIA EVALUATIVA.
def diferencia(v1, v2):
    t1 = 0
    t2 = 0
    res1 = 0
    res2 = 0

    for i in range(v1[2]-1):
        if i % 4 == 0 and i % 100 != 0:
            t1 += 366
        elif i % 100 == 0 and i % 400 == 0:
            t1 += 366
        else:
            t1 += 365
    
    for i in range(v1[1]-1):
        if i == 0 or i == 2 or i == 4 or i == 6 or i == 7 or i == 9 or i == 11:
            res1 += 31
        elif i != 1:
            res1 += 30
        else:
            if v1[2] % 4 == 0 and v1[2] % 100 != 0:
                res1 += 29
            elif v1[2] % 100 == 0 and v1[2] % 400 == 0:
                res1 += 29
            else:
                res1 += 28
    
    for i in range(v2[2]-1):
        if i % 4 == 0 and i % 100 != 0:
            t2 += 366
        elif i % 100 == 0 and i % 400 == 0:
            t2 += 366
        else:
            t2 += 365
    
    for i in range(v2[1]-1):
        if i == 0 or i == 2 or i == 4 or i == 6 or i == 7 or i == 9 or i == 11:
            res2 += 31
        elif i != 1:
            res2 += 30
        else:
            if v2[2] % 4 == 0 and v2[2] % 100 != 0:
                res2 += 29
            elif v2[2] % 100 == 0 and v2[2] % 400 == 0:
                res2 += 29
            else:
                res2 += 28
    

    t1 = t1 + (res1+v1[0])
    t2 = t2 + (res2+v2[0])
    return abs(t1 - t2)


n = int(input())
m = [[int(input()) for _ in range(3)]for _ in range(n)]
fe = input() #Fecha que ingreso el usuario.
fe = fe + "/" #Abordar en transformacion a array.
fv = [0]*3
s = ""
id = 0
for i in range(len(fe)):
    if fe[i] == "/":
        fv[id] = int(s)
        id += 1
        s = ""
    else:
        s = s + fe[i]


for i in range(n):
    f = False
    for j in range(3):
        if fv[j] != m[i][j]:
            f = True
            break
    if f == False:
        print("EXISTE EN LA FILA: ", i)
        break #Sale del for.

if f == True: #Si no existe.
    dif = 0
    dia = 0
    vp = [0]*3
    fm = [0]*3

    for i in range(n): #Obtener fecha matriz en array.
        for j in range(3):
            fm[j] = int(m[i][j])
        
        dif = diferencia(fv, fm)
        if dif < dia or dia == 0:
            dia = dif
            vp = [fm[0],fm[1],fm[2]]
    
    print(vp, dia)