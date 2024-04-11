def reverse(st):
    s = st.split()
    return ' '.join(s[::-1])



print(reverse('Hello World'))
print(reverse('Hi There.'))