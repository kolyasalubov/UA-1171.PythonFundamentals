# Просто запустіть HW9_T3/YuriiYevpakHW9_T3.py
from YuriiYevpakHW9_T3 import WeatherApp
from tkinter import Tk

def main():
    root = Tk()  # Створення екземпляру класу Tk
    app = WeatherApp(root)  # Передача екземпляру Tk у конструктор WeatherApp
    root.mainloop()

if __name__ == "__main__":
    main()