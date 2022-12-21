a = int(input())
i = 1
b = 0
while i<= (a*2):
    b += i
    i += 2
b = b/a
print("{:.2f}".format(b))