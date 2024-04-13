# def calculateCharacter (input_str):
"""Create a simple function
char_count = {} for short time , pure dict to wich we add a char after each iterations """
#     char_count = {}
    
#     for char in input_str:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1
            
#     return char_count
"""Contidion with input sting "Hello"
ouput_dict = new dict with counted char from the cicle condition above """
# input_str = "hello"
# output_dict = calculateCharacter(input_str)
# print(output_dict)

#2nd version with using list comprehetion 
def countCharacters(string):
    """char_count (dict)Wich returning after condition, that create a key: value for item in iterable"""
    char_count = {char: string.count(char)for char in string}
    return char_count

    """contidion"""
string = "hello"
output_dict = countCharacters(string)
print(output_dict)