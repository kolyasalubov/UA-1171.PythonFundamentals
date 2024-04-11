############ 1 #############

def greet(name):
    if name == "Johnny":
        return "Hello, my love!" 
    return "Hello, {name}!".format(name=name)

############ 2 #############

def distance(x1, y1, x2, y2):
    distance = round(((x1 - x2)**2 + (y1 - y2)**2)**0.5, 2)
    return distance

############ 3 #############

def filter_words(st):
    st = st.split()
    st = " ".join(st)
    return st.capitalize()

############ 4 #############

def number_to_string(num):
    return str(num)

############ 5 #############

def reverse(st):
    st = st.split()
    st = st[::-1]
    return " ".join(st)

############ 6 #############

def reverse_list(l):
    return l[::-1]

############ 7 #############

def solution(number):
    lst = []
    for i in range(number):
        if i % 5 == 0 or i % 3 == 0:
            lst.append(i)
    return sum(lst)  

############ 8 #############

def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump <= mpg*fuel_left:
        return True
    else: 
        return False
    
############ 9 #############

def are_you_playing_banjo(name):
    if name[0] == "r" or name[0] == "R":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"

############ 10 #############

def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"
    
############ 11 #############

def count_sheeps(sheep):
    counter = 0
    for i in sheep:
        if i == True:
            counter += 1
    return counter

############ 12 #############

def correct_tail(body, tail):
    if body[-1] == tail:
        return True
    else:
        return False