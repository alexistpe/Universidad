#Archivos test 1
k = int(input())
c = 0
a = open("megan.txt", "w")
a.write("sequence k:\n")
while k > 0:
    a.write(f"{c}\n")
    c = c + 1
    k = k - 1
a.close()