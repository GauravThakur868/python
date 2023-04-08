def replace(str,char,ind):
    if len(str)>ind and ind!=0:
        return str[:ind-1]+char+str[ind:]
    else:
        return 'index out of range'
print(replace(input(),input(),int(input())))