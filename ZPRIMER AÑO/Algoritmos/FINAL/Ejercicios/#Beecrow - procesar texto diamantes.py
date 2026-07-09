#Beecrow - procesar texto diamantes
g = int(input())
for k in range(g):
    t1 = 0 #Contador <.
    t2 = 0 #Contador >.
    c = input()
    for i in range(len(c)):
        if c[i] == "<":
            t1 += 1
        elif c[i] == ">":
            t2 += 1
    
    if t1 > t2:
        print(t2)
    else:
        print(t1)