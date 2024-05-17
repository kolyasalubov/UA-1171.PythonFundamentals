## Task1. In the range from 1 to 10 determine
##  even numbers that are divisible by 2,
##  odd numbers, which are divisible by 3,
##  numbers that are not divisible by 2 and 3.
#########################################################################

# even_numbers = []
# odd_numbers_divisible_by_3 = []
# other_numbers = []

# for item in range (1, 10):
#     if item % 2 == 0:
#         even_numbers. append (item)
#     elif item % 3 == 0:
#         odd_numbers_divisible_by_3. append (item)
#     else:
#         other_numbers. append (item)

# print(f"Even numbers: {even_numbers}")
# print(f"Odd numbers divisible by 3: {odd_numbers_divisible_by_3}")
# print(f"Other numbers (not divisible by 2 and 3): {other_numbers}")

########################################################################


### LIST Compehantion###

# l1 = [x for x in range(1, 10) if x % 2 == 0 ]
# l2 = [x for x in range(1, 10) if x% 2 == 1 and x % 3 == 0 ]
# l3 = [x for x in range(1, 10) if not x % 2 == 0 and not x % 3 == 0 ]

# print(l1, 'is even multiple of 2')
# print(l2, 'is an odd multiple of 3')
# print(l3, 'not divisible by 2 and 3')

##########################################################################



# Task2. Write a script that checks the login that the user enters.
# If the login is "First", then greet the users. If the login is different,
# send an error message.(need to use loop while)
# Output maximum from n numbers

# user_name = input('Hello, please input your login: ')

# while user_name != 'First':
#     user_name = input('Error: wrong username, please try one more time. Username: ')
# else:
#     print('Greeting. Access granted!!!', user_name)