import math
a = int(input())
b = int(input())
c = int(input())
vector = math.sqrt(a**2+b**2+c**2)
if vector==int(vector):
    print(vector)
else:
    print(int(vector)+1)