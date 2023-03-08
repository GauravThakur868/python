def in_list(lst):
    s=""
    for i in lst:
        s += i
    return s
a = input().split(",")
print(in_list(a))