def digitnum(num):
    return len(num)
def reverse(num):
    num = num[-1::-1]
    return num
def main(num):
    print(digitnum(num))
    print(reverse(num))
n = input()
main(n)