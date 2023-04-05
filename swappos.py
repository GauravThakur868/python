l = input().split()
p1 = int(input())
p2 = int(input())
if p1<=len(l) and p2<=len(l):
    t = l[p1-1]
    l[p1-1]=l[p2-1]
    l[p2-1]=t
    print(l)
else:
    print("index out of range")