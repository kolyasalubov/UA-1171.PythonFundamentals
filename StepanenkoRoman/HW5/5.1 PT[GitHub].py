"""Task1. 
Create a list that contains elements of integer type, then
use the loop to change the type of these elements to a floating type.
(Hint: use the built-in float () function).
Завдання1. Cтворіть список, що містить елементи цілого типу
використовуйте цикл, щоб змінити тип цих елементів на плаваючий типу.
(Підказка: використовуйте вбудовану функцію float ()."""

# for int_list in [5, 6, 10, 33, 456]:
#     float_list = float(int_list)
#     print(float_list, end=' ')
 
 #################################################
# list_number = [54, 783, 42, 13, 27, 444]
# print(list_number)
# i = 0
# for value in list_number:
#     list_number [i] = float(value)

#     i = i + 1
# print(list_number)




# list_of_number = [112, 11, 42, 61, 51, 43, 12, 689]

# for i in range(len(list_of_number)):
#     list_of_number[i] = float(list_of_number[i])
# print(list_of_number) ## mentor's variant
#####################################################
"""Task2. Print Fibonacci numbers up to the entered number n, using cycles.
(Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.)
Завдання2. Вивести числа Фібоначчі до введеного числа n,
за допомогою циклів.
(Послідовність чисел Фібоначчі 0, 1, 1, 2, 3, 5, 8, 13 тощо)"""

# # fibanacci_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
# # for n_number in fibanacci_list:  
# #     print(n_number, end=" ")
# #     if n_number == 144: 
#        break

"""або якщо  n не включно то:"""

# fibanacci_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
# for n_number in fibanacci_list:  
#     if n_number == 144: 
#        break
#     print(n_number, end=" ")

#######################################################################
# n = int(input('enter some number from fibonacci list= '))

# fibonacci_numbers = [0, 1]

# for i in range (2,n):
#     fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers [i-2])

# print(f'there are some numbers from fibanacci till that you entered {n},\n {fibonacci_numbers}')# mentor's exemple

###########################################################################
      
""" Task 3. Write a script that will calculate the factorial of the entered number 
without using recursion. Example: 0!=1, 1!=1, 2!=2, 3!= 1*2*3=6, ...."""

# import math
# user_number = int(input("Введить ціле число: "))
# factorial_number = user_number
# print(math.factorial(factorial_number))

###########################################################
# input_number = int(input("Input natural number:") )

# fact = 1

# if input_number == 1 or input_number == 0:
#     print ("Factorial {}! =". format (input_number), fact)
# elif input_number < 0:
#     print("Factorial non positive number don't exist")
# else:
#     for item in range (1, input_number + 1):
#         fact*= item
#     print ("Factorial {}! =". format(input_number), fact) # mentor's choice
##############################################################