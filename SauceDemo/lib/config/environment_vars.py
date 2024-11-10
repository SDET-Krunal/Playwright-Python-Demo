from SauceDemo.helper.config_reader import get_config_value


class EnvironmentConfig:
    """ Application configuration values """

    APP_URL = get_config_value("app_base_url")
    BROWSER = get_config_value("browser_name")
    STANDARD_USER_NAME = get_config_value("standard_user")
    LOCKED_OUT_USER = get_config_value("locked_out_user")
    PROBLEM_USER = get_config_value("problem_user")
    PERFORMANCE_GLITCH_USER = get_config_value("performance_glitch_user")
    PASSWORD = get_config_value("password")
