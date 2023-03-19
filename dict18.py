k = input("keys: ").split(',')
v = list(map(int,input("values: ").split(',')))
d = dict(zip(k,v))
print(d)
i = 0
x = {}
while i<len(d):
    if v[i]%5==0:
        x[k[i]]=v[i]
    i = i+1
print(x)