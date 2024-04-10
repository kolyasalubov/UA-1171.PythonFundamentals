from areaFunchions import *

while True:
    user_input = input("""which area you want to calcukate:
                    1 - rectangle
                    2 - Triangle
                    3 - Circle 
                    4 - Exit : """)
    if user_input == '4':
        break
    result = get_user_choice(user_input)
    print(result)