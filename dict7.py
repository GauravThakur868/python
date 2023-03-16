a = list(input("keys: ").split(","))
b = []
print("Enter a values: ")
for i in range(len(a)):
    s = list(map(int,input().split(",")))
    b.append(s)
dict1 = {a:b for a,b in zip(a,b)}
n = input("enter key: ")
if (n in a):
    print(max(dict1[n]))
else:
    print("not found")