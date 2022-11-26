# tuples store multiple in a single vaariable
# ordered
# immutable
# use -() for tuples
# allows duplivate values
# 
my_tuples = ("apple", "orange", "pineapple")
print(my_tuples)
print(len(my_tuples))
my_tuple = ("apple", )
print(my_tuple)


mytuple = ("cars", "bike", "train", "boat")
mylist = list(mytuple)
mylist.pop()
mylist.insert(3, "bus")
mylist.append("plane")
mytuple = tuple(mylist)
print(mytuple)


tuple1 = (1,2,3)
tuple2 = (4,5,6)
tuple1 += tuple2
print(tuple1)

tuple3 = (1,2,3,4,5)
print(tuple3[::-1])

tuple4= ("gauarv",)
print(tuple4)

tuple5 = ("A", "B", "C", "D")
(one,two,*three) = tuple5
print(one)
print(two)
print(three)

