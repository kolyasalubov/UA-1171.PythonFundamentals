even = []
odd = []
other = []

for item in range(1, 10):
    if item%2 == 0:
        even.append(item)  
    elif item%3 == 0:
        odd.append(item)
    else:
        other.append(item)       
        
print(f"""divisible by 2: {even}
divisible by 3: {odd}
not divisible by 3 and 2: {other}""")        