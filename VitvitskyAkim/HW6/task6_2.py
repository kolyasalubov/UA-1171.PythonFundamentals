entered_login = None
user_login = input("Enter a new login: ")
print("Hello, dear guest!")
while user_login != entered_login:
    entered_login = input("Please enter your login again: ")
    if entered_login != user_login:
        print("Error: Incorrect login.")
    else:
        print("Welcome,", user_login)