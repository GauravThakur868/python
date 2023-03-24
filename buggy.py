string = input()
n = int(input())
Dict = {x.upper(): x*n for x in string}
print(Dict)