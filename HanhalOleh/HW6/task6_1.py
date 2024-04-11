divided_by_two = []
divided_by_three = []
not_divided_by_both = []


for i in range(1, 10):
    if i % 2 == 0:
        divided_by_two.append(i)

    if i % 2 != 0 and i % 3 == 0:
        divided_by_three.append(i)

    if i % 2 != 0 and i % 3 != 0: 
        not_divided_by_both.append(i)

print(f"There are {len(divided_by_two)} numbers that are divisible by 2:\n{divided_by_two}\nThere are {len(divided_by_three)} numbers that are divisible by 3:\n{divided_by_three}\nThere are {len(not_divided_by_both)} numbers that are not divisible by both 2 and 3:\n{not_divided_by_both}")


