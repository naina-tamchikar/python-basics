
# ==========================================
# Accessing Elements in a Set
# ==========================================

# Sets are unordered collections.
# Therefore, elements cannot be accessed using an index.

numbers = {10, 20, 30, 40}

# We cannot use indexing with sets
# print(numbers[0])   # TypeError

print("Set :", numbers)

print("--------------------")

# We can access set elements using a for loop

for number in numbers:
    print("Element :", number)

print("--------------------")

# Checking whether an element exists in a set

print("20 in set :", 20 in numbers)
print("50 in set :", 50 in numbers)
