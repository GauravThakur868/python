a = list(map(int,input("list: ").split(",")))
b = sum(a)
print(b)
print(b**2)
n = []
for i in a:
    c = i**3
    n.append(c)
d = sum(n)
print(d)