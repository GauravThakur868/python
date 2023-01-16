a = input()
b = int(input())
def placevalue():
    if b >= 0 and b < len(a)-1:
        print(a[b+1])
