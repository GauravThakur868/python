a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
def digit(*args):
    x = ''
    for arg in args:
        x = x+str(arg)
    return x
print(digit(a,b,c,d,e))