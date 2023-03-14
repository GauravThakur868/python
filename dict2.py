l1 = list(map(int,input("values: ").split(",")))
l2 = list(input("keys: ").split(","))
print(dict(zip(l1,l2)))
print(dict(zip(l2,l1)))