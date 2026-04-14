import requests
import json
#
from datetime import datetime, timedelta, timezone



def read_config():
    from confi import data
    return data['API']



def get_weather2(api, coords, city):
    url = f"https://api.openweathermap.org/data/2.5/forecast?{coords}&units=metric&appid={api}"
    data_request = requests.get(url)
    content = data_request.content.decode()
        
    #lace = content['name']
    #country = content['country']

    return json.loads(content)
    #MX-CHH


def get_weather3(api, city):
    url = f"https://api.openweathermap.org/data/2.5/weather?id={city}&units=metric&appid={api}"
    data_request = requests.get(url)
    content = json.loads(data_request.content.decode())
    #place = content['name']
    #country = content['country']
    coords = content['coord']
    cords2 = f"lat={coords['lat']}&lon={coords['lon']}"

    return content, cords2


def fix_time(date, time_delay):
    # example 2026-04-16 15:00:00
    
    utc_dt = datetime.fromisoformat(date).replace(tzinfo=timezone.utc)
    local_dt = utc_dt - timedelta(hours=int(time_delay) / -3600)
    
    return str(local_dt)[:-6]


    

def order_data(data, time_delay=0):
    new_data = {}
    try:
        new_data['country'] = data['sys']['country']
        new_data['city'] = data['name']
    except:
        fixed_time = fix_time(data['dt_txt'], time_delay)
        new_data['date'] = fixed_time
    new_data['weather_desc'] = f"{data['weather'][0]['main']} {data['weather'][0]['description']}"
    new_data['temp'] =  f"{data['main']['temp']} °C (Feels like: {data['main']['feels_like']}°C)'"
    new_data['temp_max'] = f"{data['main']['temp_max']} °C"
    new_data['temp_min'] = f"{data['main']['temp_min']} °C"
    new_data['pressure'] = f"{data['main']['pressure']} hPa"
    new_data['humidity'] = f"{data['main']['humidity']} %"
    new_data['visibility'] = f"{float(data['visibility']) / 100} km"

    return new_data



def print_today(data):
    # For get_weather3
    print("Country: ", data['country'])
    print("City: ", data['city'])
    print("Weather: ", data['weather_desc'])

    print("Temperature: ", data['temp'])
    #print("Temperature Max: ", data['temp_max'])
    #print("Temperature Min: ", data['temp_min'])
    print("Pressure: ", data['pressure'])
    print("Humidity: ", data['humidity'])
    print("Visibility: ", data['visibility'])

    # For 
    #print(today_data)


def print_forecast_data(data):
    print(f"{data['date']}")
    print("Weather: ", data['weather_desc'])
    print("Temperature: ", data['temp'])
    # print("Temperature Max: ", data['temp_max'])
    # print("Temperature Min: ", data['temp_min'])
    print("Pressure: ", data['pressure'])
    print("Humidity: ", data['humidity'])
    print("Visibility: ", data['visibility'])



def main():
    city = "4014338"
    api = read_config()
    today_data, coords = get_weather3(api, city)

    today_data_sorted = order_data(today_data)
    forecast_data = get_weather2(api, coords, city)
    
    print("Today Weather")
    print('===================')
    print_today(today_data_sorted)
    print('===================')
    print("Forecast Weather")
    print('===================')

    time_delay = forecast_data['city']['timezone']  # Segundos
    for forescast_day in forecast_data['list']:
        forescast_day_sorted = order_data(forescast_day, time_delay)
        print_forecast_data(forescast_day_sorted)
        print('---------')
        


main()