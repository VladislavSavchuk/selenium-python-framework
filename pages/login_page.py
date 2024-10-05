"""
This module contains the LogInPage class which provides
common functionalities for interacting with web pages
using Selenium WebDriver.

"""

import logging
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from test_data import login_creds


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.home_page_login_btn = (By.ID, "login2")
        self.home_page_profile_btn = (By.ID, "nameofuser")
        self.home_page_logout_btn = (By.ID, "logout2")
        self.login_page_username_input = (By.ID, "loginusername")
        self.login_page_password_input = (By.ID, "loginpassword")
        self.login_page_login_btn = (By.XPATH, "//button[contains(text(),'Log in')]")
        self.login_page_close_btn = (By.LINK_TEXT, "Close")

    def open_login_window(self):
        logging.info("Wait for element to be present and click login button")
        self.wait_for_element_to_be_present(self.home_page_login_btn)
        self.click_element(self.home_page_login_btn)

    def set_users_creds_input(self, username, password):
        """ Enter the username and password. """

        logging.info("Wait for element to be present and enter username")
        self.wait_for_element_to_be_present(self.login_page_username_input)
        self.enter_text(self.login_page_username_input, username)

        logging.info("Wait for element to be present and enter password")
        self.wait_for_element_to_be_present(self.login_page_password_input)
        self.enter_text(self.login_page_password_input, password)

    def login(self):
        logging.info("Wait for element to be present and click login button")
        self.wait_for_element_to_be_present(self.login_page_login_btn)
        self.click_element(self.login_page_login_btn)

    def close_login_window(self):
        logging.info("Wait for element to be present and click close button")
        self.wait_for_element_to_be_present(self.login_page_close_btn)
        self.click_element(self.login_page_close_btn)

    def check_login_complete(self, username):
        """ Checks if the login is complete. """

        logging.info("Wait for element to be present and check login complete")
        if self.wait_for_element_to_be_present(self.home_page_profile_btn):
            profile_greet = self.get_text(self.home_page_profile_btn).strip()

            logging.info(f"Profile greeting: {profile_greet}")
            if profile_greet == f'Welcome {username}':
                return True

        logging.warning("Login check failed")
        return False

    def logout(self):
        logging.info("Wait for element to be present and click logout button")
        self.click_element(self.home_page_profile_btn)
