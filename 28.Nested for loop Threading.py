# Nested for loop Threading

list1=["vignesh","kumar"]
for i in range(0,3):
  print("outer loop",i)
  for j in range(len(list1)):
    print("inner loop",list1[j])
	
'''
#output

outer loop 0
inner loop vignesh
inner loop kumar
outer loop 1
inner loop vignesh
inner loop kumar
outer loop 2
inner loop vignesh
inner loop kumar
'''