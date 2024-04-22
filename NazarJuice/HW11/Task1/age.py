def check_age():
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise ValueError("age can not be negative")
        return "your age is even" if age % 2 == 0 else "your age is odd"
    except ValueError as e:
        return e