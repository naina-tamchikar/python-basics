
# Tuple Looping

fruits = ("Apple", "Banana", "Mango", "Orange")

# Using for loop
print("Using for loop:")
for fruit in fruits:
    print(fruit)

print()

# Using for loop with index
print("Using for loop with index:")
for index in range(len(fruits)):
    print(index, ":", fruits[index])

print()

# Using while loop
print("Using while loop:")
index = 0

while index < len(fruits):
    print(fruits[index])
    index += 1