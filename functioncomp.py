def cube(num):
    return num**3
def triple(num):
    return 3*num
num = int(input())
print(triple(cube(num)))
print(cube(triple(num)))