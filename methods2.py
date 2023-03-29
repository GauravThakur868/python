class solution:
    def isanagram(self,a,b):
        self.a = a
        self.b = b
        if(sorted(self.a) == sorted(self.b)):
            print("yes")
        else:
            print("no")
a = input()
b = input()
solution().isanagram(a,b)