import os
import requests

from rain_check.weather_service import WeatherService

def check_weather():
    url = "https://api.open-meteo.com/v1/forecast?latitude=31.7683&longitude=35.2137&current_weather=true"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        temp = data["current_weather"]["temperature"]
        print(f"The temperature in Jerusalem right now is {temp}°C")

    except Exception as e:
        print(f"Oops, an error occurred: {e}")


def main():
    api_token = os.getenv("IMS_API_TOKEN")

    # Initialize service - using mock for now since we are developing
    service = WeatherService(token=api_token, use_mock_file=True)
    city = "raanana"

    print(f"Checking weather for {city.replace('_', ' ').title()}...")

    if service.should_take_umbrella(city):
        print("☂️ It looks like rain! Don't forget your umbrella.")
    else:
        print("☀️ No rain expected. Have a great day!")


if __name__ == "__main__":
    main()