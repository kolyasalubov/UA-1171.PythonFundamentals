#1st TASK

string = ''' The Zen of Python, by Tim Peters:

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
    '''

#find separately the number of occurence of the words "better", "never", "is". 
#print( "Number of occurence of better:", string.count("better"))
#print("Number of occurence of never:", string.count("never")) 
#print("Number of occurence of is:", string.count('is'))
#print("Number of occrrence of better:", string.count('better'), ", of never:", string.count('never'), ", of is:", string.count('is'))

# display all text in appercase.
#print(string.upper())

#replace all occurence of the symbol "i" with "&"
#replaced_string = string.replace('i', '&')
#print(replaced_string)

#2nd TASK
import random
numb = random.sample("0123456789", 4)
print(numb)

#find the product of the digits of this number

from functools import reduce
int_numb = list(map(int, numb))
digits_numb = reduce((lambda x,y: x*y),int_numb)
print(digits_numb)

#write the number in reverse order
numb.reverse()
print(numb)

#in ascending order, you need to sort the numbers included in the given number
numb.sort()
print(numb)

#3rd TASK
value_one = "Your dreams"
value_two = "live in your heart"
print(value_one, value_two)
value_one, value_two = value_two, value_one
print (value_one, value_two)

