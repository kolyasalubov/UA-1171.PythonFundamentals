n = input('four-digit natural number: ')
n = str(n)

product = (int(n[0]) * int(n[1])) * (int(n[2]) * int(n[3]))
print(product)

print(n[::-1])

print(sorted(n, key=max))