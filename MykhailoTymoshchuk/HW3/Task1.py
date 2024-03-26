python_philosofhy = '''Beautiful is better than ugly.
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
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''
#Створив нову змінну під оновлену філософію, яка буде переведена до верхнього регістру та із заміщенням"І" на "&" 
upper_philosofhy = python_philosofhy.upper().replace("I","&")

#Далі створив змінні ,в які буде поміщатись кількість мені потрібних слів
all_better = upper_philosofhy.count("BETTER")
all_never = upper_philosofhy.count("NEVER")
all_is = upper_philosofhy.count("IS")
#Тут трішки не зрозумів завдання,чи потрібно було б підраховувати "IS" із заміщенним "І" на & але додав два підрахунки,про всякий випадок
all_new_is = upper_philosofhy.count("&S")

#Вивидимо потрібну нам інформацію
print(upper_philosofhy,'\n')
print("Total all 'better' count", all_better)
print("Total all 'never' count", all_never)
print("Total all 'is' count", all_is)
print("Total all '&S' count", all_new_is)