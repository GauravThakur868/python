a = {}
for row in range(1,int(input())+1):
    b = tuple([int(i) for i in input().split(',')])
    a[row] = b
print(a)