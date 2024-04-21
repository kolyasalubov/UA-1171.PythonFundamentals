def get_week_day():
    try:
        num = int(input("Enter a number from 1-7: "))
        if num > 7 or num < 1:
            raise ValueError("Invalid number\nPlease enter a number from 1-7")
        week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        choice = week_days[num - 1]
        return f"{num} - {choice}."
    except ValueError as error:
        return error


print(get_week_day())