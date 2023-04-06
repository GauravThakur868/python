s = input()
l = [chr(ord(i)-1) for i in s if i!='a']
print(l)