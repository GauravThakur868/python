class point():
    def __init__(self):
        self.x1 = int(input())
        self.y1 = int(input())
        self.x2 = int(input())
        self.y2 = int(input())
    def slope(self):
        a = ((self.y2-self.y1)/(self.x2-self.x1))
        return ("%.3f"%a)
l = point()
print(l.slope())