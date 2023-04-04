import math
def factorial(n):
    return math.factorial(n)
n = int(input("n: "))
x = int(input("x: "))
s = 1
for i in range(1,n+1):
    s = s+((x**3)/factorial(i))
print(format(s,".2f"))