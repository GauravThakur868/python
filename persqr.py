a = int(input())
b = int(input())
while a in range(a,b+1):
    if a%7 == 0:
        print(a,end=' ')
        break
    else:
        print(a,end=' ')
        a = a+1