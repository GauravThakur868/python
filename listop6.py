a = input("list: ").split(",")
b = sum(tuple(map(int,a)))
if b ==0:
    print("invalid")
else:
    for i in range(len(a)):
        if i%2 == 0:
            print(a[i],end=" ")