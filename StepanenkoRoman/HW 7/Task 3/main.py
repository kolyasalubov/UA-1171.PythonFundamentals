"""Task3. Write a function that calculates the number of characters 
included in given string
 • input: "hello"
 • output: {"h":1, "e":1,"|":2,"o":1}"""

from functions_calculate import split_str_by_char

user_string = input("Please enter your string: ")

print(split_str_by_char(user_string))