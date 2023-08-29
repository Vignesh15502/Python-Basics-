# Nester-for-loop

'''
*
* *
* * *
* * * *
* * * * *
'''

for i in range(5+1):
  for j in range(i):
    print("*",end=" ")
  print(" ")



'''
* * * * *
* * * * 
* * * 
* * 
* 
'''

for i in range(5,0,-1):
  for j in range(i):
    print("*",end=" ")
  print(" ")
  
'''
A nested loop refers to a loop within a loop, 
an inner loop within the body of an outer one. 
Further, the first pass of the outer loop will 
trigger the inner loop, which will execute to completion. 
After that, the second pass of the outer 
loop will trigger the inner loop again.
'''