#E7, Quicksort casero
import random

def Quick(s): #Organizar vector.
    t = len(s) #Tamaño de la lista.
    if t <= 2:
        if t == 2 and s[0] > s[1]:
            AU = s[0]
            s[0] = s[1]
            s[1] = AU
        return(s)
    else:
        s1 = [] #Valores menores.
        s2 = [] #Valores mayores.
        m = [] #Valor medio.
        val = s[int(t/2)]
        same = False #Flag para determinar si son iguales.
        for i in range(t):
            if s[i] < val:
                s1.append(s[i]) #Recolecta los valores menores.
            elif s[i] > val:
                s2.append(s[i]) #Recolecta los valores mayores.
            else:
                m.append(s[i]) #Recolecta los valores iguales.
            if s[i] != s[0]: #Si no son iguales.
                same = True #Alertar.

        if not same:
            return(s) #Todos los valores son iguales.
        else:
            a = Quick(s1)
            b = Quick(s2)
            return(a+m+b)

a = int(input()) #Obtener tamaño.
v = [] #Vector.
for i in range(a): #Obtener valores.
    v.append(random.randint(0,10))
print(v)
print("QUICK: -----------------------------------------------------")
print(Quick(v))