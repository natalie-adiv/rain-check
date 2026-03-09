from rain_check.settings_manager import SettingsManager

class LoggingConfig:
    """
    A configuration object that parses logging-related settings from the settings manager.
    It provides a centralized way to access log levels, formats, and file paths.
    """

    def __init__(self, settings_mgr: SettingsManager):
        """
        Loads logging configurations from settings and sets fallback values for missing keys.

        Args:
            settings_mgr (SettingsManager): Manager for application settings.
        """
        logging = settings_mgr.load_settings().get("logging", {})
        log_file = logging.get("log_file")
        file_type = logging.get("file_type")
        mode = logging.get("mode")
        level = logging.get("level")
        message_format = logging.get("message_format")
        date_format = logging.get("date_format")

        self._file_name = log_file if log_file else "logs/rain_check.log"
        self._file_type = file_type if file_type else "text"
        self._mode = mode if mode else "a"
        self._level = level if level else "INFO"
        self._message_format = message_format if message_format else "%(asctime)s - %(levelname)s - %(name)s - %(lineno)d - %(message)s"
        self._date_format = date_format if date_format else "%Y-%m-%d %H:%M:%S"

    def get_file_name(self):
        return self._file_name

    def get_file_type(self):
        return self._file_type

    def is_file_type_json(self):
        return True if self._file_type == "json" else False

    def is_file_type_text(self):
        return True if self._file_type == "text" else False

    def get_mode(self):
        return self._mode

    def get_level(self):
        return self._level

    def get_message_format(self):
        return self._message_format

    def get_date_format(self):
        return self._date_format