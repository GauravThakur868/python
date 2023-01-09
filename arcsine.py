import math
a = float(input())
if a >= -1 and a<= 1:
    b = math.acos(a)
    print("{:.4f}".format(b))
elif a < -1:
    print("invalid")
elif a> 1:
    print("invalid")