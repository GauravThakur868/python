a = int(input())
b = int(input())
c = int(input())
s = []
u = [a,b,c]
if (a+b+c)%2==0:
    pass
else:
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if (i!=j) and (i!=k) and (j!=k):
                    w = [u[i],u[j],u[k]]
                    if sum(w)%2!=0:
                        s.append(w)
print(s)