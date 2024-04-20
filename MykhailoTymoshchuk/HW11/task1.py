def even_odd_age():
    
    
    user_age = int(input("Enter your age: "))
    
    try:    
        if user_age < 0:
            raise ValueError("The age can`t be negative")
        if user_age % 2 == 0:
            print("Your age is  even")
        else:
            print("Your age is odd")
    except ValueError as ve:
        print("Error: ", ve)
    
def main():
    even_odd_age()
    
if __name__ == "__main__":
    main()