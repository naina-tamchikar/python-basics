
# Python List - Add List Items

fruits = ["Apple", "Banana", "Mango"]

print("Original List:", fruits)

# append() - Add one item at the end

fruits.append("Orange")
print(fruits)

# insert() - Add item at a specific index

fruits.insert(1, "Kiwi")
print(fruits)

# extend() - Add multiple items

more_fruits = ["Grapes", "Pineapple"]

fruits.extend(more_fruits)
print(fruits)

# Add another list using +=

fruits += ["Cherry", "Papaya"]
print(fruits)