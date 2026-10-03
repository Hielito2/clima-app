import requests
import json

from config import data
api = data['API']


def get_forecast(coords):
    url = f"https://api.openweathermap.org/data/2.5/forecast?{coords}&units=metric&appid={api}"
    data_request = requests.get(url)
    content = json.loads(data_request.content.decode())

    if data_request.status_code != 200:
        raise ValueError(f"Error getting the weather for {coords} || code {content['cod']} || message: {content['message']}")

    return content


def get_today(city_code: str = "0", city_coords: str = "0"):
    if city_code != "0":
      url = f"https://api.openweathermap.org/data/2.5/weather?id={city_code}&units=metric&appid={api}"
    else:
      url = f"https://api.openweathermap.org/data/2.5/weather?{city_coords}&units=metric&appid={api}"

    try:
        data_request = requests.get(url)
    except requests.exceptions.ConnectionError:
        raise ValueError('Error - No internet ?')

    content = json.loads(data_request.content.decode())

    if data_request.status_code != 200:
        raise ValueError(f"Error getting the weather for {city} || code {content['cod']} || message: {content['message']}")

    coords = content['coord']
    cords2 = f"lat={coords['lat']}&lon={coords['lon']}"

    city_code2 = content['id']

    return content, cords2, city_code2
