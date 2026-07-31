#Test beecrow
n = int(input()) # Recibir cadena.
a = "@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_'abcdefghijklmnopqrstuvwxyz{|}" # Tabla ascii + 3 y -1.
# sc se inicializa como una lista para permitir modificaciones eficientes.
scl = [] #Lista de caracteres.

for k in range(n): # Iterar por la cantidad de veces necesarias.
    s = input() # Guardar cadena.
    scl = list(s) # Convertir la entrada a una lista.
    
    for i in range(len(s)): # Iterar la lista.
        f = a.find(s[i]) # Buscamos la letra.

        if s[i].isalpha() and f != -1:
            scl[i] = a[f + 3]
        # Si no, el carácter se mantiene igual en scl.
    
    sc = "".join(scl) # Volvemos a la cadena 'sc' para el resto del código.
    
    mid = len(sc) // 2 # Obtener la mitad truncada.

    v = sc[::-1] 
    sc = v # Intercambiar.
    sc2 = "" # Obtener cadena.
    
    sc2 = sc[:mid] # Guarda la primera mitad sin cambios.

    # Recorrer la segunda mitad para el desplazamiento de -1.
    for i in range(len(sc) - mid):
        ci = i + mid
        f = a.find(sc[ci]) # Buscamos el caracter.
        
        if f != -1: # SI lo encontro.
            # Concatenar el carácter anterior (O(N) - Mantenido para respetar la estructura del bucle).
            sc2 = sc2 + a[f - 1] 
        else:
            # Si no lo encuentra, concatenar el carácter original.
             sc2 = sc2 + sc[ci] 
            
    print(sc2) # Imprime el texto.