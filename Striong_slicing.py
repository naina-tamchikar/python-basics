

# ==========================================
# String Slicing in Python
# ==========================================

# Slicing ka use string ka kuch specific part nikalne ke liye hota hai.

name = "Naina"

print("Original String:", name)

# Index 0 se 2 tak (3 include nahi hoga)
print("First Part:", name[0:3])

# Index 1 se 3 tak
print("Middle Part:", name[1:4])

# Starting se index 3 tak
print("From Start:", name[:4])

# Index 2 se end tak
print("Till End:", name[2:])

print("--------------------")

city = "Mumbai"

# First 3 letters
print("First 3 Letters:", city[:3])

# Last 3 letters
print("Last 3 Letters:", city[-3:])

# Complete string copy
print("Full String:", city[:])
