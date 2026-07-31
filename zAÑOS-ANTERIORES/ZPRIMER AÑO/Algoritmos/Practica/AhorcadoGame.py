def verify(c):
    for i in c:
        if i == "_":
            return False
    
    return True

c = input() #Cadena.
i = 6 #Intenetos.
cf = "" #Cadena oculta.
s = "" #Letras utilizadas.
flag = 0 #Si es incorrecto.
f2 = False

for j in range(len(c)): #Rellenar oculta.
    cf = cf + "_"

while i >= 1:
    if i > 0:
        cf = "" #Reiniciamos
        a = input()
        s = s + a #Guardar letra utilizada.
        for j in range(len(c)): #Verificar caracter.
            if c[j] == a and flag != 1:
                flag = 1 #Activamos flag.
        
        for h in c: #Actualizamos palabra oculta.
            for b in s:
                    if h == b:
                        cf = cf + h.upper()
                        f2 = True
                    
            if f2 == False:
                cf = cf + "_"
            
            f2 = False

        
        if flag == 0:
            i = i - 1
        
        flag = 0 #Reiniciar.

        
        
        if verify(cf) == True:
            print(f"{s}  {cf}  GANO")
            break #Termino el juego.
        else:
            print(f"{s}  {cf}  {i}")
            

if verify(cf) == False:
    print(f"{s}  {cf}  PERDIO")

        
