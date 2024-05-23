import logging as logger
from ssqamytest.src.SeleniumExtended import SeleniumExtended
from ssqamytest.src.pages.locators.CartPageLocators import CartPageLocators


class CartPage(CartPageLocators):
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_cart_page(self):
        pass

    def get_all_products_names_in_cart(self):
        elements = self.sl.wait_and_get_elements(self.PRODUCT_NAMES_IN_CART)
        element_names = [i.text for i in elements]
        return element_names

    def input_coupon(self, coupon_data):
        return self.sl.wait_and_input_text(self.COUPON_CODE_FIELD, coupon_data)

    def click_apply_coupon_btn(self):
        return self.sl.wait_and_click(self.APPLY_COUPON_BTN)

    def get_displayed_success_message(self):
        text = self.sl.wait_and_get_text(self.CART_PAGE_SUCCESS_MESSAGE)
        return text

    def apply_coupon(self, coupon_code):
        self.input_coupon(coupon_code)
        self.click_apply_coupon_btn()
        success_message = self.get_displayed_success_message()
        assert success_message == 'Coupon code applied successfully.', f"Unexpected message" \
                                                               f"when applying coupon."

    def click_local_pickup_radio(self):
        self.sl.wait_and_click(self.LOCAL_PICUP_RADIO)

    def click_checkout_button(self):
        self.sl.wait_and_click(self.PROCEED_TO_CHECKOUT_BTN)


