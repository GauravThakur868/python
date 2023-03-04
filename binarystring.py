import re
a = input()
b = r'[0-9]'
c = re.sub(b,'',a)
print(c)