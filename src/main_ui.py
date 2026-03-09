import customtkinter as ctk
import logging
from rain_check.settings_manager import SettingsManager
from rain_check.utils import ui_utils, logger_utils

# Create a logger instance
logger = logging.getLogger("rain_check")

class RainCheckApp(ctk.CTk):
    """
    The main graphical user interface for the RainCheck application.
    Provides a window for users to select cities and configure alert settings.
    """

    def __init__(self):
        """Initializes the RainCheck UI application and loads saved settings."""
        super().__init__()

        # Window settings
        self.title("RainCheck - Settings")
        width, height = 400, 300
        self.geometry(f"{width}x{height}")
        ctk.set_appearance_mode("dark")

        # Launching the Settings Manager
        self.settings_mgr = SettingsManager()
        self.saved_data = self.settings_mgr.load_settings()

        # Title
        self.label = ctk.CTkLabel(self, text="Alert settings", font=("Arial", 20, "bold"))
        self.label.pack(pady=20)

        # Variables for Checkboxes (loaded from file)
        saved_cities = self.saved_data.get("cities", [])
        self.var_tlv = ctk.BooleanVar(value="tel_aviv" in saved_cities)
        self.var_raanana = ctk.BooleanVar(value="raanana" in saved_cities)

        # Creating Checkboxes
        self.cb_tlv = ctk.CTkCheckBox(self, text="Tel Aviv", font=("Arial", 14), variable=self.var_tlv)
        self.cb_tlv.pack(pady=10)

        self.cb_raanana = ctk.CTkCheckBox(self, text="Raanana", font=("Arial", 14), variable=self.var_raanana)
        self.cb_raanana.pack(pady=10)

        # Save button
        self.save_btn = ctk.CTkButton(self, text="Save settings",  font=("Arial", 14), command=self.handle_save)
        self.save_btn.pack(pady=30)

        ui_utils.center_window(self, width, height)

    def handle_save(self):
        """Saves the selected cities from the UI checkboxes to the settings file."""
        # Collecting the new selections
        selected_cities = []
        if self.var_tlv.get():
            selected_cities.append("tel_aviv")
        if self.var_raanana.get():
            selected_cities.append("raanana")

        # Saving via the administrator (using the kwargs approach that doesn't overwrite everything)
        self.settings_mgr.save_settings(cities=selected_cities)
        logger.info(f"Settings saved: {selected_cities}")


if __name__ == "__main__":
    settings_mgr = SettingsManager()
    logger_utils.logging_setup(logger, settings_mgr, "ui")

    logger.info("start RainCheckApp...")
    app = RainCheckApp()
    app.mainloop()
    logger.info("RainCheckApp started.")