#Split line Function

s="he \n is \n good"
print(s)
print(s.splitlines())
print(s.splitlines(True))
a="I am Iron Man"
print(a.split(" "))
a="I am Iron Man"
print(a.split(","))

'''
Python splitlines() method splits the string based on the lines. 
It breaks the string at line boundaries and returns a list of splitted strings. 
Line breakers can be a new line (\n), carriage return (\r) etc. 
A table of line breakers are given below which split the string.
'''