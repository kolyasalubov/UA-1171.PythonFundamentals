while True:
    login = input("Enter login: ")
    if login == "First":
        print("Hello, user!")
        break
    else:
        print("Error: invalid login")
        continue