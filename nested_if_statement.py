
# ===========================================
# Nested If Statement in Python
# ===========================================

# A Nested If means an 'if' statement inside
# another 'if' statement.

# Example 1
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("You are allowed to enter.")
    else:
        print("ID Card Required.")

print("-" * 30)

# Example 2
username = "Naina"
password = "1234"

if username == "Naina":
    if password == "1234":
        print("Login Successful.")
    else:
        print("Incorrect Password.")

print("-" * 30)

# Example 3 (User Input)
marks = int(input("Enter your marks: "))

if marks >= 40:
    attendance = int(input("Enter attendance percentage: "))

    if attendance >= 75:
        print("You are eligible for the exam.")
    else:
        print("Attendance is too low.")
else:
    print("You have failed.")