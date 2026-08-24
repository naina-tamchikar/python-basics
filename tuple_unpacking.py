
# Tuple Packing and Unpacking

# Packing
student = ("Naina", 20, "BCA")
print("Packed Tuple:", student)

# Unpacking
name, age, course = student

print("Name:", name)
print("Age:", age)
print("Course:", course)

print()

# Unpacking with *
numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print("First:", first)
print("Middle:", middle)
print("Last:", last)