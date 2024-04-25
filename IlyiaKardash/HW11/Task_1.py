def get_age():
    try:
        user_inp = int(input("Enter your age: "))
        if user_inp < 0:
            raise ValueError('Not a real age')
        if user_inp % 2 == 0:
            return "Age is even"
        return "Age is odd"
    except ValueError as e:
        return f'{e}. Enter a positive digit.'


print(get_age())
