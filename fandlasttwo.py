a = input()
if a[0:2] == a[4:]:
    print(a[2:4])
elif a[0:2] == a[5] +a[4]:
    print(a[2:4])
else:
    print(a[0:2] + a[4:])
