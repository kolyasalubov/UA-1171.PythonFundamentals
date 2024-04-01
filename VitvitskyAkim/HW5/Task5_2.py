n = int(input("How many Fibonacci numbers\
               to display on the screen?: "))
f = 0
i = 0
f1,f2 = 0,1
while i < n:
    f = f1 + f2
    f1=f2
    f2=f
    i += 1
    print(f)