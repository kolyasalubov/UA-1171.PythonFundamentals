python_philosophy = "Beautiful is better than ugly.\n\
Explicit is better than implicit.\n\
Simple is better than complex.\n\
Complex is better than complicated.\n\
Flat is better than nested.\n\
Sparse is better than dense.\n\
Readability counts.\n\
Special cases aren't special enough to break the rules.\n\
Although practicality beats purity.\n\
Errors should never pass silently.\n\
Unless explicitly silenced.\n\
In the face of ambiguity, refuse the temptation to guess.\n\
There should be one-- and preferably only one --obvious way to do it.\n\
Although that way may not be obvious at first unless you're Dutch.\n\
Now is better than never.\n\
Although never is often better than *right* now.\n\
If the implementation is hard to explain, it's a bad idea.\n\
If the implementation is easy to explain, it may be a good idea.\n\
Namespaces are one honking great idea -- let's do more of those!"
#count the words in the text
print('The number of word "Better"',python_philosophy.count('better'))
print('The number of word "Never"',python_philosophy.count('never'))
print('The number of word "Is"',python_philosophy.count('is'))
#display all text in uppercase
print("ALL TEXT IN UPPERCASE:\n",python_philosophy.upper())
#replace all occurrences of the symbol “i” with “&”
changed_python_philosophy=python_philosophy.replace("i","&")
print("Python philosophy, where the 'i' symbol is replaced with the\
        '&' symbol",changed_python_philosophy)