from pyowm import OWM
import tkinter as tk
from tkinter import END

HEIGHT = 350
WIDTH = 450
API_KEY = 'ef2206ff5da67de63306d0b143e20872'

root = tk.Tk()

user_input = tk.StringVar(root)


def get_weather():
    try:
        owm = OWM(API_KEY)
        mgr = owm.weather_manager()

        input_city = user_input.get()

        # Search for current weather in London (Great Britain) and get details
        observation = mgr.weather_at_place(input_city)
        w = observation.weather

        print(w.detailed_status)
        print(w.wind())
        print(w.humidity)
        print(w.temperature('celsius'))
        print(w.rain)
        print(w.heat_index)
        print(w.clouds)

        result = (
            f"City: {input_city}\nConditions: {w.detailed_status}\nTemperature is {round(w.temperature('celsius')['temp'], 2)} C\n"
            f"Wind speed is {w.wind()['speed']} km/hours\nHumidity of the air is {w.humidity}")
        label.config(text=result)
        entry_field.delete(0, END)

    except:
        ex_message = '''Oops! There was a problem\nretrieving that information.'''
        label.config(text=ex_message)


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12), textvariable=user_input)
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame,
                   text="Get Weather",
                   bg="gray", fg="white",
                   font=('Courier', 8),
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 10))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
