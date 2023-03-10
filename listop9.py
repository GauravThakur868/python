import math
list1 = (int(s) for s in input("list: ").split(','))
res = [math.sqrt(x) for x in list1]
print("{:.2f}".format(sum(res)))