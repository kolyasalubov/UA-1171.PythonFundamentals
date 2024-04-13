def largest_number(num1, num2)->int:
    """
    function: largest_number()
    input: number_1, number_2, 
    type: int
    output: the largest number. 
    """
    if num1 > num2:
        print(f'Number largest is {num1}.')
    elif num1 < num2:
        print(f'Number largest is {num2}.')
    else:
        print('they are equal.')
    
number_1=input('nubmer 1: ')
number_2=input('number 2: ')
    
largest_number(number_1, number_2)
