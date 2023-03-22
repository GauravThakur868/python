r = int(input())
list1 = list(range(1,r+1))
print(list1)
n = int(input())
list2 = [i*n for i in list1]
print(list2)
print(sum(list2))