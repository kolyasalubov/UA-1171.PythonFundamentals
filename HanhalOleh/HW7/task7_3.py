def count_letters(word):
    letters_dict = {}
    for letter in word:
        letters_dict[letter] = letters_dict.get(letter, 0) + 1
    return letters_dict

print(count_letters("hello"))