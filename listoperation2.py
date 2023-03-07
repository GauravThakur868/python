a = input()
b = a.split(",")
for i in range(0,len(b)):
    b[i] = int(b[i])
print(b)
c = []
for i in range(len(b)):
    if (abs(b[i])%2 == 0 or b[i] > 0):
        c.append(b[i])
print(c)