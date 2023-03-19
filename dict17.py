d = dict()
i = 0
print(d)
k = input("keys: ").split(',')
v = list(map(int,input("values: ").split(',')))
d = dict(zip(k,v))
print(d)
while i<=2:
    i+=1
    x = input().split(',')
    d[x[0]]=int(x[1])
print(d)