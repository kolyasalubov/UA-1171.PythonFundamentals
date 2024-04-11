philosophy = """
beautiful is better than ugly.
explicit is better than implicit.
simple is better than complex.
complex is better than complicated.
flat is better than nested.
sparse is better than dense.
readability counts.
special cases aren't special enough to break the rules.
although practicality beats purity.
errors should never pass silently.
unless explicitly silenced.
in the face of ambiguity, refuse the temptation to guess.
there should be one-- and preferably only one --obvious way to do it.
although that way may not be obvious at first unless you're dutch.
now is better than never.
although never is often better than right now.
if the implementation is hard to explain, it's a bad idea.
if the implementation is easy to explain, it may be a good idea.
namespaces are one honking great idea -- let's do more of those!
"""

better_count = philosophy.upper().count("BETTER")
never_count = philosophy.upper().count("NEVER")
is_count = philosophy.upper().count("IS")
print(f'better - {better_count}\nnever - {never_count}\nis - {is_count}')
print()
print(philosophy.upper())
print()
philosophy = philosophy.replace('I', '&')
print(philosophy)