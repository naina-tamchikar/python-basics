

# ==========================================
# String Indexing in Python
# ==========================================

# Indexing ka matlab:
# String ke har character ki position (index) hoti hai.
# Index 0 se start hota hai.

name = "Naina"

# Positive Indexing
print("First character :", name[0])   # N
print("Second character:", name[1])   # a
print("Third character :", name[2])   # i

print("--------------------")

# Negative Indexing
# Last character se counting -1 se start hoti hai.

print("Last character        :", name[-1])  # a
print("Second last character :", name[-2])  # n
print("Third last character  :", name[-3])  # i

print("--------------------")

# Index ki help se kisi specific character ko access kar sakte hain.

city = "Mumbai"

print("First letter of city :", city[0])
print("Last letter of city  :", city[-1])
