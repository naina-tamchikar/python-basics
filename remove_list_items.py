
# Python List - Remove List Items

fruits = ["Apple", "Banana", "Mango", "Orange", "Kiwi"]

print("Original List:", fruits)

# remove() - Remove by value

fruits.remove("Banana")
print(fruits)

# pop() - Remove last item

fruits.pop()
print(fruits)

# pop(index) - Remove item by index

fruits.pop(1)
print(fruits)

# del - Delete an item

del fruits[0]
print(fruits)

# clear() - Remove all items

fruits.clear()
print(fruits)