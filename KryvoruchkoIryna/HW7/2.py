# 1

# def greeting_for_user(name):
#     if name == "Johnny":
#         return "I love you!"
#     else:
#         return "Hello my friend!"

# input_name = input("What is your name? ")
# print(greeting_for_user(input_name))

# 2

# def round_num(first, sec):
#     distance = round((first - sec), 2)
#     if distance > 0:
#         return distance
#     elif distance < 0:
#         return -distance
#     else:
#         return 0

# num1 = float(input("First number: "))
# num2 = float(input("Second number: "))
# print(f"Distance between numbers: {round_num(num1, num2)}")

# 3

# def str_capit(str):
#     final_str = ' '.join(str.split())
#     return final_str.capitalize()
#
#
# input_string = input("Enter string: ")
# print(str_capit(input_string))

# 4

# def convert_to_str(value):
#     return str(value)
#
# num1 = 123
# num2 = 999
# num3 = -69123
#
# print(convert_to_str(num1))
# print(convert_to_str(num2))
# print(convert_to_str(num3))

#5

# def reverse_words(input_string):
#     words = input_string.split()
#     reversed_words = ' '.join(reversed(words))
#     return reversed_words
#
# input_string = input("Enter string: ")
# print(reverse_words(input_string))

# 6

# def reverse_list(li):
#     return li[::-1]
#
# input_list = [1, 2, 3, 4, 5]
# print(reverse_list(input_list))

# 7

# def res_sum(value):
#     number_list = []
#
#     if input_num < 0:
#         return 0
#     else:
#         for i in range(value):
#             if i % 3 == 0 or i % 5 == 0:
#                 number_list.append(i)
#
#         return sum(number_list)
#
# input_num = int(input('Enter number: '))
# print(res_sum(input_num))

# 8

# def can_reach_gas(distance_to_pump, fuel_left, fuel_expense):
#     max_distance = fuel_left * fuel_expense
#     return max_distance >= distance_to_pump
#
# distance_to_pump = 50
# fuel_left = 2
# fuel_expense = 25
# print(can_reach_gas(distance_to_pump, fuel_left, fuel_expense))

# 9

# def winner(name):
#     if name[0].lower() == 'r':
#         return name + " plays banjo"
#     else:
#         return name + " does not play banjo"
#
# # Example
# input_name = input("What is your name? ")
# print(winner(input_name))

# 10

# def bool_word(word):
#     if word == 'True':
#         return 'Yes'
#     else:
#         return 'No'
#
# input_value = 'True'
# print(bool_word(input_value))

# 11

# def count_sheeps(array):
#     sum = 0
#     for sheep in array:
#         if sheep:
#             sum += 1
#     return sum
#
# # Example
# sheep_array = [
#     True, True, True, False,
#     True, True, True, True,
#     True, False, True, False,
#     True, False, False, True,
#     True, True, True, True,
#     False, False, True, True
# ]
# print(count_sheeps(sheep_array))

# 12

def correct_tail(body, tail):
    return body[-1] == tail

# Examples
print(correct_tail("table", "e"))
print(correct_tail("chair", "k"))
print(correct_tail("flat", "t"))