class student:
    college = "LPU"
    def __init__(self,python,web,math):
        self.sub1 = python
        self.sub2 = web
        self.sub3 = math
    def average(self):
        print((self.sub1+self.sub2+self.sub3)/3)
    def get_sub1(self): #accesor
        print(self.sub1)
    def set_marks(self,value): #mutator
        self.sub1 = value
    @classmethod
    def collegedetails(cls):
        print(cls.college)
    @staticmethod
    def staticmethod():
        print("this is static method")
student1 = student(4,7,8)
student2 = student(7,8,9)
student1.average()
student2.average()
student.collegedetails()
