a = input()
for i in range(0,len(a)):
    x = 0
    for j in range(0,len(a)):
        if (a[i]==a[j] and i != j):
            x=1
            break
    if(x==0):
        print(a[i],end=" ")