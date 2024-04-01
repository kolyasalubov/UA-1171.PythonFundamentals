"""6.1"""

LOGIN = "First"
user_log = str(input("Login: "))
while user_log == LOGIN:
    print("Greetings!")
    continue
else:
    print("Invalid login")


"""6.2"""

even_numb = []
odd_numb = []
rest_numb = []

for item in range(1, 10):
    if item % 2 == 0:
        even_numb.append(item)
    elif item % 3 == 0:
        odd_numb.append(item)
    else:
        rest_numb.append(item)

print(even_numb)
print(odd_numb)
print(rest_numb)
