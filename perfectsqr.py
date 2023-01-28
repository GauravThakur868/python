a = int(input())
b = int(input())
def perfectsqr(a,b):
    for i in range(a,b+1):
        if i**0.5 == int(i**0.5):
            print(i)
            break
perfectsqr(a,b)