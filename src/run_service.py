from rain_check.notification_engine import NotificationEngine
from rain_check.settings_manager import SettingsManager
from rain_check.weather_service import WeatherService

from plyer import notification
if __name__ == "__main__":
    engine = NotificationEngine(SettingsManager(), WeatherService(use_mock_file=True))

    print("RainCheck Service started. Looking for rain...")
    engine.start()