a = int(input())
b = int(input())
x = []
y = []
for i in range(a):
    m = tuple(map(int,input().split(',')))
    x.append(m)
for j in range(b):
    temp = 0
    for k in range(a):
        temp += x[k][j]
        p = temp//a
    y.append(p)
print(tuple(y))