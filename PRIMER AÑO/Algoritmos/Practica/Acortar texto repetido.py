#Acortar texto repetido.
s = input() #Cadena original.
a = 0 #Contador.
b = "" #Nueva cadena.

for i in range(len(s)-1): #Iteramos una vez menos ya que verificamos una posicion extra.
    if s[i] == s[i + 1]:
        a = a + 1 #Conteo de caracteres.
    else:
        b = b + s[i] + str(a+1) #Contamos el caracter actual.
        a = 0 #Reiniciamos conteo.

b = b + s[len(s)-1] + str(a+1)

if len(b) >= len(s): #Si la cadena resumida es mayor o igual a la original.
    print(s) #Imprimir la original.
else: #Sino.
    print(b) #Imprimir la resumida.