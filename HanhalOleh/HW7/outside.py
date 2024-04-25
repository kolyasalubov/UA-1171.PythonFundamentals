############ 1 ##########
def greet(name):
    return "Hello, my love!" if name == "Johnny" else "Hello, {name}!".format(name=name)

############ 2 ########
import math
def distance(x1, y1, x2, y2):
    return round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 2)
############ 3 ########
def filter_words(st):
    words = st.split()
    filtered_words = [words[0].capitalize()] + [word.lower() for word in words[1:]]
    return ' '.join(filtered_words)
############ 4 ########
def number_to_string(num):
    return str(num)
############ 5 ########
def reverse(st):
    return " ".join(st.split()[::-1])
############ 6 ########
def reverse_list(l):
    return l[::-1]
############ 7 ########
def solution(number):
    sum=0
    if number <= 0:
        return 0
    else:
        for item in range(number):
            if item % 3 == 0 or item % 5 == 0:
                sum+=item
        return sum
############ 8 #######
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return True if distance_to_pump <= fuel_left*mpg else False
############ 9 #######
def are_you_playing_banjo(name):
    # Implement me!
    return f"{name} plays banjo" if name[0].lower()=="r" else f"{name} does not play banjo"
############ 10 #######
def bool_to_word(boolean):
    return "Yes" if boolean else"No"
############ 11 #######
def count_sheeps(sheep):
  # TODO May the force be with you
  return sum(map(lambda x: 1 if x else 0, sheep))
############ 12 #######
def correct_tail(body, tail):
    sub = body[-len(tail):]
    if sub == tail:
        return True
    else:
        return False
