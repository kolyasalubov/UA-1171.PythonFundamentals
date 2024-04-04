"""7.1"""

# def maxValue(number1, number2):
#     """
#     function maxValue ()
#     Parameters:
#     argument 1 => number1 (int)
#     argument 2 => number2 (int)

#     Returns:
#     Max value of two integers, type: int
#     """
#     if int(number1) > int(number2):
#         return int(number1)
#     else:
#         return int(number2)


# print(maxValue(10.7, 20.8))

"""7.2"""


def areaRectangle(width, height):
    area = int(width) * int(height)
    return area


def areaTriangle(base, height):
    area = 1/2 * base * height
    return area


def areaCircle(radius):
    PI = 3.14
    area = PI * radius ** 2
    return area


print("Calculate the area of following shapes: \n"
      "1. Rectangle \n"
      "2. Triangle \n"
      "3. Circle \n")

user_choice = input("Select the function: ")

if user_choice == "1":
    width = int(input("Enter width: "))
    height = int(input("Enter height: "))
    print(f'Area of a rectangle is {int(areaRectangle(width, height))}')

elif user_choice == "2":
    base = int(input("Enter base: "))
    height = int(input("Enter height: "))
    print(f'Area of a triangle is {int(areaTriangle(base, height))}')

elif user_choice == "3":
    radius = int(input("Enter radius: "))
    print(f'Area of a circle is {int(areaCircle(radius))}')
else:
    print("Invalid number")


"""7.3"""

# str1 = "hello"


# def numbofcharact(str1):
#     char_count = dict.fromkeys(str1, 0)
#     for i in str1:
#         char_count[i] += 1
#     return char_count


# print(numbofcharact(str1))
