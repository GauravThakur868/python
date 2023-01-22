a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())
h = int(input())
def mysum(*args):
    sumE= 0
    sumO = 0
    for i in args:
        if(i%2 == 0):
            sumE = sumE + i
        else:
            sumO = sumO + i
    return(sumE**sumO)
print()
print()