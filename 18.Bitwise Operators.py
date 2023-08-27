#Bitwise Operators

"""
&  AND
|  OR 
^  XOR
~  NOT
<< Zero fill left shift
>> signed right shift
"""
# & AND

a=10          "Output"
b=11             
print(a&b)       '10'

# OR

a=25
b=45
print(a|b)       '61'

# ^ XOR

a=25
b=45
print(a^b)       '52'

# ~ NOT

a=46
print(~a)

# << Zero fill left shift

a=25
print(a<<2)       '100'

#>> Signed right shift

a=25
print(a>>2)       '6'

'''
In Python, bitwise operators are used to perform 
bitwise calculations on integers. The integers are 
first converted into binary and then operations 
are performed on each bit or corresponding pair 
of bits, hence the name bitwise operators. 
The result is then returned in decimal format.
'''