l1 = list(input('keys: ').split(","))
l2 = list(input('values: ').split(","))
d = dict(zip(l1,l2))
print(d)
s = input()
if s in l1:
    print(d[s])
else:
    print("fat")
