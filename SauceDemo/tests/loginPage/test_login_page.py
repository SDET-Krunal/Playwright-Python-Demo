import pytest
from playwright.sync_api import expect

from SauceDemo.lib.constant.Constant import Constant
from SauceDemo.pageObjects.HeaderPage.header_page import HeaderPage


@pytest.mark.usefixtures('login')
class TestLoginPage:
    """ Covers User Login related test cases """

    def test_login_with_associated_users(self, login):
        """
        Scenario:
            [x] Verify standard user is able to login successfully in application.
        """

        expect(HeaderPage(login).).to_have_text(Constant.HeaderConstant.PRODUCTS)
