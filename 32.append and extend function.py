#append function
'''
The append() method in the Python programming 
language adds an item to a list that already 
exists whereas the extend() method adds 
each of the iterable elements which is supplied 
as a parameter to the end of the original list.
'''

names=["Ram"]
print(a)
names.append("Vignesh")
names.append("surys")
names.append("Rolex")
print(names)
names2=["sara","anitha"]
names.extend(names2)
print(names)
names.insert(0,"Ravi")
print(names)

'''
#output

[35, 45, 25, 4, 25]
['Ram', 'Vignesh', 'surys', 'Rolex']
['Ram', 'Vignesh', 'surys', 'Rolex', 'sara', 'anitha']
['Ravi', 'Ram', 'Vignesh', 'surys', 'Rolex', 'sara', 'anitha']
'''