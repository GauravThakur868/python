a = int(input())
b = int(input())
while a in range(a,b+1):
    if a**0.5 %2 == 0:
        print(a,end=' ')
        a += 1
        break
    else:
        print(a,end=' ')
        a += 1