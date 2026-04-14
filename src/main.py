from src.get_data import get_forecast, get_today
from src.print_data import print_forecast, print_today
from src.data import order_today, order_forecast
#


def main(city: str, days: int):
    today_data, coords = get_today(city)

    today_data_sorted = order_today(today_data)
    forecast_data = get_forecast(coords)
    
    print("Today Weather")
    print('===================')
    print_today(today_data_sorted)
    print('===================')
    print("Forecast Weather")
    print('===================')

    time_delay = forecast_data['city']['timezone']  # Segundos
    count_days = []
    for forescast_data in forecast_data['list']:
        forescast_data_sorted, forecast_day = order_forecast(forescast_data, time_delay)

        if forecast_day not in count_days:
            count_days.append(forecast_day)
        
        if len(count_days) > days:
            break
        
        print_forecast(forescast_data_sorted)
        print('---------')
        
