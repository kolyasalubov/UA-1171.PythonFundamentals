def characters(input_string):
    count = {}
    for char in input_string:
        count[char] = count.get(char, 0) + 1
    return count


print(characters("hello"))