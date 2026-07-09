t = int(input()) #Tamaño vector
v = [None]*t #Vector usuario
vu = [None]*t #Vector Unicos

for l in range(t):
    v[l] = int(input())

unico = False #Lock para asegurar que no cuente mas repetidos.
r = 0 #Cuenta las repeticiones del numero.
c = 0 #Seguimiento del indice de los unicos.

for i in v: #Comparacion el valor particular.
    for j in v: #Comparacion con el vector.
        if i == j and unico == False: #Detectamos si se repite
            for k in vu: #Detectamos si ya lo guardamos antes.
                if k == i:
                    unico = True #Indicamos que ya esta guardado.
            
            r = r + 1
            if r >= 2:
                vu[c] = i #Guardamos en la posicion adecuada.
                c = c + 1 #Aumentamos el contador para seguir el indice.

    unico = False #Reiniciamos para la proxima comparacion.
    r = 0 #Reiniciamos para la proxima comparacion.

print(vu)
print(c)
        
            

            

            
