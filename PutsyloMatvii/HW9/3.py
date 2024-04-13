import tkinter as tk
from tkinter import font
from pyowm import OWM

API_KEY = 'ef2206ff5da67de63306d0b143e20872'


def weather_response(city: str):
    try:
        owm = OWM(API_KEY)
        m = owm.weather_manager()
        input_city = city
        obs = m.weather_at_place(input_city)
        w = obs.weather
        whether = f"City: {input_city} clouds: {w.detailed_status} speed: {w.wind()} humidity: {w.humidity} temperature: {w.temperature('celsius')} rain: {w.rain} heat index: {w.heat_index} clouds: {w.clouds}"

        return whether
    except:
        print('Error')


def get_weather(city):
    city = entry_field.get()
    weather_info = weather_response(city)
    if weather_info:
        label['text'] = weather_info
    else:
        label['text'] = "No data"


root = tk.Tk()
root.title("Weather App")
frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)
button = tk.Button(frame,
                   text="Get Weather",
                   bg="gray", fg="white",
                   font=('Courier', 8),
                   command=get_weather)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')
label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)
root.mainloop()