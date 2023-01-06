import math
a = int(input())
b = int(input())
while a in range(a,b+1):
    print("{:.2f}".format((math.sin(a))))
    a += 1