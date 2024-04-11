from random import randint

number_of_tries = 0
rand_number = randint(1, 100)

while number_of_tries < 10:
    number_of_tries += 1
    user_input = int(input("Enter your number: "))
    if user_input not in range(1, 101):
        print('Invalid number. Try numbers in a range from 1 to 100 only')
    elif user_input > rand_number:
        print('Your number is greater.')
    elif user_input < rand_number:
        print('Your number is smaller.')
    else:
        user_input == rand_number
        print('Congrats! You guessed the number!')
        break
else:
    print('You\'ve run out of tries.')
