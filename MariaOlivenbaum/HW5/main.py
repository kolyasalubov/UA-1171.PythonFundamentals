print("***THE FIRST TASK***")

list_size = int(input("Enter the number of numbers in the list: "))

list_of_integers = []
for i in range(list_size):
    list_of_integers.append(int(input(f"Enter {list_size-i} more numbers for the list: ")))

list_of_floats = [float(i) for i in list_of_integers]

print(f"Our list but in float type: {list_of_floats}")

# ==============================

print("\n***THE SECOND TASK***")

last_number_fibonacci = int(input("Enter the last number in this fibonacci sequence: "))

fibonacci_sequence = [0, 1]

if last_number_fibonacci == 0:
    print(f"The Fibonacci_sequence till {last_number_fibonacci}:", fibonacci_sequence[0])
else:
    while (fibonacci_sequence[-1] + fibonacci_sequence[-2]) <= last_number_fibonacci:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    print(f"The Fibonacci_sequence till {last_number_fibonacci}:", fibonacci_sequence)

# or we can use FOR
# else:
#     for i in range (last_number_fibonacci):
#         if (fibonacci_sequence[-1] + fibonacci_sequence[-2]) < last_number_fibonacci:
#             fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
#         else:
#             break
#     print(f"The Fibonacci_sequence till {last_number_fibonacci}:", fibonacci_sequence)

# ==============================

print("\n***THE THIRD TASK***")

number_for_factorial = int(input("Enter the number for which you want to calculate the factorial: "))
factorial_result = 1

for i in range(1, number_for_factorial + 1):
    factorial_result *= i

# or we can use WHILE
# while number_for_factorial > 1:
#     factorial_result *= number_for_factorial
#     number_for_factorial -= 1

print(factorial_result)
