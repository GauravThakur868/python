a = input()
i = 0
b = 1
c = ''
for i in range(0,len(a)):
    c = c+ a[i]*b
    b += 1
print(c)