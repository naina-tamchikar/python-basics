
# Student Result Management System

name = input("Enter Student Name: ")

english = float(input("Enter English Marks: "))
math = float(input("Enter Math Marks: "))
science = float(input("Enter Science Marks: "))

total = english + math + science
percentage = total / 3

if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 35:
    grade = "C"
else:
    grade = "Fail"

print("\n===== STUDENT RESULT =====")
print("Name       :", name)
print("Total      :", total)
print("Percentage :", round(percentage, 2), "%")
print("Grade      :", grade)

if percentage >= 35:
    print("Result     : Pass")
else:
    print("Result     : Fail")