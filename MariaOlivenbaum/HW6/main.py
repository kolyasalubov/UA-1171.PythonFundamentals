print("***THE FIRST TASK***")

last_number = 10
basic_array = list(range(1, last_number + 1))
print(f"We have a basic array from {basic_array[0]} to {basic_array[-1]}.")

even_numbers = [i for i in basic_array if i % 2 == 0]
print("Even numbers that are divisible by 2:", even_numbers)

odd_numbers = [i for i in basic_array if i % 2 != 0 and i % 3 == 0]
print("Odd numbers that are divisible by 3:", odd_numbers)

prime_numbers = [i for i in basic_array if i % 2 != 0 and i % 3 != 0]
print("Numbers that are not divisible by 2 and 3:", prime_numbers)

# ==========================================

print("\n***THE SECOND TASK***")
LOGIN = "First"
user_login = input("Please enter your login: ")

while(user_login != LOGIN):
    user_login = input("The login isn't correct. Please enter your login one more time: ")
else:
    print(f'\nThe login "{user_login}" is correct. You can enter. Thanks.')
