def abc(i,j,k):
    return (i**k)-j
def pqr(i):
    return i**3
i = int(input())
j = int(input())
k = int(input())
result = pqr(i**k)-pqr(j) - 3*(i**k)*(j)*abc(i,j,k)
print(result)