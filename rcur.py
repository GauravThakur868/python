num = int(input())
def oct(num):
    a = oct(num)
    return a[0:1] + a[2:]
    return oct(num)
print(oct(num))