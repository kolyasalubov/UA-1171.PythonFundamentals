#1st version password validation

import re 

""" Simple but long version to validate password """

def passChecker(password):
    
    if len(password) < 6 or len(password) > 16:
        return False
    if not re.search("[a-z]",password):
        return False
    if not re.search("[A-Z]",password):
        return False
    if not re.search("[0-9]",password):
        return False
    if not re.search("[$#@_]",password):
        return False
    return True
    
password = input("Write your password: ")

if passChecker(password):
    print("Welcome")
else:
    print("Wrong password")