import tkinter as tk

def calculate():
    try:
        # Спроба виконати обчислення виразу, введеного користувачем
        result = eval(entry.get())  # Вираз вираховується за допомогою eval() функції
        entry.delete(0, tk.END)     # Очищаємо поле введення
        entry.insert(tk.END, str(result))  # Вставляємо результат обчислення у поле введення
    except Exception as e:
        # Якщо сталася помилка при обчисленні, виводимо повідомлення про помилку у поле введення
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    # Функція для очищення поля введення
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Calculator")  # Встановлюємо заголовок вікна калькулятора

# Створюємо поле введення для виразів
entry = tk.Entry(root, width=30)
entry.grid(row=0, column=0, columnspan=4)  # Розміщуємо поле введення на головному вікні

# Створюємо список кнопок для калькулятора
buttons = [
    '7', '8', '9', '/',   # Цифри та математичні операції
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'   # Додаткові кнопки: крапка, обчислення та очищення
]

row = 1
col = 0
# Додаємо кнопки на головне вікно і призначаємо їм відповідні функції
for button in buttons:
    if button == '=':
        # Для кнопки "=", викликаємо функцію calculate()
        tk.Button(root, text=button, command=calculate).grid(row=row, column=col)
    elif button == 'C':
        # Для кнопки "C", викликаємо функцію clear()
        tk.Button(root, text=button, command=clear).grid(row=row, column=col)
    else:
        # Для інших кнопок, вставляємо відповідний символ у поле введення
        tk.Button(root, text=button, command=lambda b=button: entry.insert(tk.END, b)).grid(row=row, column=col)
    col += 1
    # Якщо колонка переповнилася, переходимо на наступний рядок
    if col > 3:
        col = 0
        row += 1

root.mainloop()  # Запускаємо головний цикл Tkinter для відображення графічного інтерфейсу