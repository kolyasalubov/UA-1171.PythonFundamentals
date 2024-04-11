def correct_tail(body, tail):
    if body[-1] == tail:
        return True
    else:
        return False
    
print(correct_tail("Fox", "x"))
print(correct_tail("Rhino", "o"))
print(correct_tail("Meerkat", "t"))
print(correct_tail("Emu", "t"))
print(correct_tail("Badger", "s"))
print(correct_tail("Giraffe", "d"))