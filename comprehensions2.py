n = int(input())
l = [[] for i in range(n)]
for i in range(n):
    for j in range(n):
        l[i].append(int(input()))
for i in range(n):
    print(l[i])
l1 = [[i,j] for i in range(n) for j in range(n) if l[i][j]==0]
print(l1)