import tkinter as tk
from style import *
from functions import *
def areaRectangle(a:float, b:float):
    """calculate the area of a rectangle
    
    a - Breadth
    b - Length
    
    return area of a rectangle"""
    
   
    return f'area of a rectangle = {a * b}'

def areaTriangle(Base:float, Height:float):
    """calculate the area of a Triangle
    
    return area of a Triangle"""
    
    return f'area of a Circle = {1/2 * Base * Height}'
def areaCircle(radius:float):
    """calculate the area of a Circle
    
    radius - circle radius
    
    return area of a Circle"""
    
    return f'area of a Circle = {pi * (radius**2)}'
 
def open_window(window_title, calculation_func):
    new_window = tk.Toplevel(window)
    new_window.title(window_title)
    new_window.state('zoomed')
   
    if window_title == "rectangle":
        label = tk.Label(new_window, text=f"enter Breadth and Length", **button_style_font)
        entry2 = tk.Entry(new_window, **button_style_entry)
        entry2.pack()
    elif window_title == "Triangle":
        label = tk.Label(new_window, text=f"enter base and heingt", **button_style_font)
        entry2 = tk.Entry(new_window, **button_style_entry)
        entry2.pack()
    else:
        label = tk.Label(new_window, text=f"enter radius", **button_style_font)
        entry2 = None
    
    entry1 = tk.Entry(new_window, **button_style_entry)
    entry1.pack()
    
    #label = tk.Label(new_window, text=f"calculate the area of a {window_title}!")
    label.pack()
    
    result_label = tk.Label(new_window,  **button_style_font, text="")
    result_label.pack()
    
    calculate_button = tk.Button(new_window, text="Calculate", **button_style_calculate, command=lambda: calculate_result(entry1, entry2, result_label, calculation_func))
    calculate_button.pack()

def calculate_result(entry1, entry2, result_label, calculation_func):
    try:
        if calculation_func == areaCircle:
            val1= float(entry1.get())
            result = calculation_func(val1)
        else:   
            val1 = float(entry1.get())
            val2 = float(entry2.get())
            result = calculation_func(val1, val2)
        result_label.config(text=result)
    except ValueError:
        result_label.config(text="Invalid input! Please enter numbers.")

window = tk.Tk()
window.title("Calculete the area")
window.state('zoomed')


buttonRectangle = tk.Button(window, text="calculate the area of a rectangle", **button_style_1, command=lambda: open_window("rectangle", areaRectangle))
buttonRectangle.pack(side="left", padx=10)

buttonTriangle = tk.Button(window, text="calculate the area of a Triangle", **button_style_2, command=lambda: open_window("Triangle", areaTriangle))
buttonTriangle.pack(side="left", padx=10)

buttonCircle = tk.Button(window, text="calculate the area of a circle", **button_style_1, command=lambda: open_window("Circle", areaCircle))
buttonCircle.pack(side="left", padx=10)

window.update_idletasks()
window_width = window.winfo_width()
buttonRectangle.place(relx=0.05, rely=0.2)
buttonTriangle.place(relx=0.35, rely=0.2)
buttonCircle.place(relx=0.65, rely=0.2)
window.mainloop()