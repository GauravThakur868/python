year = int(input())
def isleap(year):
    if year % 100 == 0:
        print(year%100 == 0)
    elif year%4 == 0:
        print(year%4 == 0)
    elif year%400 == 0:
        print(year%400 == 0)
    else:
        print("False")
isleap(year)