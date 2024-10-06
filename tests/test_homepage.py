""" This class contains all tests for the home page """

import logging
import pytest
import allure
from pages.home_page import HomePage

logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("setup")
class TestHomePage:
    @allure.title("Home page: title")
    @allure.description("Check if home page of Demoblaze has correct title")
    def test_title(self):
        with allure.step("Opening home page"):
            home_page = HomePage(self.driver)
            logger.info("Open home page")
            home_page.open()
        with allure.step("Getting title of the page"):
            logger.info("Check title of the page")
            assert ("STORE" in home_page.get_title())
            logger.info("Test title passed")

    @allure.title("Home page: URL")
    @allure.description("Check if home page of Demoblaze has correct URL")
    def test_url(self):
        with allure.step("Opening home page"):
            home_page = HomePage(self.driver)
            logger.info("Open home page")
            home_page.open()
        with allure.step("Checking URL of the page"):
            logger.info("Check URL of the page")
            assert ("demoblaze.com" in home_page.get_url())
            logger.info("Test URL passed")

    @pytest.mark.smoke
    @allure.title("Home page: title contains - PRODUCT STORE")
    @allure.description("Check if home page of Demoblaze has correct title - PRODUCT STORE")
    def test_home_page_title(self):
        with allure.step("Opening home page"):
            home_page = HomePage(self.driver)
            logger.info("Open home page")
            home_page.open()
        with allure.step("Getting title of the page"):
            logger.info("Check title of the page")
            assert ("PRODUCT STORE" in home_page.get_home_page_title())
            logger.info("Test title contains PRODUCT STORE passed")

    @pytest.mark.smoke
    @allure.title("Home page: All elements exist and present")
    @allure.description("Check if home page of Demoblaze has elements exist and present")
    def test_home_page_all_elements_exist_and_present(self):
        with allure.step("Opening home page"):
            home_page = HomePage(self.driver)
            logger.info("Open home page")
            home_page.open()

        with allure.step("Checking if elements are present"):
            logger.info("Check if elements are present")
            assert home_page.check_all_elements_exist_and_present()
            logger.info("Test all elements present passed")
        