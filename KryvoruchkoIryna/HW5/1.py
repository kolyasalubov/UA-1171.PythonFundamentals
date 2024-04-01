integer_list = list(range(10))
print(integer_list)

float_list = []
index = 0

for item in integer_list:
    float_list.append(float(item))
    index += index

print(float_list)

# 2 fibonacci
mark = True

while mark:
    input_number_fib = int(input('Enter not a negative number: '))
    if input_number_fib < 0:
        print('Invalid input. You should enter a positive number')
    else:
        mark = False