import math
a = float(input())
b = float(input())
c = a/b
x = math.asin(c)
deg = math.degrees(x)
print("{:.2f}".format(deg))