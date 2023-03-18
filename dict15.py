data1 = input("data1: ")
data2 = input("data2: ")
list1 = data1.split(",")
list2 = data2.split(",")
if (len(list1) == len(list2)):
    dict1 = dict(zip(list1,list2))
    print(dict)
    for key in sorted(dict1):
        print("%s:%s" % (key,dict1[key]))
else:
    print("invalid")