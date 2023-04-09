a = input().split(" ")
d = {}
for i in a:
    if (3<len(i)) and ('a' in i):
        d[i] = len(i)/2
    elif len(i)>10:
        d[i]=len(i)/2
print(d)