given_string = str(input("Enter some text: \n"))

dict_str  = {}

for i in range(len(given_string)):
    key = given_string[i] # Choose some character in order
    quantity = 0
    for j in range(len(given_string)):
        if given_string[j] == key: # Compare other characters with chosen one
            quantity+=1            # If there are characters same as choosen one - increase quantity 
    dict_str[given_string[i]] = quantity 

print(dict_str)