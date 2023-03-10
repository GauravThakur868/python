list1 = [s for s in input().split(',')]
list2 = [s for s in input().split(',')]
list3 = []
if len(list1) < len(list2):
    for i in range(len(list1)):
        list3.append(list1[i]+list2[i])
else:
    for i in range(len(list2)):
        list3.append(list1[i]+list2[i])
print(list3)