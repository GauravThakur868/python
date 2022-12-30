a = int(input())
b = int(input())
while True:
    choice = int(input("choices: "))
    if choice == 1:
        print("ans:",a+b)
        a = int(input())
        b = int(input())
    elif choice == 2:
        print("ans:",a-b)
        a = int(input())
        b = int(input())
    else:
        break