

def print_today(data):
    print("Country: ", data['country'])
    print("City: ", data['city'])
    print("Weather: ", data['weather_desc'])

    print("Temperature: ", data['temp'])
    #print("Temperature Max: ", data['temp_max'])
    #print("Temperature Min: ", data['temp_min'])
    print("Pressure: ", data['pressure'])
    print("Humidity: ", data['humidity'])
    print("Visibility: ", data['visibility'])



def print_forecast(data):
    print(f"{data['date']}")
    print("Weather: ", data['weather_desc'])
    print("Temperature: ", data['temp'])
    # print("Temperature Max: ", data['temp_max'])
    # print("Temperature Min: ", data['temp_min'])
    print("Pressure: ", data['pressure'])
    print("Humidity: ", data['humidity'])
    print("Visibility: ", data['visibility'])