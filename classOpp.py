# ------------------------
# ------- Class OPP ------
# ------------------------

# Syntax of Class 
# class name_of_class :
#       constractor  to create instance from class 
#       def __init__ (self):
#           body of function

# class car :
#     def __init__(self):
#         print("hello a new member")
        

# car1=car()
# print(dir(car1.__class__))
# # print(dir(str))
# def my_name():
#     name="mohamed" 
#     age=16 
#     return name , age 


class members :

    number_of_members = 0     # attributes of class

    def __init__(self,first_name,middle_name,last_name,gender):    # Constractor  atrributes of instance or object 
        self.fname=first_name
        self.mname=middle_name
        self.lname=last_name
        self.gender = gender 
        members.number_of_members +=1

    def full_name(self):
        return f"{self.fname} {self.mname} {self.lname}"
    
    def say_hello(self):

        if self.gender == "male":
            return f"Hello Mr {self.fname}"
        else :
            return f"Hello Mrs {self.fname}"    
        
    def getter(self):
        return f"{self.full_name()}"
    
    def num_of_instance(self):
        return f"number of instance is {members.number_of_members}"

mohamed = members("mohamed","ahmed","ali","male")
mona = members("mona","elsayed","ali","female")
alaa = members("alaa","elsayed","ali","female")
# ahmed = members("ahmed","elsayed","ali","female")

# print(mohamed.fname)
# print(mohamed.mname)
# print(mohamed.lname)
# print(mohamed.full_name())
# print(mona.full_name())
# print(mohamed.say_hello())
# print(mona.say_hello())
# print(mona.getter())

print(mohamed.num_of_instance())