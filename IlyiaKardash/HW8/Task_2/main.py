import pass_check

password = str(input("Check the validity of password: "))

if pass_check.is_valid(password):
    print("Pass is valid")
else:
    print("Invalid pass")
