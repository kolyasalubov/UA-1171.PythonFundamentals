days_of_week = {1: "Monday", 2: "Tuesday", 3: "Wednesday",
                4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}


def weekday():
    user_inp = int(input("Enter a number: "))
    try:
        if user_inp > 7 or user_inp <= 0:
            raise ValueError('Enter a number between 1 and 7 only')
        if user_inp in days_of_week:
            return days_of_week.get(user_inp)
    except ValueError as e:
        return f'Error. {e}'


print(weekday())
