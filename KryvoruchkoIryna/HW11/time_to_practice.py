# time practice

# def is_even_or_odd():
#     while True:
#         try:
#             number = int(input("Enter an integer: "))
#             if number % 2 == 0:
#                 print(f"{number} is even.")
#             else:
#                 print(f"{number} is odd.")
#             break
#         except ValueError:
#             print("Invalid input. Please enter an integer.")

# is_even_or_odd()

# time practice

# def divide_numbers():
#     while True:
#         try:
#             inputs = input("Enter two numbers separated by a comma (e.g., 4,2): ")
#             num1, num2 = map(float, inputs.split(','))

#             result = num1 / num2
#         except ValueError:
#             print("Invalid input. Please enter two numbers separated by a comma.")
#         except ZeroDivisionError:
#             print("Error: Division by zero!")
#         except Exception as e:
#             print(f"An unexpected error occurred: {e}")
#         else:
#             print(f"The result of {num1} divided by {num2} is {result}")
#             break
#         finally:
#             print("Thank you for using the calculator!")

# divide_numbers()

#

names = ['Sam', 'Don', 'Daniel']
names = list(map(hash, names))
print(names)

#

items = ["red", ["red", "green", "black", "red", "brown", "red", "blue", "red", "red", "yellow"]]
filtered_items = list(filter(lambda x: x == "red", items[1]))
map_items = list(map(lambda x: x == "red", items[1]))
print(filtered_items)
print(map_items)

#1

string_numbers = ['1', '2', '3', '4', '5', '7']
int_numbers = []
for num in string_numbers:
    int_numbers.append(int(num))
print(int_numbers)

#2

string_numbers = ['1', '2', '3', '4', '5', '7']
int_numbers = list(map(int, string_numbers))
print(int_numbers)

#1

def miles_to_kilometers(miles):
    return miles * 1.6

miles_list = [1, 2, 3, 4, 5]
kilometers_list = list(map(miles_to_kilometers, miles_list))
print(kilometers_list)

#2

miles_list = [1, 2, 3, 4, 5]
kilometers_list = list(map(lambda x: x * 1.6, miles_list))
print(kilometers_list)

#################

from functools import reduce

# Sample list
numbers = [3, 7, 2, 8, 6, 5]

# Using reduce to find the maximum value
max_number = reduce(lambda x, y: x if x > y else y, numbers)

print(max_number)

