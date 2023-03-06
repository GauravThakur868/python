a = input()
b = a.split(",")
print(b)
for i in range(0,len(b)):
    b[i] = int(b[i])
print(b)
print(b[0]+b[len(b)-1])