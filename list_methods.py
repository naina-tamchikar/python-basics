
# Python List - List Methods

fruits = ["Apple", "Banana", "Mango", "Banana"]

# len() - Returns the length of the list

print(len(fruits))

# count() - Counts how many times an item appears

print(fruits.count("Banana"))

# index() - Returns the index of an item

print(fruits.index("Mango"))

# sort() - Sorts the list

numbers = [50, 20, 80, 10, 40]

numbers.sort()
print(numbers)

# reverse() - Reverses the list

numbers.reverse()
print(numbers)

# copy() - Creates a copy of the list

new_list = fruits.copy()
print(new_list)
