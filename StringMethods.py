#---------------------------
#------String Methods ------
#---------------------------

# len()
# strip & rstrip & lstrip    as  same as split 
# title
# captalize 
# zfill
# lower
# upper
# split & rsplit  this method remove sapce and return a list.
# splitlines split object by lines
# center
# Count      this method count anything in the object
# index   return item
# find    return index
# just  rjust
# islower
# istitle
# isupper
# isidentifier
# isalpha
# isalnum
# replace (old value , new value , count)
# trim
# join  (Iterable) 


msg="Hell Python Community"
msg1=" Hello World    "
msg2="#### Python Community#####"
x,y,z =1,11,111
msg3,msg4="mohamed",'MOHAmmed'
msg5= "I love Python"      
msg5= "I love Python"      
msg6= "I-love-Python"      
msg7= "mohamed"
msg8= "Python is an easy language"
msg9 ="""
I love python 
Hello World
Okay.....
"""
msg10="my name"
x="mohamed ali mohamed"
list1=["mohamed","ali"]

print(len(msg))
print(msg1.strip())
print(msg1.rstrip())
print(msg1.lstrip())
print(msg2.strip("#"))
print(msg1.title())
'''
print(x.zfill(3))
print(y.zfill(3))
print(z.zfill(3))
'''
print(msg3.upper(),".........",msg4.lower())

#-----------------------------------------------

print(msg5.split())
print(msg5.split("-"))
print(msg7.center(10,"#"))
print(msg7.center(10,"@"))
print(msg8.count("m"))
print([1,2,3,4,1].count(1))
print(msg9.splitlines())
print(msg10.isidentifier())
print(x.replace("mohamed","ali"))
print("-".join(list1))





