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