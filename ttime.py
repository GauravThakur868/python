a = int(input())
b = a // 60
c = a % 60
d = "{}{}{}{}{}".format(b, "HOURS", " and", c, " Minutes")
if 100 <= a <= 550:
    print(d)
else:
    print()