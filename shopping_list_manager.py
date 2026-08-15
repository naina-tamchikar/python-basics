
# Shopping List Manager

shopping_list = []

item1 = input("Enter first item: ")
item2 = input("Enter second item: ")
item3 = input("Enter third item: ")

shopping_list.append(item1)
shopping_list.append(item2)
shopping_list.append(item3)

print("\nShopping List:", shopping_list)

remove_item = input("\nEnter item to remove: ")

if remove_item in shopping_list:
    shopping_list.remove(remove_item)
    print("Item removed successfully.")
else:
    print("Item not found.")

print("\n===== FINAL SHOPPING LIST =====")
print(shopping_list)