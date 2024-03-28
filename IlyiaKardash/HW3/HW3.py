import this
import random

"""1.1"""

# message = """The Zen of Python, by Tim Peters
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!"""

# x = 0
# count = 0

# word_to_find = str(input("Which word do you want me to find?"))

# while True:
#     x = message.find(word_to_find, x, len(message))
#     count += 1
#     if x == -1:
#         break
#     print(f"{word_to_find} was found at position: {x}")
#     x = x + 1
# print(f"Number of occurences of the word {word_to_find} is {count}")

"""1.2"""

# print(message.upper())


"""1.3"""

# print(message.replace('i','&'))


"""2.1"""


# num = int(random.randint(999,9999))

# temporary = num
# product = 1

# while(temporary != 0):

#     product = product * (temporary % 10)

#     # Remove last digit from temp.
#     temporary = int(temporary / 10)

# print("\nProduct of all digits in", num, ":", product)

"""2.2"""

# num = list(str(random.randint(999,9999)))
# print(num)
# num.reverse()
# # or reversed_list = num[::-1] 
# # print(reversed_list)
# print(num)


"""2.3"""

# num = list(str(random.randint(999,9999)))
# num.sort()
# print(num)


"""2.4"""

# a = random.randrange(0,9)
# b = random.randrange(0,9)
# print(a,b)

# a, b = b, a
# print("a:", a)
# print("b:", b)
