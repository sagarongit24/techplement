import argparse
import requests
import time

def get_weather(api_key, city):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(weather_data):
    if 'error' in weather_data:
        print(f"Error: {weather_data['error']['message']}")
    else:
        location = weather_data['location']['name']
        temperature = weather_data['current']['temp_c']
        condition = weather_data['current']['condition']['text']
        print(f"Weather in {location}:")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {condition}")

def main():
    parser = argparse.ArgumentParser(description="Weather Checking Application")
    parser.add_argument("-k", "--api_key", help="API key for WeatherAPI", required=True)
    parser.add_argument("-c", "--city", help="City name to check weather for", required=True)
    parser.add_argument("-r", "--refresh_interval", type=int, help="Auto-refresh interval in seconds", default=15)
    args = parser.parse_args()

    api_key = args.api_key
    city = args.city
    refresh_interval = args.refresh_interval

    while True:
        weather_data = get_weather(api_key, city)
        
        display_weather(weather_data)

        print(f"Auto-refreshing in {refresh_interval} seconds...")
        time.sleep(refresh_interval)

if __name__ == "__main__":
    main()