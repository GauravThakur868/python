class superclass:
    def k(self):
        print("this is super class")
class parentclass(superclass):
    def l(self):
        print("This is parent class")
class childclass(parentclass):
    def f(self):
        print("This is a child class")
obj = childclass()
obj.k()
obj.l()
obj.f()