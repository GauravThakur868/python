class point():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def square(self):
        x = self.a**2
        y = self.b**2
        z = self.c**2
        return (x,y,z)
a = int(input())
b = int(input())
c = int(input())
obj = point(a,b,c)
print(obj.square())