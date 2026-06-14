s = input()
a = 0 #Conteo de arrobas.
p = 0 #Flag validar.
v = ["Email invalido", "Email valido"]
for i in range(len(s)):
    if s[i] == "@" and i > 0:
        a = a + 1
        if a != 1:
            p = 0
    elif a == 1 and s[i] == "." and i < (len(s)-1):
        p = 1
print(v[p]) #Imprimir respuesta.
