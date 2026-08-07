
# Python List - Change List Items

fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Original List:", fruits)

# Change a single item

fruits[1] = "Kiwi"
print(fruits)

# Change multiple items

fruits[1:3] = ["Pineapple", "Grapes"]
print(fruits)

# Replace one item with multiple items

fruits[0:1] = ["Strawberry", "Cherry"]
print(fruits)

# Replace multiple items with one item

fruits[0:2] = ["Apple"]
print(fruits)