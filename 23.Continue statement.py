# continue statement

i=1
while i<=20:
	if i%2==0:
		i=i+1
		continue;
	print(i)
	i+=1
    
'''
The continue statement in Python returns the 
control to the beginning of the while loop. 
The continue statement rejects all the remaining 
statements in the current iteration of the 
loop and moves the control back to the top of the loop.
'''