a = [i for i in input().split(" ")]
b = [len(i) for i in a]
c = dict(zip(a,b))
print(c)