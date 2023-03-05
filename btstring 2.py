def eo(a,b):
    x = str(a)
    for i in x:
        if int(i)%2 != 0:
            return "False"
    return "True"
a = input()
b = len(a)
print(eo(a,b))