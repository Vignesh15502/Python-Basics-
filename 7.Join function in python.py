# join-function-in-python

#join function in python

# 1

a="vignesh"
b='-'.join(a)
print(b)

#2

c=["25","22","33"]
print(','.join(c))      

'''(" ") is convert to the string.'''
                                
#3

para=[]
print("Enter a para:")

while True:
  line=input()
  if line:
    para.append(line)
  else:
    break
  print(para)
  output='\n'.join(para)
  print(output)
