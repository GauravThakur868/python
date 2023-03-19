k = list(map(int,input("keys: ").split(',')))
v = list(map(int,input("values: ").split(',')))
t = []
d = dict(zip(k,v))
print(d)
r = {}
for k,v in d.items():
    if v not in t:
        t.append(v)
        r[k] = v
print(r)