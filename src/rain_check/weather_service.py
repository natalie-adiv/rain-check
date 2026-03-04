import json
import requests
from pathlib import Path

# Finding the full path of the folder where the app is running
BASE_DIR = Path(__file__).resolve().parent

# Constructs the path to the JSON file in the same folder.
MOCK_FILE_PATH = BASE_DIR / "mock_weather.json"

class WeatherService:
    def __init__(self, token=None, use_mock_file=False):
        self._base_url = "https://ims.gov.il/ims/node/47"   # Endpoint for daily forecast
        self._headers = {"Authorization": f"ApiToken {token}"} if token else {}
        self._use_mock_file = use_mock_file

        # Mapping cities to station identifiers
        self._city_stations = {
            "tel_aviv": "85",
            "raanana": "122"
        }

    def get_forecast(self, city):
        if city is None:
            return None
        if self._use_mock_file:
            data = self.read_mock()
            if not data:
                return None
            return data[city]

        station_id = self._city_stations.get(city.lower())
        if not station_id:
            return None

        try:
            # Calling the API for a forecast
            response = requests.get(f"{self._base_url}/{station_id}", headers=self._headers)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            print(f"API Error: {e}")
        return None

    def read_mock(self):
        try:
            with open(MOCK_FILE_PATH, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data
        except FileNotFoundError:
            print(f"Error reading mock file: {MOCK_FILE_PATH}")
            return None

    def should_take_umbrella(self, city):
        data = self.get_forecast(city)
        if not data:
            return False

        # Logic: We'll check the forecast for tomorrow
        # In the IMS data, we look for the Daily Forecast and analyze the chances of rain
        # This is where your logic comes in: for example, if the Rain probability > 30%
        # or if "Rain" appears in the weather description.
        forecast_list = data.get('forecast', [])

        # Check that there are at least two members (today and tomorrow)
        if len(forecast_list) < 2:
            return False

        forecast_tomorrow = forecast_list[1]
        rain_chance = forecast_tomorrow.get('rain_prob', 0)

        '''
        # Adding a check on the text
        description = forecast_tomorrow.get('weather_description', '').lower()        
        return rain_chance > 30 or "rain" in description or "showers" in description
        '''
        return rain_chance > 30