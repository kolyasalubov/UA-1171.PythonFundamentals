def filter_words(st):
    good_st=''
    back_item=' '
    number=1
    for item in list(st):
        if (item==' ' and item==back_item) or (item==st[-1]==' ' and number==len(st)):
            number+=1
            continue
        good_st+=item
        back_item=item
        number+=1
    return good_st.capitalize() 

print(filter_words('HELLO world!'))
print(filter_words('This    will    not    pass '))
print(filter_words('NOW THIS is a VERY EXCITING test!'))