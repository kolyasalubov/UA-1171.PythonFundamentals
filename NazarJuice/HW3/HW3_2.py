four_digit_number = input("write down the four-digit number: ")  
 
number_list = list(four_digit_number)

product = 1
for index in range(4):
     product *= int(number_list[index])

print("product: ", product)
print("reverse: ", four_digit_number[::-1])   
print("sorted: ", ''.join(sorted(number_list)))  