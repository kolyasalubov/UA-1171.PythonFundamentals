for i in range(1, 10):
    if i % 2 == 0:
        print(f'divisible by 2 = {i}')
    if i % 3 == 0:
        print(f'divisible by 3 = {i}')
    if i % 2 != 0 and i % 3 != 0:
        print(f'not divisible by 2 and 3 = {i}')