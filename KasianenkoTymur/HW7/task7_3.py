def calculates_characters(string):
    count = {}
    for char in string:
        count[char] = count.get(char, 0) + 1
    return count

while True:
    word=str(input('your word is:'))
    if word=='exit':
        break
    print(calculates_characters(word))
    