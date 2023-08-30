# List Datatype

#1                  #outputs
a=[1,2,3,4,5]       #[1, 2, 3, 4, 5]
print(a)            #<class 'list'>
print(type(a))      #[100, 2, 3, 4, 5]
a[0]=100            #2
print(a)            #5
print(a[1])         #[100, 2, 3]
print(a[-1])        #[3, 4, 5]
print(a[0:3])       #[100, 2, 3]
print(a[2:])
print(a[:3])
           
'''
List is a collection data type. 
It allows multiple values to be stored 
within the same field. In Table Design, 
you must configure the List data type with 
all the values that the field stores.

List. Lists are used to store multiple items 
in a single variable. Lists are one of 4 built-in 
data types in Python used to store collections of data, 
the other 3 are Tuple, Set, and Dictionary, 
all with different qualities and usage.
'''
#2

a=[1,True,'Ram',2.5,[1,2,3,4]]
print(a)
print(type(a))
print(a[0],"type is",type(a[0]))
print(a[1],"type is",type(a[1]))
print(a[2],"type is",type(a[2]))
print(a[3],"type is",type(a[3]))
print(a[4],"type is",type(a[4]))
print(a[4][1])

#outputs
'''
[1, True, 'Ram', 2.5, [1, 2, 3, 4]]
<class 'list'>
1 type is <class 'int'>
True type is <class 'bool'>
Ram type is <class 'str'>
2.5 type is <class 'float'>
[1, 2, 3, 4] type is <class 'list'>
2
'''