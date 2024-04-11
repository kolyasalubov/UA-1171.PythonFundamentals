def largestNumber(num1:float, num2:float):
    """returns the largest number of two numbers

    Args:
        num1 type(float)
        num2 type(float)
    """
    if num1 == num2:
        return "numbers are equal"
    elif num1 > num2:
        return f"{num1} is the largest number"
    elif num1 < num2:
        return f"{num2} is the largest number"
    else:
        return "unknown error"
    
print(largestNumber(input("inpun number 1: "), input("input number 2: ")))