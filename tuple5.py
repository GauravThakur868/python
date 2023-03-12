n = int(input())
b =[]
for i in range(n):
    a = tuple(map(int,input().split(',')))
    b.append(a)
l = len(b)
b = sorted(b)
for i in range(l):
    for j in range(l-i-1):
        if len(b[j])==len(b[j-1]):
            if b[j][0]+b[j][1]+b[j+1][0]+b[j+1][1]:
                b[j],b[j+1]+b[j+1],b[j]
print(tuple(b))