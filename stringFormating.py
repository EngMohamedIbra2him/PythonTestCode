#---------------------------
#----Strings Formating------
#---------------------------

# %s = string        %.s = string 
# %d = Number        %.d = Number 
# %f = Floating      %.f = Floating 

# We can assume this syntax like as Method
# {:s} = string
# {:d} = Number
# {:f} = Floating 

name="mohamed Ibrahim"
age=27
salary=1000

print("my name is %s and my age is %d and my salary is %f"  % (name,age,salary))
print("my name is {} and my age is {} and my salary is {}"  .format(name,age,salary))
print("my name is {:s} and my age is {:d} and my salary is {:.1f}"  .format(name,age,salary))


# Controling  floating number

print("my name is %s and my age is %d and my salary is %.2f"  % (name,age,salary))

# Truncating String

print("my name is %.8s and my age is %d and my salary is %.2f"  % (name,age,salary))

mymoney= 1632040
print("this number is {:,d} " .format(mymoney))

# Latest version of formating

myname ="mohamed" 
age=26

print(f'my name is {myname} my age is {age}')