#-----------------------------
#--------Lists Methods -------
#-----------------------------

# append()
# extend()
# remove()
# sort()
# clear()
# copy()
# count()
# insert()
# pop()

mylist1=["ali","mohamed","ahmed"]
mylist2=[1,2,3,4]
a=["a","b","c"]
b=["d","e","f"]
x=[10,22,13,14,67,1,4,6,7]
y=x.copy()


mylist1.append(mylist2)
a.extend(b)

print(mylist1)
print(mylist1[3][1])
print(a)
print(mylist1.remove("ali"))
print(mylist1)
print(x.sort(reverse=True))
#print(x.clear())
print(x)
print(y)
print(y.count(1))

f=[1,2,3]
f.insert(0,"test")
print(f)


mylist3=[1,2,3,4,5]

print(mylist3.pop(-1))



