import requests
import json


def do_request(url):
    try:
        data_request = requests.get(url)
    except requests.exceptions.ConnectionError:
        raise ValueError('Error - No internet ?')
    
    content = json.loads(data_request.content.decode())

    return content


def get_code_from_coords(coords):
    url = f"https://api.openweathermap.org/data/2.5/weather?appid=5796abbde9106b7da4febfae8c44c232&{coords}"

    return do_request(url)['id']


def get_city_names(city_name):
    url = f"https://openweathermap.org/api/widget/geo?q={city_name}&limit=10"

    return do_request(url)


def new_data(coords):
    url = f"https://openweathermap.org/api/widget/onecall?{coords}&units=metric"

    return do_request(url)


def get_coords_from_id(id):
    url = f"https://api.openweathermap.org/data/2.5/weather?appid=5796abbde9106b7da4febfae8c44c232&id={id}"

    return do_request(url)




def recomendaciones(temperature, weather):
    return