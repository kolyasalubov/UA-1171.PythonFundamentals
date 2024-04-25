from tkinter import *
from tkinter import messagebox
from random import shuffle

top = Tk()
top.title('Fifteens')


class Button_chip(Button):
    pos_x: ''
    pos_y: ''
    defvalue: ''


BUTTON_NAMES_LIST = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, " ")


buttons_list = []

def exit_callback(event):
    top.destroy()

def start_callback(event):
    shf()
    check_color()

def on_enter(event):
    if (highlights(event)):
        event.widget.configure(bg="khaki")

def on_leave(event):
    check_color()

def move(event):
    global empty_chip
    if event.widget.cget('bg') == 'khaki':
        empty_chip.configure(text=event.widget.cget('text'))
        event.widget.configure(text=' ')
        empty_chip = event.widget
        return True;
    else:
        return False;


def callback(event):
    txt = event.widget['text']

    if txt == ' ':
        return
    else:
        if (move(event)):
            check_color()
            check_win()

def highlights(event):
    txt = event.widget['text']
    if txt != ' ':
        x, y = int(event.widget.pos_x), int(event.widget.pos_y)
        empty_x, empty_y = int(empty_chip.pos_x), int(empty_chip.pos_y)

        if (-1 < x < 4) and (-1 < y < 4):
            if (x in [empty_x - 1, empty_x + 1] and y == empty_y or y in [empty_y - 1, empty_y + 1] and x == empty_x):
                return True
    return False


for x in range(4):
    for y in range(4):
        chip = Button_chip(width='10', height='5', relief='raised')
        chip.pos_x, chip.pos_y = x, y

        buttons_list.append(chip)

        chip.bind('<Button-1>', callback)
        chip.bind('<Enter>', on_enter)
        chip.bind('<Leave>', on_leave)

for i in range(16):
    buttons_list[i].configure(text=BUTTON_NAMES_LIST[i])
    buttons_list[i].defvalue = BUTTON_NAMES_LIST[i]


empty_chip = buttons_list[15]

button_exit = Button(bg='dark red', width='10', height='5', text='Exit')
button_restart = Button(bg='dark green', width='10', height='5', text='Start')
button_exit.bind('<Button-1>', exit_callback)
button_restart.bind('<Button-1>', start_callback)


def shf():
    global empty_chip

    s = list(BUTTON_NAMES_LIST)
    shuffle(s)
    for i in range(16):
        buttons_list[i].configure(text=s[i])

    for btn in buttons_list:
        if btn.cget('text') == ' ':
            empty_chip = btn
            break

def check_color():
    for i in buttons_list:
        chip = i.cget('text');

        if chip == i.defvalue and chip != ' ':
            i.configure(bg='light green')
        elif chip == ' ':
            i.configure(bg='light pink')

        else:
            i.configure(bg='SystemButtonFace')

def check_win():
    chip_count = 0
    for btn in buttons_list:
        if btn.defvalue == btn.cget('text'):
            chip_count += 1
    if chip_count == 16:
        messagebox.showinfo("You are winner!", "Again?")
        shf()
        check_color()

def main():
    for btn in buttons_list:
        btn.grid(row=btn.pos_x, column=btn.pos_y)

    button_exit.grid(row=0, column=4)
    button_restart.grid(row=3, column=4)
    check_color()

    top.mainloop()
    pass


if __name__ == '__main__':
    main()
