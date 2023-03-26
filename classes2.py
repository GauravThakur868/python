class company:
    def abc(self,n,cc,p):
        self.n = n
        self.cc = cc
        self.p = p
b1 = company()
b2 = company()
b1.abc(input(),int(input()),int(input()))
b2.abc(input(),int(input()),int(input()))
if (b1.cc >b2.cc):
    print("best values")
    print("name: ",b1.n)
    print("on road price: ",b1.p)
else:
    print("best values")
    print("name: ",b2.n)
    print("on road price: ",b2.p)