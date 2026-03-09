import logging
from rain_check.notification_engine import NotificationEngine
from rain_check.settings_manager import SettingsManager
from rain_check.utils import logger_utils
from rain_check.config.logging_config import LoggingConfig
from rain_check.weather_service import WeatherService

# Create a logger
logger = logging.getLogger("rain_check")

if __name__ == "__main__":
    settings_mgr = SettingsManager()
    logger_utils.logging_setup(logger, settings_mgr, "service")

    logger.info("start RainCheck service... ")
    engine = NotificationEngine(settings_mgr, WeatherService(use_mock_file=True))
    logger.info("RainCheck Service started. Looking for rain...")
    engine.start()