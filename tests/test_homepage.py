import logging
import pytest
import allure
from pages.home_page import HomePage

logger = logging.getLogger(__name__)


@pytest.mark.smoke
@pytest.mark.usefixtures("setup")
class TestHomePage:
    @allure.title("Home page - smoke test")
    @allure.description("Check if home page of Demoblaze has correct title")
    def test_homepage_title(self):
        with allure.step("Opening home page"):
            home_page = HomePage(self.driver)
            logger.info("Open home page")
            home_page.open()
        with allure.step("Getting title of the page"):
            logger.info("Check title of the page")
            assert ("STORE" in home_page.get_page_title())
        