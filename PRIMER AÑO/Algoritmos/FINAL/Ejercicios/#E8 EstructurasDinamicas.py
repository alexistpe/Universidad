#E8 EstructurasDinamicas
def copiacolas(c,p):
    if p == 0: #Si llego al inicio.
        return c[p]
    else:
        p -= 1
        a = copiacolas(c,p)
        global c2
        c2.append(a)
        if p+1 != len(c):
            return c[p+1]
        

c1 = [1,2,3,4,5,6,7,8]
c2 = []
copiacolas(c1, len(c1))
print(c2)