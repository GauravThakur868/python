k = [i for i in input().split(" ") if len(i)>5]
v = [len(i) for i in k]
d = dict(zip(k,v))
print(d)