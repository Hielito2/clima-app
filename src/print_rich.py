from rich import box
from rich.console import Console
from rich.table import Table
from rich.text import Text

console = Console()


def _temp_style(t: float) -> str:
    if t <= 0:
        return "bold cyan"
    if t <= 13:
        return "bold blue"
    if t <= 25:
        return "bold green"
    if t <= 34:
        return "bold yellow"
    return "bold red"


def print_today(today_data) -> None:
    today = Table(
        title="Today Weather",
        box=box.ROUNDED,
        title_style="bold magenta",
        show_header=False,
        padding=(0, 2),
    )
    today.add_column("Field", style="bold cyan", no_wrap=True)
    today.add_column("Value", style="white")

    for key, data in today_data.items():
        today.add_row(key, str(data))

    console.print(today)


def print_hourly(hourly_data, hours_interval) -> None:
    hourly = Table(
        title="Hourly Forecast",
        box=box.SIMPLE_HEAVY,
        title_style="bold magenta",
        header_style="bold white on dark_blue",
    )
    hourly.add_column("Time", style="bold cyan", no_wrap=True)
    hourly.add_column("Temp", justify="left")
    hourly.add_column("Humidity", justify="right")
    hourly.add_column("Clouds", justify="right")
    hourly.add_column("Weather", style="italic")

    huk = 0
    for key, data in hourly_data.items():
        if huk != 0 and huk != int(hours_interval):
            huk += 1
            continue

        huk = 1

        hour = key

        main = data.get("Temperature")

        hourly.add_row(
            hour,
            Text("🌡️" + main, style=_temp_style(float(main.split(" ")[0]))),
            "🫧" + data.get("Humidity", "—"),
            "☁️" + data.get("Clouds", "—"),
            data.get("Weather", "—"),
        )

    console.print(hourly)


def print_daily(daily_data, days) -> None:
    daily = Table(
        title="Daily Forecast",
        box=box.SIMPLE_HEAVY,
        title_style="bold magenta",
        header_style="bold white on dark_blue",
    )
    daily.add_column("Date", style="bold cyan", no_wrap=True)
    daily.add_column("min temp")
    daily.add_column("max temp")
    daily.add_column("Clouds")
    daily.add_column("Weather", style="italic")
    daily.add_column("Summary", style="italic")

    for i, (key, data) in enumerate(daily_data.items()):
        if i == 0:
            pass
        elif i + 1 > int(days):
            break

        day = key

        daily.add_row(
            day,
            f"{data['Temp']['min']}",
            f"{data['Temp']['max']}",
            data.get("Clouds"),
            data.get("Weather"),
            data.get("Summary"),
        )

        if i + 1 == int(days):
            break

    console.print(daily)


def rich_print(today_data, hourly_data, daily_data, days, hours_interval) -> None:

    # TODAY
    print_today(today_data)

    # HOUR
    if int(hours_interval) != 0:
        print_hourly(hourly_data, hours_interval)

    # DAYS
    if int(days) != 0:
        print_daily(daily_data, days)
