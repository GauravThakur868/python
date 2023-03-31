s = 10
import math
def call():
    p = int(input("p: "))
    global s
    print(s)
    print(p)
    print(int(math.pow(s-p,p)))
call()