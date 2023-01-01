a = int(input())
b =1
for i in range(1, a+1):
    if a %i == 0:
        b = b*i
print(b)