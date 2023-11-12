from ssqamytest.src.pages.locators.MyAccountSignedOutLocator import MyAccountSignedOutLocator
from ssqamytest.src.helpers.config_helpers import get_base_url
from ssqamytest.src.SeleniumExtended import SeleniumExtended

import logging as logger


class MyAccountSignedOut(MyAccountSignedOutLocator):
    endpoint = '/my-account/'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_my_account(self):
        base_url = get_base_url()
        my_account_url = base_url + self.endpoint
        logger.info(f"Going to: {my_account_url}")
        self.driver.get(my_account_url)

    def input_login_username(self, username):
        logger.debug("Input username.")
        self.sl.wait_and_input_text(self.LOGIN_USER_NAME, username, 10)

    def input_login_password(self, password):
        logger.debug("Input password.")
        self.sl.wait_and_input_text(self.LOGIN_USER_PASSWORD, password)

    def click_login_btn(self):
        logger.debug("Clicking 'login' button.")
        self.sl.wait_and_click(self.LOGIN_BUTTON)

    def wait_until_error_is_displayed(self, exp_err):
        logger.debug("Wait for error message will be displayed on the page.")
        self.sl.wait_until_element_contains_text(self.ERRORS_UL, exp_err)

    def input_register_email(self, email):
        logger.debug("Input email.")
        self.sl.wait_and_input_text(self.REGISTER_EMAIL, email, 10)

    def input_register_password(self, password):
        logger.debug("Input password.")
        self.sl.wait_and_input_text(self.REGISTER_PASSWORD, password, 10)

    def click_register_btn(self):
        logger.debug("Clicking 'Register' button.")
        self.sl.wait_and_click(self.REGISTER_BTN)
