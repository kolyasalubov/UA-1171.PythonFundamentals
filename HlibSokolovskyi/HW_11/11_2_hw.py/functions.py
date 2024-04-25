def number_analyze(number):
    if not str(number).isnumeric():
        raise ValueError("Non-numerical values are not accepted.")
    number = int(number)
    if number > 7 or number < 1:
        raise ValueError("The number has to be greater than 0 and less than 8.")
    
    
    match number:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:
            print("Error.")