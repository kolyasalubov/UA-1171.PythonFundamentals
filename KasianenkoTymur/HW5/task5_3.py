answer='yes'
while answer=='yes' or answer=='y':
    number=int(input('Enter number:'))

    factorial=1
    for i in range(number):
        if number==1 or number==0:
            break
        else:
            factorial*=number-i

    print(f'Factorial of {number} : {factorial}')

    answer=input('Do you want to continue?: ')
    answer=answer.lower()