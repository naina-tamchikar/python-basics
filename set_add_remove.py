
# ==========================================
# Adding and Removing Elements from a Set
# ==========================================

numbers = {10, 20, 30}

print("Original set :", numbers)

print("--------------------")

# add() adds a single element to the set

numbers.add(40)

print("After adding 40 :", numbers)

print("--------------------")

# remove() removes a specific element
# It gives an error if the element does not exist.

numbers.remove(20)

print("After removing 20 :", numbers)

print("--------------------")

# discard() also removes an element
# It does not give an error if the element does not exist.

numbers.discard(50)

print("After discard(50) :", numbers)

print("--------------------")

# pop() removes and returns an arbitrary element

removed_element = numbers.pop()

print("Removed element :", removed_element)
print("Set after pop() :", numbers)

print("--------------------")

# clear() removes all elements from the set

numbers.clear()

print("After clear() :", numbers)