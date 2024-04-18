from pyowm import OWM
import tkinter as tk

API_KEY = 'ef2206ff5da67de63306d0b143e20872'
HEIGHT = 550
WIDTH = 750

def get_weather():
    owm = OWM(API_KEY)
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(entry_field.get())
    w = observation.weather

    weather_data = (
        f"""The weather in *{entry_field.get()}* today is {w.detailed_status},
        Wind: {w.wind()['speed']} km/h\nHumidity: {w.humidity}%,
        Temperature: {w.temperature('celsius')['temp']}
        Feels like: {w.temperature('celsius')['feels_like']}""")
    label.config(text=weather_data)


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

label.pack(expand=True, ipadx=10, ipady=10)

root.mainloop()
