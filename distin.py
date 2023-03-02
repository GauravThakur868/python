a = input()
x = ["a","@","i","0","u","A","E","I","0","U"]
for i in range(len(a)):
    b = 0
    c = 0
    if a[i] not in x:
        c=c+1
        print(a[i] +":"+str(c))