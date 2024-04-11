import re
"""Import module 're'
    Writing a validator to checks if all condition True or False"""
def passwordValidator(password):
    return bool(re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,16}$",password))