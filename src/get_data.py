import requests
import json

from config import data
api = data['API']


def get_forecast(coords):
    url = f"https://api.openweathermap.org/data/2.5/forecast?{coords}&units=metric&appid={api}"
    data_request = requests.get(url)
    content = data_request.content.decode()
        
    return json.loads(content)


def get_today(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?id={city}&units=metric&appid={api}"
    data_request = requests.get(url)
    content = json.loads(data_request.content.decode())

    coords = content['coord']
    cords2 = f"lat={coords['lat']}&lon={coords['lon']}"

    return content, cords2