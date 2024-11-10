from SauceDemo.pageObjects.basePage import BasePage


class HeaderPage(BasePage):
    """ Page object for Header Page """

    def __init__(self, page):
        super().__init__(page)
        self.burger_menu_btn = page.locator("//button[@id='react-burger-menu-btn']")
        self.cart_icon = page.locator("//a[@data-test='shopping-cart-link']")
        self.page_title = page.locator("//span[@data-test='title']")

    def click_on_burger_menu_btn(self):
        """
        Click on burger menu icon from Header

        :return: None
        """
        self.burger_menu_btn.click()

    def click_on_shopping_cart_icon(self):
        """
        Click on shopping cart icon from Header

        :return: None
        """
        self.cart_icon.click()
