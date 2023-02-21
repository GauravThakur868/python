def rev(p):
    s = ''
    if len(p)>=0:
        s = p[::-1]
    return s
p = input()
print(rev(p))