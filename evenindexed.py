str1 = input()
def evenindex(str1):
    for i in range(0,len(str1)):
        if i %2 == 0:
            a = str1[i]
            print(a,end="")
evenindex(str1)