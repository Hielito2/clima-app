import requests
import json
#


def read_config():
    from confi import data
    return data['API']


def get_coords(api, city):
    url = f"https://api.openweathermap.org/data/2.5/weather?appid={api}&id={city}"
    data_request = requests.get(url)
    content = json.loads(data_request.content.decode())
    coords = content['coord']
    cords2 = f"lat={coords['lat']}&lon={coords['lon']}"
    return cords2


def get_weather(api, coords):
    url = f"https://api.openweathermap.org/data/2.5/weather?{coords}&lang=es&unit=standard&appid={api}"
    data_request = requests.get(url)
    content = data_request.content.decode()
    print(content)
    plop = json.loads(content)
    print(plop['coord'])


def get_weather2(api, coords, city):
    url = f"https://api.openweathermap.org/data/2.5/forecast?{coords}&units=metric&appid={api}"
    data_request = requests.get(url)
    content = data_request.content.decode()
        
    #lace = content['name']
    #country = content['country']

    print(content)
    #MX-CHH


def get_weather3(api, coords, city):
    url = f"https://api.openweathermap.org/data/2.5/weather?id={city}&units=metric&appid={api}"
    data_request = requests.get(url)
    content = data_request.content.decode()
    #place = content['name']
    #country = content['country']

    print(content)




city = "4014338"
api = read_config()
coords = get_coords(api, city)

weather = get_weather(api, coords)
#weathe2 = get_weather2(api, coords, city)