import random

random_number = random.randint(1, 100)

tries = 0

while True: 
    tries+=1
    user_number = int(input("Guess the integer number in range 1-100:  "))
    
    if user_number == random_number:
        print(f"\nCongratulations, you guessed the number - {random_number}! Number of tries: {tries}.\n")
        break
    elif user_number > random_number:
        print(f"\nYour number is greater. Tries left: {10-tries}.\n")
    else: 
        print(f"\nYour number is less. Tries left: {10-tries}.\n")

    if tries==10:
        print(f"\nUnfortunately, you used all tries: {tries}. The number you didn't guess: {random_number}.\n")
        break




