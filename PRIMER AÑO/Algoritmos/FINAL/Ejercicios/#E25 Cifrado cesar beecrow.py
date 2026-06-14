#E25 Cifrado cesar beecrow.
#Consiste en desplazar las letras de una cadena cierto numero.
#Expansion en papel.

v = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #ABCEDARIO
sum = 0 #Suma
n = int(input()) #Casos
for k in range(n):
    c = input() #Cadena
    num = int(input()) #Numero de salteo.

    s = "" #Subcadena.
    for i in range(len(c)):
        j = v.find(c[i])
        sum = j - num
        while sum < 0: #Aborda casos externos.
            sum += len(v)
        s = s + v[sum] #Concatena el caracter cifrado.
    print(s)
