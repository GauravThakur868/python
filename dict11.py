a = [int(k) for k in input().split(',')]
b = {}
for i in a:
    x = []
    for j in range(1,i+1):
        if i %j == 0:
            x.append(j)
    b[i] = x
print(b)