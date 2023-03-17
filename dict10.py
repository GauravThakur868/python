import math
a = [int(i) for i in input('').split(',')]
b = {}
for i in a:
    b[i] = math.factorial(i)
print(b)