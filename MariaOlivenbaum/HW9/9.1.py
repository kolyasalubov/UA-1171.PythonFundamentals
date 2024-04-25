from random import randint
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.geometry('600x400')
root.title("Number guesser")


def read_user_number():
    user_number = user_field.get()
    if user_number.isdigit():
        return int(user_number)
    else:
        messagebox.showinfo("Error",
                            "Please enter a number!")


def check(user_number, guessed_number):
    if user_number == guessed_number:
        messagebox.showinfo("You won!",
                            f"You are right. I guessed *{guessed_number}*.")
        root.destroy()
    elif user_number < 1 or user_number > 100:
        messagebox.showinfo("Try again",
                            "Hint: Number should be from 1 to 100.")
    elif user_number < guessed_number:
        messagebox.showinfo("Try again",
                            "Your number is less.")
    else:
        messagebox.showinfo("Try again",
                            "Your number is greater.")


def click_button():
    global guessed_number
    global attempt
    global flag
    user_number = read_user_number()
    attempt += 1
    check(user_number, guessed_number)
    if attempt == 10:
        messagebox.showinfo("You lose...",
                            f"This was your last try. I guessed the number *{guessed_number}*.")
        root.destroy()


guessed_number = randint(1, 100)
attempt = 0
flag = False
button_clicked = BooleanVar()
annotation = Label(text="I guessed a number from 1 to 100. You have only 10 attempts to guess!",
                   font=("Arial", 12))
annotation.pack(expand=True)

user_field = ttk.Entry(root)
user_field.pack(expand=True, ipadx=10, ipady=10)

btn = ttk.Button(root, text="Try", command=click_button)
btn.pack(expand=True, ipadx=10, ipady=10)
root.resizable(False, False)

root.mainloop()
