import math

def jennys_secret(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return f"Hello, {name}!"

def find_dist_points(x1, y1, x2, y2):
    x = x2 - x1
    y = y2 - y1
    dist = math.sqrt(x**2 + y**2)
    return round(dist, 2)

def no_yelling(st):
    st1 = " ".join(st.split())
    return st1.capitalize()

def conv_num_to_str(num):
    return str(num)

def reversing_words(st):
    lst = st.split()
    lst.reverse()
    return " ".join(lst)

def reverse_list_order(l):
    return list(reversed(l))

def multiples_of_3_or_5(number):
    sum = 0
    for item in range(number):
        if item % 3 == 0 or item % 5 == 0:
            sum = sum + item
    return sum

def will_you_make_it(distance_to_pump, mpg, fuel_left):
    return fuel_left * mpg >= distance_to_pump

def check_playing_banjo(name):
    if name[0].capitalize() == "R":
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"

def conv_bool_to_str(boolean):
    return 'Yes' if boolean else 'No'

def sheep_counter(sheeps):
    sum = 0
    for sheep in sheeps:
        if sheep:
            sum = sum + 1
    return sum

def check_if_my_tail(body, tail):
    return body[-1] == tail
