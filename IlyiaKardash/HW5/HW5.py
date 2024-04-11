"""5.1"""


# num_list = [2, 11, 90, 88, 20, 74, 91, 3, 5]
# new_num_list = []

# for item in num_list:
#     new_num_list.append(float(item))
# else:
#     f'Invalid data'

# new_num_list.sort()
# print(new_num_list)


"""5.2"""

# user_input = int(input("Enter your number: "))

# s1 = 0
# s2 = 1

# if user_input <= s1:
#     print("Invalid number. Try again")
# else:
#     print("Fibonacci sequence:")
#     for item in range(user_input):
#         print(s1)
#         s3 = s1 + s2
#         s1 = s2
#         s2 = s3


"""5.3"""


user_input = int(input("Enter your number: "))

if user_input in range(2):
    print("Factorial for 0 or 1 is 1")
elif user_input < 0:
    print("Invalid number")
else:
    a1 = 1
    for item in range(a1, user_input+1):
        a1 *= item
    print(f'Factorial for {user_input} is {a1}')
