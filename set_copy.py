
# ==========================================
# Copying Sets in Python
# ==========================================

# copy() creates a new set with the same elements.

numbers = {10, 20, 30, 40}

copied_set = numbers.copy()

print("Original set :", numbers)
print("Copied set :", copied_set)

print("--------------------")

# Changes made to the copied set
# do not affect the original set.

copied_set.add(50)

print("Original set :", numbers)
print("Copied set :", copied_set)

print("--------------------")

# copy() creates a separate set object

print("numbers is copied_set :", numbers is copied_set)
print("numbers == copied_set :", numbers == copied_set)