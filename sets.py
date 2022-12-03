# store multiple values in single variable
# unordered
#myset = {"car", "bike", "boat"}
#print(myset)
# unchangable 
# duplicates are not allowed
myset = {"car", "bike","boat","car"}
print(myset)
#
print(len(myset))
i = "bike"
if i in myset:
    print("true")
else:
    print("false")
myset.add("cycle")
print(myset)
myset.discard("car")
print(myset)
myset1 = {1,2,3,4}
myset3 = {4,5,6}
myset2 = myset.union(myset1)
print(myset2)
myset4 = myset1.intersection(myset3)
print(myset4)
myset5 = myset1.symmetric_difference(myset3)
print(myset5)
