
# Python List - List Comprehension

# Create a new list

numbers = [1, 2, 3, 4, 5]

square = [num ** 2 for num in numbers]
print(square)

# Even numbers

even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

# Odd numbers

odd_numbers = [num for num in numbers if num % 2 != 0]
print(odd_numbers)

# Convert to uppercase

fruits = ["apple", "banana", "mango"]

upper_fruits = [fruit.upper() for fruit in fruits]
print(upper_fruits)