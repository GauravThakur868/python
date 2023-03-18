a = [int(i) for i in input().split(',')]
b = list(map(lambda x: x-1,a))
c = {}
for i in b:
    if i == 1 or i == 0:
        c[i] = "not prime"
    else:
        for j in range(2,int(i**(0.5)+1)):
            if i %j == 0:
                c[i] = "not prime"
                break
        else:
            c[i] = "prime"
print(c)