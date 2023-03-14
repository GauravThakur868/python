n = int(input())
l = []
for i in range(n):
    s = input()
    t = tuple(map(str,s.split(",")))
    l.append(t)
print(list(l))
d = {}
l1 = []
l2 = []
for(x,y) in l:
    l1.append(x)
    l2.append(y)
d = dict(zip(l1,l2))
print(d)