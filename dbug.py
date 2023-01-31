def function(x,y,z,f):
    ans = (x-y)*z /f
    print("result:"+"{:.2f".format(ans))
    e = ((x-y)*z)/f
    print("result:"+"{:.2f}".format(e))
    e = (x-y)*(z/f)
    print("result:"+"{:.2f}".format(e))
x = int(input())
y = int(input())
z = int(input())
f = int(input())
function(x,y,z,f)