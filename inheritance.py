class A:
    def __init__(self):
        print("init of class A")
    def method1(self):
        print("Method 1")
    def method2(self):
        print("Method 2")
class B():
    def __init__(self):
        super().__init__()
        print("init of class B")
    def method3(self):
        print("Method 3")

    def method4(self):
        print("Method 4")
class C(B,A):
    def __init__(self):
        super().__init__()
        print("init of class c")
    def method5(self):
        print("Method 5")
obj = A()
obj.method1()
abc = B()
abc.method3()
xyz = C()
xyz.method5()