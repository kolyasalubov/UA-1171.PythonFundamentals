from random import randint

number_of_tries = 0

while number_of_tries < 10:
    rand_number = randint(1, 100)
    number_of_tries += 1
    user_input = int(input("Enter your number: "))
    if user_input <= 0:
        print('Invalid number. Try positive ones.')
    elif user_input > rand_number:
        print('Your number is greater.')
    elif user_input < rand_number:
        print('Your number is smaller.')
    else:
        user_input == rand_number
        print('Congrats! You guessed the number!')
else:
    print('You\'ve run out of tries.')
