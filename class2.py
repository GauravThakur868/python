class append:
    def __init__(self,string):
        self.string = string
    def midchar(self):
        x = self.string
        length = len(x)
        if length%2!=0:
            return x.replace(x[length//2],"*")
        else:
            a = (length//2)-1
            b = (length//2)+1
            return x.replace(x[a:b],"*")
a = input()
obj = append(a)
print(obj.midchar())