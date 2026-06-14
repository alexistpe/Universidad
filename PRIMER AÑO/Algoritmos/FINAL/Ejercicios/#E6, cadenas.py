#E6, cadenas
def borrar(c,p,l):
    ca = c[0:p] + c[p+l:]
    return ca

print(borrar(input(),int(input()),int(input())))