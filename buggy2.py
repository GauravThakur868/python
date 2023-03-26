string = input()
Dict = {x: {y: x+y for y in string} for x in string}
print(Dict)