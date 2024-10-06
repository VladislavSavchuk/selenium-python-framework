""" This class contains all tests for the login page """

import logging
import pytest
import allure
from pages.login_page import LoginPage
from test_data import login_creds

logger = logging.getLogger(__name__)


@pytest.mark.smoke
@pytest.mark.usefixtures("setup")
class TestLoginPage:
    @allure.title("Login page: login complete")
    @allure.description("Check login complete with correct credentials")
    def test_login_complete(self):
        with allure.step("Opening login page"):
            login_page = LoginPage(self.driver)
            logger.info("Open login page")
            login_page.open()
            login_page.open_login_window()

        with allure.step("Set username and password"):
            logger.info("Set username and password")
            login_page.set_users_creds_input(username=login_creds.STANDARD_USERNAME,
                                             password=login_creds.STANDARD_PASSWORD)

        with allure.step("Login"):
            logger.info("Click login button")
            login_page.login()

        with ((allure.step("Check login"))):
            logger.info("Check login complete")
            assert login_page.check_login_complete(username=login_creds.STANDARD_USERNAME
                                                   ), "Login is not complete"
            logger.info("Test login complete passed")
        