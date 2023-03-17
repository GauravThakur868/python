a = input().split()
b = {}
for i in a:
    b[i] = i[::-1]*3
print(b)