# Task 1 
# You need to write Python's philosophy in the string format:
# - find separately the number of occurrences of the words
# "better", "never" and "is" in the given line
# - you need to display all text in uppercase (all letters in uppercase)
# - replace all occurrences of the symbol “i” with “&”

zen_of_Python = """1.Beautiful is better than ugly. 
2.Explicit is better than implicit.
3.Simple is better than complex. 
4.Complex is better than complicated.
5.Flat is better than nested. 
6.Sparse is better than dense.
7.Readability counts.
8.Special cases aren't special enough to break the rules.
9.Although practicality beats purity.
10.Errors should never pass silently.
11.Unless explicitly silenced.
12.In the face of ambiguity, refuse the temptation to guess.
13.There should be one-- and preferably only one --obvious way to do it.
14.Although that way may not be obvious at first unless you're Dutch.
15.Now is better than never.
16.Although never is often better than *right* now.
17.If the implementation is hard to explain, it's a bad idea.
18.If the implementation is easy to explain, it may be a good idea.
19.Namespaces are one honking great idea -- let's do more of those!"""

print("'better' -",zen_of_Python.count('better'))
print("'never'  -",zen_of_Python.count('never'))
print("'is'     -",(zen_of_Python.count('is')))

# print(zen_of_Python .upper())

# print(zen_of_Python .replace('i','&'))

# Task 2 
# A four-digit natural number is specified:
# - find the product of the digits of this number
# - write the number in reverse order
# - in ascending order, you need to sort the numbers included in the given number


digit_natural_number = 5674
# print(type(digit_natural_number))
digit_str = str(digit_natural_number)
print(digit_str[::-1])  # it is ok
# digit_list = list(digit_str)
# print(digit_list) 
# b = count. digit_str
# print(product)

# print(digit_str [::-1])

# Task 3
# Interchange the values of two variables without using the third variable.
# value_1 = 57
# value_2 = 43
# print(value_1, value_2)
# value_1,value_2 = value_2,value_1
# print(value_1, value_2)