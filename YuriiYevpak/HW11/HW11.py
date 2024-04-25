# Task 1
def check_age():
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise ValueError("Age cannot be negative")
        
        if age % 2 == 0:
            print("Your age is even.")
        else:
            print("Your age is odd.")
    
    except ValueError as ve:
        print("Error:", ve)

if __name__ == "__main__":
    check_age()



# Task 2
def get_day_of_week(number):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if number < 1 or number > 7:
        return "Invalid input. Please enter a number between 1 and 7."
    else:
        return days[number - 1]

def main():
    while True:
        user_input = input("Enter a number (1-7) corresponding to the day of the week: ")
        if user_input.isdigit():
            number = int(user_input)
            print(get_day_of_week(number))
            break
        else:
            print("Invalid input. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()