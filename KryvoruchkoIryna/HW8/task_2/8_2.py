import re

def validate_password(password):
    if 6 <= len(password) <= 16:
        if re.search("[a-z]", password) and re.search("[A-Z]", password) and re.search("[0-9]", password) and re.search("[$#@]", password):
            return True
    return False

password = input("Enter a password: ")


if validate_password(password):
    print("Password is valid")
else:
    print("Password is not valid")