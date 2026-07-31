#Validador tarjetas

n = int(input()) #Cantidad.
t = 0 #total de tarjetas validas.

while n != 0:
    s = input() #Recibir num.
    b = 0 #Temporal.
    a = 0 #Sumador.
    c = 0 #Detectar cada 2 valores.
    k = len(s)-1 #Total indice.
    for i in range(k+1):
        b = int(s[k-i]) #Guardamos el numero.
        c = c + 1
        if c == 2:
            b = b*2
            if b > 9:
                b = b - 9
            c = 0
        
        a = a + b
    
    if a%10 != 0:
        t = t + 1
    
    n = n - 1 #Descontar tarjeta analizada.

print(t)