a = list(map(int,input().split(" ")))
print(a)
s = []
for i in a:
    if i %21==0:
        s.append(i)
print(s)