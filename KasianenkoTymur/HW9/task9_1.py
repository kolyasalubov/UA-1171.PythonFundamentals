import tkinter as tk
from random import randint

tries=1
random_number=randint(1,100)
#print(random_number)

root =tk.Tk()
root.config(bg='green')
root.geometry('600x260')
root.title('Guess a number')

def click( ):
    global tries
    global random_number
    user_number=int(enter.get())

    if user_number > random_number and 1 <= user_number <= 100:
        answer.config(text=f'Guessed number is less.({10-tries} attempts left)')
        tries+=1
    elif user_number < random_number and 1 <= user_number <= 100:
        answer.config(text=f'Guessed number is greater.({10-tries} attempts left)')
        tries+=1
    elif user_number > 100 or user_number < 1:
        answer.config(text='Your number is greater than 100 or less than 1')
    else:
        answer.config(text=f'Yay! You guessed it in {tries} tries.')
        tries=1
        random_number=randint(1,100)
    if tries > 10:
        answer.config(text='Your tries are over :(\n Try again.')
        random_number=randint(1,100)

label1=tk.Label(root, text='Guess a number from 1 to 100 in 10 tries.', font=('Arial', 18), fg='white',bg='green')
label2=tk.Label(root, text='Enter number:', font=('Arial', 18), fg='white', bg='green')
enter=tk.Entry(font=('Arial', 18), width=3, bg='yellow', bd=5)
submit=tk.Button(text='Submit',font=('Arial', 18), command=click, bg='yellow')
answer=tk.Label(text='', font=('Arial', 18), fg='white',bg='green')

label1.pack(padx=5,pady=5)
label2.pack(padx=5,pady=5)
enter.pack(padx=5,pady=5)
submit.pack(padx=10,pady=10)
answer.pack(padx=5,pady=5)

root.mainloop()