a = input()
b = a.swapcase()
c = []
for i in b:
    c.append(i)
print("[" +str(', '.join(map(str,c))+"]"))