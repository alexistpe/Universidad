#Bee E3, fabrica electrica.
n = 1 #Regions.
v = [1] #Off Regions.
t = 1 #Temp num.


while n > 0:
    n = int(input()) #Regions.
    if n == 0:
        break
    m = 1 #Sum.
    t = 1 #Temp.
    v = [1] #Off Regions.
    while True: #search m.
        while len(v) < n:
            a = 0 #Count
            while a < m:
                if t > 17: #Reset
                    t = 1

                if t in v:
                    #print("t es invalido: ",t,v)
                    t += 1 #Skip the repeated ones.
                else:
                    a += 1
                    if a < m:
                        t += 1
                    

            v.append(t)
            #print(f"t: {t}, agregado a v:{v}")
            if t == 13:
                break
        
        if len(v) == n:
            print(m)
            break

        m = m + 1
        t = 1
        v = [1]
            
