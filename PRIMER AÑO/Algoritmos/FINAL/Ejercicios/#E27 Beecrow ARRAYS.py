#E27 Beecrow ARRAYS
#Reparto de mazo de cartas.

#HACERLO EFICIENTE Y SIN NECESIDAD DE ORDENAR: Utilizar MATEMATICAS en base a las potencias de 2. Solo realizar los descartes en base a esa potencia.
#Variables: Inicio; indice; potencia; valor de salteo; cadena de descartes => Estas variables son el centro de control para solo iterando linealmente, obtener los valores de descarte de forma ordenada.
#Se inicia en el valor de inicio, guardar en cadena de descartes, se le suma el valor de salteo y repite.
    #Si el valor obtenido en el indice es > a "m", entonces se aumenta el valor de inicio y valor de salteo segun la potencia (va aumentando en 1 en cada final).
#Salir si la cant. de descartes es == a m-1.
#Al final mostrar cadena .
m = 1 #Definir cant. a barajar.
while m > 0:
    m = int(input())
    if m == 0:
        break #Terminar bucle.
    c = 1 #Contador para descartes.
    p = 0 #Potencia.
    s = "" #Cadena descartes.
    k = 1 #Contador de descartes.
    r = 0 #Valor restante.
    par = False #Bandera para saltar descartes.
    inicio = 0 #Valor donde se iniciara en la proxima etapa, para retomar los valores guardados.
    #VERIFICAR PARIDAD.

    while k < m: #Mientras aun queden descartes.
        if par == False:
            #print("DESCARTADO: ", c)
            if k+1 == m: #Si llego al ultimo descarte valido.
                s = s + str(c) #Obtener valor descartado final.
            else:
                s = s + str(c) + ", " #Obtener valor descartado en secuencia.
            
            k += 1 #Valores descartados.
        
        if p == 0: #Abordar caso inicial.
            c += 2 #Saltear entre descartes.
        else:
            c += 2 ** p #Potencia de dos.
            par = not par #Vamor intercalando entre descartes y salteos.

        
        if c > m: #Si termino la etapa.
            p += 1 #Aumentamos potencia.
            c = 2 ** p #Planteamos inicio.
            if p - 1 > 0: #Asignar cartas anteriores que quedaron.
                c = inicio #Reasignar inicio.

            if par == False: #Caso general descarte.
                if p < 2:
                    if m % 2 != 0: #Salteo impar.
                        inicio = inicio + 2 ** p #Planteamos inicio proximo.
                    else:
                        inicio = 2 ** p + 2 ** p #Planteamos inicio proximo potencia.
                else:
                    inicio = inicio + 2 ** p #Planteamos inicio proximo.
            #Cuando llega "true", el inicio no se modifica, ya que es una carta que se debe mantener y luego se eliminara.
            
            if p-1 == 0 and m % 2 != 0: #Caso inicial.
                par = True #Lo salteamos al 2 por imparidad.
                inicio = 2 ** p #Planteamos inicio (2).
        
        if k == m: #Si llego al valor final de descartes.
            #Obtenemos el valor final.
            if c < inicio:
                r = c #Si no quedo ninguna carta anterior.
            else:
                r = inicio #Si quedo alguna carta anterior.
    
    print(f"Discarded cards: {s}")
    print(f"Remaining card: {r}")




    
