#Recorrer lista entrelazada.
ca = input().split() #List preview.
id = input().split() #Index order.
s = int(input()) #Start.
c = 0 #Counter.

print(ca[s]) #Print first element.
while s != -1:
    print(ca[int(id[s])]) #Print list in order.
    c = c + 1 #count amount.
    s = int(id[s])
print(f"Total Songs: {c}")