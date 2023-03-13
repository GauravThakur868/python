list1 = [(1,3,4), (2,4,6), (3,8,1)]
print(list1)
element = int(input())
result = list(tuple(j+element for j in i) for i in list1)
print(result)