import requests
import json
from datetime import datetime

# Script 2: Using WeatherAPI
import requests
from datetime import datetime

def get_weather_weatherapi(city, api_key):
    """
    Get weather data using WeatherAPI
    Sign up at: https://www.weatherapi.com/
    """
    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {
        'key': api_key,
        'q': city,
        'aqi': 'yes'  # Include air quality data
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        
        # Extract weather information
        weather_info = {
            'city': data['location']['name'],
            'region': data['location']['region'],
            'country': data['location']['country'],
            'temperature_c': data['current']['temp_c'],
            'temperature_f': data['current']['temp_f'],
            'condition': data['current']['condition']['text'],
            'humidity': data['current']['humidity'],
            'wind_kph': data['current']['wind_kph'],
            'wind_dir': data['current']['wind_dir'],
            'pressure_mb': data['current']['pressure_mb'],
            'uv_index': data['current']['uv'],
            'visibility_km': data['current']['vis_km'],
            'last_updated': data['current']['last_updated'],
            'air_quality': data['current'].get('air_quality', {})
        }
        
        return weather_info
        
    except requests.exceptions.RequestException as e:
        return f"Error fetching weather data: {e}"
    except KeyError as e:
        return f"Error parsing weather data: {e}"

def display_weather_weatherapi(weather_data):
    """Display weather information in a formatted way"""
    if isinstance(weather_data, dict):
        print(f"\n🌤️  Weather for {weather_data['city']}")
        print(f"📍 Location: {weather_data['region']}, {weather_data['country']}")
        print(f"📅 Last Updated: {weather_data['last_updated']}")
        print(f"🌡️  Temperature: {weather_data['temperature_c']}°C ({weather_data['temperature_f']}°F)")
        print(f"☁️  Condition: {weather_data['condition']}")
        print(f"💧 Humidity: {weather_data['humidity']}%")
        print(f"💨 Wind: {weather_data['wind_kph']} km/h {weather_data['wind_dir']}")
        print(f"🔽 Pressure: {weather_data['pressure_mb']} mb")
        print(f"☀️  UV Index: {weather_data['uv_index']}")
        print(f"👁️  Visibility: {weather_data['visibility_km']} km")
        
        # Display air quality if available
        if weather_data['air_quality']:
            aq = weather_data['air_quality']
            print(f"🏭 Air Quality:")
            if 'co' in aq:
                print(f"   CO: {aq['co']:.1f} μg/m³")
            if 'pm2_5' in aq:
                print(f"   PM2.5: {aq['pm2_5']:.1f} μg/m³")
            if 'pm10' in aq:
                print(f"   PM10: {aq['pm10']:.1f} μg/m³")
    else:
        print(weather_data)

def get_weather_forecast_weatherapi(city, api_key, days=3):
    """
    Get weather forecast using WeatherAPI
    """
    base_url = "http://api.weatherapi.com/v1/forecast.json"
    params = {
        'key': api_key,
        'q': city,
        'days': days
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        
        forecast_data = []
        for day in data['forecast']['forecastday']:
            day_info = {
                'date': day['date'],
                'max_temp_c': day['day']['maxtemp_c'],
                'min_temp_c': day['day']['mintemp_c'],
                'condition': day['day']['condition']['text'],
                'chance_of_rain': day['day']['daily_chance_of_rain'],
                'max_wind_kph': day['day']['maxwind_kph']
            }
            forecast_data.append(day_info)
        
        return forecast_data
        
    except requests.exceptions.RequestException as e:
        return f"Error fetching forecast data: {e}"
    except KeyError as e:
        return f"Error parsing forecast data: {e}"

def display_forecast(forecast_data):
    """Display forecast information"""
    if isinstance(forecast_data, list):
        print(f"\n📊 {len(forecast_data)}-Day Forecast:")
        for day in forecast_data:
            print(f"📅 {day['date']}")
            print(f"   🌡️  {day['min_temp_c']}°C - {day['max_temp_c']}°C")
            print(f"   ☁️  {day['condition']}")
            print(f"   🌧️  Rain chance: {day['chance_of_rain']}%")
            print(f"   💨 Max wind: {day['max_wind_kph']} km/h")
            print()
    else:
        print(forecast_data)

# Example usage for Script 2
if __name__ == "__main__":
    # Replace with your WeatherAPI key
    API_KEY_2 = "your_weatherapi_key_here"
    CITY_2 = "New York"  # Change to your desired city
    
    # Get current weather
    weather = get_weather_weatherapi(CITY_2, API_KEY_2)
    display_weather_weatherapi(weather)
    
    # Get forecast
    forecast = get_weather_forecast_weatherapi(CITY_2, API_KEY_2, 3)
    display_forecast(forecast)

print("\n" + "="*50)
print("💡 Setup Instructions:")
print("1. Install requests: pip install requests")
print("2. Get API keys:")
print("   - OpenWeatherMap: https://openweathermap.org/api")
print("   - WeatherAPI: https://www.weatherapi.com/")
print("3. Replace the API key variables with your actual keys")
print("4. Change the city names to your desired locations")
