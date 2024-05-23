from ssqamytest.src.helpers.config_helpers import get_base_url
import logging as logger
from ssqamytest.src.SeleniumExtended import SeleniumExtended
from ssqamytest.src.pages.locators.HomePageLocators import HomePageLocators


class HomePage(HomePageLocators):
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_home_page(self):
        base_url = get_base_url()
        logger.info(f"Going to: {base_url}")
        return self.driver.get(base_url)

    def click_first_add_to_cart_button(self):
        self.sl.wait_and_click(self.ADD_TO_CART_BUTTON)


