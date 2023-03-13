def removdup(List):
    return [(a,b) for i , [a,b] in enumerate(List) if not any(c == b for _, c in List[:i])]
list1 = [(23,45),(25,17),(35,67),(25,17),(23,45),(35,67)]
element = int(input())
result = [tuple(j*element for j in sub) for sub in list1]
print(result)
print(removdup(result))