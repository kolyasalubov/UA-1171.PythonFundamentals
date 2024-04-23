def your_day():
    while True:
        try:
            day = int(input("Enter your day (1-7): "))
            if 1 <= day <= 7:
                day_input = user_day(day)
                print(day_input)
                break
            else:
                print("There are only 7 days in a week! Enter a number from 1-7")
        except ValueError:
            print("You should enter only a number")

def user_day(day):
    if day == 1:
        return "Your day is Monday"
    elif day == 2:
        return "Your day is Tuesday"
    elif day == 3:
        return "Your day is Wednesday"
    elif day == 4:
        return "Your day is Tuesday"
    elif day == 5:
        return "Your day is Friday"
    elif day == 6:
        return "Your day is Saturday"
    elif day == 7:
        return "Your day is Sunday"

your_day()