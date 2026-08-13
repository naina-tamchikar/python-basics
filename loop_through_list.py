
# Python List - Loop Through List

fruits = ["Apple", "Banana", "Mango", "Orange"]

# Using for loop

for fruit in fruits:
    print(fruit)

print()

# Using range() and len()

for i in range(len(fruits)):
    print(fruits[i])

print()

# Using while loop

i = 0

while i < len(fruits):
    print(fruits[i])
    i += 1