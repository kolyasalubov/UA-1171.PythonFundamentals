from tkinter import *
import tkinter.font as font
import requests


root = Tk()
root.title("Weather Conditions")

'''fonts collection'''
my_font = font.Font(family='Helvetica',size=15,weight='bold')
my_font_big = font.Font(family='Helvetica',size=60,weight='bold')
my_font_small = font.Font(family='Helvetica',size=15)

frame = LabelFrame(root)
frame.pack(padx=10,pady=10)

'''The function returns current weather conditions in the selected city '''
def current_weather():
    top = Toplevel()

    frame2 = LabelFrame(top)
    frame2.pack(padx=10,pady=10)

    '''Clears the entry field for the next search'''
    my_city = entry1.get()    # metod get отримує данні з поля ввода
    entry1.delete(0,END)      # metod delete очишує поле ввода

    complete_url = base_url+"appid="+api_key+"&q="+my_city

    owm_response = requests.get(complete_url)
    user_request = owm_response.json()
    
    '''Current weather conditions in the selected city '''
    user_city = user_request['name']
    user_country = user_request['sys']['country']
    current_temp = round(user_request['main']['temp']-273.15,1)
    feels_like = round(user_request['main']['feels_like']-273.15,1)
    weather = user_request['weather'][0]['main']
    min_temp = round(user_request['main']['temp_min']-273.15,1)
    max_temp = round(user_request['main']['temp_max']-273.15,1)


    label1 = Label(frame2,text = user_city+", "+user_country, fg = 'deep sky blue')
    label1['font'] = my_font
    label1.grid(column = 1,row = 0)

    label2 = Label(frame2,text = str(current_temp)+" °C", fg = 'deep sky blue' )
    label2['font'] = my_font_big
    label2.grid(column = 1,row = 1)
    
    frame3 = LabelFrame(frame2)           # Frame 3 Сама нижня рамка з даними (clouds, feel like, min/max t)
    frame3.grid(column = 1,row = 2,pady = 5)
    

    label3 = Label(frame3,text = "feels like "+str(feels_like)+" °C", fg = 'goldenrod1')#, anchor = W) # 
    label3['font'] = my_font_small
    label3.grid(column = 1,row = 3,columnspan = 2)

    label4 = Label(frame3,text = weather, fg = 'goldenrod1')
    label4['font'] = my_font
    label4.grid(column = 1,row = 2)

    label5 = Label(frame3,text = "min/max temp: "+str(min_temp)+"°/"+str(max_temp)+"°", fg = 'goldenrod1')
    label5['font'] = my_font_small
    label5.grid(column = 1,row = 4)
    
api_key = "56614bce211b58b6877c1061d307df05"

base_url = "https://api.openweathermap.org/data/2.5/weather?"

label0 = Label(frame,text = "Enter City Name:", fg = 'deep sky blue')
label0['font'] = my_font
label0.grid(column = 1,row = 0)


entry1 = Entry(frame)
entry1['font'] = my_font
entry1.grid(column = 0,row = 1,columnspan = 3,padx = 10,pady = 10,ipadx = 70,ipady = 5) # ipadx - ширина вікна, pady - висота

button1 = Button(frame,text = "VERIFY", fg = 'goldenrod1', command = current_weather)
button1['font'] = my_font
button1.grid(column = 1,row = 2,ipadx = 30,pady = 10)


root.mainloop()