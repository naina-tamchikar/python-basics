
# ==========================================
# Set Methods in Python
# ==========================================

numbers = {10, 20, 30}

print("Original set :", numbers)

print("--------------------")

# add() - adds an element

numbers.add(40)
print("After add() :", numbers)

print("--------------------")

# update() - adds multiple elements

numbers.update([50, 60])
print("After update() :", numbers)

print("--------------------")

# remove() - removes a specific element

numbers.remove(20)
print("After remove() :", numbers)

print("--------------------")

# discard() - removes an element without an error
# if the element does not exist

numbers.discard(100)
print("After discard() :", numbers)

print("--------------------")

# copy() - creates a copy of the set

new_numbers = numbers.copy()

print("Copied set :", new_numbers)