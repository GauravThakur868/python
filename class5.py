class append:
    def __init__(self,a):
        self.a = a
    def add(self):
        self.b = input()
        return(self.a+self.b)
a = input()
obj = append(a)
print(obj.add())