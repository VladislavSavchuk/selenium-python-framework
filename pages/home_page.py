from base.base_page import BasePage
import allure


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_page_title(self):
        """Returns the title of the page"""
        return self.driver.title
