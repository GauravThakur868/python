def iseven(i):
    return i%2==0
list1 = [3,4,10,9,18,66,13,15]
evennumber = list(filter(iseven,list1))
print(evennumber)
#or
oddnumber = list(filter(lambda i :i%2!=0,list1))
print(oddnumber)

square = list(map(lambda i : i**2,list1))
print(square)