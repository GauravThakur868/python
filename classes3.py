class Person:
    def __init__(self,fn,mn,ln):
        self.fn=fn
        self.mn=mn
        self.ln=ln
firstname = input()
middlename= input()
lastname = input()
myname = Person(firstname,middlename,lastname)
print(myname.mn)