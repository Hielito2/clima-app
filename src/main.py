from src.get_data import new_data, get_city_names, get_coords_from_id, get_code_from_coords
from datetime import datetime
#import rich
#

class Clima:
  def __init__(self, city_code, city_name, days, verbose):
    self.city_code = city_code
    self.city_name = city_name
    self.days = days
    self.verbose = verbose
    self.coords = None
    self.country = None


  def get_coords_by_id(self):
    code_data = get_coords_from_id(self.city_code)
    self.coords = f"lat={code_data['coord']['lat']}&lon={code_data['coord']['lon']}"
    self.city_name = code_data['name']
    self.country = code_data['sys']['country']


  def get_cords_by_name(self):
    req_data = get_city_names(self.city_name)
    if len(req_data) < 1:
      raise ValueError("Cero cities found")
    
    print("== Choose the number of your city ==")
    for i, city in enumerate(req_data, start=1):
      print(f"{i} - {city['name']} - {city['country']} - {city['state']}")

    
    valid_city_option = False

    while not valid_city_option:
      city_option = int(input("::"))
      if city_option > len(req_data) or city_option < 1:
        print("Invalid city number")
        continue
      else:
        valid_city_option = True

    city_data = req_data[city_option-1]

    self.city_name = city['name']
    self.country = city['country']
    #print(city['country'])

    self.coords = f"lat={city_data['lat']}&lon={city_data['lon']}"
    # get city code
    self.city_code = get_code_from_coords(self.coords)
    


  def measure_time(message, time_taked):
    print(f"{message} : {round(time_taked * 1000, 3)}ms")

  
  def fix_hour(self, dt):
    string_hour = datetime.fromtimestamp(int(dt)).isoformat()
    new_hour = string_hour.split('T')[1] + " " + str(string_hour).split('T')[0]

    return new_hour


  def get_clima_data(self):
    today_data = {}
    hourly_data = {}
    daily_data = {}

    request_data = new_data(self.coords)
    # Today Data
    today_data['Country'] = self.country
    today_data['City'] = self.city_name
    today_data['Code'] = self.city_code
    today_data['Time'] = self.fix_hour(request_data['current']['dt'])

    current_weather = request_data['current']['weather'][0]
    today_data['Weather'] = f'{current_weather['main']} - {current_weather['description']}'
    today_data['Summary'] = f'{request_data['daily'][0]['summary']}'
    today_data['Temperature'] = str(request_data['current']['temp']) + ' °C ' + f'(Feels Like: {request_data['current']['feels_like']} °C)'
    today_data['Humidity'] = str(request_data['current']['humidity']) + ' %'
    today_data['Pressure'] = str(request_data['current']['pressure']) + ' hPa'
    today_data['Visibility'] = str(request_data['current']['visibility'] / 100) + ' km'
    
    # Hourly
    for hour in request_data['hourly']:
      hour_time = str(hour['dt']) # str(self.fix_hour(datetime.fromtimestamp().isoformat()))
      hourly_data[hour_time] = {}
      hourly_data[hour_time]['Temperature'] = str(hour['temp']) + ' °C ' + f'(Feels Like: {hour['feels_like']} °C)'
      hourly_data[hour_time]['Humidity'] = str(hour['humidity']) + ' % '
      hourly_data[hour_time]['Clouds'] = str(hour['clouds']) + ' % '
      hourly_data[hour_time]['Weather'] = f'{hour['weather'][0]['main']} - {hour['weather'][0]['description']}'
      
      #print(fix_time(str(hour['dt']), request_data['timezone_offset']))
    # Daily
    for day in request_data['daily']:
      day_time = str(day['dt']) # str(self.fix_hour(datetime.fromtimestamp().isoformat()))
      daily_data[day_time] = {}
      daily_data[day_time]['Summary'] = str(day['summary'])
      daily_data[day_time]['Temp'] = day['temp']
      daily_data[day_time]['Feels'] = day['feels_like']
      daily_data[day_time]['Clouds'] = str(day['clouds']) + ' % '
      daily_data[day_time]['Weather'] = f'{day['weather'][0]['main']} - {day['weather'][0]['description']}'


    
    return today_data, hourly_data, daily_data


def initialize(city_code, city_name, days, hours_interval, verbose):
  # Validar
  if len(city_code) != 7  and city_code != "0":
    raise ValueError("Invalid city code")


  clima = Clima(city_code, city_name, days, verbose)

  if clima.city_code != "0":
    clima.get_coords_by_id()
  elif clima.city_name != "0":
    clima.get_cords_by_name()
  else:
    raise ValueError("Not valid city code or name...")

  # Get the info
  today_data, hourly_data, daily_data = clima.get_clima_data()

  # print
  print('===================')
  print("Today Weather")
  print('===================')

  for key, data in today_data.items():
    print(f'{key}: ', data)


  if int(hours_interval) != 0:
    print('===================')
    print("Hourly forecast")
    print('===================')

    huk = 0
    for key, data in hourly_data.items():
      if huk == 0 or huk == int(hours_interval):
        huk = 1
        hour = clima.fix_hour(key)
        print(f'{hour}: ', data)
      else:
        huk+=1 


  if int(days) != 0:
    print('===================')
    print("Daily forecast")
    print('===================')

    huk = 0
    for key, data in daily_data.items():
      huk += 1
      hour = clima.fix_hour(key)
      print(f'{hour}: ', data)

      if huk == int(days):
        break
