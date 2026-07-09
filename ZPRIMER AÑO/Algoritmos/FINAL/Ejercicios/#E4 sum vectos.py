#E4 sum vectos.
l1 = []
l2 = []
for i in range(3):
    l1.append(int(input(f"valor {i} l1: ")))
    l2.append(int(input(f"valor {i} l2: ")))

s = s2 = "" #Text transform.
tm = len(l1)
for i in range(tm):
    s = s + str(l1[tm-(i+1)])
    s2 = s2 + str(l2[tm-(i+1)])
t = int(s) + int(s2)
t = str(t)
f = []
for i in range(len(t)):
    f.append(t[len(t)-(i+1)]) 
print(f"{l1} + {l2} = {f}")