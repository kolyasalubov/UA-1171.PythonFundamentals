def greet(name):
    
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)\
        
print("Should greet people normally")
  
print(greet("James"))
print(greet("Jane"))
print(greet("Jim"))

print("Should greet Johnny a little bit more special")

print(greet("Johnny"))