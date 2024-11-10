from SauceDemo.lib.constant.Constant import Constant
from SauceDemo.pageObjects.basePage import BasePage


class SideNavigationPage(BasePage):
    """ Page object for Side navigation panel """

    def __init__(self, page):
        super().__init__(page)
        self.all_item_link = page.locator("//a[@id='inventory_sidebar_link']")
        self.about_link = page.locator("//a[@id='about_sidebar_link']")
        self.logout_link = page.locator("//a[@id='logout_sidebar_link")
        self.reset_app_state_link = page.locator("//a[@id='reset_sidebar_link")

    def click_on_side_navigation_menu(self, menu_name: str):
        """
        Click on given menu link from Side navigation panel

        :param str menu_name: side navigation menu name
        :return: None
        """
        side_nav_menu_locators = {"All Item": self.all_item_link, "About": self.about_link, "Logout": self.logout_link,
                                  "Reset App State": self.reset_app_state_link}
        side_nav_menu_locators[menu_name].press()

    def do_logout(self):
        """
        Click on logout menu from Side navigation panel

        :return: None
        """
        self.click_on_side_navigation_menu(Constant.SideNavConstants.LOGOUT)
