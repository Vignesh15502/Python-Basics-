# Dictionary and its Function

user = {"name" : "ram",
		"age"  : "25",
		"is Married" : True
		}
print(user)
print(type(user))
print(user["name"])
print(user.get("age"))

print(user.keys())
print(user.values())
print(user.items())

#loop method

for x in user:
	print(x,":",user[x])
	
for i in user:
	print(x)
	
for x in user.values():
	print(x)
	
for x in user.keys():
	print(x)
	
for x,y in user.items():
	print(x,y)
	
if "gender" in user:
	print("present")
else:
	print("No")
	
#changing values

user.update(gender = "male")
print(user)

user["age"] = 35
print(user)

user.pop("age")
print(user)

user.clear()
print(user)

	