class calculation:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def exponent(self):
        return self.a**self.b
class mycalculation(calculation):
    def floordivision(self):
        return self.a//self.b
x = int(input())
y = int(input())
a = mycalculation(x,y)
print(a.exponent())
print(a.floordivision())