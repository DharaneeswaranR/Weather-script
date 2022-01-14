import requests, socket
from colorama import Fore

WEATHER_API = "98eaf8d3fb414253a82134104221301" # Add your API key here

def check_connection():
    '''
    This function returns True if internet connection exists
    else it returns False
    '''
    try:
        host = socket.gethostbyname("1.1.1.1")
        s = socket.create_connection((host, 80), 2)
        s.close()
        return True
    except:
        pass

    return False

def process_response(response):
    '''
    Processes the json into python dictionary
    '''
    return eval(eval(str(response.content)))

def get_location():
    '''
    Uses ip to find the location (inaccurate)

    Replace get_location() in weather_request query with your city name if location
    is inaccurate.
    '''
    location_info = process_response((requests.get("http://ipinfo.io")))
    lat_long = location_info["loc"]
    return lat_long

def api_valid(response):
    '''
    Checks if given API is valid
    '''
    if 'error' in response.keys():
        return False
    return True


if __name__ == '__main__':
    if WEATHER_API == "":
        print(f"{Fore.BLUE}Missing: Need api key. Get it from https://www.weatherapi.com/ and add it to WEATHER_API{Fore.RESET}")
        exit()

    if not check_connection():
        print(f"{Fore.RED}Error: Internet Unavailable{Fore.RESET}")
        exit()

    weather_request = requests.get(f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API}&q={get_location()}&aqi=no")
    weather_info = process_response(weather_request)

    if not api_valid(weather_info):
        print(f"{Fore.RED}Error: API key is invalid{Fore.RESET}")
        exit()

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

    weather = f'''
{Fore.CYAN}Weather at {location}, {region}, {country}{Fore.RESET}

It is {Fore.YELLOW}{condition}{Fore.RESET} with a temp of {Fore.GREEN}{temp_c}°C ({temp_f}°F){Fore.RESET} which feels like {Fore.GREEN}{feelslike_c}°C ({feelslike_f}°F){Fore.RESET}
Wind speed is {Fore.MAGENTA}{wind_kph}kph ({wind_mph}mph){Fore.RESET} in {Fore.LIGHTYELLOW_EX}{wind_dir}{Fore.RESET}
Humidity is at {Fore.LIGHTBLUE_EX}{humidity}{Fore.RESET} and UV index is at {Fore.LIGHTBLUE_EX}{uv}{Fore.RESET}
'''

    print(weather)