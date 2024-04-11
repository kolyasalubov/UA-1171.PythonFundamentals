import random

user_name = input('Hello! What is your name?\n')

number = random.randint(1, 100)

print(f'Well, {user_name}, I am thinking of a number between 1 and 100.')

finish_answer = 'y'

while finish_answer == 'y':
    count_of_attempts = 1
    found = False
    while count_of_attempts <= 10:

        try:
            guess_number = int(input('Take a guess! Enter your number: '))

            if guess_number == number:
                print(f'Good job, {user_name}! You are a winner!')
                found = True
                break

            elif 1 <= guess_number <= 100 and guess_number < number:
                print('Your number is less.')

            elif 1 <= guess_number <= 100 and guess_number > number:
                print('Your number is more.')

            elif not 1 <= guess_number <= 100:
                print(f'Your number is not in the range 1 to 100. Try again:)')

        except ValueError as exception:
            print("Enter only integer numbers please!")

        count_of_attempts += 1

    if not found:
        print('You had only 10 attempts... Game over!')


    finish_answer = input('Do you want to play again? y/n\n')

print('Thank you for game')