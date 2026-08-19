
# Tuple Slicing

fruits = ("Apple", "Banana", "Mango", "Orange", "Grapes", "Pineapple")

# Basic Slicing
print("First Three Fruits:", fruits[0:3])
print("Last Three Fruits:", fruits[3:6])

# Slicing from Beginning
print("First Four Fruits:", fruits[:4])

# Slicing to End
print("From Third Fruit:", fruits[2:])

# Negative Slicing
print("Last Two Fruits:", fruits[-2:])
print("Except Last Fruit:", fruits[:-1])

# Step Slicing
print("Every Second Fruit:", fruits[::2])
print("Reverse Tuple:", fruits[::-1])