#1st short version

#варіант із вже даним списоком
int_list = [1,2,6,8,77,45] #Задаємо список з цілими числами який в подальшому будет переводити в (float)

#Варіант із введенням списку ,який хоче користувач
#int_list_str = input("Write your list: ")  # Зчитування рядка з консолі
#int_list = [int(num) for num in int_list_str.split(",")]  #Розділяємо рядок за комами і перетворюємо в цілі числа

float_list = [float(num)for num in int_list] #Щоб не розтягувати , робимо коротше і лаконічніше. Стоврили пустий список
# # в середині вказали цикл та умову перетворення на кожній ітерації "num"
print(float_list) #виводимо результат



#2nd long version


int_list = [1,2,6,8,77,45] ##Задаємо список з цілими числами який в подальшому будет переводити в (float)

float_list = [] #робимо пустий список ,куда будемо додавати нові числа в (float)

for num in int_list: # тіло циклу
     float_list.append(float(num)) #умова циклу,через команду .append - яка додає до нового списку числа в (float) 
print(float_list) #повертаємо
