celsius = float(input("Enter temperature in celsius: ")) #Поле вводу користувачем потрібної температури

fahrenheit = (celsius * 1.8) + 32 #формула для конвертації Цельсій в Фаренгейти

print('%.2f Celsius is equivalnt to: %.2f Fahrenheit' #Виводимо отриману інформацію. %.2f - це позначка ,яка вказує на те
      #що повинно бути виведено з плаваючою точкою(десяткове число)
      %(celsius,fahrenheit))