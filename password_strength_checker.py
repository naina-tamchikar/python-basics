
# Password Strength Checker

password = input("Enter your password: ")

if len(password) < 6:
    print("Password Strength : Weak")

elif len(password) <= 10:
    print("Password Strength : Medium")

else:
    print("Password Strength : Strong")

if " " in password:
    print("Password should not contain spaces.")
else:
    print("Password accepted.")