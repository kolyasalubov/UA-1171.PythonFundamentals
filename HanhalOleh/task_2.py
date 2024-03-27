number = input('Enter a four-digit natural number number: ')

if len(number) != 4:
    print("Error: number is not four-digit")
else:
    product = 1
    for digit in number:
        product *= int(digit)
    print("Product of the digits is:", product)

    print("Reversed number is:", number[::-1])

    sorted_number = sorted(number)
    sorted_number_str = ''.join(sorted_number)
    print("Цифри чотирицифрового числа в порядку зростання: ", sorted_number_str)
