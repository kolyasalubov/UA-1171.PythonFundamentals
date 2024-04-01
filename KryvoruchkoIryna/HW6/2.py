start_set = {"Ira", "Vadim", "Igor", "Maria", "Oleg"}
print(start_set)

find_name = True

while find_name:
    input_name = input("Enter new user name: ")
    if input_name in start_set:
        print(f"{input_name} registered earlier")
    else:
        start_set.add(input_name)
        print(f"Congratulation! Registration is successful")
        find_name = False

print(start_set)