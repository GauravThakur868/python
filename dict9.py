k = input('keys: ').split(',')
v = [int(i) for i in input('values: ').split(',')]
r = input().split(',')
d = dict(zip(k,v))
z = {}
for i in range(len(d)):
    key = k[i]
    x = d[key]
    try:
        n = r[i]
    except:
        break
    z[n] = {key: x}
print(d)
print(r)
print(z)