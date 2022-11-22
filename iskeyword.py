import keyword
a = ["except", "raise", "fall"]
for i in range(len(a)):
    if keyword.iskeyword(a[i]):
        print(a[i] + ": True")
    else:
        print(a[i] + ": False")