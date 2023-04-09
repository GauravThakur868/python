a = input("keys: ").split()
b = list(map(int,input("values: ").split()))
c = {a[i].upper():(b[j])**2 for i in range(len(a)) for j in range(len(b)) if i==j}
print(c)