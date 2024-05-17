
def split_str_by_char(user_str):
    dict_of_chars = {}
    list_of_chars = [*user_str]
    for ch in list_of_chars:
        ch_amount = user_str.count(ch)
        dict_of_chars[ch] = ch_amount
    return dict_of_chars