import json
from pathlib import Path

# Finding the full path of the folder where the app is running
BASE_DIR = Path(__file__).resolve().parent

class SettingsManager:
    """
    Handles persistence of application settings.
    Responsible for reading from and writing to the 'settings.json' file,
    ensuring that user preferences are maintained across sessions.
    """

    def __init__(self, filename="settings.json"):
        """Initializes the settings manager with the target file path and default configurations."""

        # Constructs the path to the settings file in the same folder
        self._file_path = BASE_DIR / filename

        # Default settings
        # Note: Using a list for 'cities' because JSON does not support sets
        self._default_settings = {
            "cities": ["raanana"],
            "notification_hour": 20
        }

    def load_settings(self):
        """
        Loads settings from the JSON configuration file.
        Returns default settings if the file does not exist or fails to load.
        """
        if not self._file_path.exists():
            return self._default_settings

        try:
            with open(self._file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error reading settings file: {e}")
            print("Return default settings")
            return self._default_settings

    def save_settings(self, **kwargs):
        """
        Updates specific keys in the settings file without overwriting the entire configuration.

        Args:
            **kwargs: Key-value pairs of settings to update (e.g., cities=["raanana"]).
        """
        # Loading all existing settings
        current_settings = self.load_settings()

        # Update specific keys
        for key, value in kwargs.items():
            current_settings[key] = value

        # Save the entire updated object back to the file
        try:
            with open(self._file_path, 'w', encoding='utf-8') as f:
                json.dump(current_settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")