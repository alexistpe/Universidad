#INSTANCIA DE EVALUACION 2 - PRACTICA
#Encontrar los diamantes procesando una cadena de texto.
g = int(input())
for i in range(g):
    t = 0 #Contador.
    c = input()
    count = 0
    while c != "":
        f = False #Reiniciamos bandera.
        id = -1 #Reiniciamos id.
        op = 0 #Optimizar iteraciones.
        punto = True #Aborda el problema de encontrar solo puntos.
        count += 1
        for i in range(len(c)):
            i = i - op
            if c[i] == "<": #Inicio diamante.
               id = i
               f = True
               punto = False #Encontramos un valor de salida.
            elif f == True and c[i] == ">": #Cierre diamante.
                c = c[0:id]+c[i+1:]
                t += 1
                op = op + i - id + 1
                f = False #Evitar que salga del bucle while.
                #break #Salir.
                
        if f == True or punto == True: #Si no logro encontrar match.
            break
    print(t) #Mostramos el total.
    #print(f"Iteraciones: {count}") #Mostramos el total.

