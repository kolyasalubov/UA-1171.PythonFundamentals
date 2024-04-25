def user_age(age):
    if age % 2 == 0:  
        return "Your age is even!"
    else:
        return "Your age is odd"

def bad_case(age):
    if age < 0:
        return "Your age can't be negative"
    else:
        return None  

def main():
    age = int(input("Enter your age: "))
    age_category = user_age(age)
    print(age_category)

    error_message = bad_case(age)
    if error_message:
        print(error_message)

if __name__ == "__main__":
    main()