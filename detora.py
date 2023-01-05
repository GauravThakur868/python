import math
x = int(input())
a = math.degrees(x)
if x >= 1 and x <= 360:
    print(round(a))
elif x == 0:
    print(round(a))
else:
    print("enter valid angle")