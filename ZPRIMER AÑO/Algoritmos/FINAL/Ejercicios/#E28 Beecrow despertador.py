#E28 Beecrow despertador
c = ""
while c != "0 0 0 0":
    try:
        c = input()
        if not c or c == " ": break
    except EOFError:
        break #Finalizo
    v = [0] * 4
    t = 0

    s = ""
    id = 0
    for i in range(len(c)):
        if c[i] == " ": #Si recupero el valor.
            v[id] = int(s)
            id += 1 #Aumentar indice.
            s = ""
        else:
            s = s + c[i] #Almacenar horario.
    if s != "":
        v[3] = int(s)
    
    if v[0]+v[1]+v[2]+v[3] == 0: #Si las lineas estan vacias.
        break

    t1 = v[0]*60 + v[1]
    t2 = v[2]*60 + v[3]

    t = t2-t1
    if t < 0:
        t += 24*60

    print(t)