a = input('keys: ').split()
b = list(map(int,input('values: ').split()))
d = {}
for i in range(min(len(a),len(b))):
    x = a[i].lower()
    d[x] = b[i]**4
print(d)
