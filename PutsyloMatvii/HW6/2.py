flag = True
while flag:
    login = input('login: ')
    if login == 'First':
        print(f'Congratulate {login}')
        flag = False
    else:
        print('Error, bad login')
