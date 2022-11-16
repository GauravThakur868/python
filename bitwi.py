a = int(input())
b = int(input())
if a >= 0 and b>=0:
    print(a >= 0 and b>=0)
elif (a>= 0 and b<=0) or (a<=0 and b>=0):
    print((a>= 0 and b<=0) or (a<=0 and b>=0))
elif a<=0 and b<=0:
    print(a<=0 and b<=0)