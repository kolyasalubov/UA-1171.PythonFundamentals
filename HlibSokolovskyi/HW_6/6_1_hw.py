# original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_div2_numbers = []
# odd_div3_numbers = []
# not_div2_and_div3_numbers = []

# for i in range(10):
#     if original_list[i]%2==0:
#         even_div2_numbers.append(original_list[i])
#     elif original_list[i]%3==0 and original_list[i]%2!=0:
#         odd_div3_numbers.append(original_list[i])
#     elif original_list[i]%3!=0 and original_list[i]%2!=0:
#         not_div2_and_div3_numbers.append(original_list[i])
    
even_div2_numbers = [i for i in range(10) if i%2==0]
odd_div3_numbers = [i for i in range(10) if i%3==0 and i%2!=0]
not_div2_and_div3_numbers = [i for i in range(10) if i%3!=0 and i%2!=0]

print(f"Even numbers that are divisible by 2: {even_div2_numbers}")
print(f"Odd numbers that are divisible by 3: {odd_div3_numbers}")
print(f"Numbers that are not divisible by 2 and 3: {not_div2_and_div3_numbers}")


