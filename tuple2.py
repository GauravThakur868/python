n = int(input())
a = []
for i in range(n):
    b = input().split(",")
    a.append(tuple(b))
print(a)
print(tuple(a))