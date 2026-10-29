
def new_print_todat(data):
    pass



def print_today(data, city_code):
    print("Country: ", data['country'])
    print("City: ", data['city'])
    print("City code: ", city_code)
    print("clima: ", data['clima'])
    print("descripcion: ", data['descripcion'])
    print("Weather: ", data['weather_desc'])
    print("Temperature: ", data['temp'])
    print("Pressure: ", data['pressure'])
    print("Humidity: ", data['humidity'])
    print("Visibility: ", data['visibility'])



def print_forecast(data):
    print(f"{data['date']}")
    print("Weather: ", data['weather_desc'])
    print("Temperature: ", data['temp'])
    print("Pressure: ", data['pressure'])
    print("Humidity: ", data['humidity'])
    print("Visibility: ", data['visibility'])
