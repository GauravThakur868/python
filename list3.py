#numbers = [1,4,2,8,6,5]
#numbers.sort()
#print(numbers)
#numbers = [1,2,3,4,5]
#list = [x**2 for x in numbers]
#print(list)
numbers = [1,2,3,4,5,2,6]
a = numbers.index(2)
numbers[a] = 200
print(numbers)

num2 = numbers.copy()
print(num2)

list1 = ['x','y', 'z']
list2 = [1,2,3]
list3 = list1 +list2

print(list3)
for x in list2:
    list1.append(x)
print(list1)