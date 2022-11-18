a = input()
b = input()
if len(a) <= 20 and len(b) <= 20:
    if a[0] in b and a[-1] in b:
        print(a[0] in b and a[-1] in b)
    else:
        print(a[0] in b and a[-1] in b)
else:
    print()