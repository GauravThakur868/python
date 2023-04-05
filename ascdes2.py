n = int(input())
l=[]
for i in range(n):
    a = int(input())
    l.append(a)
l.sort()
print(l)
l2 = []
for i in range(n,0,-1):
    l2.append(l[i-1])
print(l2)