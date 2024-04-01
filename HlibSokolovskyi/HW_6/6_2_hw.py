clear_login = ['F', 'i', 'r', 's', 't']

while True:
    user_input = str(input("Login: "))
    for i in range(5):
        if clear_login[i] != user_input[i]:
            break
        elif clear_login[i] == user_input[i]:
            pass
    if i == 4 :
        print("Access granted.")
        break
    
    print("Wrong login, try again.")