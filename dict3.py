n= int(input())
d = {}
res = 0
for i in range(n):
    k = input('keys: ')
    v = int(input('value: '))
    d[k]=v
    res+=v
print(res)