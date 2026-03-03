import json
import os

from debugpy.common.timestamp import current


class SettingsManager:
    def __init__(self, filename="settings.json"):
        # Finding the full path of the folder where the app is running
        self._current_dir = os.path.dirname(os.path.abspath(__file__))
        self._file_path = os.path.join(self._current_dir, filename)

        # Default settings
        self._default_settings = {
            "cities": {"raanana"},
            "notification_hour": 20
        }

    def load_settings(self):
        if not os.path.exists(self._file_path):
            return self._default_settings

        try:
            with open(self._file_path, 'r', encoding='uft-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error reading settings file: {e}")
            print("Return default settings")
            return self._default_settings

    def save_settings(self, **kwargs):
        """
        Accepts arguments named (kwargs) and updates only those in the existing file.
        Example usage: save_settings(cities=["raanana"])
        """
        # Loading all existing settings
        current_settings = self.load_settings()

        for key, value in kwargs.items():
            current_settings[key] = value

        # Save the entire updated object back to the file
        try:
            with open(self._file_path, 'w', encoding='utf-8') as f:
                json.dump(current_settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")