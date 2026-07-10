

# ==========================================
# Split and Join Methods in Python Strings
# ==========================================

# split() converts a string into a list

sentence = "Python is easy to learn"

words = sentence.split()

print("Original Sentence:", sentence)
print("After split():", words)

print("--------------------")

# Splitting using a specific character

data = "Apple,Mango,Banana,Grapes"

fruits = data.split(",")

print("Original Data:", data)
print("After split():", fruits)

print("--------------------")

# join() combines list items into a string

languages = ["Python", "Java", "C++"]

result = " - ".join(languages)

print("Languages List:", languages)
print("After join():", result)

print("--------------------")

names = ["Naina", "Rahul", "Aman"]

combined_names = ", ".join(names)

print("Combined Names:", combined_names)
