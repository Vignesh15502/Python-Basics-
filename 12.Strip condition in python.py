#strip() condition

s="Tony"
print(len(s))
print(len(s.strip()))
print(len(s.lstrip()))
print(len(s.rstrip()))

'''
The strip() method removes any leading, and trailing whitespaces. 
Leading means at the beginning of the string, trailing means at the end. 
You can specify which character(s) to remove, 
if not, any whitespaces will be removed.
'''