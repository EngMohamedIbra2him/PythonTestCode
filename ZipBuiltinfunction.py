#-----------------------------------------------
#----------- Zip built in function -------------
#-----------------------------------------------

# [] zip() return object contain all objects 
# [] zip() length is the lowest object 


list1 = [1,2,3,4,5]
list2 = ["a","b"]
list3 = (10,20,30)
dict = {"name":"mohamed","age":26}

for item1 , item2 ,item3 ,item4 in zip(list1,list2,list3,dict):
    print(f"{item1}-- {item2}--{item3} --{item4} -- {dict[item4]}")

# unlimitedlist = zip(list1,list2)
# for item in unlimitedlist:
#     print(item)

