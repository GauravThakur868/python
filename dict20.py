k = input("keys: ").split(',')
v = list(map(int,input("values: ").split(',')))
d = dict(zip(k,v))
print(d)
print(d.keys())
print(d.values())
