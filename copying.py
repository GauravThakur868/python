a = [int(i) for i in input().split(",")]
b = [int(i) for i in input().split(",")]
if (sum(a)%5 == 0):
    print(tuple(b))
    a = b
else:
    print(tuple(a))
    b =a
print(b is a)