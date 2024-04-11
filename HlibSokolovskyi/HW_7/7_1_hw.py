def is_largest(value_1, value_2):
    """
    
    Takes two different numbers, compares them 
    and returns the largest one.
    
    value_1: float, the first taken number.
    value_2: float, the second taken number.
    
    Return:
    The largest of the two input numbers.
    
    """
    
    if value_1 > value_2:
        return value_1
    else:
        return value_2


while True:
    first = float(input("Enter two different values: \n"))
    second = float(input())

    if first == second:
        print(f"Values are same! Enter different to exit the program. \n")
    else:
        print(f"The largest value of {first} and {second} is {is_largest(first, second)}")
        break

