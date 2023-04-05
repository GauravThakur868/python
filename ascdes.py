n = int(input())
l1 =[]
for i in range(n+1):
    l1.append(int(input()))
l2 = sorted(l1)
l3 = l2[::-1]
print(l2)
print(l3)