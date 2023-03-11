a = list(int(i) for i in input().split(","))
b = max(a)
c = []
for i in a:
    if i == b:
        c.append(min(a))
    else:
        c.append(i)
print(tuple(c))