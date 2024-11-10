import configparser
import os.path


def get_config_value(config_key: str):
    # Create a ConfigParser object
    config = configparser.ConfigParser()

    # Read the config file
    config.read(os.path.abspath("app_config.ini"))

    if "browser" in config_key:
        config_section = "browser_configs"
    elif "app" in config_key:
        config_section = "application_configs"
    else:
        config_section = "credentials"

    return config.get(config_section, config_key)
