colors = ['red', 'blue', 'red', 'black', 22]
print(colors)
print(colors[1])
print(colors[1:4])
0
colors[2] = "green"
print(colors)

colors[0:2] = "yellow", "pink"
print(colors)

colors.insert(2,"indigo")
colors.append(55)
print(colors)

cars = ["TATA", "NANO", "ALTO"]
colors.extend(cars)
print(colors)

players = ("dhoni", "messi", "dravid")
colors.extend(players)
print(colors)

colors.remove("black")
print(colors)

colors.pop(1)
print(colors)

del colors[0]
print(colors)

colors.clear()
print(colors)