from timeit import default_timer as timer

from src.get_data import get_forecast, get_today
from src.print_data import print_forecast, print_today
from src.data import order_today, order_forecast
#

def measure_time(message, time_taked):
    print(f"{message} : {round(time_taked * 1000, 3)}ms")


def main(city: int, days: int, verbose: bool):



    if verbose:
        start = timer()
    
    today_data, coords = get_today(city)

    if verbose:
        end = timer()
        measure_time(f"[Debug] Milliseconds to get the data for today weather", (end - start)) # type: ignore

    
    today_data_sorted = order_today(today_data)
    print('===================')
    print("Today Weather")
    print('===================')
    print_today(today_data_sorted)
    print('===================')

    if days == 0:
        return
    
    print("Forecast Weather")
    print('===================')

    if verbose:
        start = timer()
    forecast_data = get_forecast(coords)

    if verbose:
        end = timer()
        measure_time(f"[Debug] Milliseconds to get the data for forecast weather", (end - start)) # type: ignore

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
        
