import tkinter as tk


def get_weather():

    from pyowm import OWM

    API_KEY = 'c07c5e5a5c1f2b0616de2c755fb52094'

    country=str(entry_field.get())
    owm = OWM(API_KEY)
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(country)
    w = observation.weather
    temperature = w.temperature('celsius')
    wind = w.wind()

    label.config(text=f'''{w.detailed_status}
wind: speed({wind['speed']}), deg({wind['deg']})
humidity: {w.humidity}
temperature: {temperature['temp']}°C, max: {temperature['temp_max']}°C , min: {temperature['temp_min']}°C''')         


HEIGHT = 350
WIDTH = 750

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
                   command=get_weather)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)


root.mainloop()

