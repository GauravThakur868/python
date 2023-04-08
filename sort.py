def slicing(str,ind):
    if len(str)>ind:
        return str[:ind]
    else:
        return 'insex out of range'
print(slicing(input(),int(input())))