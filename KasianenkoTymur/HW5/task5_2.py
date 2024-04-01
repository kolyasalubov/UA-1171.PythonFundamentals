answer='yes'
while answer=='yes' or answer=='y':
    amount=int(input('Enter the number to print the Fibanacci numbers: '))

    for i in range(amount):
        number_Fibanacci=((((1+5**(0.5))/2)**i)-(((1-5**(0.5))/2)**i))/5**(0.5)

        print(int(number_Fibanacci), end=' ')
    else: 
        print()
    answer=input('Do you want to continue?: ')
    answer=answer.lower()