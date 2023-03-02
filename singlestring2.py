def add_string(str1):
    l = len(str1)
    if l >2:
        if 'ing' in str1:
            str1 = str1 +'ly'
        else:
            str1 = str1 +'ing'
    return str1
a = input()
print(add_string(a))