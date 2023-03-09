a = input("list: ").split(",")
if "0" in a:
    print("invalid")
else:
    for i in range(len(a)):
        if i %2 != 0:
            print(a[i],end=" ")
            