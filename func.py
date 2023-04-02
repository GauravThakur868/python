s = 10
def call():
    p = eval(input("p: "))
    print(s)
    print(p)
    return (s+p)**p
print(call())