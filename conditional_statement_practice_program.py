
# ===========================================
# Conditional Statement Practice Programs
# ===========================================

# Program 1: Check Even or Odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

print("--------------------------")


# Program 2: Check Voting Eligibility

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible")

print("--------------------------")


# Program 3: Find Greatest Number

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Greatest:", a)
else:
    print("Greatest:", b)

print("--------------------------")


# Program 4: Grade Calculator

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

print("--------------------------")


# Program 5: Positive, Negative or Zero

number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

print("--------------------------")


# Program 6: Check Password

password = input("Enter Password: ")

if password == "python123":
    print("Login Successful")
else:
    print("Wrong Password")

print("--------------------------")


# Program 7: Largest of Three Numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)

print("--------------------------")