def get_day_of_week(day):
    match day.lower():
        case "monday":
            return 1
        case "tuesday":
            return 2
        case "wednesday":
            return 3
        case "thursday":
            return 4
        case "friday":
            return 5
        case "saturday":
            return 6
        case "sunday":
            return 7
        case _:
            raise ValueError("invalid day")
        
try:
    print(get_day_of_week(input("enter day: ")))
except Exception as e:
    print(f"Error: {e}")