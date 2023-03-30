def And(a,b):
    return(a and b)
def Or(a,b):
    return(a or b)
def Not(a):
    return(not a)
x = int(input())
y = int(input())
print(Not(And(x,y)))
print(Not(Or(x,y)))