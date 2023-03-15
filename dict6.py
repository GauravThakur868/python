n = int(input("size: "))
i = 1
d = {}
while i<=n:
    key = int(input("key: "))
    value = input("value: ")
    d[key]=value
    i+=1
for k in d.keys():
    print(k,'->',d[k])