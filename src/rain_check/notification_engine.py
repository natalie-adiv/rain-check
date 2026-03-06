import time
from datetime import datetime
from rain_check.settings_manager import SettingsManager
from rain_check.weather_service import WeatherService
from plyer import notification

class NotificationEngine:
    def __init__(self, settings_mgr: SettingsManager, weather_srv: WeatherService):
        self._settings_mgr = settings_mgr
        self.weather_srv = weather_srv
        self._has_alert_sent = False

    def start(self):
        while True:
            settings = self._settings_mgr.load_settings()
            notification_hour = settings.get("notification_hour")
            current_time = datetime.now().time()
            if current_time.hour == notification_hour:
                if not self._has_alert_sent:
                    cities_to_check = settings.get("cities", [])
                    rain_cities = [city for city in cities_to_check if self.weather_srv.should_take_umbrella(city)]
                    if len(rain_cities) > 0:
                        formatted_cities = ", ".join(rain_cities[:-1]) + f" and {rain_cities[-1]}" if len(rain_cities) > 1 else rain_cities[0]
                        self._send_system_notification(f"Rain ☔ is expected in {formatted_cities}, take an umbrella!")
                    self._has_alert_sent = True
            else:
                print("This is not the time to send an alert.")
                self._has_alert_sent = False
            time.sleep(settings.get("sleep_time", 60))

    def _send_system_notification(self, msg):
        notification.notify(title="RainCheck Alert", message=msg, app_name='RainCheck', timeout=15)
