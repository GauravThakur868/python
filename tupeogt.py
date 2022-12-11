a = int(input("side1: "))
b = int(input("side2: "))
c = int(input("hypotenuse: "))
d = abs(a)**2 + abs(b)**2
if abs(c)**2 == d:
    print("satisfy")
else:
    print("not satisfy")