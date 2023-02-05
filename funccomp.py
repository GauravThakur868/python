def cube():
    a = int(input())
    b = a**3
    print(b*2)
    def double(a):
        c = a*2
        print(c**3)
    double(a)
cube()