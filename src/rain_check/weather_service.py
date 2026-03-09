import json
import requests
import logging
from pathlib import Path

# Create a logger
logger = logging.getLogger(__name__)

# Finding the full path of the folder where the app is running
BASE_DIR = Path(__file__).resolve().parent

# Constructs the path to the JSON file in the same folder.
MOCK_FILE_PATH = BASE_DIR / "mock_weather.json"

class WeatherService:
    """
    A service layer for interacting with weather data.
    Supports fetching live data from the IMS API or simulating data using a local mock file.
    """

    def __init__(self, token=None, use_mock_file=False):
        """
        Initializes the weather service.

        Args:
            token (str, optional): API token for the weather service.
            use_mock_file (bool): If True, reads data from a local mock JSON file instead of the API.
        """
        self._base_url = "https://ims.gov.il/ims/node/47"   # Endpoint for daily forecast
        self._headers = {"Authorization": f"ApiToken {token}"} if token else {}
        self._use_mock_file = use_mock_file

        # Mapping cities to station identifiers
        self._city_stations = {
            "tel_aviv": "85",
            "raanana": "122"
        }

    def get_forecast(self, city):
        """
        Retrieves the weather forecast for a specified city.

        Args:
            city (str): The name of the city.

        Returns:
            dict or None: The forecast data, or None if the request fails.
        """
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
            logger.error(f"API Error: {e}")
        return None

    def read_mock(self):
        """Reads and returns forecast data from the local mock JSON file."""
        try:
            with open(MOCK_FILE_PATH, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data
        except FileNotFoundError:
            logger.error(f"Error reading mock file: {MOCK_FILE_PATH}")
            return None

    def should_take_umbrella(self, city):
        """
        Determines if an umbrella is needed based on the rain probability for the next day.

        Args:
            city (str): The name of the city to check.

        Returns:
            bool: True if the rain probability exceeds 30%, False otherwise.
        """
        data = self.get_forecast(city)
        if not data:
            return False

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