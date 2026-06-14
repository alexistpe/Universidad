#E2, reorder vector.
m = int(input("Vector size: ")) #Num vector size.
v = [0]*m
for i in range(m): #Fill vector.
    v[i] = int(input(f"Num pos {i}: "))

a = 0 #Position from.
b = 0 #Target position.
while a != -1:
    a = int(input("Obj position: "))
    if a >= 0:
        b = int(input("Target position: "))

        temp = v[a] #Value to save.
        size = abs(b-a) #Iterate size.
        for i in range(size): #Order vector.
            if b > a:
                i = i + a
                v[i] = v[i+1]
            else:
                i = a - i
                v[i] = v[i-1]
        
        v[b] = temp #Put to target position.
        print(v)
