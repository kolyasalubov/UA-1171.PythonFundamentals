import random

random_num = random.randint(1, 100)
tries = 10

print("I generated a number from 1-100. Try to guess it! :)")
print(random_num)

while tries > 0:
    user_input = int(input("Your guess: "))
    if user_input == random_num:
        print("Congrats! You guessed the number right!")
        break

    elif tries == 1:
        print("You have no tries left...")
        break

    elif user_input != random_num:
        tries -= 1
        if tries >1:
            print(f"Your guess is incorrect... try again! you have {tries} more tries left!")
        else:
            print(f"Be careful! this is your last try!")
        

