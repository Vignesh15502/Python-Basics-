# Nested if statement in python

'''
3 marks as Input
Total
Average
Result
If Pass Gread
   90-100  A
   80-89   B
   70-79   C
   Else    D
'''

m1 = int(input("Enter mark-1:")
m2 = int(input("Enter mark-2:")
m3 = int(input("Enter mark-3:")

total=m1+m2+m3
average=total/3.0

print("Total:",total)
print("Average:",average)

if m1>=35 and m2>=35 and m3>=35:
	print("Result: Pass")
	
	if average>=90 and average<=100:
		print("Gread:A")
	elif average>=80 and average<=89:
		print("Gread:B")
	elif average >=70 and average<=79:
		print("Gread:c")
	else:
	print("Gread:D")
else:
	print("Result:Fail")
	print("Gread: No Gread")
    
'''
The nested if statements in Python are the nesting 
of an if statement inside another if statement with 
or without an else statement. In some cases, 
we need nesting of if statements to make the 
entire program flow of code in a semantic order and 
make it easily readable.
'''
