name = "penguin"
age = "15"
is_student = True
weight = 18.5 

print("Name:", name)
print("Data type of Name is", type(name))
print("Age:", age)
print("Data Type of age is", type(age))
print("is_student:", is_student)
print("Data Type of is_student", (is_student))
print("weight:", weight)
print("Data Type of weight is", type(weight))

print("\n After Type Casting....")
age = str(age)
print(age)
print("Data Type of age is", type(age))
weight = int(weight)
print(weight)
print("Data Type of weight is", type(weight))