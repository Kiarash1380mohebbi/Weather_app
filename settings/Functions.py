from tkinter import *
from json import *
import requests 

def get_city_name(entry_city_name):
    '''
    Using the API, a request is sent and the data for the desired city is received and stored in a JSON file.
    '''
    global load_data
    text = entry_city_name.get()
    key = "15cc8f5b012245f074d4057e50112674"
    URL_ow = f"https://api.openweathermap.org/data/2.5/weather?q={text}&appid={key}"
    get_data = requests.get(URL_ow)

    if get_data.status_code == 200:
        data = get_data.json()
        load_data = {
            "main": data["weather"][0]["main"],
            "description": data["weather"][0]["description"],
            "icon": data["weather"][0]["icon"],
            "temp": data["main"]["temp"] - 273.15, 
            "humidity": data["main"]["humidity"],
            "wind": data["wind"]["speed"]
        }
        return load_data
    else:
        return {"error": "City not found"}
    

def search_btn(text_box, entry_city_name):
    data = get_city_name(entry_city_name)
    text_box.configure(state="normal")  
    text_box.delete(1.0, END)

    if "error" in data:
        text_box.insert(1.0, f"Error: {data['error']}")
    else:
        text_box.insert(1.0, f"Weather: {data['main']}\nDescription: {data['description']}\nTemperature: {data['temp']:.1f}°C\nHumidity: {data['humidity']}%\nWind Speed: {data['wind']} m/s")
    
    text_box.configure(state="disabled") 

def delete_btn(text_box):
    text_box.configure(state="normal")
    text_box.delete(1.0, END) 
    text_box.configure(state="disabled")