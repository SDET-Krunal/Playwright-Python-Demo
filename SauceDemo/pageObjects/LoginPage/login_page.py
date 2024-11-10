from SauceDemo.pageObjects.basePage import BasePage


class LoginPage(BasePage):
    """ Page object for Login Page """

    def __init__(self, page):
        super().__init__(page)
        self.user_name = page.locator("//input[@id='user-name']")
        self.password = page.locator("//input[@id='password']")
        self.login_btn = page.locator("//input[@id='login-button")

    def enter_user_name(self, text):
        """
        Enter text value into username textfield

        :param str text: value to be entered
        :return: None
        """
        self.user_name.fill(text)

    def enter_password(self, text):
        """
        Enter text value into password textfield

        :param str text: value to be entered
        :return: None
        """
        self.password.fill(text)

    def click_on_login_btn(self):
        """
        Click on login button

        :return: None
        """
        self.login_btn.press()

    def do_login(self, user_name: str, password: str):
        """
        Perform login with given username and password value

        :param str user_name: username to be entered
        :param str password: password to be entered
        :return: None
        """
        self.enter_user_name(user_name)
        self.enter_password(password)
        self.click_on_login_btn()
