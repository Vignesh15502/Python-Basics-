# Input-Statement

# input statement

name=input()
print(name)
print(type(name))

'''
-->if your input is a numerical, the output was considering s 'str'
   because, input() function in always considering only the string
-->if you want enter the integer input, 
   use the int(input())
'''
age=int(input())
print(age)
print(type(age))

'''
now it will be considering the 'int' type
'''
'''
if you don't want blank box of input,
use any "string lines" in the input()function.   
'''
#Example:

    #Adding the two numbers:

a=int(input("Enter the Value of A:"))
b=int(input("Enter the Value of B:"))
c=a+b
print(c)
