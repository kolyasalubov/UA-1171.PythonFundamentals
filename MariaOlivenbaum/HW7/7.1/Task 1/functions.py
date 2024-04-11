def largest_number(first_number, second_number):
    """This is the solution for the first task in Lesson 7.
The function finds the largest number of two numbers.
"""
    if first_number == second_number:
        return first_number
    elif first_number > second_number:
        return first_number
    else:
        return second_number
