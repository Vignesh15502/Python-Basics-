# List type Constructers
'''
1.The LIST constructor complex function is 
used to explicitly generate lists of 
values that can be assigned 
to fields in an output message.

2.Why use Python list constructor?
The list constructor seems to me to be 
the "one obvious way" to convert any iterable 
into a list. 
'''

print(list(range(5)))
print(list("Vignesh"))

#Output
#[0, 1, 2, 3, 4]
#['V', 'i', 'g', 'n', 'e', 's', 'h']

#Sorting methord
'''
1.Ascending Order
2.Descending Order
'''
a=[100,10,20,40,15,30]
print(a)
a.sort()
print(a)

a.sort(reverse = True)
print(a)
'''
output:
[100, 10, 20, 40, 15, 30]
[10, 15, 20, 30, 40, 100]
[100, 40, 30, 20, 15, 10]
'''

#Alphabets Methord sorting
a=["Apple","Orange","Zebra"]
a.sort()
print(a)
'''
output:
['Apple', 'Orange', 'Zebra']
'''

#Key Methord
a = ["orange","Apple","Zebra"]
a.sort(key=len)
print(a)
'''
output:
['Apple', 'Zebra', 'orange']
'''