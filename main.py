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

    return json.loads(content)


def print_data(data):
    # For get_weather3
    print("Country: ", data['sys']['country'])
    print("Name: ", data['name'])
    print("Weather: ", data['weather'][0]['main'], data['weather'][0]['description'])

    print("Temperature: ", data['main']['temp'], '°C', f' (Feels like: {data['main']['feels_like']}°C)')
    print("Temperature Max: ", data['main']['temp_max'], '°C')
    print("Temperature Min: ", data['main']['temp_min'], '°C')
    print("Pressure: ", data['main']['pressure'], 'hPa')
    print("Humidity: ", data['main']['humidity'], '%')
    print("Visibility: ", float(data['visibility']) / 100, 'km')

    # For 
    print(data)




city = "4014338"
api = read_config()
coords = get_coords(api, city)
get_weather2(api, coords, city)


#weathe2 = get_weather3(api, coords, city)
#print_data(weathe2)