a = int(input())
q = str(a)
b = a//10 ** (len(q)-1)
c = a%10
p = b*c
print(p)
if p%5 == 0:
    print("True")
else:
    print("False")
