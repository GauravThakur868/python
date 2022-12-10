class laptop:
    def __init__(self):
        print("hello")
    def config(self):
        print("Asus","i5","1TB")
laptop1 = laptop()
laptop2 = laptop()
#laptop.config(laptop1)
laptop1.config()
laptop2.config()
class student:
    
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
    def info(self):
        print("name:",self.name, "rollno:",self.rollno)
student1 = student("abc","34")
student2 = student("xyz","54")
student1.info()
student2.info()
print(id(student1))
print(id(student2))

class person:
    def __init__(self):
        self.name = "abc"
        self.number = 56
    def compare(self,other):
        if(self.number == other.number):
            return True
        else:
            return False
p1 = person()
p2 = person()
#p1.name = "xyz"
#print(p1.name)
#print(p2.name)
p2.number = 11
if p2.compare(p1):
    print("same")
else:
    print("not same")
print(p1.number)
print(p2.number)

class car:
    wheels = 4
    # Instance variables - value varies from object to object
    # Static variable
    def __init__(self):
        self.company = "BMW"
        self.mileage = "10"
car1 = car()
car2 = car()
car.wheels = 5
print(car1.mileage,car1.wheels)
print(car2.mileage,car2.wheels)