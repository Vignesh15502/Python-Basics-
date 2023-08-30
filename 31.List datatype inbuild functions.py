#list datatype inbuild functions

a= [10,25,35,45]
print(a)
a.clear()
print(a)
a= [10,25,35,45]
b= a.copy()
print(b)
a=[10,25,35,45,25,4,25]
print(a.count(25))
print(a.index(25))
print(len(a))
print(max(a))
print(min(a))
print(a)
a.pop[0]
print(a)
a.remove(25)
print(a)

'''
outputs

[10, 25, 35, 45]
[]
[10, 25, 35, 45]
3
1
7
45
4
[10, 25, 35, 45, 25, 4, 25]
[25, 35, 45, 25, 4, 25]
[35, 45, 25, 4, 25]
'''