class solution:
    def missingnumber(self,a,n):
        self.a = a
        self.n = n
        for i in range(1,self.n):
            if i not in self.a:
                return i
n = int(input())
a = list(map(int,input().split()))
s = solution().missingnumber(a,n)
print(s)