
# Tuple vs List

# List
fruits_list = ["Apple", "Banana", "Mango"]

# Tuple
fruits_tuple = ("Apple", "Banana", "Mango")

print("List:", fruits_list)
print("Tuple:", fruits_tuple)

# List is mutable
fruits_list[1] = "Orange"
print("Updated List:", fruits_list)

# Tuple is immutable
# fruits_tuple[1] = "Orange"   # Error
print("Tuple cannot be modified.")

print()

print("Type of List:", type(fruits_list))
print("Type of Tuple:", type(fruits_tuple))