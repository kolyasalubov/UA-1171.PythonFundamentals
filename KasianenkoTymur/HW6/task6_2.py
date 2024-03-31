login=['First','Tymur']

answer='yes'
while answer=='yes' or answer=='y':
    who_are_you=str(input('login(login) or new person(new):')) 
    #while who_are_you!='login' or who_are_you!='new':
    #   who_are_you=str(input('"login" or "new":')) 
    if who_are_you=='login':
        while True:
            have_login=False
            user_name=str(input('Enter your login: '))
            for item in login:
                if item==user_name:
                    have_login=True
                    print(f'Welcome back, {user_name}!')
            if have_login==False:
                print('The login is incorrect.')
            if have_login==True:
                break

                

        
    #else:
    #    while True:
    #        have_login=False
    #        user_name=str(input('Enter your new login: '))
    #        for item in login:
    #            while item==user_name:
    #                have_login=True
    #        if have_login==False:        
    #            login.append(user_name)
    #            print(f'Hello, {user_name}.')
    #            break
    #        if have_login==True:
    #            print('Is not new login.')

    answer=input('Do you want to continue?: ')
    answer=answer.lower()