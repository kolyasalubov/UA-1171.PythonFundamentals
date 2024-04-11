# quetion_1
ZenPython = """
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than right now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

# find separately the number of occurrences of the words "better", "never" and "is"
count_better = ZenPython.lower().count("better")
count_never = ZenPython.lower().count("never")
count_is = ZenPython.lower().count("is")

# Number of occurrences of the words
print(f'Кількість входжень слова "better": {count_better}')
print(f'Кількість входжень слова "never": {count_never}')
print(f'Кількість входжень слова "is": {count_is}')

# You need to display all text in uppercase
print(ZenPython.upper())

# Replace all occurrences of the symbol "i" with "&"
philosophy_python_replaced = ZenPython.replace('i', '&')
print(philosophy_python_replaced)



def main():
    # four-digit natural number
    number = int(input("Enter four-digit natural number: "))

    # Product of the digits
    product = 1
    for digit in str(number):
        product *= int(digit)
    print(f"Product of the digits: {product}")

    # Number in reverse order
    reversed_number = int(str(number)[::-1])
    print(f"Number in reverse order: {reversed_number}")

    # Numbers included in the given number in ascending order
    sorted_digits = sorted(str(number))
    sorted_number = int(''.join(sorted_digits))
    print(f"Numbers included in the given number in ascending order: {sorted_number}")

if __name__ == "__main__":
    main()



# quetion_3

def main():
    # Value of two variables
    a = 5
    b = 10

    # Interchange the values of two variables
    a, b = b, a

    # Output
    print(f"After interchange: a = {a}, b = {b}")


if __name__ == "__main__":
    main()
