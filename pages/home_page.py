""" This module contains the HomePage class which provides
common functionalities for interacting with web pages
using Selenium WebDriver.
"""

import logging
from random import randrange
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.home_page_title = (By.CLASS_NAME, "navbar-brand")
        self.home_page_header = (By.CLASS_NAME, "navbar-collapse")
        self.home_page_home_btn = (By.XPATH, "//a[contains(text(),'Home')]")
        self.home_page_contact_btn = (By.XPATH, "//a[contains(text(),'Contact')]")
        self.home_page_about_us_btn = (By.XPATH, "//a[@data-target='#videoModal']")
        self.home_page_cart_btn = (By.ID, "cartur")
        self.home_page_login_btn = (By.ID, "login2")
        self.home_page_signup_btn = (By.ID, "signin2")
        self.home_page_carousel = (By.CLASS_NAME, "carousel-inner")
        self.home_page_carousel_next_icon_btn = (By.CLASS_NAME, "carousel-control-next-icon")
        self.home_page_carousel_prev_icon_btn = (By.CLASS_NAME, "carousel-control-prev-icon")
        self.home_page_category_btn = (By.ID, "cat")
        self.home_page_phones_btn = (By.XPATH, "//a[contains(text(),'Phones')]")
        self.home_page_laptops_btn = (By.XPATH, "//a[contains(text(),'Laptops')]")
        self.home_page_monitors_btn = (By.XPATH, "//a[contains(text(),'Monitors')]")
        self.home_page_products_list = (By.ID, "tbodyid")
        self.home_page_product_image = (By.CLASS_NAME, "card-img-top img-fluid")
        self.home_page_product_title = (By.CLASS_NAME, "hrefch")
        self.home_page_product_price = (By.XPATH, "//div[@class='card-block']//h5")
        self.home_page_product_desc = (By.ID, "article")
        self.home_page_previous_btn = (By.ID, "prev2")
        self.home_page_next_btn = (By.ID, "next2")
        self.home_page_footer = (By.ID, "footc")

    def get_title(self):
        """Returns the title of the page"""
        return self.driver.title

    def get_url(self):
        """Returns the URL of the page"""
        return self.driver.current_url

    def get_home_page_title(self):
        """Returns the title of the page"""
        return self.get_text(self.home_page_title)

    def check_element_exist_and_present(self, element):
        try:
            self.wait_for_element_to_be_present(element)
            if not self.is_element_visible(element):
                logging.info(f"Element not found: {element}")
        except TimeoutException:
            return False
        return True

    def check_products_exist(self):
        """ Returns elements if found, TimeoutException otherwise """
        try:
            self.wait_for_all_elements_to_be_present(self.home_page_products_list)
        except TimeoutException:
            return False
        return True

    def check_all_elements_exist_and_present(self):
        """ Returns elements if found, TimeoutException otherwise """
        elements = [self.home_page_title,
                    self.home_page_header,
                    self.home_page_home_btn,
                    self.home_page_contact_btn,
                    self.home_page_about_us_btn,
                    self.home_page_cart_btn,
                    self.home_page_login_btn,
                    self.home_page_signup_btn,
                    self.home_page_carousel,
                    self.home_page_carousel_next_icon_btn,
                    self.home_page_carousel_prev_icon_btn,
                    self.home_page_category_btn,
                    self.home_page_phones_btn,
                    self.home_page_laptops_btn,
                    self.home_page_monitors_btn,
                    self.home_page_products_list,
                    self.home_page_previous_btn,
                    self.home_page_next_btn,
                    self.home_page_footer
                    ]
        try:
            for item in elements:
                self.wait_for_element_to_be_present(item)
                if not self.is_element_visible(item):
                    logging.info(f"Element not found: {item}")
        except TimeoutException:
            return False
        return True

    def get_all_products_titles(self):
        """ Returns list of all products titles in order they're displayed
            on the page """
        return self.get_all_elements_texts(self.home_page_product_title)

    def get_all_products_prices(self):
        """ Returns list of all products prices in order they're displayed
            on the page """
        prices = self.get_all_elements_texts(self.home_page_product_price)
        for item in prices:
            if '$' in item:
                item = float(item.replace('$', ''))
                return item
        return list(prices)

    def get_all_products_descriptions(self):
        """ Returns list of all products descriptions in order they're
            displayed on the page """
        return self.get_all_elements_texts(self.home_page_product_desc)

    def open_random_product_item(self):
        """ Opens random product """
        products_list = self.wait_for_all_elements_to_be_present(self.home_page_product_title)
        self.click_element(products_list[
                               randrange(len(products_list))])

    def open_home_page(self):
        self.click_element(self.home_page_home_btn)

    def open_contact_window(self):
        self.click_element(self.home_page_contact_btn)

    def open_about_us_window(self):
        self.click_element(self.home_page_about_us_btn)

    def open_cart_window(self):
        self.click_element(self.home_page_cart_btn)

    def open_log_in_window(self):
        self.click_element(self.home_page_login_btn)

    def open_sign_up_window(self):
        self.click_element(self.home_page_signup_btn)

    def click_carousel_next_icon_btn(self):
        self.click_element(self.home_page_carousel_next_icon_btn)

    def click_carousel_prev_icon_btn(self):
        self.click_element(self.home_page_carousel_prev_icon_btn)

    def click_category_btn(self):
        self.click_element(self.home_page_category_btn)

    def click_phones_btn(self):
        self.click_element(self.home_page_phones_btn)

    def click_laptops_btn(self):
        self.click_element(self.home_page_laptops_btn)

    def click_monitors_btn(self):
        self.click_element(self.home_page_monitors_btn)

    def click_previous_page_btn(self):
        self.click_element(self.home_page_previous_btn)

    def click_next_page_btn(self):
        self.click_element(self.home_page_next_btn)
