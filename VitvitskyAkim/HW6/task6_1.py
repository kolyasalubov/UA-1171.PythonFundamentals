a = list(range(1,10))

print("\tEven numbers that are divisible by 2")
for i in a:
    if i%2 == 0 :
        print(i)
print("\tOdd numbers, which are divisible by 3")
for i in a:
    if i%3 == 0 :
        print(i)
print("\tNumbers that are not divisible by 2 and 3.")
for i in a:
    if i%3 != 0 and i%2 != 0:
        print(i)