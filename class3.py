class birthdayboy:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def birthday(self):
        return(self.b+1)
a = input()
b = int(input())
obj = birthdayboy(a,b)
print(obj.birthday())