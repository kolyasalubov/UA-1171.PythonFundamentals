"""Write a Python program to check the validity of a password (input from users).
Validation:
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16"""

import re

def validate_password(password):
    if len(password) < 6 or len(password) > 16:
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[$#@]", password):
        return False
    
    return True


if validate_password(input("Enter your password: ")):
    print("Your password valid, Welcome")
else:
    print("Your password invalid, try again")