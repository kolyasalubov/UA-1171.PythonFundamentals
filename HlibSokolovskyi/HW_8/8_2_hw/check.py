import re

def is_valid(password):

    if len(password) > 6 and len(password) < 16:
        if re.search("[a-z]", password):
            if re.search("[A-Z]", password): 
                if re.search("[0-9]", password): 
                    if re.search("[$#@]", password): 
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False