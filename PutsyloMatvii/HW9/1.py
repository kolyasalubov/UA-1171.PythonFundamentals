import random

random_number = random.randint(1,100)
tries = 10
while tries != 0:
    inp = int(input('Enter number from 1 to 100: '))
    if random_number == inp:
        print('You win')
        break
    elif inp > random_number:
        print('The number is less')
    elif inp < random_number:
        print('The number is greater')
    tries -= 1
else:
    print('You lose')