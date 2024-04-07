"""7.2.1"""


# def greet(name):
#     if name == "Johnny":
#         return "Hello, my love!"
#     else:
#         return "Hello, {name}!".format(name=name)


# print(greet("Johnny"))


"""7.2.2"""


# def distance(x1, y1, x2, y2):
#     return round(((x2 - x1)**2 + (y2 - y1)**2)**0.5, 2)


# x1, y1, x2, y2 = 1, 1, 0, 0

# print(distance(x1, y1, x2, y2))

"""7.2.3"""


# def filter_words(st):
#     form_words = [i.lower() for i in st.split()]
#     formatted_string = ' '.join(form_words).capitalize()
#     return formatted_string


# st = 'HELLO CAN YOU HEAR ME'
# # st1 = 'This   will   not'

# print(filter_words(st))


"""7.2.4"""


# def number_to_string(num):
#     return str(num)

# # number_to_string = lambda num: str(num)


# print(number_to_string(20))


"""7.2.5"""


# def reverse(st):
#     lst = st.strip().split()
#     lst.reverse()
#     return ' '.join(lst)


# print(reverse("   Hello   world"))


"""7.2.6"""


# def reverse_list(l):
#     l.reverse()
#     return l

"""7.2.7"""


# def solution(number):
#     if number < 0:
#         return 0
#     else:
#         sum_n = 0
#         for i in range(number):
#             if i % 3 == 0 or i % 5 == 0:
#                 sum_n += i
#                 continue
#     return sum_n


# number = 10

# print(solution(number))


"""7.2.8"""


# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     if distance_to_pump / mpg > fuel_left:
#         return False
#     return True


# distance_to_pump = 50
# mpg = 25
# fuel_left = 2

# print(zero_fuel(distance_to_pump, mpg, fuel_left))


"""7.2.9"""


# def are_you_playing_banjo(name):
#     # Implement me!
#     return name + f' plays banjo' if name.lower().startswith('r') else name + f' does not play banjo'


# name = "Randy"
# print(are_you_playing_banjo(name))

"""7.2.10"""


# def bool_to_word(boolean):
#     return 'Yes' if boolean == True else 'No'


# print(bool_to_word(False))


"""7.2.11"""


# def count_sheeps(sheep):
#     counter = 0
#     for i in sheep:
#         counter += 1 if i else 0
#     return counter


# sheep = [True,  True,  True,  False,
#          True,  True,  True,  True,
#          True,  False, True,  False,
#          True,  False, False, True,
#          True,  True,  True,  True,
#          False, False, True,  True]
# print(count_sheeps(sheep))

"""7.2.12"""


def correct_tail(body, tail):
    if body[-1] == tail[0]:
        return True
    return False


print(correct_tail("Fox", "x"))
