# Check-the-Id-of-variable

a=25             '''Id of Variables 
                    The id() method also returns the identity of a variable or object, as shown below.
                    The identity of the two same values is the same,as shown below.
                    In the above example,
                    the id of 10 and variable num are the same because both have the same literal value.'''               
b=25
c=50                #The id function is differented by the variable's value.   
d=a+b               #The id is refers the memory location of the Variable's Value.
print(id(a))      
print(id(c))
print(id(d))  
