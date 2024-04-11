import math #через iмпорт "math" метода ;)

print(math.factorial(5))  #120 


#Варіант через виклик функції

def factorial(num):
    result = 1 #Ставиво початкове значення = 1
    
    for i in range(1,num + 1): #проходимо через всі числа від 1 do num+1(Включно)
        result *= i # result множимо на кожне поточне число - і  
    return result #повертаємо результат
print(factorial(5)) # 5 * 4 * 3 * 2 * 1 = 120
 