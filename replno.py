a = int(input())
b = str(a)
c = b[-1]
if int(c) % 2 != 0:
    print(str(b[0:3]) + "o")
else:
    print(a)