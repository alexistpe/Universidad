def c(s):
    u = [0]*10 #Vector que almacena los 10 primeros numeros.
    f = 0 #Indice del vector.
    c = 0 #Contador de todos los numeros.
    for i in range(len(s)): #Iterar 11 primeros lugares (10 primeros digitos)
        if f < 10 and s[i].isdigit() == True: #Si le falta guardar un numero.
            u[f] = int(s[i])
            f = f + 1 #Indice interno.
        
        if s[i].isdigit() == True:
            c = c + 1 #Cantidad de numeros.

    print(f"Este es el vector del cuil:", u)

    if f != 10 or c != 11: #Detectar cantidad de numeros.
        return [0]
    elif s[2] != "-" or s[11] != "-": #Detectar formato.
        return[0]
    else:
        return u #Retornamos los 10 primeros digitos.

def m(c):
    w = 0 #Total.
    v = [5,4,3,2,7,6,5,4,3,2] #Vector de multiplicacion.
    for i in range(10):
        print(f"Calculo de {c[i]} por {v[i]}") 
        w = w + (c[i] * v[i]) #Sumar al total las multiplicaciones.
        print("forman un total de :", w)
    
    w = int(w%11) #Obtener resto final.
    print("Este es el RESTO total: ", w)
    return w

def fin(h,s):
    print(f"11-h es: {11-h}, y el bit verificador: {s[12]}")
    if 11-h != int(s[12]):
        print("CUIT incorrecto")
    else:
        print("CUIT correcto")


b = input()
r = c(b)
if r != [0]: #Si no dio ningun error.
    fin(m(r),b) #Validar ultimo digito.
else:
    print("Formato incorrecto")