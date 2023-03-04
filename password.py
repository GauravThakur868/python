a = input()
x = l = u = d = s = False
if len(a) >= 8:
    x = True
    for x in a:
        if x.islower():
            l = True
        elif x.isupper():
            u = True
        elif x.isdigit():
            d = True
        elif x == "@" or x == "%" or x == "^":
            s = True
if x and l and u and d and s:
    print("valid")
else:
    print("Invalid")