a = input()
b = ["a","e","i","o","u"]
c = 0
for i in a:
    print(a[c],end=' ')
    if a[c] in b:
        break
    c = c+1