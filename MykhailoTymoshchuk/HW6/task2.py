userInput = input("Login: ")

while userInput != "First":
    userInput = input("Error: wrong username.Try more: ")
else:
    print("Greeting!", userInput)
