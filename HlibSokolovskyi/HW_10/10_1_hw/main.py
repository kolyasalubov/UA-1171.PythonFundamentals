from classes import *

# I could just leave 5 lines with rect1, but I want to expand this script in future 
# so its functionality will be larger

while True: 
    figure = str(input("What type of polygon you want to input? \nRectangle - 1\n"))
    match figure:
        case "1": 
            rect1 = Rectangle()
            rect1.inputSides()
            rect1.dispSides()
            rect1.rect_area()
            rect1.perimeter()
        case _ :
            print("\nExpected another input.\n")
    choice = str(input("Want to try once more? Y/N:  "))
    if choice == 'y' or choice == 'Y':
        pass
    else:
        break
        
