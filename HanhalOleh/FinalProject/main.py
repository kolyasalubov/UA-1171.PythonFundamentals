import tkinter as tk
import os

current_file = __file__
parts = current_file.split(os.sep)
project_dir = os.sep.join(parts[:-1])
media_dir = os.path.join(project_dir, "media")

def calculate_bmi():
    global low_index_image, ok_index_image, not_ok_index_image, bad_index_image
    
    try:
        height = int(height_entry.get())
        weight = int(weight_entry.get())
    except ValueError:
        res_label.config(text="Please enter valid numbers for height and weight.")
        return
    
    index = weight / (height / 100) ** 2
    index_label.config(text=f"Your body index is {round(index, 2)}")
    index_label.place(relx=0.5, rely=0.5, relwidth=0.75, relheight=0.1, anchor='n')

    if index <= 16:
        res_label.config(text="Your weight is too low!")
        photo_label.config(image=low_index_image)
    elif 16 < index <= 18.5:
        res_label.config(text="Your weight is quite low!")
        photo_label.config(image=low_index_image)
    elif 18.5 < index <= 25:
        res_label.config(text="Your weight is normal!")
        photo_label.config(image=ok_index_image)
    elif 25 < index <= 30:
        res_label.config(text="You are suffering from pre-adiposity!")
        photo_label.config(image=not_ok_index_image)
    elif 30 < index <= 35:
        res_label.config(text="You are suffering from adiposity of first degree!") 
        photo_label.config(image=bad_index_image)
    elif 35 < index <= 40:
        res_label.config(text="You are suffering from adiposity of second degree!")
        photo_label.config(image=bad_index_image)
    elif index > 40:
        res_label.config(text="You are suffering from adiposity of third degree!")
        photo_label.config(image=bad_index_image)

root = tk.Tk()
root.title("BMI Calculator")

bad_index_image = tk.PhotoImage(file=os.path.join(media_dir, "index_bad.gif"))
not_ok_index_image = tk.PhotoImage(file=os.path.join(media_dir, "index_notok.gif"))
ok_index_image = tk.PhotoImage(file=os.path.join(media_dir, "index_ok.gif"))
low_index_image = tk.PhotoImage(file=os.path.join(media_dir, "index_low.gif"))

HEIGHT = 350
WIDTH = 660

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

height_label = tk.Label(root, text="Enter your height in centimeters", font="Arial 16 bold")
height_label.place(relx=0.5, rely=0, relwidth=0.75, relheight=0.1, anchor='n')

height_entry = tk.Entry(root, font="Arial 16 bold")
height_entry.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

weight_label = tk.Label(root, text="Enter your weight in kilograms", font="Arial 16 bold")
weight_label.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.1, anchor='n')

weight_entry = tk.Entry(root, font="Arial 16 bold")
weight_entry.place(relx=0.5, rely=0.35, relwidth=0.75, relheight=0.1, anchor='n')

index_label = tk.Label(root, font="Arial 16 bold")

res_label = tk.Label(root, font="Arial 16 bold")
res_label.place(relx=0.5, rely=0.6, relwidth=0.75, relheight=0.1, anchor='n')

photo_label = tk.Label(root)
photo_label.place(relx=0.5, rely=0.7, anchor='n')

btn = tk.Button(root, text="Count my BMI!", font="Arial 16 bold", command=calculate_bmi)
btn.place(relx=0.5, rely=0.85, relwidth=0.75, relheight=0.1, anchor='n')

root.mainloop()