
# ===========================================
# If...Elif...Else Statement in Python
# ===========================================

# The 'if...elif...else' statement is used to
# check multiple conditions. If one condition
# is True, its block is executed.

# Example 1
marks = 75

if marks >= 90:
    print("Grade A+")
elif marks >= 75:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")

print("-" * 30)

# Example 2
number = 0

if number > 0:
    print("Positive Number")
elif number < 0:
    print("Negative Number")
else:
    print("Zero")

print("-" * 30)

# Example 3 (User Input)
age = int(input("Enter your age: "))

if age >= 60:
    print("Senior Citizen")
elif age >= 18:
    print("Adult")
else:
    print("Minor")