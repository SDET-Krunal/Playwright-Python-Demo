from SauceDemo.pageObjects.basePage import BasePage


class HeaderPage(BasePage):
    """ Page object for Header Page """

    def __init__(self, page):
        super().__init__(page)
        self.burger_menu_btn = page.locator("//a[@id='react-burger-menu-btn']")
        self.cart_icon = page.locator("//a[@id='shopping_cart_link']")

    def click_on_burger_menu_btn(self):
        """
        Click on burger menu icon from Header

        :return: None
        """
        self.burger_menu_btn.press()

    def click_on_shopping_cart_icon(self):
        """
        Click on shopping cart icon from Header

        :return: None
        """
        self.cart_icon.press()
