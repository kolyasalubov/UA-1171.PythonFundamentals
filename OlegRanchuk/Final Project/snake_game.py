from tkinter import *
import time
import random

game_running = True

game_width = 500
game_height = 500
snake_item = 10



virtual_game_x = game_width // snake_item
virtual_game_y = game_height // snake_item

snake_x = virtual_game_x // 2
snake_y = virtual_game_y // 2
snake_x_nav = 0
snake_y_nav = 0

snake_color1 = "blue"
snake_list = []
snake_size = 3


tk = Tk()
tk.title("Snake Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width = game_width, height = game_height, bd = 0, highlightthickness = 0)
canvas.pack()
tk.update()

food_color1 = "yellow"
food_list = []
food_size = 25
for i in range(food_size):
    x = random.randrange(virtual_game_x)
    y = random.randrange(virtual_game_y)
    id1 = canvas.create_oval(x * snake_item, y * snake_item, x * snake_item + snake_item, y * snake_item + snake_item, fill = food_color1)    
    food_list.append([x, y, id1])
print(food_list)

def snake_paint_item(canvas, x, y):
    global snake_list
    id1 = canvas.create_rectangle(x * snake_item, y * snake_item, x * snake_item + snake_item, y * snake_item + snake_item, fill = snake_color1)
    snake_list.append([x,y,id1])

snake_paint_item(canvas, snake_x, snake_y)

def check_can_we_delete_snake_item():
    if len(snake_list) >= snake_size:
        temp_item = snake_list.pop(0)
        canvas.delete(temp_item[2])
        

def check_if_we_found_food():
    global snake_size
    for i in range(len(food_list)):
        if food_list[i][0] == snake_x and food_list[i][1] == snake_y: 
            snake_size = snake_size + 1
            canvas.delete(food_list[i][2])

def snake_move(event):
    global snake_x
    global snake_y
    global snake_x_nav
    global snake_y_nav
    
    if event.keysym == "Up":
        snake_x_nav = 0
        snake_y_nav = -1
        check_can_we_delete_snake_item()
    elif event.keysym == "Down":
        snake_x_nav = 0
        snake_y_nav = 1
        check_can_we_delete_snake_item()
    elif event.keysym == "Left":
        snake_x_nav = -1
        snake_y_nav = 0
        check_can_we_delete_snake_item()
    elif event.keysym == "Right":
        snake_x_nav = 1
        snake_y_nav = 0
        check_can_we_delete_snake_item()
    snake_x = snake_x + snake_x_nav
    snake_y = snake_y + snake_y_nav
    snake_paint_item(canvas, snake_x, snake_y)
    check_if_we_found_food()

canvas.bind_all("<KeyPress-Left>", snake_move)
canvas.bind_all("<KeyPress-Right>", snake_move)
canvas.bind_all("<KeyPress-Up>", snake_move)
canvas.bind_all("<KeyPress-Down>", snake_move)

def game_over():
    global game_running
    game_running = False
    
    
def check_if_borders():
        if snake_x > virtual_game_x or snake_x < 0 or snake_y > virtual_game_y or snake_y < 0:
            game_over()

while game_running:
    check_can_we_delete_snake_item()
    check_if_we_found_food()
    check_if_borders()
    snake_x = snake_x + snake_x_nav
    snake_y = snake_y + snake_y_nav
    snake_paint_item(canvas, snake_x, snake_y)
    tk.update_idletasks()
    tk.update()
    time.sleep(0.15)

def fun_nothing(event):
    pass
canvas.bind_all("<KeyPress-Left>", fun_nothing)
canvas.bind_all("<KeyPress-Right>", fun_nothing)
canvas.bind_all("<KeyPress-Up>", fun_nothing)
canvas.bind_all("<KeyPress-Down>", fun_nothing)