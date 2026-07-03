

# ==========================================
# Find and Count Methods in Python Strings
# ==========================================

text = "Python is easy and Python is powerful"

# find() returns the index of the first occurrence
print("Index of Python:", text.find("Python"))

# find() returns -1 if the word is not found
print("Index of Java:", text.find("Java"))

print("--------------------")

# count() returns the number of occurrences
print("Count of Python:", text.count("Python"))
print("Count of is:", text.count("is"))

print("--------------------")

word = "banana"

print("Count of 'a':", word.count("a"))
print("Count of 'n':", word.count("n"))