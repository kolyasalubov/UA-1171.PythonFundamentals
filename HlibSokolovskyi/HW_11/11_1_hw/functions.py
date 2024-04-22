def process_age(age):
    if age < 0:
        raise ValueError("The age cannot be negative.")
    if age%2 == 0:
        print(f"Your age {age} is even.")
    else:
        print(f"Your age {age} is odd.")
        