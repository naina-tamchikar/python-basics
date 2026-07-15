
# ===========================================
# If...Else Statement in Python
# ===========================================

# The 'if...else' statement is used to execute
# one block of code if the condition is True,
# and another block if the condition is False.

# Example 1
age = 16

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

print("-" * 30)

# Example 2
number = 9

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

print("-" * 30)

# Example 3 (User Input)
marks = int(input("Enter your marks: "))

if marks >= 40:
    print("Congratulations! You Passed.")
else:
    print("Sorry! You Failed.")