data1 = input("list1: ")
data2 = input("list2: ")
list1 = data1.split(",")
list2 = data2.split(",")
dict1 = dict(zip(list1,list2))
data3 = input("list3: ")
data4 = input("list4: ")
list3 = data3.split(",")
list4 = data4.split(",")
dict2 = dict(zip(list3,list4))
print(dict1)
print(dict2)
keyvalue = input("key: ")
if (keyvalue in dict1.keys() and keyvalue in dict2.keys()):
    print("present in dict1 and dict2")
else:
    print("invalid")