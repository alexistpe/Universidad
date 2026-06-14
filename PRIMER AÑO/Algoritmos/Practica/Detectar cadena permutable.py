#Detectar cadena permutable.
s = input() #Cadena.
p = 0 #Contador de impares.

s = s.lower() #Transformar en minisculas (homogenio).
t = len(s)
for i in range(t):
    c = 0 #Contador paridad.
    for j in range(t):
        if s[i] == s [j] and s[i] != " ": #Cuenta la cantidad de esa mismo caracter, sin contar a los espacios.
            c = c + 1
    if c%2 != 0: #Si es impar.
        p = p + 1
    
    if p > 1:
        t = 0 #Break

if p > 1:
    print("NO es permutable.")
else:
    print("SI es permutable.")
