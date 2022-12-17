print(len("hello"))
print(len([10,20,30,40]))
def add(x,y,z = 0):
    return x+y+z
print(add(4,7))
print(add(3,4,5))
#
#
class india:
    def capital(self):
        print("Delhi")
    def language(self):
        print("hindi")
    def type(self):
        print("developing")

class usa:
    def capital(self):
        print("washington dc")
    def language(self):
        print("english")
    def type(self):
        print("developed")
obj1 = india()
obj2 = usa()
for i in (obj1,obj2):
    i.capital()
    i.language()
    i.type()
#
#
class bird:
    def wings(self):
        print("has 2 wings")
    def eyes(self):
        print("has 2 eyes")
    def fly(self):
        print("most can fly")

class sparrow(bird):
    def fly(self):
        print("can fly")

class ostrich(bird):
    def fly(self):
        print("cannot fly")

birds = bird()
spa = sparrow()
ost = ostrich()

birds.eyes()
birds.fly()
spa.fly()
ost.fly()

#
#
class car:
    pass

#
#
#
class vehicle:
    def __init__(self,name,milage):
        self.name = name
        self.milage = milage

class bus(vehicle):
    pass

buses = bus("xyz",20)
print(buses.milage,buses.name)
