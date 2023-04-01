class solution:
    def printsequence(self,s):
        res=""
        dict1 = {"A":"2","B":"22","C":"222"}
        for i in s:
            res+=dict1[i]
        print(res)
        return(res[::-1])
inputstr = input()
solobj = solution()
print(solobj.printsequence(inputstr))
