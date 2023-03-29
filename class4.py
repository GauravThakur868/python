class bankaccount:
    def __init__(self,balance):
        self.balance = balance
    def withdraw(self,wbalance):
        return (self.balance-wbalance)//2
    def deposit(self,dbalance):
        return (self.balance+dbalance)//2
balance = int(input())
ins = bankaccount(balance)
print("1 . wthdraw")
print("2.deposit")
a = int(input("select: "))
amnt = int(input())
if a == 1:
    print(ins.withdraw(amnt))
else:
    print(ins.deposit(amnt))