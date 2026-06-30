

# ==========================================
# String Replace Method in Python
# ==========================================

# replace() method string ke kisi word ya character ko
# dusre word ya character se replace karta hai.

text = "I like tea"

print("Original Text :", text)

# tea ko coffee se replace karna
new_text = text.replace("tea", "coffee")

print("Updated Text  :", new_text)

print("--------------------")

sentence = "Python is easy to learn"

print("Original Sentence :", sentence)

# easy ko powerful se replace karna
updated_sentence = sentence.replace("easy", "powerful")

print("Updated Sentence  :", updated_sentence)

print("--------------------")

# Character replace example

word = "banana"

print("Original Word :", word)

new_word = word.replace("a", "@")

print("Updated Word  :", new_word)