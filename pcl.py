a = float(input("enter first number"))
b = float(input("enter second number"))
z = int(input("1 for addition \n 2 for subtraction \n 3 for multiplication \n 4 for division"))
def add(a,b):
    c = a+b
    print(c)
def sub(a,b):
    d = a-b
    print(d)
def multi(a,b):
    i = a*b
    print(i)
def div(a,b):
    x = a/b
    print(x)
if z == 1:
    add(a,b)
elif z == 2:
    sub(a,b)
elif z == 3:
    multi(a,b)
elif z == 4:
    div(a,b)
else:
    print("enter a valid value")
