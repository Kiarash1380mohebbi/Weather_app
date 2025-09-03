import key_api as ka
from tkinter import *
import requests 
from json import *
from main import *

def get_city_name(entry_city_name):
    '''
    Using the API, a request is sent and the data for the desired city is received and stored in a JSON file.
    '''
    global load_data
    text = entry_city_name.get()
    URL_ow = f"https://api.openweathermap.org/data/2.5/weather?q={text}&appid={ka.API_KEY_app}"
    get_data = requests.get(URL_ow)
    load_data = get_data.json()

def search_btn(text_box,load_data):
    text_box.insert(0.0,load_data)

def delete_btn(text_box):
    text_box.delete('end',0.0)