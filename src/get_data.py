import requests
import json

from config import data


def get_code_from_coords(coords):
    url = f"https://api.openweathermap.org/data/2.5/weather?appid=5796abbde9106b7da4febfae8c44c232&{coords}"
    try:
        data_request = requests.get(url)
    except requests.exceptions.ConnectionError:
        raise ValueError('Error - No internet ?')
    
    req_data = json.loads(data_request.content)

    return req_data['id']


def get_city_names(city_name):
    url = f"https://openweathermap.org/api/widget/geo?q={city_name}&limit=10"
    try:
        data_request = requests.get(url)
    except requests.exceptions.ConnectionError:
        raise ValueError('Error - No internet ?')
    
    req_data = json.loads(data_request.content)
    return req_data


def new_data(coords):
    url = f"https://openweathermap.org/api/widget/onecall?{coords}&units=metric"
    try:
        data_request = requests.get(url)
    except requests.exceptions.ConnectionError:
        raise ValueError('Error - No internet ?')
    
    content = json.loads(data_request.content.decode())

    return content


def get_coords_from_id(id):
    url = f"https://api.openweathermap.org/data/2.5/weather?appid=5796abbde9106b7da4febfae8c44c232&id={id}"

    try:
        data_request = requests.get(url)
    except requests.exceptions.ConnectionError:
        raise ValueError('Error - No internet ?')
    
    content = json.loads(data_request.content.decode())

    return content



def get_forecast(coords):
    url = f"https://api.openweathermap.org/data/2.5/forecast?{coords}&units=metric&appid={api}"
    try:
        data_request = requests.get(url)
    except requests.exceptions.ConnectionError:
        raise ValueError('Error - No internet ?')
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
        raise ValueError(f"Error getting the weather for {city_code if city_code != "0" else city_coords} || code {content['cod']} || message: {content['message']}")

    coords = content['coord']
    cords2 = f"lat={coords['lat']}&lon={coords['lon']}"

    city_code2 = content['id']

    return content, cords2, city_code2


def recomendaciones(temperature, weather):
    return