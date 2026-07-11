

# ==========================================
# String Practice Programs
# ==========================================

# Program 1: Find the length of a string

text = input("Enter a string: ")
print("Length:", len(text))

print("--------------------")

# Program 2: Print first and last character

name = input("Enter your name: ")

print("First Character:", name[0])
print("Last Character:", name[-1])

print("--------------------")

# Program 3: Convert text to uppercase

message = input("Enter a message: ")

print("Uppercase:", message.upper())

print("--------------------")

# Program 4: Check if a word exists

sentence = input("Enter a sentence: ")

print("Python" in sentence)

print("--------------------")

# Program 5: Count a character

word = input("Enter a word: ")

print("Count of 'a':", word.count("a"))
