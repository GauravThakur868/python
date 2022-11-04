a = float(input())
b = a * (a + 1) * (2 * a + 1) / 6
c = "{:.2f}".format(b)
if a >= 1:
    print(c)