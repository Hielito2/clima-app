from datetime import datetime
from zoneinfo import ZoneInfo

from get_data import (
    get_city_names,
    get_code_from_coords,
    get_coords_from_id,
    new_data,
)
from print_rich import rich_print


class Clima:
    def __init__(self, city_code, city_name, days, hours_interval, verbose):
        self.city_code = city_code
        self.city_name = city_name
        self.days = days
        self.hours_interval = hours_interval
        self.verbose = verbose
        self.coords = None
        self.country = None

    def fix_hour(self, timestamp, timezone_api):
        local_dt = datetime.fromtimestamp(timestamp, tz=ZoneInfo(timezone_api))
        return str(local_dt)[:-6]

    def get_coords_by_id(self):
        code_data = get_coords_from_id(self.city_code)
        self.coords = f"lat={code_data['coord']['lat']}&lon={code_data['coord']['lon']}"
        self.city_name = code_data["name"]
        self.country = code_data["sys"]["country"]

    def get_cords_by_name(self):
        req_data = get_city_names(self.city_name)
        if len(req_data) < 1:
            raise ValueError("Cero cities found")

        print("== Choose the number of your city ==")
        for i, city in enumerate(req_data, start=1):
            print(f"{i} - {city['name']} - {city['country']} - {city['state']}")

        while True:
            try:
                city_option = int(input("::").strip())
                if city_option > len(req_data) or city_option < 1:
                    print("Invalid city number")
                else:
                    break
            except ValueError:
                print("Invalid city number")

        city_data = req_data[city_option - 1]

        self.city_name = city["name"]
        self.country = city["country"]

        self.coords = f"lat={city_data['lat']}&lon={city_data['lon']}"
        self.city_code = get_code_from_coords(self.coords)

    def measure_time(message, time_taked):
        print(f"{message} : {round(time_taked * 1000, 3)}ms")

    def get_clima_data(self):
        self.today_data = {}
        self.hourly_data = {}
        self.daily_data = {}

        request_data = new_data(self.coords)
        # Today Data
        self.today_data["Country"] = self.country
        self.today_data["City"] = self.city_name
        self.today_data["Code"] = self.city_code
        self.today_data["Time"] = self.fix_hour(
            request_data["current"]["dt"], timezone_api=request_data["timezone"]
        )

        current_weather = request_data["current"]["weather"][0]
        self.today_data["Weather"] = (
            f"{current_weather['main']} - {current_weather['description']}"
        )

        self.today_data["Summary"] = f"{request_data['daily'][0]['summary']}"
        self.today_data["Temperature"] = (
            str(request_data["current"]["temp"])
            + " °C "
            + f"(Feels Like: {request_data['current']['feels_like']} °C)"
        )
        self.today_data["Humidity"] = str(request_data["current"]["humidity"]) + " %"
        self.today_data["Pressure"] = str(request_data["current"]["pressure"]) + " hPa"
        self.today_data["Visibility"] = (
            str(request_data["current"]["visibility"] / 100) + " km"
        )

        # Hourly
        for hour in request_data["hourly"]:
            hour_time = self.fix_hour(hour["dt"], timezone_api=request_data["timezone"])
            self.hourly_data[hour_time] = {}
            self.hourly_data[hour_time]["Temperature"] = (
                str(hour["temp"]) + " °C " + f"(Feels Like: {hour['feels_like']} °C)"
            )
            self.hourly_data[hour_time]["Humidity"] = str(hour["humidity"]) + " % "
            self.hourly_data[hour_time]["Clouds"] = str(hour["clouds"]) + " % "
            self.hourly_data[hour_time]["Weather"] = (
                f"{hour['weather'][0]['main']} - {hour['weather'][0]['description']}"
            )

        # Daily
        for day in request_data["daily"]:
            day_time = self.fix_hour(day["dt"], timezone_api=request_data["timezone"])
            self.daily_data[day_time] = {}
            self.daily_data[day_time]["Summary"] = str(day["summary"])
            self.daily_data[day_time]["Temp"] = day["temp"]
            self.daily_data[day_time]["Feels"] = day["feels_like"]
            self.daily_data[day_time]["Clouds"] = str(day["clouds"]) + " % "
            self.daily_data[day_time]["Weather"] = (
                f"{day['weather'][0]['main']} - {day['weather'][0]['description']}"
            )

    def print_rich(self):
        rich_print(
            self.today_data,
            self.hourly_data,
            self.daily_data,
            self.days,
            self.hours_interval,
        )


def initialize(city_code, city_name, days, hours_interval, verbose):
    # Validar
    if len(city_code) != 7 and city_code != "0":
        raise ValueError("Invalid city code")

    clima = Clima(city_code, city_name, days, hours_interval, verbose)

    if clima.city_code != "0":
        clima.get_coords_by_id()
    elif clima.city_name != "0":
        clima.get_cords_by_name()
    else:
        raise ValueError("Not valid city code or name...")

    # Get the info
    clima.get_clima_data()
    # Print Weather
    clima.print_rich()
