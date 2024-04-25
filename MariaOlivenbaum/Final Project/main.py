from random import randint
from tkinter import *
from tkinter import Button
from tkinter import Entry
from tkinter import messagebox

WIDTH_DISPLAY = 600
HEIGHT_DISPLAY = 400

DARK_ORANGE_COLOR = '#8B4000'
ORANGE_COLOR = '#FFE5B4'

root = Tk()
root.geometry(f'{WIDTH_DISPLAY}x{HEIGHT_DISPLAY}')
root.title("Number guesser")

icon = PhotoImage(file="icon.png")
root.iconphoto(False, icon)


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
                            f"You are right. I guessed *{guessed_number}*. \n"
                            f"You guessed it in {attempt} attempt(s).")
        root.destroy()
    elif user_number < 1 or user_number > 100:
        messagebox.showinfo("Try again",
                            "Hint: Number should be from 1 to 100.")
        label_attempts.configure(text=f"{str(10 - attempt)} attempt(s) left!",
                                 font=("Arial", 14))
    elif user_number < guessed_number:
        messagebox.showinfo("Try again",
                            "Your number is less.")
        label_attempts.configure(text=f"{str(10 - attempt)} attempt(s) left!",
                                 font=("Arial", 14))
    else:
        messagebox.showinfo("Try again",
                            "Your number is greater.")
        label_attempts.configure(text=f"{str(10 - attempt)} attempt(s) left!",
                                 font=("Arial", 14))


def click_button():
    global guessed_number
    global attempt
    user_number = read_user_number()
    attempt += 1
    check(user_number, guessed_number)
    if attempt == 10:
        messagebox.showinfo("You lose...",
                            f"This was your last try. I guessed the number *{guessed_number}*.")
        root.destroy()


guessed_number = randint(1, 100)
attempt = 0
button_clicked = BooleanVar()
annotation = Label(text="I guessed a number from 1 to 100. \nYou have only 10 attempts to guess!",
                   font=("Arial", 14))
annotation.pack(expand=True)

user_field = Entry(root, width=15, font=("Arial", 14))
user_field.pack(expand=True, ipadx=10, ipady=10)

label_attempts = Label(text=f"{str(10 - attempt)} attempt(s) left!", font=("Arial", 14))
label_attempts.pack(expand=True)

try_button = Button(root, text="Try", font=("Arial", 12),
                    height=1, width=15,
                    bg=ORANGE_COLOR, fg=DARK_ORANGE_COLOR,
                    command=click_button)
try_button.pack(expand=True, ipadx=10, ipady=10)

root.resizable(False, False)

root.mainloop()
