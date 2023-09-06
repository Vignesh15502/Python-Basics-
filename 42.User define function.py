# User define functions

def welcome():
	print("Welcome to the class")
	
welcome()
welcome()
welcome()

# No return type without argument Function

def add():
	a = int(input("Enter the value of A:"))
	b = int(input("Enter the value of B:"))
	c = a+b
	print("Total:",c)
	
add()

#No return with Argument

def sub(a,b):
	c = a-b
	print("Total:",c)
	
sub(30,10)

#Return type without argument

def mul():
	a=int(input("Enter the value of A:"))
	b=int(input("Enter the value of B:"))
	c = a*b
	return c
	
mul()

#Return type with argument

def div(a,b):
	c = a/b
	return c
		
div(20,2)
