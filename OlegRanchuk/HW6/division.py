divisible_2 = []
divisible_3 = []
non_divisible_2_3 = []

for num in range(1,11):
    if num % 2 == 0:
        divisible_2.append(num)
    elif num % 3 == 0:
        divisible_3.append(num)
    else:
        non_divisible_2_3.append(num)

    print("Divisible 2:" , divisible_2)
    print("Divisible 3:" , divisible_3)
    print("Not divisible 2 and 3" , non_divisible_2_3)
