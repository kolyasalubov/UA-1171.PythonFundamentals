from tkinter import Tk, Label, Button, Entry, messagebox


class WeatherApp:
    def __init__(self, master):
        self.master = master
        master.title("Weather App")

        self.label = Label(master, text="Enter city:")
        self.label.pack()

        self.entry = Entry(master)
        self.entry.pack()

        self.button = Button(master, text="Get Weather", command=self.get_weather)
        self.button.pack()

        self.result_label = Label(master, text="")
        self.result_label.pack()

    def get_weather(self):
        city = self.entry.get()
        if not city:
            messagebox.showerror("Error", "Please enter a city name.")
            return

        try:
            from pyowm import OWM
            owm = OWM('64d8c4fd75d87984f685e491371e3050')
            mgr = owm.weather_manager()
            observation = mgr.weather_at_place(city)
            weather = observation.weather
            self.result_label.config(text=f"Weather in {city}: {weather}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to retrieve weather information: {str(e)}")

root = Tk()
app = WeatherApp(root)
root.mainloop()