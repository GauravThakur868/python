p = int(input())
r = int(input())
t = float(input())
ci = (p*(1+(t/12))**12*r)-p
a = "{:.2f}".format(ci)
if p >= 1 and r >= 1 and t >= 0:
    print(a)
else:
    print()