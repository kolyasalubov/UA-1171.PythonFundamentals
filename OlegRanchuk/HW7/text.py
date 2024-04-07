def calculate_text(text):
    char_text= {}
    for char in text:
        if char in char_text:
            char_text[char] += 1
        else:
            char_text[char] = 1
        return char_text
    
text = "hello"
char_text= calculate_text(text)
print(char_text)