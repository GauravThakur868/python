k = input('keys: ').split(',')
print("values: ")
d = {}
l = []
for i in k:
    v = list(map(int,input().split(',')))
    l.append(v)
    d[i]=v
print(d)
for row in zip(*([key]+(value) for key , value in d.items())):
    print(*row)