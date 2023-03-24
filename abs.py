k = [i for i in input("keys: ").split(" ")]
v = [(int(i)) for i in input("values: ").split(" ")]
d = {k[i][-1]:abs(v[i]) for i in range(len(k))}
print(d)