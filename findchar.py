str1 = input()
char = input()
def findchar(str1,char):
    if char in str1:
        print(str1.find(char)+1)
    else:
        print("not found")
findchar(str1,char)