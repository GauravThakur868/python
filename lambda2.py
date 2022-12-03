list1 = [10,20,30,40,50]
a = list(map(lambda i : i*3,list1))

print(a)

list2 = ["a","B","c","D","e","f"]
#def abcd(i):
#    if i.islower():
#        return list2.upper()
#    else:
#        return list2.lower()
#a = list(map(abcd,list2))
#print(a)
from functools import reduce
l1 = [1,2,3,4,5,6]
z = reduce(lambda i,j: i+j,l1)
print(z)