a = input()
b = input()
if b in a:
    c = a.find(b)+1
    d = a.rfind(b)+1
print(c**2)
print(d**2)