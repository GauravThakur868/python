bookreaders = []
n = int(input())
for i in range(n):
    name = input()
    bookcount = int(input())
    u25 = int(input())
    list1 = [name , bookcount,u25]
    bookreaders.append(list1)
print(bookreaders)
intelligentreaders = [reader[0] for reader in bookreaders if reader[1]>200]
print(intelligentreaders)
youngreaders = [reader[0] for reader in bookreaders if reader[2] ==1]
print(youngreaders)