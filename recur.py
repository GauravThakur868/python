#a = int(input("enter a input"))
#def number(a):
  #  if a == 0:
 #       return 0
#    return a+number(a-1)


def factorial(a):
    if  a == 1:
        print(a*factorial(a-1))
        return 0
    return a * factorial(a - 1)
factorial(3)