import tkinter as tk
from tkinter import font
from pyowm import OWM


API_KEY = 'ef2206ff5da67de63306d0b143e20872'
    

def get_weather():
    global API_KEY
    global entry_field
    global label
    
    owm = OWM(API_KEY)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(entry_field.get())
    w = observation.weather

    detailed_status = w.detailed_status
    wind = w.wind()
    humidity = w.humidity
    temperature = w.temperature('celsius')
    rain = w.rain
    heat_index = w.heat_index
    clouds = w.clouds

    label.config(text=f"""Detailed status: {detailed_status}\nWind: {wind['speed']} m/s\nHumidity: {humidity}%\nTemperature: {temperature['temp']}°C\nRain: {rain}\nHeat index: {heat_index}\nClouds: {clouds}%""", font=("Courier", 8))


HEIGHT = 350
WIDTH = 450


root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()



frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)



root.mainloop()