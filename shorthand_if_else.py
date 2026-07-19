
# ===========================================
# Shorthand If...Else (Ternary Operator)
# ===========================================

# Shorthand If...Else is used to write
# an 'if...else' statement in a single line.

# Syntax:
# value_if_true if condition else value_if_false

# Example 1
age = 20

message = "Eligible to vote" if age >= 18 else "Not eligible to vote"
print(message)

print("-" * 30)

# Example 2
number = 7

result = "Even Number" if number % 2 == 0 else "Odd Number"
print(result)

print("-" * 30)

# Example 3 (User Input)
marks = int(input("Enter your marks: "))

status = "Pass" if marks >= 40 else "Fail"
print(status)