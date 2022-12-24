#try:
    #this block of code will run and throw errors if there are any
#except:
    # this will raise the errors
#else:
    #this will execute if there are no errors
#finally:
    #this will execute regardless the result of try and except


#try:
#    f = open("demo.py")
#    try:
#        f.write("abc")
#    except:
#        print("error")
#    finally:
#        f.close()
#except:
#    print("cant open file")

a = 5
if a<10:
    raise Exception("value is less than 5")
    