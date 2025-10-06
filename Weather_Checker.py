#!/usr/bin/env python3
"""
Weather Checker with Styled Output (3-day forecast, °C + °F)
Requires: pip install requests colorama
"""

import requests
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Endpoints
GEOCODE_URL = "https://nominatim.openstreetmap.org/search"
FALLBACK_GEOCODE = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

HEADERS = {"User-Agent": "WeatherChecker/2.0 (ryan@example.com)"}
REQUEST_TIMEOUT = 10

# Map codes → description + icon
WEATHER_CODE_MAP = {
    0: ("Clear sky", "☀️"),
    1: ("Mainly clear", "🌤"),
    2: ("Partly cloudy", "⛅"),
    3: ("Overcast", "☁️"),
    45: ("Fog", "🌫"),
    48: ("Depositing rime fog", "🌫"),
    51: ("Light drizzle", "🌦"),
    53: ("Moderate drizzle", "🌦"),
    55: ("Dense drizzle", "🌧"),
    61: ("Slight rain", "🌧"),
    63: ("Moderate rain", "🌧"),
    65: ("Heavy rain", "🌧"),
    71: ("Slight snow", "🌨"),
    73: ("Moderate snow", "🌨"),
    75: ("Heavy snow", "❄️"),
    80: ("Slight rain showers", "🌦"),
    81: ("Moderate rain showers", "🌦"),
    82: ("Violent rain showers", "⛈"),
    95: ("Thunderstorm", "⛈"),
    96: ("Thunderstorm with hail", "⛈"),
    99: ("Thunderstorm with heavy hail", "⛈"),
}


def get_coordinates(city):
    params = {"q": city, "format": "json", "limit": 1}
    try:
        resp = requests.get(GEOCODE_URL, params=params, headers=HEADERS, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        data = resp.json()
        if data:
            d = data[0]
            return float(d["lat"]), float(d["lon"]), d.get("display_name", city)
    except requests.RequestException:
        pass

    # Fallback
    try:
        resp2 = requests.get(FALLBACK_GEOCODE, params={"name": city, "count": 1}, timeout=REQUEST_TIMEOUT)
        resp2.raise_for_status()
        res = resp2.json().get("results")
        if res:
            r = res[0]
            return float(r["latitude"]), float(r["longitude"]), r.get("name", city)
    except requests.RequestException:
        pass

    return None


def get_weather(lat, lon):
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
        "timezone": "auto",
        "daily": "temperature_2m_max,temperature_2m_min,weathercode",
    }

    try:
        # Celsius
        resp_c = requests.get(WEATHER_URL, params=params, timeout=REQUEST_TIMEOUT)
        resp_c.raise_for_status()
        data_c = resp_c.json()

        # Fahrenheit
        params["temperature_unit"] = "fahrenheit"
        resp_f = requests.get(WEATHER_URL, params=params, timeout=REQUEST_TIMEOUT)
        resp_f.raise_for_status()
        data_f = resp_f.json()

        return data_c, data_f
    except requests.RequestException:
        return None, None


def pretty_print_weather(place_name, data_c, data_f):
    if not data_c or not data_f:
        print(Fore.RED + "❌ No weather data available.")
        return

    current_c, current_f = data_c["current_weather"], data_f["current_weather"]
    daily_c, daily_f = data_c["daily"], data_f["daily"]

    # Current
    code = current_c.get("weathercode")
    desc, icon = WEATHER_CODE_MAP.get(code, (f"Code {code}", "❓"))
    print(Fore.CYAN + f"\n🌍 Weather for {place_name}")
    print(Fore.YELLOW + "─" * 40)
    print(Fore.GREEN + "Current Conditions:")
    print(f" {icon}  {desc}")
    print(f" 🌡 Temp: {Fore.RED}{current_c['temperature']}°C{Style.RESET_ALL} / {Fore.RED}{current_f['temperature']}°F")
    print(f" 💨 Wind: {current_c['windspeed']} km/h  |  🧭 {current_c['winddirection']}°")
    print(f" ⏰ Time: {current_c['time']}")

    # Forecast
    print(Fore.YELLOW + "\n3-Day Forecast:")
    for i in range(3):
        date = daily_c["time"][i]
        tmax_c, tmin_c = daily_c["temperature_2m_max"][i], daily_c["temperature_2m_min"][i]
        tmax_f, tmin_f = daily_f["temperature_2m_max"][i], daily_f["temperature_2m_min"][i]
        code = daily_c["weathercode"][i]
        desc, icon = WEATHER_CODE_MAP.get(code, (f"Code {code}", "❓"))
        print(
            f" {date}: {icon} {desc:<20} "
            f"{Fore.BLUE}{tmin_c}°C/{tmin_f}°F{Style.RESET_ALL} – "
            f"{Fore.RED}{tmax_c}°C/{tmax_f}°F{Style.RESET_ALL}"
        )


def main():
    print(Fore.CYAN + "🌤 Weather Checker – type 'quit' to exit.\n")

    while True:
        city = input("Enter a city: ").strip()
        if not city:
            continue
        if city.lower() in {"quit", "exit", "q"}:
            print("👋 Goodbye!")
            break

        coords = get_coordinates(city)
        if not coords:
            print(Fore.RED + "❌ Could not find that city.")
            continue

        lat, lon, place = coords
        data_c, data_f = get_weather(lat, lon)
        if not data_c or not data_f:
            print(Fore.RED + "❌ Could not fetch weather data.")
            continue

        pretty_print_weather(place, data_c, data_f)
        print(Fore.YELLOW + "\n" + "─" * 40 + "\n")


if __name__ == "__main__":
    main()

