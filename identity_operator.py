

# ==========================================
# Identity Operators in Python
# ==========================================

# Identity operators check whether two variables
# refer to the same object in memory.

a = [1, 2, 3]
b = a

# Both variables refer to the same object
print("a is b :", a is b)

print("--------------------")

x = [1, 2, 3]
y = [1, 2, 3]

# Values are the same, but objects are different
print("x == y :", x == y)
print("x is y :", x is y)

print("--------------------")

# Using 'is not'

num1 = 10
num2 = 20

print("num1 is not num2 :", num1 is not num2)
