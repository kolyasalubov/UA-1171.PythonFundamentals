import re


def pass_validation(password):
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


if pass_validation(input("Enter a password: ")):
    print("Valid password")
else:
    print("Invalid password")
