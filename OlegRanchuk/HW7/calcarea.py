def calc_rec(length, width):
    return length * width 

def calc_circ(radius):
    pi = 3.14
    return pi * radius * radius 

def calc_trian(height, base):
    return 0.5 * height * base

def figure():
    while True:
        print("Select figure: ")
        print("1. Rectangle")
        print("2. Circle")
        print("3. Triangle")

        choise = input("Enter your choise: ")

        if choise == "1":
            length = float(input("Enter your lenght: "))
            width = float (input("Enter your width: "))
            area = calc_rec(length, width)
            print(f"Area of rectangle: {area}")
            break

        elif choise == "2":
            radius = float(input("Enter your radius: "))
            area = calc_circ(radius)
            print(f"Area of circle {area}")
            break

        elif choise == "3":
            height = float(input("Enter your height:"))
            base = float(input("Enter your base: "))
            area = calc_trian(height, base)
            print(f"Area of trangle {area}")
            break
        else:
            print("Error choise correct number")   
if __name__ == "__main__":
  figure()       

