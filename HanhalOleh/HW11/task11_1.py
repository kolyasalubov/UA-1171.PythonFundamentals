def odd_or_even(age):
    age_div = age % 2
    if age >= 0:
        match age_div:
            case 0:
                return "your age is even"
            case _:
                return "your age is odd"
    else:
        raise ValueError("negative age")
    
try:
    print(odd_or_even(int(input("enter your age: "))))
except Exception as e:
    print(f"Error: {e}")
