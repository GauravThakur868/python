a = input()
b = a.split(",")
for i in range(len(b)):
    b[i] = int(b[i])
print(max(b),min(b))