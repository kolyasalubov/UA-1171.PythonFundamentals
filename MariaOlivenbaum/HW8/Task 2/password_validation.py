def validation (password):
    flag_upper_letter = False
    flag_low_letter = False
    flag_number = False
    flag_symbol = False

    if len(password) < 6 or len(password) > 16:
        print("Password length should be 6-16 symbols.")
        return False
    else:
        for ch in password:
            if 65 <= ord(ch) <= 90:
                flag_upper_letter = True
            if 97 <= ord(ch) <= 122:
                flag_low_letter = True
            if 48 <= ord(ch) <= 57:
                flag_number = True
            if ch == "$" or ch == "#" or ch == "@":
                flag_symbol = True

        if not flag_upper_letter:
            print("Password must contain at least one uppercase letter.")
            return False

        elif not flag_low_letter:
            print("Password must contain at least one lowercase letter.")
            return False

        elif not flag_number:
            print("Password must contain at least one digit.")
            return False

        elif not flag_symbol:
            print("Password must contain at least one character ($, # or @).")
            return False

        else:
            print("Your password is accepted.")
            return True
