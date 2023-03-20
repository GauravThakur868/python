a = tuple(map(int,input().split(',')))
b = []
c = {}
for i in a:
    if i not in b:
        d = a.count(i)
        c[i] = d
print(c)