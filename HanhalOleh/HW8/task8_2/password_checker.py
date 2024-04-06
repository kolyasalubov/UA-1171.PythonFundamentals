def password_checker(password):
    a_z = ['a','b','c','d','e','f','g','j','k','i','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    A_Z = ['A','B','C','D','E','F','G','J','K','I','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numbers09 = ['0','1','2','3','4','5','6','7','8','9']
    spec_symbols = ['$','#','@']

    a_z_check = False
    A_Z_check = False
    numbers_check = False
    spec_symbols_check = False
    for elem in password:
        if elem in a_z:
            a_z_check = True
        if elem in A_Z:
            A_Z_check = True
        if elem in numbers09:
            numbers_check = True
        if elem in spec_symbols:
            spec_symbols_check = True
    
    if a_z_check == True and A_Z_check == True and numbers_check == True and spec_symbols_check == True and 6 < len(password) < 16:
        print("Your password is valid!")

    if a_z_check == False:
        print("Password must contain at least 1 letter between a-z")

    if A_Z_check == False:
        print("Password must contain at least 1 letter between A-Z")

    if numbers_check == False:
        print("Password must contain at least number between 0-9")

    if spec_symbols_check == False:
        print("Password must contain at least 1 character from #, @, or $")

    if len(password) < 6:
        print("Minimum length is 6 characters")

    if len(password) > 16:
        print("Maximum length is 16 characters")