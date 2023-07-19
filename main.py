import requests
import json
import tkinter as tk
import time


window = tk.Tk()

frame = tk.Frame(window)
# ADDED FONT
font = ("Arial", 32)

b = tk.Button(frame, text = "monkey")
b.pack()

weather_data = [tk.StringVar(frame), tk.StringVar(frame), tk.StringVar(frame), tk.StringVar(frame), tk.StringVar(frame), tk.StringVar(frame), tk.StringVar(frame)]
labels = [
#   CHANGED textvariable to text
    tk.Label(frame,text= "Temperature:"),
    tk.Label(frame, textvariable = weather_data[0]),
    tk.Label(frame,text= "Humidity:"),
    tk.Label(frame, textvariable = weather_data[1]),
    tk.Label(frame,text= "Feels Like:"),
    tk.Label(frame, textvariable = weather_data[2]),
    tk.Label(frame,text= "Wind:"),
    tk.Label(frame, textvariable = weather_data[3]),
    tk.Label(frame,text= "Forecast:"),
    tk.Label(frame, textvariable = weather_data[4]),
    tk.Label(frame,text= "UV:"),
    tk.Label(frame, textvariable = weather_data[5]),
    tk.Label(frame,text= "Precipation:"),
    tk.Label(frame, textvariable = weather_data[6])
]

def get_weather():
    api_url = "http://api.weatherapi.com/v1/current.json?key=c7fe0e023fcc441eb0f203609231107&q=33408&aqi=no"
    response = requests.get(api_url).json()
    current = response.get("current")

    weather_data[0].set(current.get("temp_f"))
    weather_data[1].set(current.get("humidity"))
    weather_data[2].set(current.get("feelslike_f"))
    weather_data[3].set((current.get("wind_mph"), current.get("wind_dir")))
    weather_data[4].set(current.get("condition").get("text"))
    weather_data[5].set(current.get("uv"))
    weather_data[6].set(current.get("precip_in"))
    # weather_data[6].set(time.time())
    # I used line 47 to prove that tkinter was updating

    for label in labels:
        # as we loop through the labels, we can also set thier options at the same time
        label.config(padx=5, pady=5, width=30, bd=5, font=font)#https://www.tutorialspoint.com/python/tk_label.htm
        label.pack()

    window.after(10000, get_weather)#ms 1 s = 1000 ms, function to run at end of timer
    # window.after(1000, get_weather())  this is a callback. its a function passed in as an argument. There for we need to referance the function, not call it by adding "()"

get_weather()
frame.pack()
window.mainloop()
