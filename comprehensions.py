l = []
for i in range(3):
    l.append(int(input()))
l1 = [[i,j,k] for i in l for j in l for k in l if i!=j and i!=k and j!=k and (i+j+k)%2==0]
print(l1)