import decision

""" Program that prompts the user to calculate rectanle,triangle,circle area`s 
    The program will work untill the keyword is entered 'quit' for exit """

while True:
    task = str(input("What we count now? rectangle,triangle,circle or 'quit' to exit: "))

    if task == 'quit':
        print('<3 Goodbye!')
        break

    if task == 'rectangle':
        length = float(input("Write length: "))
        wigth = float(input("Write wight: "))
        area = decision.rectangleArea(length,wigth)
        print("Area of rectangle: ", area)
        
    if task == 'triangle':
        base = float(input("Write base: "))
        height = float(input("Write height: "))
        area = decision.triangleArea(base,height)
        print("Area of triangle: ", area)
        
    if task == 'circle':
        radius = float(input("Write radius: "))
        area = decision.circleArea(radius)
        print("Area of circle: ", area)

    