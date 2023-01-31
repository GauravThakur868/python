str1 = input()
ind = int(input())
def remove(str1,ind):
    if len(str1) <= ind:
        print("index out of range")
    else:
        for i in range(0,len(str1)):
            if i != ind-1:
                print(str1[i],end="")
remove(str1,ind)