import pytest
from playwright.sync_api import Playwright

from SauceDemo.helper.common_helpers import decrypt_string
from SauceDemo.lib.config.environment_vars import EnvironmentConfig as Config
from SauceDemo.pageObjects.HeaderPage.header_page import HeaderPage
from SauceDemo.pageObjects.LoginPage.login_page import LoginPage
from SauceDemo.pageObjects.SideNavigationPanel.side_navigation_panel import SideNavigationPage
from SauceDemo.pageObjects.basePage import BasePage


@pytest.fixture()
def initialize_browser(playwright: Playwright):
    """
    Initialize browser given in config property file

    :return: None
    """
    browser_types = {"chrome": playwright.chromium, "firefox": playwright.firefox, "webkit": playwright.webkit}
    browser = browser_types[Config.BROWSER].launch(headless=False)

    try:
        page = browser.new_page()
        base_page = BasePage(page=page)
        base_page.open_app_url()
        yield page
    finally:
        browser.close()


@pytest.fixture()
def login(initialize_browser):
    """ Perform login and logout in application before each test """
    try:
        login_page = LoginPage(initialize_browser)
        login_page.do_login(Config.STANDARD_USER_NAME, decrypt_string(Config.PASSWORD))

        yield login_page
    finally:
        HeaderPage(initialize_browser).click_on_burger_menu_btn()
        SideNavigationPage(initialize_browser).do_logout()
