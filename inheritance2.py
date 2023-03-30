class person:
    def __init__(self,fn,ln):
        self.fn = fn
        self.ln = ln
    def printname(self):
        print(self.fn,self.ln)
class student(person):
    pass
x = student(input(),input())
x.printname()