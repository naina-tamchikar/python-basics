
# Python List - Practice Program

# Program 1: Create a list

fruits = ["Apple", "Banana", "Mango"]
print(fruits)

# Program 2: Add a new item

fruits.append("Orange")
print(fruits)

# Program 3: Remove an item

fruits.remove("Banana")
print(fruits)

# Program 4: Change an item

fruits[1] = "Kiwi"
print(fruits)

# Program 5: Find the length

print(len(fruits))

# Program 6: Check item exists

if "Apple" in fruits:
    print("Apple Found")
else:
    print("Apple Not Found")

# Program 7: Sort the list

numbers = [50, 10, 40, 20, 30]
numbers.sort()
print(numbers)

# Program 8: Reverse the list

numbers.reverse()
print(numbers)

# Program 9: Loop through the list

for item in fruits:
    print(item)

# Program 10: Copy the list

new_list = fruits.copy()
print(new_list)