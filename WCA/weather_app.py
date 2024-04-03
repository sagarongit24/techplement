import argparse
import requests
import time

# Get the current time
current_time = time.time()
print("Current time:", current_time)

# Wait for 2 seconds
time.sleep(2)

# Get the current time again
new_time = time.time()
print("New time:", new_time)

# Calculate the time difference
time_difference = new_time - current_time
print("Time difference:", time_difference, "seconds")

# Function to fetch weather data for a specific city
def get_weather(api_key, city):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    data = response.json()
    return data

# Function to display weather information
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

# Main function to handle command-line arguments
def main():
    parser = argparse.ArgumentParser(description="Weather Checking Application")
    parser.add_argument("-k", "--api_key", help="API key for WeatherAPI", required=True)
    parser.add_argument("-c", "--city", help="City name to check weather for", required=True)
    args = parser.parse_args()

    # Fetch weather data for the specified city
    weather_data = get_weather(args.api_key, args.city)
    
    # Display weather information
    display_weather(weather_data)

if __name__ == "__main__":
    main()
