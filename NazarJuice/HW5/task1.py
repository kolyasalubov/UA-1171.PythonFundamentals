integer_list = [int(input(f"Enter {i+1} number: ")) for i in range(int(input("enter amount: ")))]
print(integer_list)


float_list=[]
for item in integer_list:
    float_list.append(float(item))
print(float_list)    