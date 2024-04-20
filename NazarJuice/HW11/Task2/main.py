def get_day_of_week():
    try:
        num = int(input("Enter a number (1-7): "))
        if num < 1 or num > 7:
            raise ValueError("Invalid input. Please enter a number between 1 and 7.")
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day_of_week = days[num - 1]
        return(f"{num}: {day_of_week}.")
    except ValueError as e:
        return e

print(get_day_of_week())