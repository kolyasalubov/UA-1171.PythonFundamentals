import re

def is_valid_password(password):

    if not 6 <= len(password) <= 10:
        return False
    
    sings = r"(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$])"
    return bool(re.search(sings, password))

        
def main():
    password = input("Enter your password: ")
    if is_valid_password(password):
        print("Voled password!")
    else:
        print("Involed password!")
        print("Minimum 6 characters, maximum 16")
        print("You must have letters from a to z and from A to Z")
        print("You must have special charactes like @, $, #")
        

if __name__ == "__main__":
    main()
    