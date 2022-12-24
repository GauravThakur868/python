import re
value = "this is string"
output = re.search("^this.*string$",value)
print(output)
pattern = r"^(?=.*[a-z])(?=.*[!@#$%^&*()_+=-])(?=.{8,})"

# ^ = starts with it
# *[] = 
# ?=  = lookhead assertion
# {} = from 8 to infinity 
# r = raw stringazxcxcvbn6+01423
