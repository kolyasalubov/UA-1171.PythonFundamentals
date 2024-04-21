number = input("Enter a four-digit natural number: ")

product = 1
for num in number:
    product *= int(num)

reverse_number = number[::-1]

sorted_number = ''.join(sorted(number))

print("Product of digits:", product)
print("Number in reverse order:", reverse_number)
print("Number in ascending order:", sorted_number)


