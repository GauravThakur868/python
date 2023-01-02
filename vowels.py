a = input()
b = ["a","e","i","o","u","A","E","I","O","U"]
i = 0
for i in range(0,len(a)):
    if a[i] in b:
        print(end='')
    else:
        print(a[i],end='')