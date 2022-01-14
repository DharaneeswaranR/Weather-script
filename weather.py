import requests, socket
from colorama import Fore, Style

WEATHER_API = "98eaf8d3fb414253a82134104221301"

def check_connection():
    try:
        host = socket.gethostbyname("1.1.1.1")
        s = socket.create_connection((host, 80), 2)
        s.close()
        return True
    except:
        pass

    return False

def process_response(response):
    return eval(eval(str(response.content)))

def get_location():
    location_info = process_response((requests.get("http://ipinfo.io")))
    lat_long = location_info["loc"]
    return lat_long


def display(message):
    print(message)

if __name__ == '__main__':
    if WEATHER_API == "":
        display("Need weather api")
        exit()

    if not check_connection():
        display("Internet Unavailable")
        exit()

    weather_request = requests.get(f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API}&q={'Nagercoil'}&aqi=no")
    weather_info = process_response(weather_request)

    # Weather stats
    location = weather_info['location']['name']
    region = weather_info['location']['region']
    country = weather_info['location']['country']
    temp_c = weather_info['current']['temp_c']
    temp_f = weather_info['current']['temp_f']
    condition = weather_info['current']['condition']['text']
    wind_mph = weather_info['current']['wind_mph']
    wind_kph = weather_info['current']['wind_kph']
    wind_dir = weather_info['current']['wind_dir']
    humidity = weather_info['current']['humidity']
    feelslike_c = weather_info['current']['feelslike_c']
    feelslike_f = weather_info['current']['feelslike_f']
    uv = weather_info['current']['uv']

    # Text colors and styling


    weather = f'''
Weather at {location}, {region}, {country}

{condition} {temp_c}°C ({temp_f}°F) which feels like {feelslike_c}°C ({feelslike_f}°F)
Wind speed is {wind_kph}kph ({wind_mph}mph) in {wind_dir}
Humidity is at {humidity} and UV index is at {uv}
'''

    display(weather)