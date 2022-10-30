# company
salary = input("enter your salary")
time = input("enter years spent in company")
if  time >= 10:
    salary = salary*10/100
    print("final salary = ",salary)
elif time >= 8:
    salary = salary*8/100
    print("final salary = ",salary)
elif time >= 5:
    salary = salary*5/100
    print("final salary = ", salary)
else:
    print("enter a valid number")