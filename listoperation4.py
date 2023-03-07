def in_list(lis):
    s = []
    for i in range(len(lis)):
        s.append(lis[len(lis)-i-1])
    return s
a = input()
b = a.split(",")
print(in_list(b))