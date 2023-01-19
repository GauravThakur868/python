a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
def mysum(*args):
    x = 0
    for arg in args:
        x = x+arg
    return x