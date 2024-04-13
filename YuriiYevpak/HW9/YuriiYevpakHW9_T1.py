import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 10

    print("Welcome to the Guess the Number game!")
    print("I've picked a number between 1 and 100. Can you guess it in 10 attempts?")

    while attempts > 0:
        guess = int(input("Enter your guess: "))

        if guess == secret_number:
            print("Congratulations! You've guessed the number!")
            return
        elif guess < secret_number:
            print("Incorrect. The secret number is greater than your guess.")
        else:
            print("Incorrect. The secret number is less than your guess.")

        attempts -= 1
        print("Attempts left:", attempts)

    print("You've run out of attempts. The secret number was:", secret_number)

# Launch the game
guess_the_number()