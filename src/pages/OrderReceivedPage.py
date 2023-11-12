from ssqamytest.src.SeleniumExtended import SeleniumExtended
from ssqamytest.src.pages.locators.OrderReceivedPageLocators import OrderReceivedPageLocators

class OrderReceivedPage(OrderReceivedPageLocators):
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def verify_order_received_page_loaded(self, text):
        self.sl.wait_until_element_contains_text(self.ORDER_RECEIVED_TITLE, text)

    def get_order_number(self):
        return self.sl.wait_and_get_text(self.ORDER_NUMBER)
