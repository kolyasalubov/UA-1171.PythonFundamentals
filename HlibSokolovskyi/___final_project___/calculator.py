
from tkinter import *

HEIGHT = 500
WIDTH = 700
root = Tk()
canvas = Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Calculator")
canvas.pack()


def read_numbers():
    try:
        first_number = float(entry_field_first.get())
        second_number = float(entry_field_second.get())
        numbers = [first_number, second_number]
        return numbers
    except ValueError:
        output_label.configure(text='An error occured: please enter numbers.')

def addition():
    numbers = read_numbers()
    output_label['text'] = f'The sum is {round(numbers[0]+numbers[1], 3)}'

def substraction():
    numbers = read_numbers()
    output_label['text'] = f'The difference is {round(numbers[0]-numbers[1], 3)}'

def multiplication():
    numbers = read_numbers()
    output_label['text'] = f'The product is {round(numbers[0]*numbers[1], 3)}'

def division():
    numbers = read_numbers()
    if numbers[1] == 0:
        output_label.configure(text="An error occured: can't divide by zero.")
    else:
        output_label['text'] = f'The quotient is {round(numbers[0]/numbers[1], 3)}'

def modulation():
    numbers = read_numbers()
    if numbers[1] == 0:
        output_label.configure(text="An error occured: can't divide by zero.")
    else:
        output_label['text'] = f'The remainder is {round(numbers[0]%numbers[1], 3)}'


entry_field_first = Entry(root, font=('Courier', 12))
entry_field_first.place(relx=0.1, rely=0.25, relwidth=0.2, relheight=0.05)


entry_field_second = Entry(root, font=('Courier', 12))
entry_field_second.place(relx=0.7, rely=0.25, relwidth=0.2, relheight=0.05)


top_label = Label(root, text='Welcome to the calculator!\nEnter two numbers and choose the operation button.\n', font=('Courier', 12), fg='#A79277')
top_label.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.25)


output_label = Label(root, font=('Courier', 12))
output_label.place(relx=0.5,rely=0.7, anchor='n')


add_button = Button(root, text='+', font=('Courier', 12),
                    bg='#5D0E41', fg='#FF204E',
                    command=addition)
add_button.place(relx=0.4, rely=0.25, relwidth=0.1, relheight=0.1)


substract_button = Button(root, text='-', font=('Courier', 12),
                    bg='#008DDA', fg='#ACE2E1',
                    command=substraction)
substract_button.place(relx=0.5, rely=0.25, relwidth=0.1, relheight=0.1)


multiply_button = Button(root, text='*', font=('Courier', 12),
                    bg='#2C7865', fg='#90D26D',
                    command=multiplication)
multiply_button.place(relx=0.4, rely=0.35, relwidth=0.1, relheight=0.1)


divide_button = Button(root, text='/', font=('Courier', 12),
                    bg='#FCDC2A', fg='#FFFBDA',
                    command=division)
divide_button.place(relx=0.5, rely=0.35, relwidth=0.1, relheight=0.1)

modulo_button = Button(root, text='%(rem)', font=('Courier', 12),
                    bg='#86469C', fg='#FFCDEA',
                    command=modulation)
modulo_button.place(relx=0.45, rely=0.45, relwidth=0.1, relheight=0.1)

canvas.create_oval(56, 399, 75, 380, fill="black")

canvas.create_line(40, 370, 92, 370, fill="black", width=7)

canvas.create_oval(56, 360, 75, 341, fill="black")

canvas.create_line(120, 250, 160, 210, fill="black", width=7)

canvas.create_line(120, 210, 160, 250, fill="black", width=7)

canvas.create_line(500, 210, 550, 210, fill="black", width=7)

canvas.create_line(580, 380, 630, 380, fill="black", width=7)

canvas.create_line(605, 355, 605, 405, fill="black", width=7)



mainloop()

