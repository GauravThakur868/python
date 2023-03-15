a = input("keys: ").split(",")
b = list(map(int,input("values: ").split(",")))
d = {}
for i in range(len(b)):
    d[a[i]]=b[i]
print(d)
k = input()
if k in d:
    d.pop(k)
else:
    d.pop(a[2])
print(d)
