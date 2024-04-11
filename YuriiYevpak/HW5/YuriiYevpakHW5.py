# Task 1
ls = [1, 2, 3, 4, 5]

result_ls = []
for num in ls:
    result_ls.append(float(num))

print(ls)
print(result_ls)



# Task 2
n = int(input("n: "))
fib = [0, 1]

while fib[-1] + fib[-2] <= n:
    f = fib[-1] + fib[-2]
    fib.append(f)
    print(f, end=" ")
