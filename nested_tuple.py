
# Nested Tuple

students = (
    ("Naina", 20, "BCA"),
    ("Rahul", 21, "BSc"),
    ("Priya", 19, "BCom")
)

# Print complete tuple
print("Students:", students)

print()

# Access first student's details
print("First Student:", students[0])

# Access second student's name
print("Second Student Name:", students[1][0])

# Access third student's course
print("Third Student Course:", students[2][2])

print()

# Loop through nested tuple
for student in students:
    print(student)