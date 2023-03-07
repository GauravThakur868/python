a = input()
b = a.split(" ")
for i in range(len(b)):
    b[i] = int(b[i])
print(b)
b.sort(reverse = True)
print(b)
print(min(b))