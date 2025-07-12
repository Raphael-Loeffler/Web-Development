import requests
from requests import Response
from dotenv import load_dotenv
import os
from pprint import pprint
from argparse import ArgumentParser


def run():
    load_dotenv()
    
    API_KEY = os.getenv("API_KEY")

    parser = ArgumentParser(description="Weather Report")
    parser.add_argument('-c', '--city', type=str, help="- Type in a city", default=None)
    parser.add_argument('-f', '--form', type=str, help="- Forms: short, medium, long, all (prints whole json file)", default="medium")
    arguments = parser.parse_args()
    
    city = arguments.city
    form = arguments.form
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"
    data: Response = requests.get(url)
    
    # HTTP STATUS CODES
    # 404: Not access
    # 200: Success
    
    # pprint(data.json()) # Remove '#' to see json data
    
    main_weather: str = data.json()['weather'][0]['main']
    temperature: float = data.json()['main']['temp']
    
    humidity: int = data.json()['main']['humidity']
    temperature_min: float = data.json()['main']['temp_min']
    temperature_max: float = data.json()['main']['temp_max']
    wind_speed: float = data.json()['wind']['speed']
    
    long: float = data.json()['coord']['lon']
    lat: float = data.json()['coord']['lat']
    country: str = data.json()['sys']['country']
    timezone: int = data.json()['timezone']
    
    
    match form:
        case "short": form = 0
        case "medium": form = 1
        case "long": form = 2
        case "all": form = 3
    
    if form == 3:
        pprint(data.json())
        return
    
    if form >= 0:
        print(f"Main Weather: {main_weather}")
        print(f"Temperature: {temperature}")
    
    if form >= 1:
        print(f"Lowest Temperature: {temperature_min}")
        print(f"Highest Temperature: {temperature_max}")
        print(f"Humidity: {humidity}")
        print(f"Wind Speed: {wind_speed}")
    
    if form == 2:
        print(f"Longitude: {long}")
        print(f"Latitude: {lat}")
        print(f"Country: {country}")
        print(f"Timezone: {timezone}")
        
        
    

"""
{'base': 'stations',
 'clouds': {'all': 0},
 'cod': 200,
 'coord': {'lat': 50.088, 'lon': 14.4208},
 'dt': 1752327600,
 'id': 3067696,
 'main': {'feels_like': 18.11,
          'grnd_level': 978,
          'humidity': 73,
          'pressure': 1012,
          'sea_level': 1012,
          'temp': 18.32,
          'temp_max': 19.03,
          'temp_min': 16.27},
 'name': 'Prague',
 'sys': {'country': 'CZ',
         'id': 2010430,
         'sunrise': 1752289566,
         'sunset': 1752347362,
         'type': 2},
 'timezone': 7200,
 'visibility': 10000,
 'weather': [{'description': 'clear sky',
              'icon': '01d',
              'id': 800,
              'main': 'Clear'}],
 'wind': {'deg': 210, 'speed': 4.12}}
"""


if __name__ == "__main__":
    run()