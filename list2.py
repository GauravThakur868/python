cars = ["TATA", "NANO", "ALTO", "jeep"]
[print(x) for x in cars]
newlist = []
for x in cars:
    if "a" in x or "A" in x:
        newlist.append(x)
print(newlist)
listnew = [x for x in cars if x != "TATA"]
print(listnew)
#         expressions item list condition
