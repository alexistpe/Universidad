#E10 ADN
def ADN(a, b):
    c = 0
    e = 0
    f = False
    for i in range(len(a)):
        if a[0] == b[i]: #Si coincide.
            for j in range(len(a)): #Iterar para comprobar punto de inicio
                c = i+j #Obtenemos el indice real.
                if c >= len(a): #SI llego al limite.
                    c = e
                    e +=1
                
                if a[j] != b[c]:
                    f = True #Activa bandera.
                    break
                
            if f == False: #Si no todo coincide.
                return (True)
            
            f = False #Reinicia para la proxima.
    
    return False

n = int(input("Tamaño de la matriz (NxN), N = "))
m1 = [[int(input("Ingresar valor M1: ")) for _ in range(n)]for _ in range(n)]
m2 = [[int(input("Ingresar valor M2: ")) for _ in range(n)]for _ in range(n)]

print(m1)
print(m2)

A1 = S1 = S2 = S3 = S4 = [0]*n
A2 = SA =  SB = SC = SD = [0]*n

if len(m1) != len(m2):
    print("No es posible comparar")
else:
    for i in range(n):
        S1[i] = m1[0][i]
        S2[i] = m1[i][len(m1)-1]
        S3[i] = m1[len(m1)-1][len(m1)-(i+1)]
        S4[i] = m1[len(m1)-(i+1)][0]

        SA[i] = m2[0][i]
        SB[i] = m2[i][len(m2)-1]
        SC[i] = m2[len(m2)-1][len(m2)-(i+1)]
        SD[i] = m2[len(m2)-(i+1)][0]

A1 = S1 + S2 + S3 + S4
A2 = SA + SB + SC + SD

print(A1, A2)

print(ADN(A1, A2))

