""" This class contains all tests for the login page """

import logging
import pytest
import allure
from pages.login_page import LoginPage
from test_data import login_creds

logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("setup")
class TestLoginPage:
    @pytest.mark.smoke
    @allure.title("Login page: login complete")
    @allure.description("Check login complete with correct credentials")
    def test_login_complete(self):
        with allure.step("Opening login page"):
            logger.info("Open login page")
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

        with allure.step("Verify login is complete"):
            logger.info("Check login complete")
            assert login_page.check_login_complete(username=login_creds.STANDARD_USERNAME
                                                   ), "Login is not complete"

            logger.info("Test Login complete passed")

    @allure.title("Login page: close login window")
    @allure.description("Check if login window is closed")
    def test_close_login_window(self):
        with allure.step("Opening login page"):
            login_page = LoginPage(self.driver)
            logger.info("Open login page")
            login_page.open()
            login_page.open_login_window()

        with allure.step("Close login window"):
            logger.info("Click Close button in login window")
            login_page.close_login_window()

        with allure.step("Verify login window closed"):
            assert login_page.check_close_login_window(), "Login window is not closed"

            logger.info("Test login window closed passed")

    @pytest.mark.smoke
    @pytest.mark.xfail(reason="Element not found on DOM")
    @allure.title("Logout functionality")
    @allure.description("Check logout functionality after successful login")
    def test_logout(self):
        with allure.step("Opening login page"):
            logger.info("Open login page")
            login_page = LoginPage(self.driver)
            login_page.open()
            login_page.open_login_window()

        with allure.step("Set username and password"):
            logger.info("Set username and password")
            login_page.set_users_creds_input(username=login_creds.STANDARD_USERNAME,
                                             password=login_creds.STANDARD_PASSWORD)

        with allure.step("Login"):
            logger.info("Click login button")
            login_page.login()

        with allure.step("Performing logout"):
            logger.info("Click logout button")
            login_page.logout()

        with allure.step("Verify logout is successful"):
            logger.info("Check logout complete")
            assert login_page.check_logout_complete(), "Logout was not successful"

            logger.info("Test Logout passed")
