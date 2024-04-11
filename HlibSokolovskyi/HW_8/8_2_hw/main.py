import check

password = str(input("Check the validity of password: "))

if check.is_valid(password):
    print("\nThe passsword is valid!\n")
else:
    print("\nInvalid password.\n")
