import configparser
import os.path
from pathlib import Path


def get_config_value(config_key: str):
    # Create a ConfigParser object
    config = configparser.ConfigParser()

    # Read the config file
    config.read(os.path.join(Path(__file__).parent.parent, "lib", "config", "app_config.ini"))

    if "browser" in config_key:
        config_section = "browser_configs"
    elif "app" in config_key:
        config_section = "application_configs"
    else:
        config_section = "credentials"

    return config.get(config_section, config_key)
