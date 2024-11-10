from playwright.sync_api import Playwright

from SauceDemo.lib.config.environment_vars import EnvironmentConfig


class BasePage(object):
    """ Defines common properties and methods inherited by all page objects """

    def __init__(self, page):
        self.page = page
        self.url = EnvironmentConfig.APP_URL + 'v1/'
        self.base_url = self.url

    def open_app_url(self) -> None:
        """
        Hit application URL in browser

        :returns: None
        """
        self.page.goto(EnvironmentConfig.APP_URL)

    def initialize_browser(self, playwright: Playwright):
        """
        Initialize browser given in config property file

        :return: None
        """
        browser_types = {"chrome": playwright.chromium, "firefox": playwright.firefox, "webkit": playwright.webkit}
        browser = browser_types[EnvironmentConfig.BROWSER].launch(headless=False)
        self.page = browser.new_page()

    def get_href_from_link(self) -> str:
        """
        Fetch the 'href' attribute value from a link element

        :return: link url
        :rtype: str
        """
        return self.page.get_by_role("link").get_attribute('href')
