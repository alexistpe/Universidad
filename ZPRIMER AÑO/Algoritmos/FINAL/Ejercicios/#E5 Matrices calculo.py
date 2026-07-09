#E5 Matrices calculo
v = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
n = input()
t = 0

for i in range(len(n)):
    for j in range(len(v)):
        if v[j] == n[i]:
            t += j+1
            break
    
    if i > 0: #En caso que sea uno mayor.
        t += len(v)
        if (i+1) == len(n): #Si llego al final.
            break #Sale del programa.

print(t)