# set and (set function)

names = {"Ram","Sam","Ravi"}

print(names)
print(type(names))

# access values, using for loop

for name in names:
	print(name)
	
# Adding new Element

names.add("sara")
print(names)
	
#Update another set of Data

a={"Kumar","sundar","Suresh"}
names.update(a)
print(names)

# remove and discard method

names.remove("sara")
print(names)
names.discard("suresh")
print(names)

# pop function

names.pop()
print(names)

#clear and delete method

names.clear()
print(names)

'''
del names
print(names)
'''
#Mathametical (union,Intersection)

a= {1,2,3,4}
b= {'a','b','c','d'}
c=a.union(b)
print(c)
a.update(b)
print(a)

#Inbuild Functions

#intersection method

a = {1,2,3,4,5}
b = {5,6,7,8,9}
c = a.intersection_update(b)
print(a)

#symmetric differrence method

a = {1,2,3,4,5}
b = {5,6,7,8,9}
c = a.symmetric_difference(b)
print(c)
a.symmetric_difference_update(b)
print(a)

#disjoint method

a = {1,2,3,4,5}
b = {5,6,7,8,9}
c = a.isdisjoint(b)
print(c)

#sub set or super set method

a = {5,6,7}
b = {5,6,7,8,9}
c = a.issubset(b)
print(c)

a = {5,6,7}
b = {5,6,7,8,9}
c = a.issuperset(b)
print(c)

