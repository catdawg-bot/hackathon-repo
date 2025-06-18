import requests
import json
from datetime import datetime

def get_weather_openweather(city, api_key):
    """
    Get weather data using OpenWeatherMap API
    Sign up at: https://openweathermap.org/api
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        
        # Extract weather information
        weather_info = {
            'city': data['name'],
            'country': data['sys']['country'],
            'temperature': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],
            'description': data['weather'][0]['description'],
            'wind_speed': data['wind']['speed'],
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        return weather_info
        
    except requests.exceptions.RequestException as e:
        return f"Error fetching weather data: {e}"
    except KeyError as e:
        return f"Error parsing weather data: {e}"

def display_weather_openweather(weather_data):
    """Display weather information in a formatted way"""
    if isinstance(weather_data, dict):
        print(f"\n🌤️  Weather for {weather_data['city']}, {weather_data['country']}")
        print(f"📅 Time: {weather_data['timestamp']}")
        print(f"🌡️  Temperature: {weather_data['temperature']}°C")
        print(f"🤔 Feels like: {weather_data['feels_like']}°C")
        print(f"☁️  Description: {weather_data['description'].title()}")
        print(f"💧 Humidity: {weather_data['humidity']}%")
        print(f"🔽 Pressure: {weather_data['pressure']} hPa")
        print(f"💨 Wind Speed: {weather_data['wind_speed']} m/s")
    else:
        print(weather_data)

# Example usage for Script 1
if __name__ == "__main__":
    # Replace with your OpenWeatherMap API key
    API_KEY = "your_openweathermap_api_key_here"
    CITY = "London"  # Change to your desired city
    
    weather = get_weather_openweather(CITY, API_KEY)
    display_weather_openweather(weather)

print("\n" + "="*50 + "\n")
