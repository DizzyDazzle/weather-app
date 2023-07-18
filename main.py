import requests
import json
import tkinter as tk
import time


window = tk.Tk()

frame = tk.Frame(window)
b = tk.Button(frame, text = "monkey")
b.pack()

weather_data = [tk.StringVar(frame), tk.StringVar(frame), tk.StringVar(frame), tk.StringVar(frame), tk.StringVar(frame), tk.StringVar(frame), tk.StringVar(frame)]
labels = [
    tk.Label(frame,textvariable= "Temperature:"),
    tk.Label(frame, textvariable = weather_data[0]),
    tk.Label(frame,textvariable= "Humidity:"),
    tk.Label(frame, textvariable = weather_data[1]),
    tk.Label(frame,textvariable= "Feels Like:"),
    tk.Label(frame, textvariable = weather_data[2]),
    tk.Label(frame,textvariable= "Wind:"),
    tk.Label(frame, textvariable = weather_data[3]),
    tk.Label(frame,textvariable= "Forecast:"),
    tk.Label(frame, textvariable = weather_data[4]),
    tk.Label(frame,textvariable= "UV:"),
    tk.Label(frame, textvariable = weather_data[5]),
    tk.Label(frame,textvariable= "Precipation:"),
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

    for label in labels:
        label.pack()

    #window.after(1000, get_weather())

get_weather()
frame.pack()
window.mainloop()
