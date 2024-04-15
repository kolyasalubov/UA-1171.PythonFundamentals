from random import randint

""" Program would ask user to guess the guessed number in range 1 - 100 for 10 tries
    Some key condition for less or greeter number.And for the num that not in range.
    While - will be perform untill the user guessed number or user exhausted tries """

triesValue = 0

guessedNumber = randint(1,100)

while triesValue  < 10:
    triesValue += 1
    userNumber = int(input("Hi, u have 10 triese to guess the number from 1 to 100 what I guessed.Good luck <3: "))
        
    if userNumber == guessedNumber:
        print("You win, lucker :).You will try again?)")
        break
    elif userNumber > guessedNumber:
        print("Your number is greeter")
    elif userNumber < guessedNumber:
        print("Your number is less")
    elif userNumber < 1 or userNumber > 100:
        print("Your numbe out of stock. Try more :)")
            
    else:
        print("Tries exhausted")
            