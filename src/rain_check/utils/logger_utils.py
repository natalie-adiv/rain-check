import logging
import os.path
from rain_check.settings_manager import SettingsManager
from rain_check.config.logging_config import LoggingConfig
from pythonjsonlogger import json


def create_directories(file_name):
    """Extracts the directory path from a filename and creates it if it does not exist."""
    dir_name = os.path.dirname(file_name)
    try:
        os.makedirs(dir_name, exist_ok=True)
    except OSError as e:
        print(f"Error creating directories: {e}")

def logging_setup(logger, settings_mgr : SettingsManager, system: str):
    """
    Configures the specified logger with file and console handlers based on settings.

    Args:
        logger (logging.Logger): The logger instance to configure.
        settings_mgr (SettingsManager): Manager to load logging configurations.
        system (str): The system identifier (e.g., 'ui', 'service') to append to the log filename.
    """
    logging_config = LoggingConfig(settings_mgr)
    logger.setLevel(logging_config.get_level())
    if logging_config.is_file_type_json():
        create_json_file_handler(logger, logging_config, system)
    else:
        create_log_file_handler(logger, logging_config, system)

    create_console_handler(logger, logging_config)

def create_log_file_handler(logger, logging_config: LoggingConfig, system: str):
    """Creates and attaches a standard text file handler to the logger."""
    file_name = logging_config.get_file_name()
    len_till_extension = file_name.rfind(".")
    file_name = f"{file_name[:len_till_extension]}-{system}{file_name[len_till_extension:]}"
    create_directories(file_name[:])

    # Create a FileHandler to write logs to a file
    log_file_handler = logging.FileHandler(file_name, mode=logging_config.get_mode())

    # Define and set formatter with clean timestamp
    formatter = logging.Formatter(fmt=logging_config.get_message_format(), datefmt=logging_config.get_date_format())

    # Set the formatter for the handler
    log_file_handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(log_file_handler)

def create_json_file_handler(logger, logging_config: LoggingConfig, system: str):
    """Creates and attaches a JSON formatted file handler to the logger."""
    file_name = logging_config.get_file_name()
    len_till_extension = file_name.rfind(".")
    file_name = f"{file_name[:len_till_extension]}-{system}{file_name[len_till_extension:]}"
    create_directories(file_name)

    # Create a FileHandler to write logs to a json file
    log_file_handler = logging.FileHandler(file_name, mode=logging_config.get_mode())

    # Create the JsonFormatter
    jsonformatter = json.JsonFormatter(fmt=logging_config.get_message_format(), datefmt=logging_config.get_date_format(), rename_fields={"levelname": "level", "asctime": "date"})

    # Set the formatter for the handler
    log_file_handler.setFormatter(jsonformatter)

    # Add the handler to the logger
    logger.addHandler(log_file_handler)

def create_console_handler(logger, logging_config: LoggingConfig):
    """Creates and attaches a console stream handler to the logger."""
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter(fmt=logging_config.get_message_format(), datefmt=logging_config.get_date_format())
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)