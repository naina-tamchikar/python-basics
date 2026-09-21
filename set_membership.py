
# ==========================================
# Membership Operators with Sets
# ==========================================

numbers = {10, 20, 30, 40, 50}

# 'in' checks whether an element exists in the set

print("20 in numbers :", 20 in numbers)
print("60 in numbers :", 60 in numbers)

print("--------------------")

# 'not in' checks whether an element does not exist

print("60 not in numbers :", 60 not in numbers)
print("30 not in numbers :", 30 not in numbers)

print("--------------------")

# Membership operators are useful for checking
# whether a value is present before performing an operation

if 40 in numbers:
    print("40 is present in the set")