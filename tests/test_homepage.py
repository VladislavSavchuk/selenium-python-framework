import pytest
import allure
from pages.home_page import HomePage


@pytest.mark.usefixtures("setup")
class TestHomePage:
    @allure.title("Home page - smoke test")
    @allure.description("Check if home page of Demoblaze has correct title")
    def test_homepage_title(self):
        home_page = HomePage(self.driver)
        home_page.open()

        assert ("STORE" in home_page.get_page_title())
        