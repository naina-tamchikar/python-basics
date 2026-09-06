# Tuple Mini Project
# Student Records

students = (
    ("Naina", 20, "BCA"),
    ("Rahul", 21, "BSc"),
    ("Priya", 19, "BCom"),
    ("Amit", 22, "BBA")
)

print("=== Student Records ===\n")

for student in students:
    name, age, course = student

    print("Name  :", name)
    print("Age   :", age)
    print("Course:", course)
    print("-" * 20)

print("Total Students:", len(students))
