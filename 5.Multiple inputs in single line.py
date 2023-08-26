# Multiple-inputs-in-single-line

#use the split() function

name1,name2 name3=input("Enter Three Numbers:").split()
print("Name 1:",name1)      
print("Name 2:",name2)        
print("Name 3:",name3)        '''
                              The split() method splits a string into a list. 
                              You can specify the separator, default separator is any whitespace. 
                              Note: When maxsplit is specified, 
                              the list will contain the specified number of elements plus one.
                              '''
                              '''
                              -->The Normal Split function is consider the empty space
                              -->if you want any other identifier use (",") ("|")
                              '''
name1,name2 name3=input("Enter Three Numbers:").split(",")
print("Name 1:",name1)      
print("Name 2:",name2)        
print("Name 3:",name3)  
