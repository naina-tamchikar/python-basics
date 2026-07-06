

# ==========================================
# Strip Method in Python Strings
# ==========================================

# strip() removes extra spaces from the beginning
# and end of a string.

text = "   Hello World   "

print("Original Text:")
print(text)

print("--------------------")

# Remove spaces from both sides
clean_text = text.strip()

print("After strip():")
print(clean_text)

print("--------------------")

# Remove spaces from the left side
left_clean = text.lstrip()

print("After lstrip():")
print(left_clean)

print("--------------------")

# Remove spaces from the right side
right_clean = text.rstrip()

print("After rstrip():")
print(right_clean)

print("--------------------")

name = "   Naina   "

print("Original Name:", name)
print("Clean Name:", name.strip())
