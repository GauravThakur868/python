def stringk(k,str):
    text = str.split(" ")
    for x in text:
        string = ""
        if len(x)>k:
            string=x
            print(string)
str1 = input()
k = int(input())
stringk(k,str1)