def placevalue(str1,val):
    if val in range(len(str1)-1):
        return str1[val+1]
    else:
        return 'index out of range'
print(placevalue(input(), int(input())))