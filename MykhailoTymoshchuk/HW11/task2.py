week_days = {1: "Mondey" , 2: "Thuesday", 3: "Wednesday", 4: "Thursday", 
             5: "Friday", 6: "Saturday", 7: "Sunday"}


def weekdays():
    
    try:
        input_user = input("Enter a number between 1-7: ")
        if not input_user.isdigit():
            raise TypeError("Only integers and numbers are allowed")
        input_user = int(input_user)
        
        
        # # if input_user not in weekdays():
        # #     raise KeyError("Key doesn't exist")
        # else:
        #     return week_days.get(input_user)
        
        
        if input_user > 7 or input_user < 1:
            raise ValueError ("Invalid number, must be between 1 and 7")
        return week_days.get(input_user)
    
    except ValueError as ve:
        return f"Error: {ve} - input number not in range"
    # except KeyError as ke:
    #     return f"Error: {ke} - input key doesn't exist"
    except TypeError as  te:
        return f"Error: {te} - invalid input. Only numbers are allowed"
        
print(weekdays())