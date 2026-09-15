
# ==========================================
# Set Operations in Python
# ==========================================

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union - combines elements from both sets

print("Union :", set1 | set2)

print("--------------------")

# Intersection - returns common elements

print("Intersection :", set1 & set2)

print("--------------------")

# Difference - elements present in set1 but not in set2

print("Difference :", set1 - set2)

print("--------------------")

# Symmetric Difference - elements that are not common

print("Symmetric Difference :", set1 ^ set2)