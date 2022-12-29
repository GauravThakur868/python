a = 10
b = 1
d = 0
while b <= 10:
    c = int(input())
    if c < 0:
        break
    d += c
    b += 1
print(d)