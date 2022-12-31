str1 = input()
repo = "0123456789"
count = 0
str2 = ""
for i in str1:
    if i in repo:
        count = count+1
    else:
        str2 = str2+i
print(count)
print(str2)