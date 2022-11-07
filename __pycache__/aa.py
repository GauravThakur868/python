import keyword
a = "lambda"
b = "gamma"
c = "class"
if keyword.iskeyword(a):
    print(a + ": True")
else:
    print(a + ": False")
if keyword.iskeyword(b):
    print(b + ": True")
else:
    print(b + ": False")
if keyword.iskeyword(c):
    print(c + ": True")
else:
    print(c + ": False")