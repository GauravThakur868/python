list1 = [22,56,77,99,45,36,87,93,5,78,2,66]
evenlist1 = list(filter(lambda x : x%2 == 0,list1))
print("even:",evenlist1)
oddlist1 = list(filter(lambda x : x%2 != 0,list1))
print("odd:",oddlist1)