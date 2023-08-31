#Tuple in Python
'''
1. A tuple is an immutable object, 
which means it cannot be changed, 
and we use it to represent fixed collections 
of items. Let's take a look at some examples 
of Python tuples: () — an empty tuple. 
(1.0, 9.9, 10) — a tuple containing three 
numeric objects.

2. Tuples are used to store multiple items 
in a single variable. Tuple is one of 4 
built-in data types in Python used to store 
collections of data, the other 3 are 
List, Set, and Dictionary, all with different 
qualities and usage.
'''
a = (1,2.5,True,"Ram)   #outputs
print(a)                #(1, 2.5, True, 'Ram')
print(type(a))          #<class 'tuple'>
print(a[1])2.5
print(a[0:2])           #(1, 2.5)
print(a[-1])            #Ram
b = list(a)
print(b)                #[1, 2.5, True, 'Ram']
b.append("Raja")
print(b)                #[1, 2.5, True, 'Ram', 'Raja']
print(type(b))          #<class 'list'>
a = tuple(b)
print(a)                #(1, 2.5, True, 'Ram', 'Raja')
print(type(a))          #<class 'tuple'>