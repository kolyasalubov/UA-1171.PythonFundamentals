import random
int_numbers = []
float_numbers = []

n = int(input("how many numbers do you want to appear in a list? "))
for i in range(n):
    int_numbers.append(random.randint(0, 99))

for item in int_numbers:
    float_numbers.append(float(item))

print(f"Integer numbers list:  {int_numbers}\nFloat numbers list:    {float_numbers}")