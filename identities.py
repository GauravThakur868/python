import math
x = int(input())
y = int(input())
a = math.radians(x)
b = math.radians(y)
c = math.sin(a)*math.cos(b)+math.cos(a)*math.sin(b)
print("{:.2f}".format(c))