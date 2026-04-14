from src.get_data import get_forecast, get_today
from src.print_data import print_forecast, print_today
from src.data import order_data
#




def main(city: str):
    today_data, coords = get_today(city)

    today_data_sorted = order_data(today_data)
    forecast_data = get_forecast(coords)
    
    print("Today Weather")
    print('===================')
    print_today(today_data_sorted)
    print('===================')
    print("Forecast Weather")
    print('===================')

    time_delay = forecast_data['city']['timezone']  # Segundos
    for forescast_day in forecast_data['list']:
        forescast_day_sorted = order_data(forescast_day, time_delay)
        print_forecast(forescast_day_sorted)
        print('---------')
        
