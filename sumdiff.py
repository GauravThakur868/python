a = int(input("num1: "))
b = int(input("num2: "))
c = str(a)
d = str(b)
e = int(c[0])**2 + int(c[1])**2
f = int(d[0])**2 + int(d[1])**2
g = e-f
if g > 0:
    print("P")
elif g == 0:
    print("Z")
else:
    print("N")