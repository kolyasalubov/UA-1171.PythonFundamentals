def number_of_characters(word):
    characters_dict = {}
    for i in word:
        characters_dict[i] = word.count(i)
    return characters_dict
word = input("Enter the word: ")
print(number_of_characters(word))