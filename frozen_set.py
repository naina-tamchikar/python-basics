
# ==========================================
# Frozen Set in Python
# ==========================================

# A frozenset is an immutable version of a set.
# Once created, its elements cannot be changed.

numbers = frozenset({10, 20, 30, 40})

print("Frozen set :", numbers)

print("--------------------")

# We can check whether an element exists

print("20 in numbers :", 20 in numbers)

print("--------------------")

# We cannot add or remove elements from a frozenset
# numbers.add(50)       # AttributeError
# numbers.remove(20)    # AttributeError

print("Frozenset cannot be modified.")

print("--------------------")

# Frozensets support set operations

set1 = frozenset({1, 2, 3})
set2 = frozenset({3, 4, 5})

print("Union :", set1 | set2)
print("Intersection :", set1 & set2)
print("Difference :", set1 - set2)