my_tuple = ("car", "boat", "bike")
#my_tuple.count()

#for i in my_tuple:
#    print(i)
#i = 0
#while i < len(my_tuple):
#    print(my_tuple[i])
#    i = i+1

tuple1 = (1,[6,7],2,3,4)
#a= tuple1[1][0]
#print(a)

b = list(tuple1)
b.remove([6,7])
b.insert(1,[8,7])
tuple1 = b
print(tuple1)