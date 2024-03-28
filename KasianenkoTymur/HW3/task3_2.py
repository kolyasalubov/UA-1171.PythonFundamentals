number_4digit=input("A 4-digit natural number:")

product= int(number_4digit[0])*int(number_4digit[1])*int(number_4digit[2])*int(number_4digit[3])

print(product,'\n')

print(number_4digit[::-1],'\n')

print(sorted(number_4digit,key=max))
