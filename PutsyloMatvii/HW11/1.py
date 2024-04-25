def check_age():
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise ValueError("Not real age")
        if age % 2 == 0:
            return "Your age is even"
        else:
            return "Your age is odd"
    except ValueError as error:
        return error


print(check_age())