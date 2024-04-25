def check_age():
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise ValueError("Age cannot be negative")
        if age % 2 == 0:
            print("Your age is even.")
        else:
            print("Your age is odd.")
    except ValueError as e:
        print(e)

check_age()

##############################

def get_day_of_week(number):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    if 1 <= number <= 7:
        return days[number - 1]
    else:
        return "Invalid input. Please enter a number between 1 and 7."

while True:
    user_input = input("Enter a number to get the corresponding day of the week: ")
    try:
        number = int(user_input)
        print(get_day_of_week(number))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")