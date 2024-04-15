import tkinter as tk
from style import *
from random import randint

def generate_random_number():
    return randint(1,100)

randomNumber = generate_random_number()
item = 1


def main_window():
    window = tk.Tk()
    window.title("guess the number")
    window.state('zoomed')
    
    result_label = tk.Label(window, text="guess the number from 1 to 100", **label_style_2)
    result_label.place(relx=0.5, rely=0.3, anchor='center')
    
    entry_number = tk.Entry(text=f" enter Number ", **entry_style)
    entry_number.place(relx=0.5, rely=0.4, anchor='center')

     
    calculate_button = tk.Button(window, text="check Number",command=lambda: less_greater(entry_number, result_label,calculate_button,restart_button), **button_style_2)
    calculate_button.place(relx=0.5, rely=0.5, anchor='center')
    
    restart_button = tk.Button(window, text="play agein", command=lambda: restart(restart_button,calculate_button,result_label), **button_style_2)
    restart_button.place(relx=0.5, rely=0.6, anchor='center')
    restart_button.place_forget()
    
    window.mainloop()
    

def restart(restart_button,calculate_button,result_label):
    restart_button.place_forget()  # Приховуємо кнопку почати спробу заново
    calculate_button.place(relx=0.5, rely=0.5, anchor='center')
    global randomNumber 
    randomNumber = generate_random_number()
    global item 
    item = 1
    result_label.config(text = "let's start!")
    
    
def less_greater(entry_number, result_label,calculate_button,restart_button):
    global item
    Number = int(entry_number.get())
    if Number < 1 or Number > 100:
        result_label.config(text = "enter Number from 1 to 100: ") 
    elif item == 10:
        result_label.config(text = "Your attempts are over")
        calculate_button.place_forget()
        restart_button.place(relx=0.5, rely=0.6, anchor='center')       
    elif Number < randomNumber:
        item += 1
        result_label.config(text = "Number is less")        
    elif Number > randomNumber:
        item += 1 
        result_label.config(text = "Number is greater")        
    elif Number == randomNumber:
        result_label.config(text = "Congratulations, you won!")
        calculate_button.place_forget()
        restart_button.place(relx=0.5, rely=0.6, anchor='center')