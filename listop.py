a = input()
b = a.split(",")
c = 0
for i in range(0,len(b)):
    c += int(b[i])
print(c)
if c >0:
    print("+ve")
elif c<0:
    print("-ve")
else:
    print("unsigned")