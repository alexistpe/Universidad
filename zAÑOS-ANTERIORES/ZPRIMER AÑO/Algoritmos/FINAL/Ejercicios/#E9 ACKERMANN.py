#E9 ACKERMANN
import sys
sys.setrecursionlimit(20000)
def ack(m,n):
    if m == 0:
        n+=1
        return n
    elif n == 0:
        return ack(m-1,1)
    else:
        return ack(m-1, ack(m,n-1))


m = int(input())
n = int(input())
print(ack(m,n))