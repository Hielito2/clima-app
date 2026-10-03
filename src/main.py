from timeit import default_timer as timer

from src.get_data import get_forecast, get_today
from src.print_data import print_forecast, print_today
from src.data import order_today, order_forecast
#

class Clima:
  def __init__(self, city_code, city_name, days, verbose):
    self.city_code = city_code
    self.city_name = city_name
    self.days = days
    self.verbose = verbose


  def by_name(self):
    import requests
    import json
    url_req = requests.get(f"https://openweathermap.org/api/widget/geo?q={self.city_name}&limit=10")
    req_data = json.loads(url_req.content)
    print("== Choose the number of your city ==")
    for i, city in enumerate(req_data, start=1):
      print(f"{i}.- {city['name']} - {city['country']} - {city['state']}")

    city_option = int(input("::"))
    if city_option > len(req_data) or city_option < 1:
      return False

    city_data = req_data[city_option-1]

    self.today_data, self.coords, self.city_code  = get_today(city_coords=f"lat={city_data['lat']}&lon={city_data['lon']}")


  def measure_time(message, time_taked):
    print(f"{message} : {round(time_taked * 1000, 3)}ms")


  def print_info(self):
    today_data_sorted = order_today(self.today_data)
    print('===================')
    print("Today Weather")
    print('===================')
    print_today(today_data_sorted,  self.city_code)
    print('===================')

    if self.days == 0:
        return

    print("Forecast Weather")
    print('===================')

    if self.verbose:
        start = timer()

    forecast_data = get_forecast(self.coords)

    if self.verbose:
        end = timer()
        measure_time(f"[Debug] Milliseconds to get the data for forecast weather", (end - start)) # type: ignore

    time_delay = forecast_data['city']['timezone']  # Segundos

    for day_n in range(self.days):
        forescast_data_sorted, forecast_day = order_forecast(forecast_data['list'][day_n], time_delay)

        print_forecast(forescast_data_sorted)
        print('---------')



  def by_code(self):
    self.today_data, self.coords, self.city_code = get_today(city_code=self.city_code)



def initialize(city_code, city_name, days, verbose):
  clima = Clima(city_code, city_name, days, verbose)
  if clima.city_code != "0":
    clima.by_code()
  elif clima.city_name != "0":
    clima.by_name()
  else:
    print("IDK ?")
    return

  clima.print_info()
