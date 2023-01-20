r = int(input())
h = int(input())
def area(r,h):
    a = 2*(3.14)*r*15
    b = 2*(3.14)*r*h
    print("area1: ","{:.2f}".format(a))
    print("area2: ","{:.2f}".format(b))
area(r,h)