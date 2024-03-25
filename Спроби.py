# CONST1 = "same\name\table"

# CONST1 = r"same\name\table"

# print("Const1", CONST1)


# # This prints out "John is 23 years old. Your sallary is 999.990 $"
# name = "John"
# age = 23
# salary = 999.99
# print("%s is %d years old. Your sallary is %.3f $" % (name, age, salary))




# New style of string - format method
# name1 = "Oleh"
# name2 = "Bill"
# name3 = "Sean"

# # default(implicit) order
# # Як це виглядає:
# # Умова
# default_order = "{}, {} and {}".format(name1, name2, name3)
# print(default_order)

# # order using positional argument
# positional_order = "{1}, {0} and {2}".format('John','Bill','Sean')
# print(positional_order)
# # order using keyword argument
# keyword_order = "{s}, {b} and {j}".format(j='John',b='Bill',s='Sean')
# print(keyword_order)

# str = 'programiz'
# print('str = ', str)
# #first character
# print('str[0] = ', str[0])
# #last character
# print('str[-1] = ', str[-1])
# #slicing 2nd to 5th character
# print('str[1:5] = ', str[1:5])
# #slicing 6th to 2nd last character
# print('str[5:-2] = ', str[5:-2]


# >>>f = 'Happy New Year'
# >>>f.replace('Happy','Brilliant')
# 'Brilliant New Year'
# >>>f
# 'Happy New Year'
# >>>d = f.replace('Happy','Brilliant')
# d = 'Brilliant New Year'
# >>>f
# 'Happy New Year'


# f = 1234
# f[0]


# >>>str = 'programiz'
# >>>str[:]
# 'programiz'



def main():
    # Задання чотирицифрового числа
    number = int(input("Enter four-digit natural number: "))

    # Знайдемо добуток цифр числа
    product = 1
    for digit in str(number):
        product *= int(digit)
    print(f"Product of the digits: {product}")

    # Запишемо число у зворотному порядку
    reversed_number = int(str(number)[::-1])
    print(f"Number in reverse order: {reversed_number}")

    # Відсортуємо цифри числа за зростанням
    sorted_digits = sorted(str(number))
    sorted_number = int(''.join(sorted_digits))
    print(f"Numbers included in the given number in ascending order: {sorted_number}")

if __name__ == "__main__":
    main()