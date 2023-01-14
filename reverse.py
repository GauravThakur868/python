num = int(input())
def reverse(num):
    b = str(num)
    c = str(num)
    if b == c:
        print("palindrome")
        return("palindrome")
    else:
        print("not palindrome")
        return("not palindrome")
reverse(num)