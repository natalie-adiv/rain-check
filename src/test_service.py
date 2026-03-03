from weather_service import WeatherService

def run_test():
    service = WeatherService(mock_file="mock_weather.json")
    cities_to_check = ["tel_aviv", "raanana"]

    print("--- RainCheck Service Test ---")

    for city in cities_to_check:
        need_umbrella = service.should_take_umbrella(city)
        status = "Take an umbrella! ☔" if need_umbrella else "No need for an umbrella. ☀️"
        print(f"City: {city.replace('_', ' ').title():<10} | Result: {status}")


if __name__ == "__main__":
    run_test()
