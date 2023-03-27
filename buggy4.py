class Record:
    def __init__(self,name,rollno,emailid):
        self.name = name
        self.rollno = rollno
        self.emailid = emailid
n = int(input())
for i in range(1,n+1):
    name = input()
    rollno = int(input())
    emailid = input()
    record = Record(name,rollno,emailid)
    print('Record: ',i,'is',record.name,record.rollno,record.emailid)