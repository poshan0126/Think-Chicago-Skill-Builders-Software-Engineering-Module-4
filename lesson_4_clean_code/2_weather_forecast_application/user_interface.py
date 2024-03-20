
from weather_data import WeatherDataFetcher, DataParser

class UserInterface:
    def get_detailed_forecast(city):
        data = WeatherDataFetcher.fetch_weather_data(city)
        return DataParser.parse_weather_data(city,data)

    def display_weather(city):
        data = WeatherDataFetcher.fetch_weather_data(city)
        if not data:
            print(f"Weather data not available for {city}")
        else:
            weather_report = DataParser.parse_weather_data(city,data)
            print(weather_report)
