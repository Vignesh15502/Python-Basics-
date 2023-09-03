# Nested tuple 

a = (1,2,3,4)
b = (5,6,7,8)
c = (a,b)
print(c)             #((1, 2, 3, 4), (5, 6, 7, 8))
                     
print(c[0])          #(1, 2, 3, 4)
print(c[1])          #(5, 6, 7, 8)
print(c[0][1])       #2
print(c[1][0])       #5

# Repetations of tuple

x=("Vignesh",)*10     

print(x)            #('Vignesh', 'Vignesh', 'Vignesh', 'Vignesh', 'Vignesh', 'Vignesh', 'Vignesh', 'Vignesh', 'Vignesh', 'Vignesh')

# Maximum and minimum Function in tuple

a = (1,2,3,4)

print(min(a))
print(max(a))

#output
1
4