from random import randint

tries = 0
game_numbers = (1, 100)

while tries < 10:
    tries += 1
    user_number = input("Enter your number: ")
    if user_number not in range(1, 100):
        print("Your number is incorrect!")
    elif user_number > game_numbers:
        print("Your number is bigger!")
    elif user_number < game_numbers:
        print("Your number is smaller!")
        break

         