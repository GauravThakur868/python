r = float(input("radius: "))
h = float(input("height: "))
a = (2*3.141*r*h) + (2*3.141*r**2)
if r>0 and h>0:
    print("area: {:.2f}" .format(a))