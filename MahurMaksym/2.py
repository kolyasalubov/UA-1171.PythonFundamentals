number = 7547

product = 1
for digit in str(number):
    product *= int(digit)

reverse_number = int(str(number)[::-1])
sorted_digits = int(''.join(sorted(str(number))))

print(f"Product of digits: {product}")
print(f"Number in reverse order: {reverse_number}")
print(f"Digits sorted in ascending order: {sorted_digits}")