def solution(number):
    sum=0
    if number<=0:
        return sum
    for i in range(number):
        if i%3==0 or i%5==0:
            sum+=i
    return sum
    


print("Sample tests")  

print("Should return 3 for n=4")
print(solution(4))
        
print("Should return 8 for n=6")   
print(solution(6))
    
print("Should return 60 for n=16")
print(solution(16))
    
print("Should return 0 for n=3")
print(solution(3))

print("Should return 3 for n=5")
print(solution(5))

print("Should return 45 for n=15")
print(solution(15))
    
print("Should return 0 for n=0")
print(solution(0))
    
print("Should return 0 for n=-1")
print(solution(-1))
    
print("Should return 23 for n=10")
print(solution(10))
        
print("Should return 78 for n=20")
print(solution(20))

print("Should return 9168 for n=200")
print(solution(200))