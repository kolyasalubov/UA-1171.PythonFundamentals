import re

def is_valid_password(password):
    if len(password) < 6 or len(password) > 16:
        return False
    if not re.search("[a-z]", password) or not re.search("[A-Z]", password) or not re.search("[0-9]", password):
        return False
    if not re.search("[$#@!]", password):
        return False
    return True


password = is_valid_password(input('Enter the password: '))
if password:
    print('GOOD PASSWORD')
else:
    print('BAD PASSWORD')