#Cadena, verificar hora.
def com(h1): #Comprobar
    c = 0
    if len(h1) != 5: #Cadena limite.
        return False
    elif h1[2] != ":": #Incluye el ":".
        return False
    elif int(h1[0]) > 5 or int(h1[3]) > 5:
        return False
    else:
        for i in range(5):
            if h1[i].isdigit():
                c = c + 1
        
        if c != 4: #tiene 4 digitos.
            return False
    return True #Sino, es verdadero.

def hym(m, mf): #Calcular minutos y poner en string.
    s = ""
    res = mf - m
    if res < 0: #Si es negativo.
        res = (24*60) + res #Obtenemos el valor real.
    
    s = str(res) + " Minutos"
    return s

def separar(h1,h2): #Pasar a minutos.
    #Pasar a minutos (Ponderacion).
    m = ((int(h1[0])*10) + (int(h1[1]))) * 60 #La diferencia de horas en minutos.
    m = m + ((int(h1[3])*10) + (int(h1[4]))) #Sumar minutos.
    mf = ((int(h2[0])*10) + (int(h2[1]))) * 60 #La diferencia de horas en minutos.
    mf = mf + ((int(h2[3])*10) + (int(h2[4]))) #Sumar minutos.
    return hym(m,mf)


h1 = input()
h2 = input()
if com(h1) == True and com(h2) == True:
    s = separar(h1,h2)
    print(s)
else:
    print("Error en el ingreso de datos.")