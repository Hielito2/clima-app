from datetime import datetime, timedelta, timezone

def fix_time(date, time_delay):    
    utc_dt = datetime.fromisoformat(date).replace(tzinfo=timezone.utc)
    local_dt = utc_dt - timedelta(hours=int(time_delay) / -3600)
    
    return str(local_dt)[:-6]


def order_today(data):
    new_data = {}
    new_data['country'] = data['sys']['country']
    new_data['city'] = data['name']

    new_data['weather_desc'] = f"{data['weather'][0]['main']} {data['weather'][0]['description']}"
    new_data['temp'] =  f"{data['main']['temp']} °C (Feels like: {data['main']['feels_like']}°C)"
    new_data['temp_max'] = f"{data['main']['temp_max']} °C"
    new_data['temp_min'] = f"{data['main']['temp_min']} °C"
    new_data['pressure'] = f"{data['main']['pressure']} hPa"
    new_data['humidity'] = f"{data['main']['humidity']} %"
    new_data['visibility'] = f"{float(data['visibility']) / 1000} km"

    return new_data


def order_forecast(data, time_delay):
    new_data = {}
    #print(data['dt_txt'], time_delay)
    fixed_time = fix_time(data['dt_txt'], time_delay)
    new_data['date'] = fixed_time
    new_data['weather_desc'] = f"{data['weather'][0]['main']} {data['weather'][0]['description']}"
    new_data['temp'] =  f"{data['main']['temp']} °C (Feels like: {data['main']['feels_like']}°C)"
    new_data['temp_max'] = f"{data['main']['temp_max']} °C"
    new_data['temp_min'] = f"{data['main']['temp_min']} °C"
    new_data['pressure'] = f"{data['main']['pressure']} hPa"
    new_data['humidity'] = f"{data['main']['humidity']} %"
    new_data['visibility'] = f"{float(data['visibility']) / 1000} km"

    return new_data, fixed_time.split(' ')[0]